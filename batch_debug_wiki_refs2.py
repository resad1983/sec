import os

fpath = r"D:\gemini\obsidian\02_wiki\人工智慧.md"
with open(fpath, encoding="utf-8") as f:
    content = f.read()

old_keys = [
    "2026-03-31-As more Americans adopt AI tools, fewer say they can trust the results",
    "2026-03-31-Former Coatue partner raises huge $65M seed for enterprise AI agent startup",
    "2026-03-31-Mistral AI raises $830M in debt to set up a data center near Paris",
]

for key in old_keys:
    # Check with [[...|...]] wrapping
    check = f"[[{key}|{key}]]"
    found = check in content
    print(f"  '{check[:60]}...' in file: {found}")
    # Try direct substring
    found2 = key in content
    print(f"  just key '{key[:60]}...' in file: {found2}")
