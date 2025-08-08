"""OSNR and SNR conversion utilities."""

from __future__ import annotations

import numpy as np

REFERENCE_BW_HZ = 12.5e9  # 0.1 nm reference bandwidth


def osnr_to_snr(osnr_db: float, symbol_rate: float, npol: int) -> float:
    """Convert OSNR (dB/0.1 nm) to per-polarization SNR in dB.

    Parameters
    ----------
    osnr_db : float
        Optical signal-to-noise ratio in decibels.
    symbol_rate : float
        Symbol rate of the transmitted signal.
    npol : int
        Number of polarizations in the signal.

    Returns
    -------
    float
        Per-polarization signal-to-noise ratio in decibels.
    """
    return (
        osnr_db
        - 10 * np.log10(symbol_rate / REFERENCE_BW_HZ)
        - 10 * np.log10(npol)
    )
