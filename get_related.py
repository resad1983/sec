import pathlib, yaml, sys
if sys.stdout.encoding != 'utf-8': sys.stdout.reconfigure(encoding='utf-8', errors='replace')
tags = set(sys.argv[1].split(','))
LITER = pathlib.Path(r'C:/Users/resad.huang/Documents/COWORK/PROJECTS/obsidian/sec/01_Liter')
results = []
for f in sorted(LITER.glob('*.md'), reverse=True):
    content = f.read_text(encoding='utf-8', errors='replace')
    if not content.startswith('---'): continue
    end = content.find('\n---', 3)
    if end == -1: continue
    try: meta = yaml.safe_load(content[3:end]) or {}
    except: continue
    ft = meta.get('tags', [])
    if isinstance(ft, str): ft = [ft]
    overlap = len(tags & set(ft))
    if overlap > 0: results.append((overlap, f.stem, meta.get('title', f.stem)))

results.sort(key=lambda x: -x[0])
for _, stem, title in results[:3]: 
    print(f'[[{stem}|{title}]]')
if not results: 
    print('#待連結')
