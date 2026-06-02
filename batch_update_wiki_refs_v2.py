"""
Update wiki references using regex - handles $ and special chars.
"""
import os, re

WIKI_DIR = r"D:\gemini\obsidian\02_wiki"

# Old pattern → New pattern (regex patterns)
REPLACEMENTS = [
    (
        r"\[\[2026-03-31-As more Americans adopt AI tools, fewer say they can trust the results\|As more Americans adopt AI tools, fewer say they can trust the results\]\]",
        "[[2026-03-31-更多美國人使用AI工具卻越來越不信任AI的結果|更多美國人使用AI工具，卻越來越不信任AI的結果]]"
    ),
    (
        r"\[\[2026-03-31-Former Coatue partner raises huge \$65M seed for enterprise AI agent startup\|Former Coatue partner raises huge \$65M seed for enterprise AI agent startup\]\]",
        "[[2026-03-31-前Coatue合夥人為企業AI新創募得6500萬美元種子輪|前Coatue合夥人為企業AI Agent新創募得6500萬美元種子輪]]"
    ),
    (
        r"\[\[2026-03-31-Mistral AI raises \$830M in debt to set up a data center near Paris\|Mistral AI raises \$830M in debt to set up a data center near Paris\]\]",
        "[[2026-03-31-Mistral AI募資8.3億美元在巴黎近郊建立資料中心|Mistral AI募資8.3億美元，將在巴黎近郊建立資料中心]]"
    ),
]

total = 0
for fname in os.listdir(WIKI_DIR):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(WIKI_DIR, fname)
    with open(fpath, encoding="utf-8") as f:
        content = f.read()
    original = content
    for old_pat, new_str in REPLACEMENTS:
        content = re.sub(old_pat, new_str, content)
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        changed = sum(1 for old_pat, _ in REPLACEMENTS if re.search(old_pat, original))
        total += changed
        print(f"  Updated {fname}")

print(f"Done. Total files updated.")
