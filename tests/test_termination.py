"""Contract tests for episode termination."""

import pytest


@pytest.mark.skip(reason="Episode termination implementation is not available yet.")
def test_termination_reports_success_failure_or_time_limit() -> None:
    """Every completed episode must expose one mutually exclusive reason."""
    raise AssertionError("Replace the skip with termination-reason assertions.")
