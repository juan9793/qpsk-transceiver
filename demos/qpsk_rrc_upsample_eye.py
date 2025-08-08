"""QPSK RRC filtering and eye-diagram demo.

Generate a single-polarization QPSK signal and upsample it using a
root-raised cosine (RRC) filter to a user defined oversampling ratio.
The constellation of the original symbols is displayed and, in a
separate figure, the eye diagram of the RRC filtered signal.

Run this file directly with Python to display the plots:

    python demos/qpsk_rrc_upsample_eye.py

Use ``main(osr, roll_off)`` to customize the oversampling ratio and
RRC roll-off.
"""

from __future__ import annotations

import os
import sys
from typing import Any
from numbers import Real

import matplotlib.pyplot as plt
import numpy as np

# Add QAMpy submodule to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QAMPY_PATH = os.path.join(BASE_DIR, "base", "QAMpy")
if QAMPY_PATH not in sys.path:
    sys.path.insert(0, QAMPY_PATH)



def validate_osr(osr: float) -> int:
    """Validate and convert the oversampling ratio to a positive integer.

    Parameters
    ----------
    osr : float
        Desired oversampling ratio.

    Returns
    -------
    int
        Oversampling ratio as an integer.

    Raises
    ------
    TypeError
        If ``osr`` is not a real number.
    ValueError
        If ``osr`` is not a positive integer.
    """
    if isinstance(osr, bool) or not isinstance(osr, Real):
        raise TypeError("Oversampling ratio must be a real number")
    if osr <= 0 or not float(osr).is_integer():
        raise ValueError("Oversampling ratio must be a positive integer")
    return int(osr)


def plot_eye_diagram(signal: np.ndarray, sps: int, ax: Any) -> None:
    """Plot the eye diagram of the in-phase component of ``signal``.

    Parameters
    ----------
    signal : np.ndarray
        Complex baseband signal after RRC filtering.
    sps : int
        Samples per symbol (oversampling ratio).
    ax : Any
        Matplotlib axis where the eye diagram is drawn.
    """
    span = 2 * sps
    ntraces = len(signal) // sps - 1
    for i in range(ntraces):
        start = i * sps
        segment = signal[start : start + span]
        ax.plot(segment.real, color="tab:blue", alpha=0.2)
    ax.set_title("Eye Diagram (In-phase)")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    ax.grid(True)


def main(osr: float = 2.0, roll_off: float = 0.25) -> None:
    """Generate an RRC filtered signal and visualize it.

    Parameters
    ----------
    osr : float, optional
        Oversampling ratio (must be a positive integer). Defaults to 2.
    roll_off : float, optional
        RRC roll-off factor. Defaults to 0.25.
    """
    from qampy.core.resample import rrcos_resample
    from qampy.signals import SignalQAMGrayCoded

    sps = validate_osr(osr)
    n_symbols = 2 ** 14
    symbol_rate = 64e9  # 64 GBd

    signal = SignalQAMGrayCoded(M=4, N=n_symbols, nmodes=1, fb=symbol_rate)
    symbols = signal[0]

    filtered = rrcos_resample(symbols, symbol_rate, symbol_rate * sps, beta=roll_off)

    fig_const, ax_const = plt.subplots(figsize=(6, 5))
    ax_const.scatter(symbols.real, symbols.imag, s=1)
    ax_const.set_title("Original QPSK Constellation")
    ax_const.set_xlabel("In-phase")
    ax_const.set_ylabel("Quadrature")
    ax_const.grid(True)
    ax_const.axis("equal")

    fig_eye, ax_eye = plt.subplots(figsize=(6, 5))
    plot_eye_diagram(filtered, sps, ax_eye)

    plt.show()


if __name__ == "__main__":
    main()

