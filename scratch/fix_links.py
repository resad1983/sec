import os
import re

liter_dir = r"D:\gemini\obsidian\01_Liter"
all_files = os.listdir(liter_dir)
target_prefixes = "2026-05-30-"

for filename in all_files:
    if not filename.startswith(target_prefixes):
        continue
    if "擺脫成長瓶頸" in filename or "誠品衝刺營運" in filename or "During off-peak" in filename:
        continue
        
    filepath = os.path.join(liter_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. 修正 "### 2. 顧問..." 的標題 (有些是啟發，有些是應用)
        content = re.sub(r"###\s*2\.\s*顧問與地方創生.*?\n", "## 重點摘要\n", content)
        
        # 2. 清洗 raw_ref 欄位中的 [[路徑|路徑]] 變成 [[路徑]]
        content = re.sub(r'raw_ref:\s*"\[\[(.*?)\|(.*?)\]\]"', r'raw_ref: "[[\1]]"', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        pass
