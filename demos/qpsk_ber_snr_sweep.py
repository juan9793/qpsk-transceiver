"""QPSK BER versus SNR sweep demo.

Generate a single-polarization QPSK signal at 64 GBd, sweep the SNR from
0 to 17 dB in 1 dB steps, add complex AWGN, demodulate, calculate the bit
error rate (BER), plot BER versus SNR, and overlay the theoretical curve.

Run this file directly with Python to display and save the plot:

    python demos/qpsk_ber_snr_sweep.py
"""

import os
import sys
from typing import List

import matplotlib.pyplot as plt
import numpy as np

# Add QAMpy submodule to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QAMPY_PATH = os.path.join(BASE_DIR, "base", "QAMpy")
if QAMPY_PATH not in sys.path:
    sys.path.insert(0, QAMPY_PATH)

from qampy.core.ber_functions import cal_ber_syncd
from qampy.core.impairments import change_snr
from qampy.signals import SignalQAMGrayCoded
from qampy import theory


def main() -> None:
    """Sweep SNR, calculate BER, and generate a plot."""
    n_symbols = 2 ** 18
    symbol_rate = 64e9  # 64 GBd
    snr_range_db = np.arange(0, 18, 1)

    signal = SignalQAMGrayCoded(M=4, N=n_symbols, nmodes=1, fb=symbol_rate)
    tx_bits = signal.bits[0]
    constellation = signal[0]

    ber_values: List[float] = []
    for snr_db in snr_range_db:
        noisy = change_snr(constellation, snr_db, symbol_rate, symbol_rate)
        rx_bits = signal.demodulate(noisy)
        ber, _, _ = cal_ber_syncd(rx_bits, tx_bits, threshold=1.0)
        ber_values.append(max(ber, 1e-12))
    ber_values = np.array(ber_values)
    snr_linear = 10 ** (snr_range_db / 10)
    ber_theory = theory.ber_vs_es_over_n0_qam(snr_linear, 4)

    reports_dir = os.path.join(BASE_DIR, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    plt.semilogy(snr_range_db, ber_values, marker="o", label="Simulation")
    plt.semilogy(snr_range_db, ber_theory, linestyle="--", label="Theory")
    plt.xlabel("SNR (dB)")
    plt.ylabel("BER")
    plt.title("QPSK BER vs SNR")
    plt.xlim(0, 17)
    plt.ylim(1e-7, 0.5)
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    output_path = os.path.join(reports_dir, "qpsk_ber_vs_snr.png")
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    main()
