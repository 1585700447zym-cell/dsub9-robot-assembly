"""Contract tests for coordinate-frame conversions."""

import pytest


@pytest.mark.skip(reason="Coordinate-frame implementation is not available yet.")
def test_coordinate_frame_round_trip_recovers_pose() -> None:
    """A transform followed by its inverse must recover the original pose."""
    raise AssertionError("Replace the skip with a round-trip transform assertion.")
