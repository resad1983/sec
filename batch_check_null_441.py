"""
Check the 441 notes with project: [~] for possible false negatives.
Scans not just frontmatter but also note body content.
"""
import os, re, json, csv
from collections import Counter

VAULT = r"D:\gemini\obsidian"
LITER_DIR = os.path.join(VAULT, "01_Liter")

# The same rules but we also search body content now
RULES = {
    "勤美誠品": ["百貨", "零售", "商場", "購物中心", "專櫃", "outlet", "mall", "Mall", "MALL",
                  "零售業", "實體店", "店面", "櫃位", "樓層", "誠品", "新光", "遠百", "SOGO",
                  "體驗經濟", "零售趨勢", "商圈", "快閃店", "pop-up", "POP-UP",
                  "消費體驗", "商場改造", "老百貨", "百貨改造", "百貨公司"],
    "不二製餅": ["電商", "D2C", "DTC", "d2c", "dtc", "食品", "零食", "伴手禮", "烘焙", "糕點",
                  "品牌轉型", "線上銷售", "食品品牌", "小吃", "飲料", "茶飲", "手搖",
                  "新零售", "供應鏈", "食品創新", "團購", "訂閱制"],
    "民生路老宅": ["地方創生", "老屋", "老宅", "街區", "台中中區", "舊城", "活化",
                    "街區再生", "老店", "在地", "中區", "鄉鎮", "社區營造",
                    "老街", "老城區", "城市更新", "老建築"],
    "台中舊城區": ["地方創生", "老屋", "老宅", "街區", "台中中區", "舊城", "活化",
                    "街區再生", "老店", "在地", "中區", "鄉鎮", "社區營造",
                    "老街", "老城區", "城市更新", "老建築"],
    "個人顧問品牌": ["個人品牌", "顧問", "教練", "coach", "Coach", "一人公司",
                      "個人IP", "知識變現", "自媒體", "專家", "個人事業",
                      "freelance", "Freelance", "自由職業", "知識產品",
                      "個人定位", "個人商業", "個人工作室"],
    "典典文創": ["文創", "品牌策略", "創作者經濟", "IP", "設計", "美學",
                  "文化內容", "創意", "策展", "展覽", "藝術",
                  "品牌年輕化", "品牌升級", "品牌定位", "品牌設計"],
    "寵物保母": ["寵物", "毛小孩", "貓", "狗", "寵物保母", "寵物服務",
                  "遛狗", "寵物用品", "寵物食品", "寵物友善"],
}

# Load all note paths
null_notes = []  # (fname, title, tags, keywords, type, core_insight, first_500_chars)

for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8", errors="replace") as f:
        content = f.read()
    if "project: [~]" not in content:
        continue

    # Parse frontmatter
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        continue
    fm_raw = m.group(1)
    body = content[m.end():].strip()

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

    ci_match = re.search(r"##\s*核心洞察.*?\n+(.*?)(?=\n+##|\Z)", body, re.DOTALL)
    core_insight = ci_match.group(1).strip() if ci_match else ""

    null_notes.append((fname, title, tags, keywords, note_type, core_insight, body[:500]))

# Now re-evaluate with stricter logic + body content
# Also search body for project-specific keywords
found_matches = []  # (fname, title, matched_projects, reason)
still_null = []
project_hints = Counter()

def search_body(body, keywords_list):
    body_lower = body.lower()
    found = set()
    for project, kws in RULES.items():
        for kw in kws:
            if kw.lower() in body_lower:
                found.add(project)
                break
    return sorted(found)

for fname, title, tags, keywords, note_type, core_insight, body_start in null_notes:
    # Check all searchable text (broader than before)
    search_text = f"{title} {' '.join(tags)} {' '.join(keywords)} {note_type} {core_insight}"
    search_text += " " + body_start  # also check first 500 chars of body
    
    matches = set()
    reasons = []
    for project, kws in RULES.items():
        for kw in kws:
            if kw.lower() in search_text.lower():
                matches.add(project)
                reasons.append(f"fm:{kw}")
                break
    
    # Also check deeper body for specific strong signals
    body_matches = search_body(body_start, RULES)
    for p in body_matches:
        if p not in matches:
            matches.add(p)
            reasons.append("body")

    if matches:
        found_matches.append((fname, title, sorted(matches), "; ".join(reasons)))
        for p in matches:
            project_hints[p] += 1
    else:
        still_null.append((fname, title, tags, keywords, note_type))

# Output report
report_lines = []
report_lines.append("# Step 5 Recheck: False Negative Analysis")
report_lines.append("")
report_lines.append(f"Total [~] notes: {len(null_notes)}")
report_lines.append(f"Newly detected candidates: {len(found_matches)}")
report_lines.append(f"Confirmed [~]: {len(still_null)}")
report_lines.append("")

if found_matches:
    report_lines.append("## Candidates that may need assignment")
    report_lines.append("")
    report_lines.append("| # | File | Title | Suggested Project | Reason |")
    report_lines.append("|---|---|---|---|---|")
    for i, (fname, title, matches, reason) in enumerate(found_matches, 1):
        report_lines.append(f"| {i} | {fname[:60]} | {title[:60]} | {', '.join(matches)} | {reason} |")
    report_lines.append("")
    report_lines.append("## By Project")
    for p, c in sorted(project_hints.items()):
        report_lines.append(f"- {p}: {c}")
    report_lines.append("")

report_lines.append("## Sample of confirmed null (first 50)")
report_lines.append("")
for fname, title, tags, keywords, note_type in still_null[:50]:
    tag_str = ", ".join(tags[:3]) if tags else ""
    report_lines.append(f"- {title[:70]} | tags={tag_str}")

report_path = os.path.join(VAULT, "98_LOG", "null-441-recheck.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"Done. New candidates: {len(found_matches)}, Confirmed null: {len(still_null)}")
print(f"Report: {report_path}")
