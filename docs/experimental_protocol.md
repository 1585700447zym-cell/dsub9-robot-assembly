# Experimental Protocol

## Reproducibility

Each run must record the source revision, environment, complete configuration, model versions, random seed, start time, and termination reason.

## Procedure

1. Validate the selected models and configuration.
2. Reset the simulation using the recorded seed.
3. Run one episode until success, failure, or the time limit.
4. Write immutable step data and an episode summary.
5. Repeat across the registered seed set.
6. Aggregate metrics without editing raw run records.

## Comparisons

Use identical model versions, reset distributions, seed sets, termination rules, and metric definitions when comparing methods.

## Reporting

Report sample count, success rate, uncertainty, failure categories, runtime, pose error, and contact-force statistics. Link each summary to its registry entry and configuration.
