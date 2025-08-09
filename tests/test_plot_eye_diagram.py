"""Tests for the ``plot_eye_diagram`` helper used in QPSK visualization."""

import sys
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parents[1]))

from demos.qpsk_rrc_upsample_eye import plot_eye_diagram


def _create_signal(length: int) -> np.ndarray:
    """Return a simple complex ramp signal of the requested length."""

    return np.linspace(0, 1, length) + 1j * 0


def test_plot_eye_diagram_draws_expected_traces():
    """``plot_eye_diagram`` draws one trace per symbol except the first."""
    sps = 2
    signal = _create_signal(8)
    fig, ax = plt.subplots()
    plot_eye_diagram(signal, sps, ax)
    expected_traces = len(signal) // sps - 1
    assert len(ax.lines) == expected_traces
    plt.close(fig)


def test_plot_eye_diagram_sets_labels_and_title():
    """``plot_eye_diagram`` sets title and axis labels appropriately."""
    sps = 2
    signal = _create_signal(8)
    fig, ax = plt.subplots()
    plot_eye_diagram(signal, sps, ax)
    assert ax.get_title() == "Eye Diagram (In-phase)"
    assert ax.get_xlabel() == "Sample Index"
    assert ax.get_ylabel() == "Amplitude"
    plt.close(fig)


def test_plot_eye_diagram_plots_only_real_part():
    """Only the real part of the signal is plotted."""
    sps = 2
    real = np.arange(8)
    imag = np.linspace(1, -1, 8)
    signal = real + 1j * imag
    fig, ax = plt.subplots()
    plot_eye_diagram(signal, sps, ax)
    first_segment = real[: 2 * sps]
    plotted = ax.lines[0].get_ydata()
    assert np.array_equal(plotted, first_segment)
    plt.close(fig)


def test_plot_eye_diagram_enables_grid():
    """Gridlines are enabled on both axes."""
    sps = 2
    signal = _create_signal(8)
    fig, ax = plt.subplots()
    plot_eye_diagram(signal, sps, ax)
    assert all(gl.get_visible() for gl in ax.xaxis.get_gridlines())
    assert all(gl.get_visible() for gl in ax.yaxis.get_gridlines())
    plt.close(fig)


def test_plot_eye_diagram_with_short_signal_draws_no_lines():
    """Signals shorter than two spans produce no plotted lines."""
    sps = 4
    signal = _create_signal(6)
    fig, ax = plt.subplots()
    plot_eye_diagram(signal, sps, ax)
    assert len(ax.lines) == 0
    plt.close(fig)


def test_plot_eye_diagram_segments_are_sequential():
    """Consecutive segments appear in sequential order."""
    sps = 2
    signal = _create_signal(12)
    fig, ax = plt.subplots()
    plot_eye_diagram(signal, sps, ax)
    span = 2 * sps
    first = signal[:span].real
    second = signal[sps:sps + span].real
    assert np.array_equal(ax.lines[0].get_ydata(), first)
    assert np.array_equal(ax.lines[1].get_ydata(), second)
    plt.close(fig)

