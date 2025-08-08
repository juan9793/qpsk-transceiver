import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from demos.qpsk_rrc_upsample_eye import validate_osr


def test_validate_osr_accepts_positive_integer():
    assert validate_osr(4) == 4


def test_validate_osr_rejects_non_integer():
    with pytest.raises(ValueError):
        validate_osr(2.5)
