"""
Fix 營運管理.md - keep first clean copy, remove all trailing duplicates.
"""
fpath = r"D:\gemini\obsidian\02_wiki\營運管理.md"
with open(fpath, encoding="utf-8") as f:
    lines = f.readlines()

# Lines 74-101 are duplicates or corrupted - remove them
# Keep lines 0-72 (1-73 1-indexed)
clean = lines[:73]
with open(fpath, "w", encoding="utf-8") as f:
    f.writelines(clean)

print(f"Kept {len(clean)} lines, removed {len(lines) - len(clean)} trailing duplicate lines")
