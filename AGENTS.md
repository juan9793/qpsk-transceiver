Overview
This document defines the roles, responsibilities, and workflows for human and AI agents contributing to the QPSK Transceiver project.
The goal is to ensure smooth collaboration across design, implementation, testing, and documentation while maintaining code quality and reproducibility.

Agent Roles
1. Research Agent
Explore QPSK-related algorithms (timing recovery, carrier recovery, equalization).

Provide design notes and parameter suggestions.

Deliver references and trade-off analyses.

2. DSP Development Agent
Implement and optimize DSP blocks (modulator, demodulator, RRC filters, Costas loop, equalizers).

Ensure code follows PEP-8.

Provide inline docstrings and usage examples.

3. Simulation Agent
Run channel simulations in Python or Jupyter notebooks.

Sweep parameters (OSNR, SNR, roll-off factor, CFO/SFO, laser linewidth, and others).

Save artifacts: BER plots, constellation diagrams, equalizer learning curves, BPS phase plots.

4. Verification Agent
Create and maintain unit tests and integration tests.

Define pass/fail criteria for DSP blocks.

Automate regression testing.

5. Documentation Agent
Maintain the README, tutorials, and API references.

Update usage instructions for VS Code terminal and Jupyter.

Generate diagrams for the signal chain and workflows.

6. Release Agent
Manage versioning and changelogs.

Tag and publish releases.

Ensure artifacts and documentation are included in release packages.

7. Maintainer (Human)
Review all pull requests.

Approve merges into main.

Resolve conflicts and arbitrate design decisions.

Repository Structure
/base – Core DSP modules.

/demos – Example scripts and Jupyter notebooks.

/integration-tests – End-to-end validation scenarios.

/unit-tests – Component-level test cases.

Workflows
Development
Research Agent proposes design via issue or ADR.

DSP Development Agent implements feature in a branch.

Verification Agent writes/updates tests.

Simulation Agent validates with performance plots.

Documentation Agent updates guides and examples.

Maintainer reviews and merges PR into main.

Testing
Unit tests check individual DSP blocks.

Integration tests validate complete TX → Channel → RX pipelines.

Simulation Agent includes visual inspection artifacts (plots) in PR.

Release
Release Agent bumps version, updates changelog, publishes release.

All artifacts and documentation are archived.

Collaboration Rules
Main branch is protected – no direct pushes.

All changes must go through Pull Requests.

PRs require maintainer review.

All AI-generated code must comply with PEP-8.

Tests must pass before merge.

Artifacts & Storage
Performance plots: BER, constellation diagrams, equalizer learning curves, BPS phase plots.

Store generated artifacts in /reports or attach them to PRs.

Tools & Environment
Python (version pinned in requirements.txt or environment.yml).

Runs in VS Code terminal and Jupyter notebooks.

Recommended libraries: NumPy, SciPy, Matplotlib

Glossary
QPSK – Quadrature Phase Shift Keying.

RRC – Root Raised Cosine filter.

BER – Bit Error Rate 

CFO/SFO – Carrier / Symbol Frequency Offset.

BPS phase – Blind Phase Search phase.
