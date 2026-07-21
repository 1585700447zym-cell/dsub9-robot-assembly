"""Contract tests for simulation reset behavior."""

import pytest


@pytest.mark.skip(reason="Simulation reset implementation is not available yet.")
def test_reset_is_deterministic_for_a_fixed_seed() -> None:
    """Equal seeds and configuration must produce equal initial states."""
    raise AssertionError("Replace the skip with a deterministic reset assertion.")
