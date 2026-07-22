"""st_yled - Advanced styling and custom components for Streamlit applications."""

from pathlib import Path
from typing import Optional
import sys

import streamlit as st

from st_yled import styler  # type: ignore
from st_yled.elements import *  # type: ignore # noqa: F403
from st_yled.validation import ValidationConfig  # type: ignore

# Import custom components
from st_yled.components.streamlit_split_button import split_button  # type: ignore # noqa: F401
from st_yled.components.streamlit_redirect import redirect  # type: ignore # noqa: F401
from st_yled.components.sticky_header import sticky_header  # type: ignore # noqa: F401
from st_yled.components.badge_card_one import badge_card_one  # type: ignore # noqa: F401
from st_yled.components.image_card_one import image_card_one  # type: ignore # noqa: F401
from st_yled.components.tooltip import tooltip  # type: ignore # noqa: F401

__version__ = "0.5.1"


def init(
    css_path: Optional[str] = None,
    theme: Optional[str] = None,
    disable_light_dark_mode: bool = False,
    bypass_css_validation: bool = False,
    strict_css_validation: bool = False,
    reset_tracebacklimit: bool = True,
) -> None:
    """Initialize st_yled with CSS styling."""

    ValidationConfig.set_init_validation_mode(
        bypass=bypass_css_validation,
        strict=strict_css_validation,
    )

    if reset_tracebacklimit:
        sys.tracebacklimit = 1000

    caller_hash = styler.extract_caller_path_hash_init()

    if theme is not None:
        styler.apply_theme(theme, disable_light_dark_mode=disable_light_dark_mode)

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
