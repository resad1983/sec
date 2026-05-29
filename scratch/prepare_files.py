import os
import shutil

clippings_dir = r"D:\gemini\obsidian\Clippings"
scratch_dir = r"D:\gemini\obsidian\scratch"

if not os.path.exists(scratch_dir):
    os.makedirs(scratch_dir)

# 定義關鍵字與目標編號的對照表
targets = {
    "34": "数字断连",
    "35": "既下山",
    "36": "杀猪盘",
    "37": "李开复", # 注意：可能匹配到多個，我們取大小最大的那個或特定的一個
    "38": "横店",
    "39": "气球",
    "40": "汤泉",
    "41": "洁丽雅",
    "42": "海底捞",
    "43": "淡季",
    "44": "男色",
    "45": "碳水脸",
    "46": "负鼠",
    "47": "Labubu"
}

files = os.listdir(clippings_dir)
print(f"Total files in Clippings: {len(files)}")

for num, kw in targets.items():
    matched = [f for f in files if kw in f]
    if not matched:
        print(f"Warning: No file matched for {num} ({kw})")
        continue
    
    # 如果有多個匹配，例如李開復，選擇檔名包含 "独家" 的，如果沒有就選第一個，或者最大的
    if len(matched) > 1:
        if num == "37":
            # 優先選包含 独家 的
            dujia = [f for f in matched if "独家" in f]
            selected = dujia[0] if dujia else matched[0]
        else:
            selected = matched[0]
    else:
        selected = matched[0]
        
    src_path = os.path.join(clippings_dir, selected)
    dst_path = os.path.join(scratch_dir, f"{num}.md")
    shutil.copy2(src_path, dst_path)
    print(f"Copied: {selected} -> {num}.md")
