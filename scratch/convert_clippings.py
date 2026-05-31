import os
import sys
import subprocess

# 強制使用 utf-8 輸出
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 嘗試載入 opencc，若無則嘗試安裝
try:
    from opencc import OpenCC
except ImportError:
    print("找不到 opencc，嘗試安裝 opencc-python-reimplemented...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "opencc-python-reimplemented"])
        from opencc import OpenCC
    except Exception as e:
        print(f"安裝 opencc 失敗: {e}")
        sys.exit(1)

cc = OpenCC('s2t') # 簡體到繁體

# 定義 24 個檔案的原始簡體檔名與對應的繁體檔名對照表
# 這樣可以確保檔名與 task.md 完全一致
clippings_map = {
    "Charlene：把文化变成一件可以用的事.md": "Charlene：把文化變成一件可以用的事.md",
    "一个行业正在被AI悄悄重写.md": "一個行業正在被AI悄悄重寫.md",
    "不想做饭的年轻人，爱上成人辅食.md": "不想做飯的年輕人，愛上成人輔食.md",
    "不想结婚了，只想找人同居.md": "不想結婚了，只想找人同居.md",
    "中产三宝，杀出一个新劲敌.md": "中產三寶，殺出一個新勁敵.md",
    "中国人的肠道里，藏着一张饮食地图.md": "中國人的腸道裡，藏著一張飲食地圖.md",
    "倦怠社会中的鸡尾酒效应：青年健身趣缘群体的身份重构.md": "倦怠社會中的雞尾酒效應：青年健身趣緣群體的身份重構.md",
    "卖不出去的Apple Watch，被出片女孩炒火了？.md": "賣不出去的Apple Watch，被出片女孩炒火了？.md",
    "压迫，很多时候以真理的姿态出现.md": "壓迫，很多時候以真理的姿態出現.md",
    "天津大悦城，如何把青年文化做成慢生意.md": "天津大悅城，如何把青年文化做成慢生意.md",
    "奶茶界ENFP，用快乐感染年轻人.md": "奶茶界ENFP，用快樂感染年輕人.md",
    "对广州，聚龙湾到底改变了什么.md": "對廣州，聚龍灣到底改變了什麼.md",
    "小山姆成了商场B1新顶流.md": "小山姆成了商場B1新頂流.md",
    "小红书彻底爆发了.md": "小紅書徹底爆發了.md",
    "当AI成为你的同事，组织真的开始变了.md": "當AI成為你的同事，組織真的開始變了.md",
    "当代打工人，把阿福用成了工伤银行.md": "當代打工人，把阿福用成了工傷銀行.md",
    "快闪，正在成为商场的主菜.md": "快閃，正在成為商場的主菜.md",
    "永生，会成为有钱人的特权吗？.md": "永生，會成為有錢人的特權嗎？.md",
    "猫都已经有小天才手表了.md": "貓 dead 已經有小天才手錶了 (貓都已經有小天才手錶了).md", # 根據 task.md 的檔名對應
    "聊聊那些拿到结果的主理人.md": "聊聊那些拿到結果的主理人.md",
    "腾讯综艺，重写内娱的造人逻辑.md": "騰訊綜藝，重寫內娛的造人邏輯.md",
    "花知晓接住了珀莱雅的增长焦虑.md": "花知曉接住了珀萊雅的增長焦慮.md",
    "长鑫科技上市，合肥为何逢赌必赢.md": "長鑫科技上市，合肥為何逢賭必贏.md",
    "阿里们并不需要标价50亿美元的朴朴.md": "阿里們並不需要標價50億美元的朴朴.md"
}

clippings_dir = r"D:\gemini\obsidian\Clippings"
inbox_dir = r"D:\gemini\obsidian\00_Inbox\2026-05-30"

if not os.path.exists(inbox_dir):
    os.makedirs(inbox_dir)

success_count = 0
for src_name, dest_name in clippings_map.items():
    src_path = os.path.join(clippings_dir, src_name)
    # 有些檔案可能是檔名有微調，我們做模糊匹配
    if not os.path.exists(src_path):
        # 尋找部分匹配的
        base = os.path.splitext(src_name)[0]
        found = False
        for f in os.listdir(clippings_dir):
            if base in f or f in base:
                src_path = os.path.join(clippings_dir, f)
                found = True
                break
        if not found:
            print(f"找不到檔案: {src_name}")
            continue
            
    dest_path = os.path.join(inbox_dir, dest_name)
    
    try:
        with open(src_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # 進行簡轉繁
        converted_content = cc.convert(content)
        
        # 寫入 00_Inbox
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(converted_content)
            
        print(f"成功備份並繁體化: {src_name} -> {dest_name}")
        success_count += 1
    except Exception as e:
        print(f"處理 {src_name} 失敗: {e}")

print(f"處理完成，成功轉換 {success_count} 個檔案。")
