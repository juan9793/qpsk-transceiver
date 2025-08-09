"""Tests for input validation in :func:`validate_osr`.

These tests ensure that ``validate_osr`` accepts only positive integer
oversampling ratios and rejects invalid inputs.
"""

import pytest
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[1]))

from demos.qpsk_rrc_upsample_eye import validate_osr


def test_validate_osr_accepts_positive_integer():
    """Returns the OSR when given a positive integer."""

    assert validate_osr(4) == 4


def test_validate_osr_rejects_non_integer():
    """Non-integer OSR values raise ``ValueError``."""

    with pytest.raises(ValueError):
        validate_osr(2.5)


def test_validate_osr_rejects_non_positive():
    """Zero or negative OSR values raise ``ValueError``."""

    for invalid in [0, -3]:
        with pytest.raises(ValueError):
            validate_osr(invalid)


def test_validate_osr_rejects_nan():
    """``NaN`` OSR values raise ``ValueError``."""

    with pytest.raises(ValueError):
        validate_osr(np.nan)


def test_validate_osr_rejects_infinity():
    """Infinite OSR values raise ``ValueError``."""

    with pytest.raises(ValueError):
        validate_osr(np.inf)

 
def test_validate_osr_rejects_bool():
    """Boolean inputs raise ``TypeError``."""

    with pytest.raises(TypeError):
        validate_osr(True)


def test_validate_osr_rejects_non_numeric():
    """Non-numeric inputs raise ``TypeError``."""

    with pytest.raises(TypeError):
        validate_osr("3")

