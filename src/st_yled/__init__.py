"""st_yled - Advanced styling and custom components for Streamlit applications."""

from pathlib import Path
from typing import Optional

import streamlit as st

from . import styler
from .components import *  # noqa: F403

__version__ = "0.1.0"

# Extra Components


def init(css_path: Optional[str] = None) -> None:
    """Initialize st_yled with CSS styling."""
    cwd = Path.cwd()

    if css_path:
        # Check if provided path exists
        css_file = Path(css_path)
        if css_file.exists():
            st.html(str(css_file))
            return
        msg = f"CSS file not found at provided path: {css_path}"
        raise FileNotFoundError(msg)

    # Check if .streamlit/st-styled.css exists
    css_default_path = cwd / ".streamlit" / "st-styled.css"
    if css_default_path.exists():
        st.html(str(css_default_path))
        return

    # Check if directory in home exists
    home_dir = Path.home() / ".streamlit" / "st-styled.css"
    if home_dir.exists():
        st.html(str(home_dir))
        return

    # If no CSS file found, apply no styles
    # TODO: Potentially raise a warning here


def set(component: str, property: str, value: str) -> None:
    styler.apply_component_css_global(component, {property: value})
