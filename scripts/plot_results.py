"""Prepare plotting inputs from an experiment result table."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path, help="CSV result table to summarize.")
    parser.add_argument("--output", type=Path, help="Optional output image path.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.results.is_file():
        parser.error(f"results file does not exist: {args.results}")

    output = args.output.resolve() if args.output else "interactive"
    print(f"Plot request: results={args.results.resolve()} output={output}")
    print("Plot definitions are not configured yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
