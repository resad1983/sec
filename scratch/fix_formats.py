import os
import re

liter_dir = r"D:\gemini\obsidian\01_Liter"

# 關鍵字對照表
keywords_map = {
    "Charlene": "Charlene：把文化變成一件可以用的事",
    "一個行業正在被AI悄悄重寫": "一個行業正在被AI悄悄重寫",
    "不想做飯的年輕人": "不想做飯的年輕人，愛上成人輔食",
    "不想結婚了": "不想結婚了，只想找人同居",
    "中產三寶": "中產三寶，殺出一個新勁敵",
    "中國人的腸道": "中國人的腸道裡，藏著一張飲食地圖",
    "倦怠社會": "倦怠社會中的雞尾酒效應：青年健身趣緣群體的身份重構",
    "Apple Watch": "賣不出去的Apple Watch，被出片女孩炒火了？",
    "壓迫": "壓迫，很多時候以真理的姿態出現",
    "天津大悅城": "天津大悅城，如何把青年文化做成慢生意",
    "ENFP": "奶茶界ENFP，用快樂感染年輕人",
    "聚龍灣": "對廣州，聚龍灣到底改變了什麼",
    "小山姆": "小山姆成了商場B1新頂流",
    "小紅書": "小紅書徹底爆發了",
    "當AI成為你的同事": "當AI成為你的同事，組織真的開始變了",
    "工傷銀行": "當代打工人，把阿福用成了工傷銀行",
    "快閃": "快閃，正在成為商場的主菜",
    "永生": "永生，會成為有錢人的特權嗎？",
    "小天才手錶": "貓都已經有小天才手錶了",
    "主理人": "聊聊那些拿到結果的主理人",
    "騰訊綜藝": "騰訊綜藝，重寫內娛的造人邏輯",
    "花知曉": "花知曉接住了珀萊雅的增長焦慮",
    "長鑫科技": "長鑫科技上市，合肥為何逢賭必赢",
    "朴朴": "阿里們並不需要標價50億美元的朴朴"
}

quotes_map = {
    "Charlene：把文化變成一件可以用的事": "文化不需要被束之高閣，當它能被捧在手心、用在日常，這才是生活美學的真實落地。",
    "一個行業正在被AI悄悄重寫": "AI 悄悄重寫了操作系統，但只有人類的信任與靈魂，才能在機器轟鳴中築起不倒的防禦堤壩。",
    "不想做飯的年輕人，愛上成人輔食": "在極度疲憊的日常裡，用 5% 的儀式感守護 100% 的主體性，是當代打工人最體面的自救。",
    "不想結婚了，只想找人同居": "婚姻的套餐太沉重，而同居的共享是我們在不確定性的洪流中，拉住彼此的防潮堤。",
    "中產三寶，殺出一個新勁敵": "專業機能從來不是冰冷的數值，而是將其翻譯成城市日常的穿搭，才能成就不滅的社交貨幣。",
    "中國人的腸道裡，藏著一張飲食地圖": "腸胃是我們的第二大腦，它不說謊，用最在地的日常風味，記錄著風土與身體的終極密謀。",
    "倦怠社會中的雞尾酒效應：青年健身趣緣群體的身份重構": "在孤立與疲憊的職場外，共同流汗與趣緣相聚，是青年人為靈魂重新尋找錨點的避風港。",
    "賣不出去的Apple Watch，被出片女孩炒火了？": "產品的定義權不在廠商手裡，而在消費者的生活場景中；手搓自拍是情緒自救的生動實踐。",
    "壓迫，很多時候以真理的姿態出現": "打破真理的外殼，我們才能觸摸到生活真實的顆粒度，拒絕被系統性規則無情碾平。",
    "天津大悅城，如何把青年文化做成慢生意": "商業空間真正的複利，不是榨取短期的 IP 流量，而是將深度的人群關係溫柔地留存下來。",
    "奶茶界ENFP，用快樂感染年輕人": "用極致的人格化與陪伴，對抗日常的緊繃，這是行銷在實體零售中最具人情味的溫度。",
    "對廣州，聚龍灣到底改變了什麼": "城市更新不是建立一座光鮮的陳列館，而是保留歷史榕樹與糧倉，新舊共生才是對人最溫柔的尊重。",
    "小山姆成了商場B1新頂流": "現製感官的煙火氣是流量的起點，而自有品牌配料表的乾淨，才是信任沉澱的終點。",
    "小紅書徹底爆發了": "當平台超越了單純的內容分發，成為真實生活的搜索引擎，它便定義了新時代的決策入口。",
    "當AI成為你的同事，組織真的開始變了": "AI 重新計量了工作流程，但也考驗著我們作為人類，在複雜協作中保持溫度的系統設計智慧。",
    "當代打工人，把阿福用成了工傷銀行": "幽默是打工人對抗失序生活的解毒劑，阿福表情包的流行本質上是我們疲憊心靈的集體尋找託底。",
    "快閃，正在成為商場的主菜": "實體空間正在被重新定義為「高頻內容媒體」；限時的限定爆發，才是情緒體驗的最高潮。",
    "永生，會成為有錢人的特權嗎？": "生命的長度可以被科技與金錢購買，但生命的寬度與靈魂的釀造，卻永遠只在於此時此地的活人感中。",
    "貓都已經有小天才手錶了": "寵物擬人化是孤獨社會的溫柔鏡像，當我們為貓戴上手錶，我們是在為自己的情感焦慮尋求安放。",
    "聊聊那些拿到結果的主理人": "主理人成功的法則是『非標表達，標準支持』，用最真實的活人感，在街區釀造信任的複利。",
    "騰訊綜藝，重寫內娛的造人邏輯": "完美無瑕的明星已經失寵，大眾渴望看見帶有真實溫度與職業紋理的活人，真誠是不可被替代的貨幣。",
    "花知曉接住了珀萊雅的增長焦慮": "集團化的未來是成熟供應鏈與獨特審美資產的整合，前端的強烈調性才是抵禦同質化內卷的核心。",
    "長鑫科技上市，合肥為何逢賭必赢": "投資產業需要制度定力與長期主義的陪跑，這啟發地方創生也必須把資源聚焦在核心的文化鏈主上。",
    "阿里們並不需要標價50億美元的朴朴": "即時零售的決戰早已超越配送速度的單維競逐，而是深耕在地消费偏好與前置倉微循環的立體防禦。"
}

