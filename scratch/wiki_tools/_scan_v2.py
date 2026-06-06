import os, glob, re, collections

def scan_file(fpath):
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
        issues.append(('size', 'size: {} lines'.format(total)))
    
    # 2. Empty entries
    blank_count = 0
    blank_samples = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('---'):
            continue
        m = re.match(r'^-?\s*\[\[([^\]]+)\]\](.*)$', stripped)
        if m:
            after = m.group(2).strip()
            after_clean = after.rstrip('\uff1a:\uff1a/')
            if after_clean == '' or after_clean == '\uff1a' or after_clean == ':':
                blank_count += 1
                if len(blank_samples) < 3:
                    blank_samples.append('L{}: {}'.format(i, stripped[:70]))
    if blank_count > 0:
        issues.append(('blank', 'blank entries ({} spots, e.g. {})'.format(blank_count, ' ; '.join(blank_samples))))
    
    # 3. Broken footers
    broken_lines = []
    for i, line in enumerate(lines, 1):
        if '021_wiki/' in line:
            broken_lines.append(i)
    if broken_lines:
        sample_text = lines[broken_lines[0]-1].strip()[:60] if broken_lines else ''
        issues.append(('broken_path', 'broken 021_wiki/ ({} lines, L{}: {})'.format(len(broken_lines), broken_lines[0], sample_text)))
    
    # 4. Format mix
    has_gt = any(l.strip().startswith('\uff1a>') for l in lines)
    has_dash = any(l.strip().startswith('\uff1a-') for l in lines)
    if has_gt and has_dash:
        issues.append(('mixfmt', 'mixed :> and :- prefixes'))
    
    # 5. Duplicate links
    body = '\n'.join(lines[:-3]) if len(lines) > 3 else content
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)
    link_counts = {}
    for link in wikilinks:
        link = link.split('|')[0]
        link = link.split('/')[-1]
        link_counts[link] = link_counts.get(link, 0) + 1
    dups = {k: v for k, v in link_counts.items() if v > 2}
    if dups:
        dup_list = sorted(dups.items(), key=lambda x: -x[1])[:3]
        dup_str = ' ; '.join(['{}({}x)'.format(k, v) for k, v in dup_list])
        issues.append(('dup', 'duplicate links ({} groups, e.g. {})'.format(len(dups), dup_str)))
    
    # 6. Flat structure
    headers = [l for l in lines if l.strip().startswith('#')]
    if total > 100 and len(headers) <= 2:
        issues.append(('structure', 'flat structure: >100 lines but only {} headers'.format(len(headers))))
    
    # 7. Shell page
    has_subpage_refs = bool(re.findall(r'\[\[02_wiki/[^\]]+\]\]', content))
    if total <= 30 and has_subpage_refs:
        issues.append(('shell', 'shell page: minimal content with subpage links'))
    
    # 8. Corrupted characters
    corrupt = []
    for i, line in enumerate(lines, 1):
        if re.search(r'\?\d+\s+\?\?', line):
            corrupt.append(i)
    if corrupt:
        issues.append(('corrupt', 'corrupted text (lines: {})'.format(', '.join([str(x) for x in corrupt]))))
    
    # Priority
    types = [t for t, _ in issues]
    if not issues:
        priority = 'low'
    elif 'corrupt' in types:
        priority = 'high'
    elif 'broken_path' in types:
        priority = 'high'
    elif 'blank' in types:
        priority = 'high'
    elif 'shell' in types:
        priority = 'high'
    elif 'structure' in types:
        priority = 'high'
    elif 'mixfmt' in types:
        priority = 'medium'
    elif 'dup' in types:
        priority = 'medium'
    elif 'size' in types and len(issues) == 1:
        priority = 'low'
    else:
        priority = 'medium'
    
    return fname, total, issues, priority

results = []
for fpath in sorted(glob.glob('D:/gemini/obsidian/02_wiki/*.md')):
    results.append(scan_file(fpath))

# Print
print('{:<28} {:>4}  {:<85} {:<6}'.format('File', 'Lines', 'Issues', 'Priority'))
print('=' * 128)
for fname, lines, issues, priority in results:
    issue_str = ' ; '.join([d for _, d in issues]) if issues else '-'
    print('{:<28} {:>4}  {:<85} {:<6}'.format(fname, lines, issue_str, priority))

# Summary
print()
h = sum(1 for _,_,_,p in results if p=='high')
m = sum(1 for _,_,_,p in results if p=='medium')
l = sum(1 for _,_,_,p in results if p=='low')
print('Total files: {} | High: {} | Medium: {} | Low/None: {}'.format(len(results), h, m, l))
print()
print('=== Issue Frequency ===')
all_types = [t for _,_,issues,_ in results for t,_ in issues]
cnt = collections.Counter(all_types)
for t, c in cnt.most_common():
    print('  {}: {} files'.format(t, c))
