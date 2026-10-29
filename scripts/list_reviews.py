#!/usr/bin/env python3
"""Emit the review-slug array for the CI dynamic build matrix."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
reviews = sorted(p.name for p in (root / 'reviews').iterdir() if (p / 'main.tex').is_file())
print(json.dumps(reviews, ensure_ascii=True, separators=(',', ':')))
