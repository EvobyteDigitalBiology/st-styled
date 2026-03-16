"""Minimal Streamlit app for tooltip Playwright integration testing."""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Ensure local source imports work when running from the component test directory.
PROJECT_ROOT = Path(__file__).resolve().parents[5]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from st_yled.components.tooltip import tooltip  # noqa: E402

st.set_page_config(page_title="Tooltip Integration Test", layout="wide")
st.title("Tooltip Component Integration Test")
st.caption("App variants are used for semantic Playwright assertions.")

st.markdown("## Baseline")
tooltip(
    title="Baseline Tooltip",
    text="Baseline style",
    width=220,
    top="80px",
    left="40px",
    background_color="white",
    shadow="0 4px 10px rgba(0, 0, 0, 0.2)",
    show=True,
    key="test-basic",
)

st.markdown("## Width + Color + Shadow Variant")
tooltip(
    title="Variant Tooltip",
    text="Variant style",
    width=360,
    top="130px",
    left="70px",
    background_color="#ffe082",
    shadow="none",
    show=True,
    key="test-variant",
)

st.markdown("## Hidden On Load Variant")
tooltip(
    title="Hidden Tooltip",
    text="Starts hidden",
    show=False,
    key="test-hidden",
)

st.success("Tooltip fixtures rendered")
