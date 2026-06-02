"""
Batch Step 5: Classify project assignments for notes with project: [~]
Rules from skill (宁缺勿滥):
  1. 百貨/零售/體驗經濟 → [勤美誠品]
  2. 電商/D2C/食品品牌轉型 → [不二製餅]
  3. 地方創生/老屋/台中中區活化 → [民生路老宅, 台中舊城區]
  4. 個人品牌/顧問方法論/知識變現 → [個人顧問品牌]
  5. 文創/品牌策略/創作者經濟 → [典典文創]
  6. 寵物/服務設計/社群商業 → [寵物保母]
"""
import os, re, json, datetime

VAULT = r"D:\gemini\obsidian"
LITER_DIR = os.path.join(VAULT, "01_Liter")
REPORT_DIR = os.path.join(VAULT, "98_LOG")
os.makedirs(REPORT_DIR, exist_ok=True)

# Keyword rules - check title, tags, keywords, core_insight, type
RULES = {
    "勤美誠品": {
        "keywords": [
            "百貨", "零售", "商場", "購物中心", "專櫃", "outlet", "mall", "Mall", "MALL",
            "零售業", "實體店", "店面", "櫃位", "樓層", "誠品", "新光", "遠百", "SOGO",
            "體驗經濟", "零售趨勢", "商圈", "快閃店", "pop-up", "POP-UP",
            "消費體驗", "商場改造", "老百貨", "百貨改造", "百貨公司",
        ],
    },
    "不二製餅": {
        "keywords": [
            "電商", "D2C", "DTC", "d2c", "dtc", "食品", "零食", "伴手禮", "烘焙", "糕點",
            "品牌轉型", "線上銷售", "食品品牌", "小吃", "飲料", "茶飲", "手搖",
            "新零售", "供應鏈", "食品創新", "團購", "訂閱制",
        ],
    },
    "民生路老宅": {
        "keywords": [
            "地方創生", "老屋", "老宅", "街區", "台中中區", "舊城", "活化",
            "街區再生", "老店", "在地", "中區", "鄉鎮", "社區營造",
            "老街", "老城區", "城市更新", "老建築",
        ],
    },
    "台中舊城區": {
        "keywords": [
            "地方創生", "老屋", "老宅", "街區", "台中中區", "舊城", "活化",
            "街區再生", "老店", "在地", "中區", "鄉鎮", "社區營造",
            "老街", "老城區", "城市更新", "老建築",
        ],
    },
    "個人顧問品牌": {
        "keywords": [
            "個人品牌", "顧問", "教練", "coach", "Coach", "一人公司",
            "個人IP", "知識變現", "自媒體", "專家", "個人事業",
            "freelance", "Freelance", "自由職業", "知識產品",
            "個人定位", "個人商業", "個人工作室",
        ],
    },
    "典典文創": {
        "keywords": [
            "文創", "品牌策略", "創作者經濟", "IP", "設計", "美學",
            "文化內容", "創意", "策展", "展覽", "藝術",
            "品牌年輕化", "品牌升級", "品牌定位", "品牌設計",
        ],
    },
    "寵物保母": {
        "keywords": [
            "寵物", "毛小孩", "貓", "狗", "寵物保母", "寵物服務",
            "遛狗", "寵物用品", "寵物食品", "寵物友善",
        ],
    },
}

def check_rules(title, tags, keywords, note_type, core_insight):
    """Return list of matching projects based on keyword rules."""
    text = f"{title} {' '.join(tags)} {' '.join(keywords)} {note_type} {core_insight}"
    matches = set()
    for project, rule in RULES.items():
        for kw in rule["keywords"]:
            if kw.lower() in text.lower():
                matches.add(project)
                break
    return sorted(matches)

# Scan files with project: [~]
stats = {"scanned": 0, "assigned": 0, "kept_null": 0, "changes": []}
log_lines = []

for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Check if project is [~]
    if "project: [~]" not in content:
        continue

    stats["scanned"] += 1

    # Parse frontmatter
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        continue
    fm_raw = m.group(1)
    title = ""
    tags = []
    keywords = []
    note_type = ""

    for line in fm_raw.split("\n"):
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("tags:"):
            tags_raw = line.split(":", 1)[1].strip()
            tags = [t.strip().strip("'\"") for t in tags_raw.strip("[]").split(",") if t.strip()]
        elif line.startswith("keywords:"):
            kw_raw = line.split(":", 1)[1].strip()
            keywords = [k.strip().strip("'\"") for k in kw_raw.strip("[]").split(",") if k.strip()]
        elif line.startswith("type:"):
            note_type = line.split(":", 1)[1].strip().strip('"').strip("'")

    # Parse core_insight
    ci_match = re.search(r"##\s*核心洞察.*?\n+(.*?)(?=\n+##|\Z)", content, re.DOTALL)
    core_insight = ci_match.group(1).strip() if ci_match else ""

    # Check rules
    matches = check_rules(title, tags, keywords, note_type, core_insight)
    if matches:
        project_str = ", ".join(matches)
        new_project = f"project: [{project_str}]"
        new_content = content.replace("project: [~]", new_project, 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        stats["assigned"] += 1
        stats["changes"].append((fname, project_str))
        log_lines.append(f"ASSIGN {fname} -> [{project_str}]")
    else:
        stats["kept_null"] += 1

# Generate report
report = f"""# Batch Project Classification Report
Date: {datetime.date.today()}

## Summary
- Total [~] notes scanned: {stats['scanned']}
- Assigned to project: {stats['assigned']}
- Kept as [~]: {stats['kept_null']}

## Changes
"""
for fname, project in stats["changes"]:
    report += f"- {fname} → [{project}]\n"

# Count by project
from collections import Counter
project_counts = Counter()
for _, p in stats["changes"]:
    for proj in p.split(", "):
        project_counts[proj] += 1
report += "\n## By Project\n"
for proj, count in sorted(project_counts.items()):
    report += f"- {proj}: {count}\n"

report_path = os.path.join(REPORT_DIR, f"project-classify-{datetime.date.today().isoformat()}.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report)

print(f"Done! Scanned: {stats['scanned']}, Assigned: {stats['assigned']}, Kept null: {stats['kept_null']}")
print(f"Report: {report_path}")
