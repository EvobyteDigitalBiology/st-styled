"""st_yled - Advanced styling and custom components for Streamlit applications."""

from pathlib import Path
from typing import Optional
import sys

import streamlit as st

from st_yled import styler  # type: ignore
from st_yled.elements import *  # type: ignore # noqa: F403

# Import custom components
from st_yled.components.streamlit_split_button import split_button  # type: ignore # noqa: F401
from st_yled.components.streamlit_redirect import redirect  # type: ignore # noqa: F401
from st_yled.components.sticky_header import sticky_header  # type: ignore # noqa: F401
from st_yled.components.badge_card_one import badge_card_one  # type: ignore # noqa: F401
from st_yled.components.image_card_one import image_card_one  # type: ignore # noqa: F401

__version__ = "0.3.0"


def init(css_path: Optional[str] = None, reset_tracebacklimit: bool = True) -> None:
    """Initialize st_yled with CSS styling."""

    if reset_tracebacklimit:
        sys.tracebacklimit = 1000

    caller_hash = styler.extract_caller_path_hash_init()

    # Set session_state
    st.session_state[f"st-yled-comp-{caller_hash}-counter"] = 0
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


def set(element: str, property: str, value: str) -> None:
    styler.apply_component_css_global(element, {property: value})
