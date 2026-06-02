import os, re

fpath = r"D:\gemini\obsidian\02_wiki\人工智慧.md"
with open(fpath, encoding="utf-8") as f:
    content = f.read()

# Find all mistral references
for line in content.split("\n"):
    if "Mistral" in line and "[[" in line:
        print(repr(line))
        # Try to match
        old_key = "2026-03-31-Mistral AI raises $830M in debt to set up a data center near Paris"
        escaped = re.escape(old_key)
        pattern = r"\[\[" + escaped + r"\|" + escaped + r"\]\]"
        print(f"  Pattern: {pattern}")
        m = re.search(pattern, line)
        print(f"  Match: {m}")
        break
