import os
import sys

import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QAMPY_PATH = os.path.join(BASE_DIR, "base", "QAMpy")
if QAMPY_PATH not in sys.path:
    sys.path.insert(0, QAMPY_PATH)

from qampy.core.ber_functions import cal_ber_syncd
from qampy.core.impairments import change_snr
from qampy.signals import SignalQAMGrayCoded
from qampy import theory


def test_ber_snr_matches_theory() -> None:
    """BER from simulation should match the theoretical curve."""
    n_symbols = 2 ** 15
    symbol_rate = 64e9  # 64 GBd
    snr_range_db = np.array([0, 5, 10, 15])

    signal = SignalQAMGrayCoded(M=4, N=n_symbols, nmodes=1, fb=symbol_rate)
    tx_bits = signal.bits[0]
    constellation = signal[0]

    ber_values = []
    for snr_db in snr_range_db:
        noisy = change_snr(constellation, snr_db, symbol_rate, symbol_rate)
        rx_bits = signal.demodulate(noisy)
        ber, _, _ = cal_ber_syncd(rx_bits, tx_bits, threshold=1.0)
        ber_values.append(max(ber, 1e-12))

    ber_values = np.array(ber_values)
    snr_linear = 10 ** (snr_range_db / 10)
    ber_theory = theory.ber_vs_es_over_n0_qam(snr_linear, 4)

    np.testing.assert_allclose(ber_values, ber_theory, rtol=0.2, atol=1e-3)
