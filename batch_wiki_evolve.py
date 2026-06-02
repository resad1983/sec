"""
Batch Step 7: Knowledge Compilation for all 01_Liter notes.
For each note, inserts entries into 02_wiki/{tag}.md, then sets wiki_evolved: true.
"""
import os, re, json, datetime
from collections import defaultdict

VAULT = r"D:\gemini\obsidian"
LITER_DIR = os.path.join(VAULT, "01_Liter")
WIKI_DIR = os.path.join(VAULT, "02_wiki")
REPORT_DIR = os.path.join(VAULT, "98_LOG")

os.makedirs(REPORT_DIR, exist_ok=True)

# Collect all data
entries_by_tag = defaultdict(list)  # tag -> list of (filename, title, core_insight)
stats = {"total": 0, "skipped_no_tags": 0, "skipped_no_insight": 0, "updated": 0}
log_lines = []

for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8") as f:
        content = f.read()

    # Parse frontmatter
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        log_lines.append(f"SKIP no frontmatter: {fname}")
        continue

    fm_raw = m.group(1)
    title = ""
    tags = []

    for line in fm_raw.split("\n"):
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("tags:"):
            tags_raw = line.split(":", 1)[1].strip()
            # Parse [tag1, tag2] format
            tags = [t.strip().strip("'\"") for t in tags_raw.strip("[]").split(",") if t.strip()]

    if not tags:
        stats["skipped_no_tags"] += 1
        continue

    # Parse core_insight
    # Content between ## 核心洞察\n\n and \n## 重點摘要
    ci_match = re.search(
        r"##\s*核心洞察\s*\n+(.*?)\n+##\s*重點摘要",
        content, re.DOTALL
    )
    core_insight = ""
    if ci_match:
        core_insight = ci_match.group(1).strip()

    if not core_insight:
        stats["skipped_no_insight"] += 1
        core_insight = "(待補核心洞察)"

    slug = fname.replace(".md", "")
    for tag in tags:
        entries_by_tag[tag].append((slug, title, core_insight))

    stats["total"] += 1
    stats["updated"] += 1

log_lines.append(f"Total notes processed: {stats['total']}")
log_lines.append(f"Skipped (no tags): {stats['skipped_no_tags']}")
log_lines.append(f"Skipped (no core insight): {stats['skipped_no_insight']}")

# Write/update wiki files
wiki_updated = []
for tag in sorted(entries_by_tag.keys()):
    tag_file = os.path.join(WIKI_DIR, f"{tag}.md")
    entries = entries_by_tag[tag]

    # Build new entry block
    new_entries = []
    for slug, title, insight in entries:
        new_entries.append(f"- [[{slug}|{title}]]：{insight}")

    new_block_text = "\n".join(new_entries)

    if not os.path.exists(tag_file):
        # Create new wiki file
        wiki_content = f"""---
title: {tag}
type: 核心概念
---

# {tag}

## 核心定義
（待 AI 根據累積的洞察補充定義）

## 實踐洞察與案例
{new_block_text}
"""
        with open(tag_file, "w", encoding="utf-8") as f:
            f.write(wiki_content)
        wiki_updated.append(f"CREATED {tag}.md ({len(entries)} entries)")
        log_lines.append(f"CREATED 02_wiki/{tag}.md with {len(entries)} entries")
    else:
        with open(tag_file, encoding="utf-8", errors="replace") as f:
            existing = f.read()

        # Check if section exists
        section_marker = "## 實踐洞察與案例"
        if section_marker in existing:
            # Insert after the section header (find the first blank line after header or the next section)
            # Find position of section header
            pos = existing.index(section_marker)
            # Find content after the header
            rest = existing[pos + len(section_marker):]
            # Look for the first non-blank line after header, or next ##
            insert_pos = pos + len(section_marker)
            # Skip blank lines after header
            while insert_pos < len(existing) and existing[insert_pos] in '\n\r ':
                insert_pos += 1
            # Check if the next non-blank text is another section
            next_section = existing.find("\n##", insert_pos)
            if next_section == -1:
                next_section = len(existing)

            # Insert new entries at the beginning of the section content
            section_content_start = insert_pos
            # But we need to handle the case where there's just a blank after the header
            # and then the next section or end of file

            # Let's find: after "## 實踐洞察與案例\n", we want to insert new entries
            # followed by \n\n, then the existing content of that section
            header_end = pos + len(section_marker)
            # Find where the section content starts (skip blank lines)
            content_start = header_end
            while content_start < len(existing) and existing[content_start] in '\n\r ':
                content_start += 1

            # Build new content
            before = existing[:content_start]
            # Get existing section content (up to next ## or end)
            next_section_pos = existing.find("\n## ", content_start)
            if next_section_pos == -1:
                existing_content = existing[content_start:]
                after = ""
            else:
                existing_content = existing[content_start:next_section_pos]
                after = existing[next_section_pos:]

            # Strip blank lines from existing_content
            existing_content_stripped = existing_content.strip()

            if existing_content_stripped:
                new_section_content = new_block_text + "\n" + existing_content_stripped + "\n"
            else:
                new_section_content = new_block_text + "\n"

            new_file_content = before + new_section_content + after
        else:
            # Add the section
            new_file_content = existing.rstrip() + f"\n\n## 實踐洞察與案例\n{new_block_text}\n"

        with open(tag_file, "w", encoding="utf-8") as f:
            f.write(new_file_content)
        wiki_updated.append(f"UPDATED {tag}.md (+{len(entries)} entries)")
        log_lines.append(f"UPDATED 02_wiki/{tag}.md with {len(entries)} new entries")

# Now update wiki_evolved: true in all 01_Liter files
evolved_count = 0
for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Check if already true
    if "wiki_evolved: true" in content:
        continue

    new_content = content.replace("wiki_evolved: false", "wiki_evolved: true", 1)
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        evolved_count += 1

log_lines.append(f"\nWiki files updated: {len(wiki_updated)}")
log_lines.append(f"Notes marked wiki_evolved: true: {evolved_count}")
for w in wiki_updated:
    log_lines.append(f"  {w}")

report = f"""# Batch Wiki Evolution Report
Date: {datetime.date.today()}

## Summary
- Total notes processed: {stats['total']}
- Skipped (no tags): {stats['skipped_no_tags']}
- Skipped (no core insight): {stats['skipped_no_insight']}
- Wiki files created/updated: {len(wiki_updated)}
- Notes marked wiki_evolved: true: {evolved_count}

## Tags Updated
"""
for w in wiki_updated:
    report += f"- {w}\n"

report_path = os.path.join(REPORT_DIR, f"wiki-evolve-{datetime.date.today().isoformat()}.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report)

print(f"Done! Report: {report_path}")
print(f"Notes: {stats['total']}, Wiki files: {len(wiki_updated)}, Evolved: {evolved_count}")
