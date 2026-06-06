"""Compatibility wrapper for the knowledge pipeline skill get_related.py."""

import runpy
import sys
from pathlib import Path

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

CANONICAL = Path(r"D:\gemini\skill\知識蒸餾_處理器\scripts\get_related.py")

if __name__ == "__main__":
    if not CANONICAL.exists():
        print(f"Canonical get_related.py not found: {CANONICAL}", file=sys.stderr)
        sys.exit(1)
    sys.argv[0] = str(CANONICAL)
    runpy.run_path(str(CANONICAL), run_name="__main__")
