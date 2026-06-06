from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE = Path("D:/gemini/obsidian")
WIKI = BASE / "02_wiki"
ARCHIVE = BASE / "021_wiki"
TOPICS = BASE / "022_wiki_topics"
TOOLS = BASE / "scratch" / "wiki_tools"
BACKUP_ROOT = BASE / "scratch" / f"wiki_cleanup_backup_{datetime.now():%Y%m%d_%H%M%S}"
REPORT = BASE / "wiki_cleanup_report.md"

STANDARD_TAGS = [
    "人工智慧",
    "人格與自我",
    "人機互動",
    "心理",
    "文化現象",
    "世代變遷",
    "市場與需求",
    "平台與生態系",
    "生活方式",
    "地方創生",
    "行為決策",
    "行銷",
    "社會結構",
    "社群與關係網絡",
    "品牌",
    "城市與空間",
    "科技影響",
    "商業模式",
    "情緒與關係",
    "產品",
    "組織與策略",
    "設計",
    "創作方法",
    "媒體與敘事",
    "資料與演算法",
    "價值與定價",
    "數位系統",
    "學習與思考",
    "營運管理",
    "體驗",
]
STANDARD_SET = set(STANDARD_TAGS)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def backup(path: Path) -> None:
    if not path.exists():
        return
    target = BACKUP_ROOT / path.relative_to(BASE)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)


