# -*- coding: utf-8 -*-
import os

wiki_dir = r"D:\gemini\obsidian\02_wiki"

def add_case_to_wiki(filename, new_case_line):
    filepath = os.path.join(wiki_dir, filename)
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = "## 實踐洞察與案例"
    if target not in content:
        print(f"Error: {target} not found in {filename}")
        return
    
    # 找到 target 的位置
    idx = content.find(target)
    # 插入在新行
    insert_pos = idx + len(target)
    # 找到 target 後面的換行符
    newline_pos = content.find('\n', insert_pos)
    if newline_pos == -1:
        content = content + "\n" + new_case_line
    else:
        content = content[:newline_pos+1] + new_case_line + "\n" + content[newline_pos+1:]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {filename}")

# 1. 商業模式.md
case_business = "- [[2026-05-29-李開復內部談話：今年15億訂單，2027年IPO｜獨家|李開復內部談話：今年15億訂單，2027年IPO]]：剖析了零一萬物從技術理想主義向「商業現實主義」的戰略換擋；其專注於高毛利、高複購的 To B ARR 商業模式，以及與客戶「共創合資公司」共享長期收益的策略，為 AI 2.0 時代的企業提供了自我造血的生存路徑。"
add_case_to_wiki("商業模式.md", case_business)

# 2. 組織與策略.md
case_org = "- [[2026-05-29-李開復內部談話：今年15億訂單，2027年IPO｜獨家|李開復內部談話：今年15億訂單，2027年IPO]]：介紹了零一萬物的「DRI（直接責任人）組織範式」，其實行無視架構與資歷的「動態授權」，讓成事者擁有超越層級的決斷權，高管僅提供 Coach 輔導而非審批，極大釋放了組織中的個體能動性。"
add_case_to_wiki("組織與策略.md", case_org)

# 3. 人工智慧.md
case_ai = "- [[2026-05-29-李開復內部談話：今年15億訂單，2027年IPO｜獨家|李開復內部談話：今年15億訂單，2027年IPO]]：探討了智譜、MiniMax、零一萬物等中國大模型「基模小虎」在 DeepSeek 衝擊下的戰略分化與商業化探索；零一萬物主動放棄超大模型軍備競賽，轉向擁抱產業 AI，致力於成為中國首家盈利打平的 AI 2.0 公司。"
add_case_to_wiki("人工智慧.md", case_ai)
