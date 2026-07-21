"""Run lightweight preflight checks on a robot or connector model file."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


SUPPORTED_SUFFIXES = {".mjcf", ".obj", ".stl", ".urdf", ".xml"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path, help="Path to the model file to inspect.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    model: Path = args.model

    if not model.is_file():
        parser.error(f"model file does not exist: {model}")
    if model.suffix.lower() not in SUPPORTED_SUFFIXES:
        parser.error(
            f"unsupported model extension {model.suffix!r}; "
            f"expected one of {sorted(SUPPORTED_SUFFIXES)}"
        )

    print(f"Model preflight passed: {model.resolve()}")
    print("Backend-specific geometry, joints, and collision checks are not configured yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
