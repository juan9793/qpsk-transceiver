"""Configuration for integration tests.

This module defines dataclasses that store commonly used
parameters for integration testing. Users can modify these
values to explore different link configurations without
changing the tests themselves.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class QPSKAWGNConfig:
    """Parameters for the QPSK over AWGN integration test.

    The noise level is specified as an optical signal-to-noise ratio (OSNR) in
    decibels using a 0.1 nm reference bandwidth (12.5 GHz).
    """

    modulation_order: int = 4
    symbol_rate: float = 64e9  # 64 GBd
    roll_off: float = 0.1
    oversampling_ratio: int = 2
    osnr_db: float = 30.0
    n_symbols: int = 2048
    npol: int = 2  # dual-polarization
    seed: int | None = 0
