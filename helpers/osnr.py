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
        Symbol rate of the transmitted signal in Hz.
    npol : int
        Number of signal polarizations (1 for single polarization,
        2 for dual).

    Returns
    -------
    float
        Per-polarization signal-to-noise ratio in decibels.

    Examples
    --------
    >>> osnr_to_snr(osnr_db=20, symbol_rate=32e9, npol=2)
    12.9...
    """
    return (
        osnr_db
        - 10 * np.log10(symbol_rate / REFERENCE_BW_HZ)
        - 10 * np.log10(npol)
    )