def link_target(line: str) -> str | None:
    match = re.search(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", line)
    if not match:
        return None
    return match.group(1).split("/")[-1]


def case_date(line: str) -> str:
    target = link_target(line) or ""
    match = re.match(r"(\d{4}-\d{2}-\d{2})", target)
    return match.group(1) if match else "0000-00-00"


def quarter_for(line: str) -> str:
    date = case_date(line)
    match = re.match(r"(\d{4})-(\d{2})-\d{2}", date)
    if not match or match.group(1) == "0000":
        now = datetime.now()
        return f"{now.year}Q{((now.month - 1) // 3) + 1}"
    year = match.group(1)
    month = int(match.group(2))
    if month < 1 or month > 12:
        now = datetime.now()
        return f"{now.year}Q{((now.month - 1) // 3) + 1}"
    return f"{year}Q{((month - 1) // 3) + 1}"


def unique_cases(lines: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for line in lines:
        target = link_target(line)
        key = target or line
        if key in seen:
            continue
        seen.add(key)
        result.append(line.rstrip())
    return result


def extract_frontmatter(text: str, tag: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return f"---{parts[1]}---".strip()
    return f"---\ntitle: {tag}\ntype: 核心概念\nwiki_evolved: true\n---"


def extract_core_definition(text: str) -> list[str]:
    match = re.search(r"^## 核心定義\s*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    if not match:
        return []
    body = [line.rstrip() for line in match.group(1).splitlines()]
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return body


def extract_cases(text: str) -> list[str]:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- [["):
            continue
        if "021_wiki/" in stripped:
            continue
        lines.append(stripped)
    return unique_cases(lines)


def ensure_archive(tag: str, quarter: str, lines: list[str]) -> tuple[Path, int]:
    archive_path = ARCHIVE / f"{tag}_{quarter}.md"
    backup(archive_path)
    if archive_path.exists():
        text = read_text(archive_path)
    else:
        text = (
            f"---\n"
            f"title: {tag} {quarter}\n"
            f"type: wiki_archive\n"
            f"parent: [[{tag}]]\n"
            f"period: {quarter}\n"
            f"---\n\n"
            f"# {tag} {quarter}\n\n"
            f"## 實踐洞察與案例\n"
        )

    existing_targets = {target for target in (link_target(line) for line in text.splitlines()) if target}
    additions = [line for line in lines if (link_target(line) or line) not in existing_targets]
    if not additions:
        return archive_path, 0

    if "## 實踐洞察與案例" not in text:
        text = text.rstrip() + "\n\n## 實踐洞察與案例\n"
    text = text.rstrip() + "\n" + "\n".join(additions) + "\n"
    write_text(archive_path, text)
    return archive_path, len(additions)


def archive_links(tag: str) -> list[str]:
    pattern = re.compile(rf"^{re.escape(tag)}_(\d{{4}}Q[1-4])\.md$")
    quarters = []
    for path in ARCHIVE.glob(f"{tag}_*.md"):
        match = pattern.match(path.name)
        if match:
            quarters.append(match.group(1))
    return [f"- [[021_wiki/{tag}_{quarter}|{quarter}]]" for quarter in sorted(set(quarters), reverse=True)]


def rebuild_standard_page(path: Path) -> dict:
    tag = path.stem
    text = read_text(path)
    cases = extract_cases(text)
    sorted_cases = sorted(cases, key=case_date, reverse=True)
    keep = sorted_cases[:30]
    move = sorted_cases[30:]

    moved_by_quarter: dict[str, list[str]] = defaultdict(list)
    for line in move:
        moved_by_quarter[quarter_for(line)].append(line)

    archive_additions = 0
    touched_archives = []
    for quarter, lines in sorted(moved_by_quarter.items(), reverse=True):
        archive_path, added = ensure_archive(tag, quarter, lines)
        archive_additions += added
        touched_archives.append(archive_path.name)

    backup(path)
    frontmatter = extract_frontmatter(text, tag)
    core = extract_core_definition(text)
    output: list[str] = [frontmatter, "", f"# {tag}", ""]
    if core:
        output.extend(["## 核心定義", *core, ""])
    output.extend(["## 實踐洞察與案例", *keep, ""])
    links = archive_links(tag)
    if links:
        output.extend(["## 歸檔", *links, ""])
    write_text(path, "\n".join(output).rstrip() + "\n")

    return {
        "page": path.name,
        "original_cases": len(cases),
        "kept_cases": len(keep),
        "moved_cases": len(move),
        "archive_additions": archive_additions,
        "archives": touched_archives,
    }


def move_content_file(src: Path, dest_dir: Path) -> Path:
    backup(src)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if dest.exists():
        suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = dest_dir / f"{src.stem}_{suffix}{src.suffix}"
    shutil.move(str(src), str(dest))
    return dest


def audit() -> dict:
    markdown = list(WIKI.glob("*.md"))
    non_markdown = [p for p in WIKI.iterdir() if p.is_file() and p.suffix.lower() != ".md"]
    non_standard = [p.name for p in markdown if p.stem not in STANDARD_SET]
    standard_counts = {}
    over_30 = []
    for path in markdown:
        if path.stem not in STANDARD_SET:
            continue
        count = len(extract_cases(read_text(path)))
        standard_counts[path.name] = count
        if count > 30:
            over_30.append((path.name, count))
    return {
        "markdown_count": len(markdown),
        "non_markdown": [p.name for p in non_markdown],
        "non_standard": sorted(non_standard),
        "standard_pages": len([p for p in markdown if p.stem in STANDARD_SET]),
        "over_30": sorted(over_30),
        "standard_counts": standard_counts,
    }


def main() -> None:
    before = audit()
    moved_tools = []
    moved_topics = []

    for path in sorted(WIKI.iterdir()):
        if path.is_file() and path.suffix.lower() != ".md":
            moved_tools.append({"from": path.name, "to": str(move_content_file(path, TOOLS).relative_to(BASE))})

    for path in sorted(WIKI.glob("*.md")):
        if path.stem not in STANDARD_SET:
            moved_topics.append({"from": path.name, "to": str(move_content_file(path, TOPICS).relative_to(BASE))})

    rebuilt = []
    for tag in STANDARD_TAGS:
        path = WIKI / f"{tag}.md"
        if path.exists():
            rebuilt.append(rebuild_standard_page(path))

    after = audit()
    result = {
        "backup": str(BACKUP_ROOT.relative_to(BASE)),
        "before": before,
        "moved_tools": moved_tools,
        "moved_topics": moved_topics,
        "rebuilt": rebuilt,
        "after": after,
    }

    lines = [
        "# Wiki 清理報告",
        "",
        f"產生時間：{datetime.now():%Y-%m-%d %H:%M:%S}",
        "",
        "## 備份位置",
        "",
        f"- `{result['backup']}`",
        "",
        "## 移出 02_wiki 的工具檔",
        "",
    ]
    lines.extend([f"- `{item['from']}` → `{item['to']}`" for item in moved_tools] or ["- 無"])
    lines.extend(["", "## 移到 022_wiki_topics 的頁面", ""])
    lines.extend([f"- `{item['from']}` → `{item['to']}`" for item in moved_topics] or ["- 無"])
    lines.extend(["", "## 標準主頁瘦身結果", ""])
    for item in rebuilt:
        lines.append(
            f"- `{item['page']}`：{item['original_cases']} → {item['kept_cases']} 條近期案例，"
            f"搬移 {item['moved_cases']} 條，新增歸檔 {item['archive_additions']} 條"
        )
    lines.extend(["", "## 清理後 Audit", ""])
    lines.append(f"- `02_wiki` Markdown 檔案數：{after['markdown_count']}")
    lines.append(f"- 標準標籤主頁：{after['standard_pages']} / {len(STANDARD_TAGS)}")
    lines.append(f"- 非 Markdown 檔案：{len(after['non_markdown'])}")
    lines.append(f"- 非標準頂層頁：{len(after['non_standard'])}")
    lines.append(f"- 超過 30 條案例的標準主頁：{len(after['over_30'])}")
    write_text(REPORT, "\n".join(lines).rstrip() + "\n")

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
