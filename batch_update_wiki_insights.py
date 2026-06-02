"""
Replace "(待補核心洞察)" in 02_wiki files with actual core insights from 01_Liter.
"""
import os, re

VAULT = r"D:\gemini\obsidian"
LITER_DIR = os.path.join(VAULT, "01_Liter")
WIKI_DIR = os.path.join(VAULT, "02_wiki")

# Pre-load all core insights from 01_Liter
insights = {}  # slug -> (title, core_insight, tags)
for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    slug = fname.replace(".md", "")
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Parse frontmatter for title
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        continue
    fm_raw = m.group(1)
    title = ""
    tags = []
    for line in fm_raw.split("\n"):
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("tags:"):
            tags_raw = line.split(":", 1)[1].strip()
            tags = [t.strip().strip("'\"") for t in tags_raw.strip("[]").split(",") if t.strip()]
    if not title:
        continue

    # Parse core_insight - try both standard and parenthesized heading
    ci_match = re.search(r"##\s*核心洞察.*?\n+(.*?)(?=\n+##\s*重點摘要|\n+##\s*關聯筆記|\n+##\s*值得深思)", content, re.DOTALL)
    core_insight = ""
    if ci_match:
        core_insight = ci_match.group(1).strip()
        # For bullet-point format, take the first bold section
        if core_insight.startswith("-"):
            # Extract text from first bullet: "- **text**：rest" -> "text：rest"
            bullet_match = re.search(r'-\s*\*\*(.+?)\*\*[：:]\s*(.+?)(?:\n|$)', core_insight)
            if bullet_match:
                core_insight = f"{bullet_match.group(1)}：{bullet_match.group(2)}"
            else:
                # Just take first line
                core_insight = core_insight.split("\n")[0].strip().lstrip("- ")

    if not core_insight:
        core_insight = "(待補)"

    if core_insight != "(待補)":
        insights[slug] = (title, core_insight, tags)

print(f"Loaded {len(insights)} insights with core insights")

# Debug: show first 5 insights
for i, (slug, (t, ci, _)) in enumerate(list(insights.items())[:5]):
    print(f"  {slug}: {t} -> {ci[:50]}...")

print(f"Loaded {len(insights)} insights")

# Now update wiki files
total_replaced = 0
for tag_file in sorted(os.listdir(WIKI_DIR)):
    if not tag_file.endswith(".md"):
        continue
    tag = tag_file.replace(".md", "")
    wiki_path = os.path.join(WIKI_DIR, tag_file)

    with open(wiki_path, encoding="utf-8", errors="replace") as f:
        content = f.read()

    lines = content.split("\n")
    new_lines = []
    changed = False

    for line in lines:
        # Check if line has "(待補核心洞察)"
        if "待補核心洞察" in line:
            # Find which slug this line references
            m = re.search(r'\[\[([^\]]+)\]\]', line)
            if m:
                raw = m.group(1)
                slug = raw.split("|")[0]  # strip title part after |
                if slug in insights:
                    _, core_insight, _ = insights[slug]
                    new_line = line.replace("：(待補核心洞察)", f"：{core_insight}")
                    if new_line != line:
                        changed = True
                        total_replaced += 1
                        new_lines.append(new_line)
                        continue
        new_lines.append(line)

    if changed:
        with open(wiki_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print(f"UPDATED {tag_file}")

print(f"\nTotal replacements: {total_replaced}")
