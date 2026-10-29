#!/usr/bin/env python3
"""Create a minimal independently compilable review from the shared template."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    if len(sys.argv) != 3:
        print('Usage: python3 scripts/new_review.py <slug> "Title"', file=sys.stderr)
        return 2
    slug, title = sys.argv[1:]
    if not re.fullmatch(r'[a-z][a-z0-9-]*', slug) or slug.endswith('-') or '--' in slug:
        print('Slug must be lowercase letters, digits and single hyphens.', file=sys.stderr)
        return 2
    if not title.strip() or '\\' in title or any(c in title for c in '{}%$&#_^~'):
        print('Title cannot be empty or contain LaTeX control characters.', file=sys.stderr)
        return 2
    dest = ROOT / 'reviews' / slug
    if dest.exists():
        print(f'Already exists: {dest}', file=sys.stderr)
        return 1
    source = (ROOT / 'templates' / 'review' / 'main.tex').read_text(encoding='utf8')
    source = source.replace('Review Title', title).replace('A Precise Research Question', 'Scope and Evidence')
    dest.mkdir(parents=True)
    (dest / 'main.tex').write_text(source, encoding='utf8')
    (dest / 'figures').mkdir()
    (dest / 'figures' / '.gitkeep').touch()
    print(f'Created reviews/{slug}/main.tex')
    print(f'Compile: cd reviews/{slug} && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex')
    print(f'Next: add {slug} to CATALOG.md; build targets and CI discovery are automatic.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
