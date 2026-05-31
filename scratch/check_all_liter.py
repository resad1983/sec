import os
import re

liter_dir = r"D:\gemini\obsidian\01_Liter"
all_files = os.listdir(liter_dir)

bad_files = []

for filename in all_files:
    if not filename.endswith(".md"):
        continue
        
    filepath = os.path.join(liter_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. 檢測 frontmatter
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        reasons = []
        
        if not match:
            reasons.append("缺少 YAML frontmatter")
        else:
            fm = match.group(1)
            # 檢測必填
            required = ["title:", "date:", "tags:", "project:"]
            for r_f in required:
                if r_f not in fm:
                    reasons.append(f"缺少必填欄位 {r_f}")
            # 檢測標準欄位
            standards = ["source:", "keywords:", "type:", "raw_ref:", "wiki_evolved:", "links:", "status:"]
            for s_f in standards:
                if s_f not in fm:
                    reasons.append(f"缺少標準欄位 {s_f}")
                    
        # 2. 檢測標題
        if "### 1." in content or "### 1. 核心洞察" in content:
            reasons.append("使用###三級標題")
            
        # 3. 檢測金句
        if "> [!TIP]" not in content:
            reasons.append("缺少結尾TIP金句")
            
        if reasons:
            bad_files.append((filename, reasons))
            
    except Exception as e:
        bad_files.append((filename, [f"讀取錯誤: {str(e)}"]))

# 寫入檢查報告
report_path = os.path.join(liter_dir, "..", "scratch", "all_liter_check_report.txt")
with open(report_path, "w", encoding="utf-8") as out:
    out.write(f"=== 01_Liter 全局格式體檢報告 ===\n")
    out.write(f"總共掃描檔案數: {len([f for f in all_files if f.endswith('.md')])} 篇\n")
    out.write(f"不合格式檔案數: {len(bad_files)} 篇\n\n")
    
    for name, reasons in bad_files:
        out.write(f"- {name}\n")
        for reason in reasons:
            out.write(f"  * {reason}\n")