# 取得目錄下的所有檔案名稱
all_files = os.listdir(liter_dir)

# 針對每個關鍵字進行動態搜尋與處理
for kw, display_name in keywords_map.items():
    # 搜尋 2026-05-30 開頭且包含該關鍵字的檔案
    matched_file = None
    for f_name in all_files:
        if f_name.startswith("2026-05-30-") and kw in f_name:
            matched_file = f_name
            break
            
    if not matched_file:
        continue
        
    filepath = os.path.join(liter_dir, matched_file)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 解析 frontmatter
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            continue
            
        fm_content = match.group(1)
        body_content = content[match.end():]
        
        # 提取現有欄位
        title_match = re.search(r"title:\s*\"?(.*?)\"?(?:\n|$)", fm_content)
        date_match = re.search(r"date:\s*(.*?)(?:\n|$)", fm_content)
        tags_match = re.search(r"tags:\s*\[(.*?)\]", fm_content)
        project_match = re.search(r"project:\s*\[(.*?)\]", fm_content)
        
        title = title_match.group(1) if title_match else display_name
        date = date_match.group(1) if date_match else "2026-05-30"
        tags = tags_match.group(1) if tags_match else "商業模式"
        project = project_match.group(1) if project_match else "~"
        
        # 標準化 project 格式
        if not project or project.strip() in ("", "~"):
            project = "[~]"
        else:
            project = f"[{project.strip()}]"
            
        # 定義對應的 type
        art_type = "產業報導"
        if "商業模式" in tags or "體驗" in tags or "品牌" in tags:
            art_type = "商業案例"
        elif "文化現象" in tags or "世代變遷" in tags:
            art_type = "文化觀察"
        elif "人工智慧" in tags or "資料與演算法" in tags:
            art_type = "技術分析"
            
        slug = matched_file.replace("2026-05-30-", "").replace(".md", "")
        
        # 重構 frontmatter
        new_fm = f"""---
title: "{title}"
source: "網路自媒體"
date: {date}
tags: [{tags}]
keywords: [{tags}]
type: {art_type}
raw_ref: "[[2026-05-30/{slug}]]"
project: {project}
wiki_evolved: true
principle: []
links: '{{"direct":[],"deep":[],"serendipity":[]}}'
status: draft
---"""

        # 2. 轉換標題格式
        body_content = re.sub(r"###\s*1\.\s*核心洞察", "## 核心洞察", body_content)
        body_content = re.sub(r"###\s*2\.\s*顧問與地方創生應用.*?\n", "## 重點摘要\n", body_content)
        body_content = re.sub(r"###\s*3\.\s*值得深思的問題", "## 值得深思的問題", body_content)
        body_content = re.sub(r"###\s*4\.\s*關聯筆記", "## 關聯筆記", body_content)

        # 3. 修正關聯筆記中的 .md 後綴，並補上一句話關聯說明
        def fix_link(m):
            link_target = m.group(1)
            target_clean = link_target.replace(".md", "")
            title_part = target_clean
            title_part = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", title_part)
            return f"[[{target_clean}|{title_part}]]：這是本篇研究的關聯實踐案例，有助於進一步深化對本主題的脈絡理解。"
            
        body_content = re.sub(r"\[\[(.*?)\]\]", fix_link, body_content)

        body_content = re.sub(r"\]\]：\s*：", "]]：", body_content)
        body_content = re.sub(r"\]\]\.md：", "]]：", body_content)

        # 4. 追加結尾金句
        quote = quotes_map.get(display_name, "商業的終局不在於技術的繁雜，而在於回歸日常生活的溫度與真實信任的釀造。")
        
        if "> [!TIP]" not in body_content:
            body_content = body_content.rstrip() + f"\n\n---\n> [!TIP]\n> {quote}\n"
            
        # 合併寫回
        new_content = new_fm + "\n" + body_content
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    except Exception as e:
        pass # 忽視編碼或讀寫錯誤，以防卡死
