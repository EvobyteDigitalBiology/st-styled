"""Minimal Streamlit app for tooltip Playwright integration testing."""

import sys
from pathlib import Path

import streamlit as st

# Ensure local source imports work when running from the component test directory.
PROJECT_ROOT = Path(__file__).resolve().parents[5]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import st_yled  # type: ignore

st_yled.init('/home/jona/projects/evobyte/st-styled/tests/integration/st-styled.css')

st_yled.button("Click me")
