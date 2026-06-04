import pathlib
import sys

import yaml

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_DIR = pathlib.Path(__file__).resolve().parent
LITER_DIR = VAULT_DIR / "01_Liter"


def parse_tags(raw):
    return {tag.strip() for tag in raw.split(",") if tag.strip()}


def read_frontmatter(path):
    content = path.read_text(encoding="utf-8", errors="replace")
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(content[3:end]) or {}
    except yaml.YAMLError:
        return {}


def normalize_tags(value):
    if isinstance(value, str):
        return {value.strip()} if value.strip() else set()
    if isinstance(value, list):
        return {str(tag).strip() for tag in value if str(tag).strip()}
    return set()


def is_current_file(path, current_file):
    if not current_file:
        return False
    current = pathlib.Path(current_file).stem
    return path.stem == current or path.name == current_file


def get_related_notes(tags_str, current_file=""):
    input_tags = parse_tags(tags_str)
    if not input_tags or not LITER_DIR.exists():
        return []

    results = []
    for path in sorted(LITER_DIR.glob("*.md"), reverse=True):
        if is_current_file(path, current_file):
            continue
        meta = read_frontmatter(path)
        file_tags = normalize_tags(meta.get("tags", []))
        overlap = len(input_tags & file_tags)
        if overlap > 0:
            title = meta.get("title") or path.stem
            results.append((overlap, path.stat().st_mtime, path.stem, title))

    results.sort(key=lambda item: (-item[0], -item[1], item[2]))
    return [f"[[{stem}|{title}]]" for _, _, stem, title in results[:3]]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python get_related.py \"標籤1,標籤2\" [目前蒸餾筆記檔名.md]", file=sys.stderr)
        sys.exit(1)

    notes = get_related_notes(sys.argv[1], sys.argv[2] if len(sys.argv) >= 3 else "")
    if notes:
        print("\n".join(notes))
    else:
        print("#待連結")