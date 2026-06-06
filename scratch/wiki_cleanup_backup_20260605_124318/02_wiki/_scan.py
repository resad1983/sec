import os, glob, re

results = []

for fpath in sorted(glob.glob('D:/gemini/obsidian/02_wiki/*.md')):
    fname = os.path.basename(fpath)
    issues = []
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        total = len(lines)
        while total > 0 and lines[total-1].strip() == '':
            total -= 1
    
    # 1. File size
    if total > 100:
        issues.append('maybe_too_long_' + str(total))
    
    # 2. Empty entries
    empty_wikilinks = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        m = re.match(r'^-?\s*\[\[([^\]]+)\]\](.*)$', stripped)
        if m:
            after = m.group(2).strip()
            if after == '' or after == '\uff1a' or after == ':' or after.startswith('\uff1a/') or after.startswith(':/'):
                empty_wikilinks.append((i, stripped[:60]))
    if empty_wikilinks:
        sample = '; '.join([f'L{l}: {t}' for l, t in empty_wikilinks[:5]])
        issues.append(f'blank_entries ({len(empty_wikilinks)} spots, e.g. {sample})')
    
    # 3. Broken footers
    broken_footer_matches = []
    for i, line in enumerate(lines, 1):
        if '021_wiki/' in line:
            broken_footer_matches.append(i)
    if broken_footer_matches:
        issues.append(f'broken_path_021_wiki/ (at {len(broken_footer_matches)} lines, e.g. L{broken_footer_matches[0]})')
    
    # 4. Format mix
    has_gt = False
    has_dash = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('\uff1a>'):
            has_gt = True
        if stripped.startswith('\uff1a-'):
            has_dash = True
    if has_gt and has_dash:
        issues.append('mixed_format ：> and ：-')
    
    # 5. Duplicate links
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    link_counts = {}
    for link in wikilinks:
        link = link.split('|')[0]
        link_counts[link] = link_counts.get(link, 0) + 1
    dups = {k: v for k, v in link_counts.items() if v > 1 and k != ''}
    if dups:
        dup_list = sorted(dups.items(), key=lambda x: -x[1])[:3]
        dup_text = '; '.join([f'{k} ({v}x)' for k, v in dup_list])
        issues.append(f'duplicate_links ({len(dups)} groups, e.g. {dup_text})')
    
    # 6. Flat structure
    headers = [l for l in lines if l.strip().startswith('#')]
    if total > 100 and len(headers) <= 1:
        issues.append('flat_structure: >100 lines with no section headers')
    
    # 7. Empty shell with subpage links
    subpage_links = re.findall(r'\[\[([^\]]+/[^\]]+)\]\]', content)
    has_subpages = len(subpage_links) > 0
    if total <= 30 and has_subpages:
        issues.append('shell_page: minimal content but has subpage links')
    
    # Priority
    priority = 'high'
    if not issues:
        priority = 'low'
    elif len(issues) == 1:
        pri_issue = issues[0]
        if 'maybe_too_long' in pri_issue:
            priority = 'low'
        elif 'mixed_format' in pri_issue:
            priority = 'medium'
        elif 'duplicate_links' in pri_issue:
            priority = 'medium'
        elif 'blank_entries' in pri_issue:
            priority = 'high'
        else:
            priority = 'high'
    elif all('maybe_too_long' in i for i in issues if 'maybe_too_long' in i):
        priority = 'medium'
    else:
        priority = 'high'
    
    results.append((fname, total, issues, priority))

for fname, lines, issues, priority in results:
    issue_str = '; '.join(issues) if issues else 'none'
    print(f'FILE|{fname}|{lines}|{issue_str}|{priority}')

print(f'\nSUMMARY|Total files: {len(results)}')
print(f'SUMMARY|With issues: {sum(1 for _,_,i,_ in results if i)}')
h = sum(1 for _,_,_,p in results if p=="high")
m = sum(1 for _,_,_,p in results if p=="medium")
l = sum(1 for _,_,_,p in results if p=="low")
print(f'SUMMARY|High: {h}  Medium: {m}  Low/Clean: {l}')
