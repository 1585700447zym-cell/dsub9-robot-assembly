"""Prepare a reproducible batch of assembly episodes."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("value must be at least 1")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path, help="Batch YAML file.")
    parser.add_argument("--episodes", type=positive_int, default=10)
    parser.add_argument("--seed-start", type=int, default=0)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.config.is_file():
        parser.error(f"configuration file does not exist: {args.config}")

    seed_end = args.seed_start + args.episodes - 1
    print(
        f"Batch request: config={args.config.resolve()} episodes={args.episodes} "
        f"seeds={args.seed_start}..{seed_end}"
    )
    print("Batch execution is not configured yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
