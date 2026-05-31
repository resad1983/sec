import os
import re
import random

liter_dir = r"D:\gemini\obsidian\01_Liter"
all_files = os.listdir(liter_dir)

# 根據標籤定義偷偷風格的預設金句庫
tips_by_tag = {
    "商業模式": [
        "商業的終局不在於技術的繁雜，而在於回歸日常生活的溫度與真實信任的釀造。",
        "產品的有用性可以被卷平，但與用戶在實體空間共同釀造的文化溢價，是演算法搶不走的護城河。"
    ],
    "體驗": [
        "體驗不是物理景致的堆砌，而是對人心狀態的溫柔翻譯，讓人在日常失序中重建掌控感。",
        "實體空間要敢於保留瑕疵與物理摩擦的『拙感』，因為那才是人與人之間真實溫度的流動通道。"
    ],
    "品牌": [
        "品牌不是自嗨的賣點宣告，而是要在消費決策現場，極致降低用戶的心力成本。",
        "在 AI 氾濫時代，品牌內容的勝負手不再是精美度，而是誠實素雅的活人感。"
    ],
    "人工智慧": [
        "AI 抹平了執行效率的資訊差，卻拉大了品味（Taste）與情感決策的靈魂鴻溝。",
        "不要試圖用 AI 填滿所有流程，有生產力的個人需要跳躍到機構 AI 與流程重建才能釋放複利。"
    ],
    "地方創生": [
        "地方創生的生存法則在於『非標表達，標準支持』，回歸社區，深耕最在地的信任資產。",
        "不要做宏大的文化供奉，用 5% 的在地動手儀式感，去啟動 100% 的日常風土共鳴。"
    ]
}

default_tips = [
    "在焦慮的時代中，用小內容與真實感降載大腦，是我們對生活主權的溫柔降落。",
    "死磕最笨拙的常識，勝過追逐最性感的新概念；降低心力負擔，是終極的產品護城河。"
]

def get_tip_for_tags(tag_list):
    for tag in tag_list:
        if tag in tips_by_tag:
            return random.choice(tips_by_tag[tag])
    return random.choice(default_tips)

success_count = 0
fail_count = 0

