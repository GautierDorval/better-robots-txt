#!/usr/bin/env python3
import json
from pathlib import Path

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    artefacts = root / "artefacts"
    if not artefacts.exists():
        print("No artefacts/ directory found.")
        return 1

    failed = False
    for p in sorted(artefacts.glob("*.json*")):
        # Only validate pure JSON files. Skip JSON-LD if it is still JSON (it is).
        if p.suffix in {".json", ".jsonld"}:
            try:
                json.loads(p.read_text(encoding="utf-8"))
                print(f"OK  {p.relative_to(root)}")
            except Exception as e:
                print(f"ERR {p.relative_to(root)}: {e}")
                failed = True
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
