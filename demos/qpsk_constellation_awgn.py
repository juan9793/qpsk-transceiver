"""QPSK signal with AWGN noise demo.

Generate a single-polarization QPSK signal at 64 GBd with 2**18 samples,
add complex AWGN at a specified SNR using QAMpy's ``change_snr``
function, and plot the constellations before and after noise injection.

Run this file directly with Python to display the plots:

    python demos/qpsk_constellation_awgn.py
"""

import os
import sys

import matplotlib.pyplot as plt

# Add QAMpy submodule to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QAMPY_PATH = os.path.join(BASE_DIR, "base", "QAMpy")
if QAMPY_PATH not in sys.path:
    sys.path.insert(0, QAMPY_PATH)

from qampy.core.impairments import change_snr
from qampy.signals import SignalQAMGrayCoded


def main() -> None:
    """Generate the signal, add noise, and plot constellations."""
    n_symbols = 2 ** 18
    symbol_rate = 64e9  # 64 GBd
    snr_db = 12.0

    signal = SignalQAMGrayCoded(M=4, N=n_symbols, nmodes=1, fb=symbol_rate)
    constellation = signal[0]
    noisy_constellation = change_snr(constellation, snr_db, symbol_rate, symbol_rate)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].scatter(constellation.real, constellation.imag, s=1)
    axes[0].set_title("Original QPSK Constellation")
    axes[0].set_xlabel("In-phase")
    axes[0].set_ylabel("Quadrature")
    axes[0].grid(True)
    axes[0].axis("equal")

    axes[1].scatter(noisy_constellation.real, noisy_constellation.imag, s=1)
    axes[1].set_title(f"QPSK with AWGN at {snr_db} dB")
    axes[1].set_xlabel("In-phase")
    axes[1].set_ylabel("Quadrature")
    axes[1].grid(True)
    axes[1].axis("equal")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
