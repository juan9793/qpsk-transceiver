# Overview

This document defines the roles, responsibilities, and workflows for human and AI agents contributing to the QPSK Transceiver project. The goal is to ensure smooth collaboration across design, implementation, testing, and documentation while maintaining code quality and reproducibility.

## Agent Roles

### 1. Research Agent
- Explore QPSK-related algorithms (timing recovery, carrier recovery, equalization).
- Provide design notes and parameter suggestions.
- Deliver references and trade-off analyses.

### 2. DSP Development Agent
- Implement and optimize DSP blocks (modulator, demodulator, RRC filters, Costas loop, equalizers).
- Ensure code follows PEP-8.
 - Provide inline docstrings and usage examples using standard Python docstring syntax.

### 3. Simulation Agent
- Run channel simulations in Python or Jupyter notebooks.
- Sweep parameters (OSNR, SNR, roll-off factor, CFO/SFO, laser linewidth, and others).
- Save artifacts: BER plots, constellation diagrams, equalizer learning curves, BPS phase plots.

### 4. Verification Agent
- Create and maintain unit tests and integration tests.
- Define pass/fail criteria for DSP blocks.
- Automate regression testing.

### 5. Documentation Agent
 - Maintain the README, tutorials, and API references.
 - Keep the README's directory structure current whenever files or directories are added or removed.
 - Update usage instructions for VS Code terminal and Jupyter.
 - Generate diagrams for the signal chain and workflows.
 - Ensure documentation uses standard Python docstrings; Doxygen builds the API reference without extra filters.

### 6. Release Agent
- Manage versioning and changelogs.
- Tag and publish releases.
- Ensure artifacts and documentation are included in release packages.

### 7. Maintainer (Human)
- Review all pull requests.
- Approve merges into main.
- Resolve conflicts and arbitrate design decisions.

## Repository Structure
- `/base` – Core DSP modules.
- `/base/QAMpy` – QAMpy submodule; do not install as external dependency.
- `/demos` – Example scripts and Jupyter notebooks.
- `/tests` – Test suite.
- `/documentation` – Project documentation.

References to QAMpy refer to the submodule located at `/base/QAMpy`; do not attempt to install QAMpy as a standalone dependency.

## Workflows

### Development
1. Research Agent proposes design via issue or ADR.
2. DSP Development Agent implements feature in a branch.
3. Verification Agent writes or updates tests.
4. Simulation Agent validates with performance plots.
5. Documentation Agent updates guides and examples.
6. Maintainer reviews and merges PR into main.

### Testing
- Unit tests check individual DSP blocks.
- Integration tests validate complete TX → Channel → RX pipelines.
- Simulation Agent includes visual inspection artifacts (plots) in PRs.
- Run tests with `pytest`, treating warnings as errors; the suite must pass without warnings.

### Release
- Release Agent bumps version, updates changelog, and publishes release.
- All artifacts and documentation are archived.

## Collaboration Rules
- Main branch is protected – no direct pushes.
- All changes must go through Pull Requests.
- PRs require maintainer review.
- All AI-generated code must comply with PEP-8.
- Always use QAMpy functions if available.
- Avoid glue code; it is never recommended.
- Follow "Divide and conquer"—each function should implement a single, well-defined functionality with optional configuration.
- Tests must pass without warnings before merge.
- Avoid adding new dependencies unless absolutely necessary; prefer using the existing requirements.

## Artifacts & Storage
- Performance plots (BER, constellation diagrams, equalizer learning curves, BPS phase plots) may be generated locally but must not be committed to the repository.
- Attach any necessary artifacts to PRs instead of storing them in version control.

## Tools & Environment
- Python 3.11 (install dependencies using `requirements.txt` or `environment.yml`).
- Runs in VS Code terminal and Jupyter notebooks.
- Recommended libraries: NumPy, SciPy, Matplotlib.

## Glossary
- **QPSK** – Quadrature Phase Shift Keying.
- **RRC** – Root Raised Cosine filter.
- **BER** – Bit Error Rate.
- **CFO/SFO** – Carrier / Symbol Frequency Offset.
- **BPS phase** – Blind Phase Search phase.

