# System Architecture

## Components

- `src/simulation`: simulator lifecycle, stepping, and reset orchestration.
- `src/models`: robot, connector, receptacle, and geometry loaders.
- `src/control`: scripted, optimization-based, and learned controllers.
- `src/sensing`: observation construction and sensor processing.
- `src/logging`: episode events, trajectories, and metadata schemas.
- `src/learning`: training algorithms, policies, and datasets.
- `src/evaluation`: metrics, aggregations, and comparisons.

## Data flow

Configuration selects models and an experiment. The simulation produces observations for the controller, applies the returned action, evaluates termination, and sends structured step and episode records to logging. Evaluation consumes completed run records without changing them.

## Boundaries

Keep simulator-specific APIs inside `src/simulation` and `src/models`. Controllers should consume documented observations and return documented actions so they can be evaluated independently of the backend.
