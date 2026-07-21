# Agent Guidelines

## Scope

This repository develops and evaluates simulation and control methods for robotic assembly of a D-sub 9 connector. Keep changes focused on reproducible experiments and clearly documented coordinate conventions.

## Project conventions

- Keep reusable implementation code under `src/` and command-line entry points under `scripts/`.
- Store configuration in `configs/`; do not hard-code experiment-specific values in reusable modules.
- Add or update tests for coordinate transforms, reset behavior, termination logic, and logging schemas when those components change.
- Treat `data/` and `runs/` as generated local artifacts unless a small fixture is intentionally reviewed and committed.
- Record material architecture or protocol choices in `DECISIONS.md` and user-visible changes in `CHANGELOG.md`.

## Validation

Run the narrowest relevant tests while developing, then run the full test suite before opening or updating a pull request.
