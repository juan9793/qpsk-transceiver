"""Pytest configuration for test suite.

Adds the QAMpy submodule to ``sys.path`` so that tests can import it
without installing the package.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Compute repository root and ensure it's on ``sys.path`` so internal helpers
# and packages can be imported during tests.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Add the QAMpy submodule to the path without installing it
QAMPY_PATH = ROOT / "base" / "QAMpy"
if str(QAMPY_PATH) not in sys.path:
    sys.path.insert(0, str(QAMPY_PATH))
