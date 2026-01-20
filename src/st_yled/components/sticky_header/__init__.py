"""Sticky Header Component for Streamlit.

This module provides a sticky header component that remains fixed at the top of the
Streamlit app while scrolling. The header supports customizable styling including
height, background color, alignment, and padding.
"""
from typing import Literal
import typing

import streamlit as st

import st_yled
import st_yled.elements as ste
from st_yled.styler import generate_component_key  # type: ignore
from st_yled.validation import validate_styling_kwargs  # type: ignore
from st_yled.validation import ValidationConfig  # type: ignore

__version__ = "0.1.0"


@typing.no_type_check
def sticky_header(
    height: int | str = "56px",
    background_color: str | None = None,
    vertical_alignment: Literal["top", "center", "bottom"] = "center",
    horizontal_alignment: Literal["left", "center", "right"] = "left",
    padding: str = "0px 32px",
    gap: Literal["small", "medium", "large"] = "small",
    key: str | None = None,
):
    """Create a sticky header container that remains fixed at the top of the page.

    This function creates a header container that stays fixed at the top of the Streamlit
    app while the rest of the content scrolls beneath it. The header supports horizontal
    layout with customizable styling options.

    Args:
        height (int | str, optional): Height of the header. Can be an integer (pixels) or
            a CSS value string. Defaults to '56px'.
        background_color (str | None, optional): Background color of the header. Accepts CSS color
            values (hex, rgb, named colors). Defaults to None, in which case the theme's primary color
            is used.
        vertical_alignment (str, optional): Vertical alignment of content within the header.
            Options: "top", "center", "bottom". Defaults to "center".
        horizontal_alignment (str, optional): Horizontal alignment of content within the header.
            Options: "left", "center", "right". Defaults to "left".
        padding (str, optional): CSS padding value for the header content. Defaults to "0px 32px".
        gap (str, optional): Gap between elements in the header. Options: "small", "medium",
            "large" or CSS value. Defaults to "small".
        key (str | None, optional): Unique key for the component. If None, a key will be
            auto-generated. Defaults to None.

    Returns:
        ste.container: A styled container object configured as a sticky header that can be
            used with a context manager to add content.

    Example:
        >>> with sticky_header(height='60px', background_color='#ffffff'):
        ...     st.title("My App")
        ...     st.button("Menu")

    Note:
        The header uses absolute positioning with high z-index values (999991-999992) to
        ensure it stays on top of other content. Styling parameters are validated unless
        validation is bypassed via ValidationConfig.
    """

    # Check if validation should be bypassed
    bypass_validation = ValidationConfig.is_validation_bypassed()
    strict_mode = ValidationConfig.get_strict_mode()

    background_color = (
        background_color or st.get_option("theme.primaryColor") or "#ff4b4b"
    )

    # run validation for vertical alignment and background color
    css_kwargs = {
        "height": height,
        "background_color": background_color,
        "padding": padding,
    }

    # Validate styling parameters if not bypassed
    if not bypass_validation:
        css_kwargs = validate_styling_kwargs(
            component_type="sticky_header",
            kwargs=css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

    height = css_kwargs["height"]
    background_color = css_kwargs["background_color"]
    padding = css_kwargs["padding"]

    key = key or generate_component_key(type="custom_component")
    header_bg_key = f"{key}-bg"

    st.html(
        f"""
    <style>
    .st-key-{header_bg_key} {{
        position: absolute;
        top: 0;
        left: 0;
        z-index: 999991;
        width: 100%;
        border-radius: 0px;
        height: {height} !important;
        min-height: {height} !important;
    }}

    .st-key-{key} {{
        position: absolute;
        top: 0;
        left: 0;
        z-index: 999992;
        height: {height} !important;
        min-height: {height} !important;
        background-color: transparent;
    }}
    </style>
    """
    )

    sticky_header_bg = ste.container(
        key=header_bg_key,
        background_color=background_color,
        padding="0px",
        border_width="0px",
    )

    with sticky_header_bg:
        st.write("")

    return st_yled.container(
        key=key,
        horizontal=True,
        vertical_alignment=vertical_alignment,
        horizontal_alignment=horizontal_alignment,
        width="stretch",
        padding=padding,
        gap=gap,
    )
