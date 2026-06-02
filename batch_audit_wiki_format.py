"""
Audit all wiki files in 02_wiki/ for format issues.
Checks: frontmatter, core definition presence, duplicate entries, broken wiki links.
"""
import os, re
from collections import Counter

WIKI_DIR = r"D:\gemini\obsidian\02_wiki"
issues = []
stats = {"total": 0, "ok": 0, "with_issues": 0}

for fname in sorted(os.listdir(WIKI_DIR)):
    if not fname.endswith(".md"):
        continue
    stats["total"] += 1
    fpath = os.path.join(WIKI_DIR, fname)
    with open(fpath, encoding="utf-8") as f:
        content = f.read()
    
    file_issues = []
    
    # 1. Check frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        file_issues.append("Missing frontmatter")
    else:
        fm = fm_match.group(1)
        if "title:" not in fm:
            file_issues.append("Frontmatter missing title")
        if "type:" not in fm:
            file_issues.append("Frontmatter missing type")
    
    # 2. Check for placeholder core definition
    if "（待完善概念定義）" in content or "（待完善核心定義）" in content:
        file_issues.append("Core definition is placeholder")
    if "（待完善）" in content:
        file_issues.append("Has placeholder text '（待完善）'")
    
    # 3. Check if core definition section exists
    if "## 核心定義" not in content:
        file_issues.append("Missing ## 核心定義 section")
    
    # 4. Check for duplicate entries (same wiki link appearing twice)
    links = re.findall(r"\[\[([^|]+?)(?:\|[^\]]+)?\]\]", content)
    link_counts = Counter(links)
    dups = {k: v for k, v in link_counts.items() if v > 1}
    if dups:
        for link, count in dups.items():
            file_issues.append(f"Duplicate entry ({count}x): {link[:50]}")
    
    # 5. Check for broken wiki link syntax ([[... without matching ]])
    open_brackets = content.count("[[")
    close_brackets = content.count("]]")
    if open_brackets != close_brackets:
        file_issues.append(f"Mismatched wiki brackets: [[={open_brackets} ]]={close_brackets}")
    
    # 6. Check for lines that break list continuity (blank lines between list items)
    in_list = False
    blank_in_list = 0
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("- [["):
            in_list = True
        elif stripped == "" and in_list:
            blank_in_list += 1
        elif stripped.startswith("## ") or stripped.startswith("---"):
            in_list = False
    
    if blank_in_list > 1:
        file_issues.append(f"{blank_in_list} blank lines inside entry list")
    
    if file_issues:
        stats["with_issues"] += 1
        issues.append((fname, file_issues))
    else:
        stats["ok"] += 1

# Generate report
report_lines = []
report_lines.append("# Wiki Format Audit Report\n")
report_lines.append(f"Total files: {stats['total']}")
report_lines.append(f"Clean: {stats['ok']}")
report_lines.append(f"With issues: {stats['with_issues']}\n")

if issues:
    report_lines.append("## Issues by File\n")
    for fname, file_issues in issues:
        report_lines.append(f"### {fname}")
        for iss in file_issues:
            report_lines.append(f"- {iss}")
        report_lines.append("")

report_path = os.path.join(WIKI_DIR, "..", "98_LOG", "wiki-format-audit.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"Report: {report_path}")
print(f"Total: {stats['total']}, Clean: {stats['ok']}, Issues: {stats['with_issues']}")
