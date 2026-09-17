"""Rebuild all senior-math maps.

Run: python3 scripts/_build_senior_math.py
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

MODULES = [
    "_build_sm_sets_logic",
    "_build_sm_functions",
    "_build_sm_trig",
    "_build_sm_vectors_complex",
    "_build_sm_solid_geometry",
    "_build_sm_analytic_geometry",
    "_build_sm_probability_statistics",
    "_build_sm_derivatives",
    "_build_sm_counting_probability",
    "_build_sm_sequences",
    "_build_sm_practice",
]


def main() -> None:
    for name in MODULES:
        mod = importlib.import_module(name)
        print(f"== {name}")
        mod.main()


if __name__ == "__main__":
    main()
