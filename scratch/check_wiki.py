import os, glob

base = r'D:\gemini\obsidian\02_wiki'
articles = ['2025全国商场', '2026儿童节', 'AI时代最该练', 'AI时代的第一性原理']
labels = ['商場TOP10', '兒童節行銷', 'AI感受直覺', 'AI第一性原理']

tags = ['城市與空間','商業模式','市場與需求','體驗','行銷','品牌','情緒與關係','世代變遷','人工智慧','學習與思考','人格與自我','行為決策','科技影響']

for tag in tags:
    path = os.path.join(base, f'{tag}.md')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    found = []
    for i, article in enumerate(articles):
        if article in content:
            found.append(labels[i])
    if found:
        print(f'{tag}: 已有 {", ".join(found)}')
    else:
        print(f'{tag}: 全無，需插入')
