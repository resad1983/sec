import os, glob, re, collections

def analyze_file(fpath):
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
        issues.append('size>100 ({})'.format(total))
    
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
                link_name = m.group(1).split('|')[-1][:30]
                blank_count += 1
                if len(blank_samples) < 2:
                    blank_samples.append('L{}: {}'.format(i, link_name))
    if blank_count > 0:
        issues.append('blank x{} (e.g. {})'.format(blank_count, '; '.join(blank_samples)))
    
    # 3. Broken footers 021_wiki/
    broken_lines = []
    corrupt_lines = []
    for i, line in enumerate(lines, 1):
        if '021_wiki/' in line:
            broken_lines.append(i)
            if re.search(r'\?\d+\s+\?\?', line):
                corrupt_lines.append(i)
    if broken_lines:
        extra = ''
        if corrupt_lines:
            extra = ' + garbage at L{}'.format(','.join([str(x) for x in corrupt_lines]))
        sample = lines[broken_lines[0]-1].strip()[-30:]
        issues.append('021_wiki/ x{} (e.g. L{}: ...{}){}'.format(
            len(broken_lines), broken_lines[0], sample, extra))
    
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
        issues.append('duplicate x{} (e.g. {} appears {}x)'.format(
            len(dups), dup_list[0][0][:25], dup_list[0][1]))
    
    # 6. Flat structure
    headers = [l for l in lines if l.strip().startswith('#')]
    if total > 100 and len(headers) <= 2:
        issues.append('flat_list (>100 lines, {} headers only)'.format(len(headers)))
    
    # 7. Shell page
    has_subpage_refs = bool(re.findall(r'\[\[02_wiki/[^\]]+\]\]', content))
    if total <= 30 and has_subpage_refs:
        issues.append('shell_page (minimal content)')
    
    # Priority
    if not issues:
        priority = 'LOW'
    elif any('021_wiki/' in i for i in issues):
        if any('garbage' in i for i in issues):
            priority = 'HIGH'
        elif len(broken_lines) >= 3:
            priority = 'HIGH'
        elif any('blank' in i for i in issues):
            priority = 'HIGH'
        else:
            priority = 'MED'
    elif any('blank' in i for i in issues):
        priority = 'HIGH'
    elif any('flat_list' in i for i in issues):
        priority = 'HIGH'
    elif any('shell_page' in i for i in issues):
        priority = 'HIGH'
    elif any('duplicate' in i for i in issues):
        priority = 'MED'
    elif total > 100 and len(issues) == 1:
        priority = 'LOW'
    else:
        priority = 'MED'
    
    return fname, total, issues, priority

results = []
for fpath in sorted(glob.glob('D:/gemini/obsidian/02_wiki/*.md')):
    results.append(analyze_file(fpath))

print('=' * 130)
print('{:28s} {:>4s}  {:75s} {:>6s}'.format('File', 'Lines', 'Issues', 'Priority'))
print('=' * 130)
for fname, lines, issues, priority in results:
    issue_str = ' ; '.join(issues) if issues else '-'
    print('{:28s} {:>4d}  {:75s} {:>6s}'.format(fname, lines, issue_str[:75], priority))

print()
h = sum(1 for _,_,_,p in results if p == 'HIGH')
m = sum(1 for _,_,_,p in results if p == 'MED')
l = sum(1 for _,_,_,p in results if p == 'LOW')
print('SUMMARY: {} files | HIGH: {} | MED: {} | LOW/clean: {}'.format(len(results), h, m, l))

# Clean files
clean = [(f, l) for f, l, i, p in results if not i]
print()
print('Clean files ({}):'.format(len(clean)))
for f, l in clean:
    print('  - {} ({} lines)'.format(f, l))

# Issue frequency
print()
print('Issue frequency:')
all_type_text = []
for _,_,issues,_ in results:
    for i in issues:
        cat = i.split()[0]
        all_type_text.append(cat)
cnt = collections.Counter(all_type_text)
for t, c in cnt.most_common():
    print('  {}: {} files'.format(t, c))