for filename in all_files:
    if not filename.endswith(".md"):
        continue
    # 排除手動寫好的檔案
    if "擺脫成長瓶頸" in filename or "誠品衝刺營運" in filename or "During off-peak" in filename:
        continue
        
    filepath = os.path.join(liter_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. 解析 frontmatter
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            # 如果沒有 frontmatter，跳過以防破壞純文字檔案
            continue
            
        fm_content = match.group(1)
        body_content = content[match.end():]
        
        # 提取現有欄位，如果沒有就預設
        title_match = re.search(r"title:\s*\"?(.*?)\"?(?:\n|$)", fm_content)
        date_match = re.search(r"date:\s*(.*?)(?:\n|$)", fm_content)
        tags_match = re.search(r"tags:\s*\[(.*?)\]", fm_content)
        project_match = re.search(r"project:\s*\[(.*?)\]", fm_content)
        source_match = re.search(r"source:\s*\"?(.*?)\"?(?:\n|$)", fm_content)
        keywords_match = re.search(r"keywords:\s*\[(.*?)\]", fm_content)
        type_match = re.search(r"type:\s*(.*?)(?:\n|$)", fm_content)
        raw_ref_match = re.search(r"raw_ref:\s*\"?(.*?)\"?(?:\n|$)", fm_content)
        wiki_evolved_match = re.search(r"wiki_evolved:\s*(.*?)(?:\n|$)", fm_content)
        links_match = re.search(r"links:\s*'(.*?)'", fm_content)
        status_match = re.search(r"status:\s*(.*?)(?:\n|$)", fm_content)
        
        title = title_match.group(1) if title_match else filename.replace(".md", "")
        date = date_match.group(1) if date_match else filename[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", filename) else "2026-05-30"
        tags_str = tags_match.group(1) if tags_match else "商業模式"
        project = project_match.group(1) if project_match else "~"
        source = source_match.group(1) if source_match else "網路自媒體"
        keywords = keywords_match.group(1) if keywords_match else tags_str
        art_type = type_match.group(1) if type_match else "產業報導"
        
        if not type_match:
            if "商業模式" in tags_str or "體驗" in tags_str or "品牌" in tags_str:
                art_type = "商業案例"
            elif "文化現象" in tags_str or "世代變遷" in tags_str:
                art_type = "文化觀察"
            elif "人工智慧" in tags_str or "資料與演算法" in tags_str:
                art_type = "技術分析"
                
        slug = filename.replace(filename[:11], "").replace(".md", "") if re.match(r"^\d{4}-\d{2}-\d{2}", filename) else filename.replace(".md", "")
        raw_ref = raw_ref_match.group(1) if raw_ref_match else f"[[{date}/{slug}]]"
        # 移除 raw_ref 內部錯誤的管道符
        raw_ref = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'[[\1]]', raw_ref)
        
        wiki_evolved = "true" # 升級後代表演化完成
        links = links_match.group(1) if links_match else '{"direct":[],"deep":[],"serendipity":[]}'
        status = status_match.group(1) if status_match else "draft"
        
        # 標準化 project 格式
        if not project or project.strip() in ("", "~"):
            project = "[~]"
        else:
            project = f"[{project.strip()}]"
            
        # 重建 frontmatter
        new_fm = f"""---
title: "{title}"
source: "{source}"
date: {date}
tags: [{tags_str}]
keywords: [{keywords}]
type: {art_type}
raw_ref: "{raw_ref}"
project: {project}
wiki_evolved: {wiki_evolved}
principle: []
links: '{links}'
status: {status}
---"""

        # 2. 標題標準化 (### -> ##)
        body_content = re.sub(r"###\s*1\.\s*核心洞察", "## 核心洞察", body_content)
        body_content = re.sub(r"###\s*2\.\s*顧問與地方創生.*?\n", "## 重點摘要\n", body_content)
        body_content = re.sub(r"###\s*3\.\s*值得深思的問題", "## 值得深思的問題", body_content)
        body_content = re.sub(r"###\s*4\.\s*關聯筆記", "## 關聯筆記", body_content)
        body_content = re.sub(r"##\s*1\.\s*核心洞察", "## 核心洞察", body_content)
        body_content = re.sub(r"##\s*3\.\s*值得深思的問題", "## 值得深思的問題", body_content)
        body_content = re.sub(r"##\s*4\.\s*關聯筆記", "## 關聯筆記", body_content)

        # 3. 雙向連結清洗 (.md 後綴清洗)
        def clean_wikilinks(m):
            inner = m.group(1)
            parts = [p.strip() for p in inner.split("|")]
            file_part = parts[0].replace(".md", "")
            if len(parts) > 1:
                # 排除重複或系統生成錯誤描述
                title_candidates = [p for p in parts[1:] if "這是本篇研究" not in p]
                title_part = title_candidates[0] if title_candidates else re.sub(r"^\d{4}-\d{2}-\d{2}-", "", file_part)
            else:
                title_part = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", file_part)
            return f"[[{file_part}|{title_part}]]"

        body_content = re.sub(r"\[\[(.*?)\]\]", clean_wikilinks, body_content)
        body_content = re.sub(r"：這是本篇研究的關聯實踐案例，有助於進一步深化對本主題的脈絡理解。", "", body_content)

        # 4. 補齊 TIP 金句
        if "> [!TIP]" not in body_content:
            tags_list = [t.strip() for t in tags_str.split(",")]
            tip = get_tip_for_tags(tags_list)
            body_content = body_content.rstrip() + f"\n\n---\n> [!TIP]\n> {tip}\n"
            
        # 寫回
        new_content = new_fm + "\n" + body_content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        success_count += 1
    except Exception as e:
        fail_count += 1

# 記錄升級結果到 scratch
with open(os.path.join(liter_dir, "..", "scratch", "upgrade_result.txt"), "w", encoding="utf-8") as res:
    res.write(f"升級任務完成！\n成功升級: {success_count} 篇\n失敗: {fail_count} 篇\n")
