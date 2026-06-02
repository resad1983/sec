"""
Update wiki references for 3 renamed files.
"""
import os, re

WIKI_DIR = r"D:\gemini\obsidian\02_wiki"
REPORT = r"D:\gemini\obsidian\98_LOG\wiki-refs-update-3files.md"

# Old → New mapping
OLD_NEW = {
    "2026-03-31-As more Americans adopt AI tools, fewer say they can trust the results": (
        "2026-03-31-更多美國人使用AI工具卻越來越不信任AI的結果",
        "更多美國人使用AI工具，卻越來越不信任AI的結果"
    ),
    "2026-03-31-Former Coatue partner raises huge $65M seed for enterprise AI agent startup": (
        "2026-03-31-前Coatue合夥人為企業AI新創募得6500萬美元種子輪",
        "前Coatue合夥人為企業AI Agent新創募得6500萬美元種子輪"
    ),
    "2026-03-31-Mistral AI raises $830M in debt to set up a data center near Paris": (
        "2026-03-31-Mistral AI募資8.3億美元在巴黎近郊建立資料中心",
        "Mistral AI募資8.3億美元，將在巴黎近郊建立資料中心"
    ),
}

log_lines = []
total_replaced = 0

for fname in os.listdir(WIKI_DIR):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(WIKI_DIR, fname)
    with open(fpath, encoding="utf-8") as f:
        content = f.read()
    
    original = content
    for old_key, (new_filename, new_display) in OLD_NEW.items():
        # Use regex to handle $ signs in filenames
        escaped_old = re.escape(old_key)
        old_pattern = r"\[\[" + escaped_old + r"\|" + escaped_old + r"\]\]"
        new_pattern = f"[[{new_filename}|{new_display}]]"
        content = re.sub(old_pattern, new_pattern, content)
    
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        count = sum(1 for _ in range(content.count("[[2026-03-31-")))
        total_replaced += count
        log_lines.append(f"{fname}: updated")

print(f"Updated {len(log_lines)} wiki files, total references: {total_replaced}")
with open(REPORT, "w", encoding="utf-8") as f:
    f.write(f"# Wiki Ref Update\nUpdated {len(log_lines)} files, {total_replaced} refs\n")
    for l in log_lines:
        f.write(f"- {l}\n")
