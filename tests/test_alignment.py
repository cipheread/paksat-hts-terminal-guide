"""
Tests for antenna alignment calculations.
"""
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from align_antenna import calc_pointing


def test_karachi_pointing():
    az, el = calc_pointing(24.86, 67.01)
    # PakSat-MM1 at 38°E — Pakistan is east of satellite, so dish points southwest (~120-135°)
    assert 100 < az < 160, f"Unexpected azimuth: {az}"
    assert 30 < el < 60, f"Unexpected elevation: {el}"


def test_islamabad_pointing():
    az, el = calc_pointing(33.72, 73.04)
    # Islamabad further east, azimuth shifts more southward
    assert 100 < az < 160
    assert 20 < el < 55


def test_elevation_positive():
    """All major Pakistani cities should have positive elevation to PakSat-MM1."""
    cities = [
        (24.86, 67.01),  # Karachi
        (31.55, 74.35),  # Lahore
        (33.72, 73.04),  # Islamabad
        (34.01, 71.57),  # Peshawar
        (30.19, 66.99),  # Quetta
    ]
    for lat, lon in cities:
        _, el = calc_pointing(lat, lon)
        assert el > 0, f"Negative elevation at {lat},{lon}: {el}"
