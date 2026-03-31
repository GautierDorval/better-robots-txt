#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {'.git', '__pycache__'}


def iter_json_files():
    for p in ROOT.rglob('*'):
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        if p.is_file() and p.suffix in {'.json', '.jsonld'}:
            yield p


def validate_json_artifacts() -> list[str]:
    errors: list[str] = []
    for p in sorted(iter_json_files()):
        try:
            json.loads(p.read_text(encoding='utf-8'))
            print(f"OK  {p.relative_to(ROOT)}")
        except Exception as e:
            errors.append(f"JSON error: {p.relative_to(ROOT)}: {e}")
    return errors


def check_markdown_fences() -> list[str]:
    errors: list[str] = []
    for md in ROOT.rglob('*.md'):
        if any(part in SKIP_PARTS for part in md.parts):
            continue
        text = md.read_text(encoding='utf-8', errors='replace')
        fences = len(re.findall(r'^```', text, flags=re.MULTILINE))
        if fences % 2 != 0:
            errors.append(f"Unbalanced code fences: {md.relative_to(ROOT)} (count={fences})")
    return errors


def check_internal_links() -> list[str]:
    errors: list[str] = []
    link_re = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
    for md in ROOT.rglob('*.md'):
        if any(part in SKIP_PARTS for part in md.parts):
            continue
        text = md.read_text(encoding='utf-8', errors='replace')
        for target in link_re.findall(text):
            if target.startswith(('http', '#', 'mailto:')):
                continue
            t = target.split('#', 1)[0].split('?', 1)[0].strip()
            if not t:
                continue
            resolved = (md.parent / t).resolve()
            if not resolved.exists():
                errors.append(f"Broken link: {md.relative_to(ROOT)} -> {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_json_artifacts())
    errors.extend(check_markdown_fences())
    errors.extend(check_internal_links())

    if errors:
        print('Validation failed:')
        for e in errors:
            print(f' - {e}')
        return 1

    print('All checks passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
