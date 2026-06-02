import os, re
from collections import Counter

VAULT = r"D:\gemini\obsidian"
LITER_DIR = os.path.join(VAULT, "01_Liter")
OUT = os.path.join(VAULT, "98_LOG", "sample-null-notes.md")

samples = []
for fname in sorted(os.listdir(LITER_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(LITER_DIR, fname)
    with open(fpath, encoding="utf-8", errors="replace") as f:
        content = f.read()
    if "project: [~]" not in content:
        continue
    
    m = re.match(r"^---\s*\n(.*?)\n", content)
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
    samples.append((fname, title, tags))

all_tags = Counter()
for _, _, tags in samples:
    for t in tags:
        all_tags[t] += 1

lines = []
lines.append("# Sample of 441 Null Notes\n")
lines.append(f"Total: {len(samples)}\n")
lines.append("## Tag Distribution\n")
lines.append("| Tag | Count |")
lines.append("|---|---|")
for tag, count in all_tags.most_common(30):
    lines.append(f"| {tag} | {count} |")

lines.append("\n## First 50 Notes\n")
lines.append("| # | Title | Tags |")
lines.append("|---|---|---|")
for i, (fname, title, tags) in enumerate(samples[:50], 1):
    tag_str = ", ".join(tags[:4]) if tags else "(none)"
    lines.append(f"| {i} | {title[:80]} | {tag_str} |")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Written to {OUT}")
