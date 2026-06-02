"""
Deduplicate 營運管理.md - remove the duplicated list block.
The file has:
  - Lines 7-9: header + definition
  - Lines 10-75: first occurrence of entry list
  - Lines 76-140: DUPLICATE of lines 10-75
  - Lines 141-165: additional entries (keep these)

Also remove the Vpon warning block that breaks list continuity.
"""
import re

fpath = r"D:\gemini\obsidian\02_wiki\營運管理.md"

with open(fpath, encoding="utf-8") as f:
    content = f.read()

# Strategy: Parse the file into sections
# We know the duplicate starts at the second occurrence of the first entry
# Let's find all entry lines and identify the duplicate

lines = content.split("\n")

# Find the first line of the second duplicate block
# It starts with the same entry as line index where the first entry appears
entry_lines = [i for i, l in enumerate(lines) if l.strip().startswith("- [[2026-03-27-AI提升20%生產力")]
print(f"First entry appears at line indices: {entry_lines}")

# entry_lines should show [10, 75] (or similar) - the second is the duplicate start
if len(entry_lines) >= 2:
    dup_start = entry_lines[1]
    # Now find where the duplicate block ends (before the additional entries)
    # Lines 141+ are additional entries, so dup_end should be the last entry before that
    # Find the last entry in the dup block - look for the line before "2026-05-30-擺脫成長瓶頸"
    additional_start = None
    for i in range(dup_start, len(lines)):
        if "2026-05-30-擺脫成長瓶頸台灣零售業" in lines[i] and lines[i].strip().startswith("- [["):
            additional_start = i
            break
    
    if additional_start:
        # Remove lines from dup_start to additional_start - 1
        new_lines = lines[:dup_start] + lines[additional_start:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print(f"Removed lines {dup_start} to {additional_start - 1}. New total: {len(new_lines)} lines")
    else:
        print("Could not find additional entries section")
else:
    print("No duplicate found")
