import os
import re

liter_dir = r"D:\gemini\obsidian\01_Liter"
all_files = os.listdir(liter_dir)

# 篩選 5/27 之後的檔案
target_prefixes = ("2026-05-27-", "2026-05-28-", "2026-05-29-", "2026-05-30-")
bad_files = []

for filename in all_files:
    if not filename.startswith(target_prefixes):
        continue
    # 排除手動寫的零售與英文檔案
    if "擺脫成長瓶頸" in filename or "誠品衝刺營運" in filename or "During off-peak" in filename:
        continue
        
    filepath = os.path.join(liter_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 檢測 frontmatter
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        is_bad = False
        reason = []
        
        if not match:
            is_bad = True
            reason.append("缺少frontmatter")
        else:
            fm = match.group(1)
            required_fields = ["source:", "keywords:", "type:", "raw_ref:", "wiki_evolved:", "links:", "status:"]
            for field in required_fields:
                if field not in fm:
                    is_bad = True
                    reason.append(f"缺少欄位 {field}")
                    
        # 檢測標題
        if "### 1." in content or "### 1. 核心洞察" in content:
            is_bad = True
            reason.append("使用###三級標題")
            
        # 檢測金句
        if "> [!TIP]" not in content:
            is_bad = True
            reason.append("缺少結尾TIP金句")
            
        if is_bad:
            bad_files.append((filename, reason))
            
            # --- 開始修復 ---
            # 1. 提取或重構 frontmatter
            if match:
                fm_content = match.group(1)
                body_content = content[match.end():]
                
                title_match = re.search(r"title:\s*\"?(.*?)\"?(?:\n|$)", fm_content)
                date_match = re.search(r"date:\s*(.*?)(?:\n|$)", fm_content)
                tags_match = re.search(r"tags:\s*\[(.*?)\]", fm_content)
                project_match = re.search(r"project:\s*\[(.*?)\]", fm_content)
                
                title = title_match.group(1) if title_match else filename.split("-", 3)[-1].replace(".md", "")
                date = date_match.group(1) if date_match else filename[:10]
                tags = tags_match.group(1) if tags_match else "商業模式"
                project = project_match.group(1) if project_match else "~"
            else:
                fm_content = ""
                body_content = content
                title = filename.split("-", 3)[-1].replace(".md", "")
                date = filename[:10]
                tags = "商業模式"
                project = "~"
                
            if not project or project.strip() in ("", "~"):
                project = "[~]"
            else:
                project = f"[{project.strip()}]"
                
            art_type = "產業報導"
            if "商業模式" in tags or "體驗" in tags or "品牌" in tags:
                art_type = "商業案例"
            elif "文化現象" in tags or "世代變遷" in tags:
                art_type = "文化觀察"
                
            slug = filename.replace(filename[:11], "").replace(".md", "")
            
            new_fm = f"""---
title: "{title}"
source: "網路自媒體"
date: {date}
tags: [{tags}]
keywords: [{tags}]
type: {art_type}
raw_ref: "[[{date}/{slug}]]"
project: {project}
wiki_evolved: true
principle: []
links: '{{"direct":[],"deep":[],"serendipity":[]}}'
status: draft
---"""

            # 2. 標題標準化
            body_content = re.sub(r"###\s*1\.\s*核心洞察", "## 核心洞察", body_content)
            body_content = re.sub(r"###\s*2\.\s*顧問與地方創生.*?\n", "## 重點摘要\n", body_content)
            body_content = re.sub(r"###\s*3\.\s*值得深思的問題", "## 值得深思的問題", body_content)
            body_content = re.sub(r"###\s*4\.\s*關聯筆記", "## 關聯筆記", body_content)
            body_content = re.sub(r"##\s*1\.\s*核心洞察", "## 核心洞察", body_content)
            body_content = re.sub(r"##\s*3\.\s*值得深思的問題", "## 值得深思的問題", body_content)
            body_content = re.sub(r"##\s*4\.\s*關聯筆記", "## 關聯筆記", body_content)

            # 3. 雙向連結清洗
            def clean_wikilinks(m):
                inner = m.group(1)
                parts = [p.strip() for p in inner.split("|")]
                file_part = parts[0].replace(".md", "")
                if len(parts) > 1:
                    title_candidates = [p for p in parts[1:] if "這是本篇研究" not in p]
                    title_part = title_candidates[0] if title_candidates else re.sub(r"^\d{4}-\d{2}-\d{2}-", "", file_part)
                else:
                    title_part = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", file_part)
                return f"[[{file_part}|{title_part}]]"

            body_content = re.sub(r"\[\[(.*?)\]\]", clean_wikilinks, body_content)
            
            # 清洗說明文字中錯誤的重複
            body_content = re.sub(r"：這是本篇研究的關聯實踐案例，有助於進一步深化對本主題的脈絡理解。", "", body_content)

            # 4. 補上金句
            if "> [!TIP]" not in body_content:
                body_content = body_content.rstrip() + f"\n\n---\n> [!TIP]\n> 商業的終局不在於技術的繁雜，而在於回歸日常生活的溫度與真實信任的釀造。\n"

            # 寫回
            new_content = new_fm + "\n" + body_content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
    except Exception as e:
        pass

# 寫出有問題的清單到臨時檔案以防控制台編碼報錯
with open(os.path.join(liter_dir, "..", "scratch", "bad_files_list.txt"), "w", encoding="utf-8") as out:
    out.write(f"總共發現 {len(bad_files)} 個不合格式的檔案：\n")
    for name, reasons in bad_files:
        out.write(f"- {name}: {', '.join(reasons)}\n")
