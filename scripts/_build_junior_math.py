"""Rebuild all junior-math maps.

Run: python3 scripts/_build_junior_math.py
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

MODULES = [
    "_build_jm_g7_algebra",
    "_build_jm_g7_geometry",
    "_build_jm_g7_statistics",
    "_build_jm_g7_practice",
    "_build_jm_g8_algebra",
    "_build_jm_g8_geometry",
    "_build_jm_g8_statistics",
    "_build_jm_g8_practice",
    "_build_jm_g9_algebra",
    "_build_jm_g9_geometry",
    "_build_jm_g9_statistics",
    "_build_jm_g9_practice",
]


def main() -> None:
    for name in MODULES:
        mod = importlib.import_module(name)
        print(f"== {name}")
        mod.main()


if __name__ == "__main__":
    main()
