r"""End-to-end dual-polarization QPSK link over an optical AWGN channel.

This test verifies a dual-polarization QPSK transmission using root-raised
cosine pulse shaping with a roll-off of 0.1 and an oversampling ratio of two
samples per symbol. The optical channel is modeled as additive white Gaussian
noise (AWGN) with a specified OSNR. The receiver employs only a matched RRC
filter without further equalization.

\image html qpsk_transmission_chain.svg "QPSK transmission chain"
"""

import sys
from pathlib import Path

import numpy as np

# Add QAMpy submodule to path
BASE_DIR = Path(__file__).resolve().parents[1]
QAMPY_PATH = BASE_DIR / "base" / "QAMpy"
if str(QAMPY_PATH) not in sys.path:
    sys.path.insert(0, str(QAMPY_PATH))

from qampy.signals import SignalQAMGrayCoded
from qampy import impairments

from integration_config import QPSKAWGNConfig
from helpers.osnr import osnr_to_snr


def test_qpsk_awgn_link_ber_below_threshold() -> None:
    """Generate, transmit and recover a QPSK signal over AWGN."""
    cfg = QPSKAWGNConfig()

    tx = SignalQAMGrayCoded(
        M=cfg.modulation_order,
        N=cfg.n_symbols,
        nmodes=cfg.npol,  # dual polarization
        fb=cfg.symbol_rate,
        seed=cfg.seed,
    )

    tx_os = tx.resample(
        cfg.symbol_rate * cfg.oversampling_ratio, beta=cfg.roll_off
    )

    snr_db = osnr_to_snr(cfg.osnr_db, cfg.symbol_rate, cfg.npol)
    rx_os = impairments.change_snr(tx_os, snr_db)

    rx = rx_os.resample(cfg.symbol_rate, beta=cfg.roll_off)

    ber = tx.cal_ber(signal_rx=rx)

    assert np.all(ber < 1e-3)
