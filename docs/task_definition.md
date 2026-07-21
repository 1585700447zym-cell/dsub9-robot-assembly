# Task Definition

## Objective

Insert and fully seat a D-sub 9 connector into its matching receptacle using a simulated robot while respecting pose, force, and time constraints.

## Episode inputs

- Robot and end-effector initial state.
- Connector and receptacle geometry and poses.
- Controller, sensing, and randomization configuration.
- Deterministic random seed.

## Success criteria

Define measurable thresholds for insertion depth, translational and rotational alignment, contact force, and sustained seating before implementing termination logic.

## Failure criteria

Define limits for excessive force, loss of the connector, unsafe joint state, workspace violation, and episode duration.

## Metrics

At minimum, report success rate, time to insertion, final pose error, peak contact force, and the termination reason.
