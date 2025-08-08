"""QPSK signal generation demo.

Generate a single-polarization QPSK signal at 64 GBd with 2**18 samples
using the QAMpy submodule and plot the resulting constellation.

Run this file directly with Python to display the plot:

    python demo/qpsk_constellation.py
"""

import os
import sys

import matplotlib.pyplot as plt

# Add QAMpy submodule to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QAMPY_PATH = os.path.join(BASE_DIR, "base", "QAMpy")
if QAMPY_PATH not in sys.path:
    sys.path.insert(0, QAMPY_PATH)

from qampy.signals import SignalQAMGrayCoded


def main() -> None:
    """Generate the signal and plot its constellation."""
    n_symbols = 2 ** 18
    symbol_rate = 64e9  # 64 GBd

    signal = SignalQAMGrayCoded(M=4, N=n_symbols, nmodes=1, fb=symbol_rate)
    constellation = signal[0]

    plt.figure(figsize=(5, 5))
    plt.scatter(constellation.real, constellation.imag, s=1)
    plt.title("QPSK Constellation at 64 GBd")
    plt.xlabel("In-phase")
    plt.ylabel("Quadrature")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
