"""Prepare a single deterministic assembly episode from a YAML configuration."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path, help="Episode YAML file.")
    parser.add_argument("--seed", type=int, default=0, help="Deterministic random seed.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.config.is_file():
        parser.error(f"configuration file does not exist: {args.config}")

    print(f"Episode request: config={args.config.resolve()} seed={args.seed}")
    print("Simulation execution is not configured yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
