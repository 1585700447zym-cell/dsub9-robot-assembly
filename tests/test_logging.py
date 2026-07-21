"""Contract tests for structured experiment logging."""

import pytest


@pytest.mark.skip(reason="Structured logging implementation is not available yet.")
def test_episode_log_contains_required_reproducibility_fields() -> None:
    """Logs must capture revision, config, model versions, seed, and outcome."""
    raise AssertionError("Replace the skip with logging-schema assertions.")
