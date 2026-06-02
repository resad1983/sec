"""
Strict recheck of 441 null notes.
Only flag if:
  1. Note's tags overlap with a project's wiki tag (e.g. tag "零售" → 勤美誠品)
  2. Core insight OR title has 2+ unique keywords pointing to the SAME project
  3. Keywords field in frontmatter explicitly mentions a relevant project term
"""
import os, re

VAULT = r"D:\gemini\obsidian"
LITER_DIR = os.path.join(VAULT, "01_Liter")
WIKI_DIR = os.path.join(VAULT, "02_wiki")

# Load wiki tags (each wiki file = a tag name without .md)
wiki_tags = {}
for fname in os.listdir(WIKI_DIR):
    if fname.endswith(".md"):
        tag_name = fname[:-3]
        with open(os.path.join(WIKI_DIR, fname), encoding="utf-8") as f:
            content = f.read()
        wiki_tags[tag_name] = content[:200]

# Project-specific tags (wiki tags that map to projects)
PROJECT_TAGS = {
    "勤美誠品": ["零售", "百貨", "商場", "消費", "品牌"],
    "不二製餅": ["電商", "食品", "餐飲", "供應鏈", "品牌", "消費"],
    "民生路老宅": ["地方創生", "老屋", "台中", "街區", "城市更新"],
    "台中舊城區": ["地方創生", "老屋", "台中", "街區", "城市更新"],
    "個人顧問品牌": ["個人品牌", "一人公司", "自媒體", "顧問", "知識變現"],
    "典典文創": ["文創", "品牌", "設計", "美學", "IP", "策展", "創意", "文化"],
    "寵物保母": ["寵物", "寵物保母", "寵物服務"],
}

# Strong project indicator keywords (very specific, low noise)
STRONG_KW = {
    "勤美誠品": ["勤美", "百貨公司", "百貨業", "購物中心"],
    "不二製餅": ["不二製餅", "不二", "伴手禮", "D2C", "d2c", "食品品牌"],
    "民生路老宅": ["民生路老宅", "老宅", "老屋活化", "街區活化"],
    "台中舊城區": ["台中中區", "舊城區", "中區", "台中舊城"],
    "個人顧問品牌": ["一人公司", "個人品牌", "個人事業", "顧問品牌", "個人IP", "知識變現"],
    "典典文創": ["文創", "創作者經濟", "IP授權", "品牌年輕化", "品牌升級"],
    "寵物保母": ["寵物保母", "寵物保姆", "遛狗"],
}

null_notes = []
for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8", errors="replace") as f:
        content = f.read()
    if "project: [~]" not in content:
        continue

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

    null_notes.append((fname, title, tags, keywords, note_type, core_insight))

# Strict evaluation
false_negatives = []  # Strong evidence
possible_miss = []    # Moderate evidence

for fname, title, tags, keywords, note_type, core_insight in null_notes:
    text = f"{title} {' '.join(tags)} {' '.join(keywords)} {note_type} {core_insight}"
    
    for project, strong_kws in STRONG_KW.items():
        for kw in strong_kws:
            if kw.lower() in text.lower():
                false_negatives.append((fname, title, project, f"strong_kw:{kw}"))
                break
    
    # Check tag overlap with project tags
    tag_matches = {}
    for project, proj_tags in PROJECT_TAGS.items():
        matches = [t for t in tags if t in proj_tags]
        if matches:
            tag_matches[project] = matches
    
    if tag_matches:
        for proj, matched_tags in tag_matches.items():
            already = any(fn[2] == proj and fn[0] == fname for fn in false_negatives)
            if not already:
                # Check if any strong signal in body too
                body_lower = (core_insight + " " + title).lower()
                strong_in_body = any(kw.lower() in body_lower for kw in STRONG_KW.get(proj, []))
                if strong_in_body:
                    false_negatives.append((fname, title, proj, f"tag_match:{matched_tags}+body_kw"))
                # Multiple tag matches = stronger signal
                elif len(matched_tags) >= 2:
                    possible_miss.append((fname, title, proj, f"tag_match_x2:{matched_tags}"))

# Deduplicate
seen_fn = set()
unique_fn = []
for item in false_negatives:
    key = (item[0], item[2])
    if key not in seen_fn:
        seen_fn.add(key)
        unique_fn.append(item)

seen_pm = set()
unique_pm = []
for item in possible_miss:
    key = (item[0], item[2])
    if key not in seen_pm and key not in seen_fn:
        seen_pm.add(key)
        unique_pm.append(item)

# Output
lines = []
lines.append("# Step 5 Strict Recheck of 441 Null Notes")
lines.append("")
lines.append(f"Total rechecked: {len(null_notes)}")
lines.append(f"Strong false negatives (strong keyword match): {len(unique_fn)}")
lines.append(f"Possible misses (tag overlap): {len(unique_pm)}")
lines.append(f"Confirmed correct null: {len(null_notes) - len(unique_fn) - len(unique_pm)}")
lines.append("")

if unique_fn:
    lines.append("## Strong False Negatives — Should assign")
    lines.append("")
    lines.append("| # | File | Project | Reason |")
    lines.append("|---|---|---|---|")
    for i, (fname, title, proj, reason) in enumerate(unique_fn, 1):
        lines.append(f"| {i} | {fname[:55]} | {proj} | {reason} |")
    lines.append("")

if unique_pm:
    lines.append("## Possible Misses — Review recommended")
    lines.append("")
    lines.append("| # | File | Project | Reason |")
    lines.append("|---|---|---|---|")
    for i, (fname, title, proj, reason) in enumerate(unique_pm, 1):
        lines.append(f"| {i} | {fname[:55]} | {proj} | {reason} |")

report_path = os.path.join(VAULT, "98_LOG", "null-441-strict-recheck.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Strong false negatives: {len(unique_fn)}")
print(f"Possible misses: {len(unique_pm)}")
print(f"Confirmed null: {len(null_notes) - len(unique_fn) - len(unique_pm)}")
print(f"Report: {report_path}")
