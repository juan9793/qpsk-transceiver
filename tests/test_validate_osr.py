import pytest
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[1]))

from demos.qpsk_rrc_upsample_eye import validate_osr


def test_validate_osr_accepts_positive_integer():
    assert validate_osr(4) == 4


def test_validate_osr_rejects_non_integer():
    with pytest.raises(ValueError):
        validate_osr(2.5)


def test_validate_osr_rejects_non_positive():
    for invalid in [0, -3]:
        with pytest.raises(ValueError):
            validate_osr(invalid)


def test_validate_osr_accepts_float_integer():
    assert validate_osr(6.0) == 6


def test_validate_osr_rejects_nan():
    with pytest.raises(ValueError):
        validate_osr(np.nan)


def test_validate_osr_rejects_infinity():
    with pytest.raises(ValueError):
        validate_osr(np.inf)
