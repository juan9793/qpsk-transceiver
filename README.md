# qpsk-transceiver

QPSK (Quadrature Phase Shift Keying) transceiver simulation built on top of the
[QAMpy](https://github.com/ChalmersPhotonicsLab/QAMpy) project. The QAMpy code
is included as a Git submodule and supplies the foundational DSP building
blocks. This repository adds transceiver glue code, demos, tests, and documentation
infrastructure that showcase how to construct a complete QPSK transmission
chain.

## Installation

### Prerequisites

- Python 3.10 or newer
- [Git](https://git-scm.com/) with submodule support
- `numpy`, `scipy`, and `matplotlib`

### Setup

```bash
git clone --recurse-submodules <repo_url>
cd qpsk-transceiver
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
```

If you cloned without `--recurse-submodules`, initialize the submodule using

```bash
git submodule update --init --recursive
```

## Running demos and tests

Demo scripts can be executed directly with Python:

```bash
python demos/<demo_script>.py

# Example
python demos/qpsk_constellation.py
python demos/qpsk_constellation_awgn.py
```

Run tests with `pytest`:

```bash
python -m pytest tests
```

## Contributing

Contributions are welcome through pull requests. Please follow the workflow and
role definitions in [AGENTS.md](AGENTS.md). Key points:

- Adhere to PEP-8 and include docstrings for new modules.
- Update or add tests for any new functionality.
- Ensure all tests pass before submitting a PR.

## Directory Structure

```
.
├─ AGENTS.md
├─ README.md
├─ base/
├─ demos/
├─ tests/
└─ documentation/
```

- `base/` – core transceiver implementation (includes the `QAMpy` submodule).
- `demos/` – example scripts and notebooks.
- `tests/` – test suite.
- `documentation/` – project documentation.

