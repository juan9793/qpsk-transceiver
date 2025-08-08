# qpsk-transceiver

QPSK (Quadrature Phase Shift Keying) transceiver simulation built on top of the
[QAMpy](https://github.com/ChalmersPhotonicsLab/QAMpy) project. The QAMpy code
is included as a Git submodule and supplies the foundational DSP building
blocks. This repository adds transceiver glue code, demos, tests, and documentation
infrastructure that showcase how to construct a complete QPSK transmission
chain.

## Installation

### Prerequisites

- Python 3.11
- [Git](https://git-scm.com/) with submodule support
- `numpy`, `scipy`, and `matplotlib`

### Setup

```bash
git clone --recurse-submodules <repo_url>
cd qpsk-transceiver
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -c constraints.txt
```

The commands above create an isolated Python environment and install the
packages required by the project using the pinned versions defined in
`requirements.txt` and `constraints.txt`.

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
python demos/qpsk_rrc_upsample_eye.py
python demos/qpsk_ber_snr_sweep.py
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
├─ constraints.txt
├─ demos/
├─ documentation/
├─ requirements.txt
└─ tests/
```

- `base/` – core transceiver implementation (includes the `QAMpy` submodule).
- `constraints.txt` – pinned versions for dependencies.
- `demos/` – example scripts and notebooks.
- `documentation/` – project documentation.
- `requirements.txt` – project dependencies.
- `tests/` – test suite.


