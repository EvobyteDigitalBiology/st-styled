"""Badge Card Component for Streamlit.

This module provides a badge card component that displays a badge, title, and
text content in a styled card container. The component supports extensive
customization of styling, colors, and typography.
"""
from typing import Optional, Literal
import typing

import streamlit as st

import st_yled.elements as ste

from st_yled.styler import generate_component_key  # type: ignore
from st_yled.validation import validate_styling_kwargs  # type: ignore
from st_yled.validation import ValidationConfig  # type: ignore
from st_yled.components.base import card_base  # type: ignore

__version__ = "0.1.0"


@typing.no_type_check
def badge_card_one(
    badge_text: str,
    title: str,
    text: str,
    badge_icon: Optional[str] = None,
    width: int | str = 200,
    height: int | str = "content",
    background_color: Optional[str] = None,
    card_shadow: bool = True,
    border_width: Optional[int] = None,
    border_color: Optional[str] = None,
    border_style: Optional[str] = None,
    badge_color: Literal[
        "red", "orange", "yellow", "blue", "green", "violet", "gray", "grey", "primary"
    ] = "primary",
    title_font_size: Optional[int] = None,
    title_font_weight: Optional[str] = None,
    title_color: Optional[str] = None,
    text_font_size: Optional[int] = None,
    text_font_weight: Optional[str] = None,
    text_color: Optional[str] = None,
    key: Optional[str] = None,
) -> ste.container:
    """Create a badge card component with a badge, title, and text content.

    This function creates a styled card container that displays a badge at the top,
    followed by a title and text content. The card supports extensive customization
    including border styling, shadows, colors, and typography options for each element.

    Args:
        badge_text (str): Text to display in the badge.
        title (str): Title text for the card.
        text (str): Main content text for the card.
        badge_icon (str | None, optional): Material icon to display in the badge.
            Format: ":material/icon_name:". Defaults to None.
        width (int | str, optional): Width of the card. Can be an integer (pixels),
            "stretch", or a CSS value string. Defaults to 200.
        height (int | str, optional): Height of the card. Can be an integer (pixels),
            "content", "stretch", or a CSS value string. Defaults to "content".
        background_color (str | None, optional): Background color of the card. Accepts CSS
            color values (hex, rgb, named colors). Defaults to None, using theme's
            secondaryBackgroundColor.
        card_shadow (bool, optional): Whether to display a shadow on the card.
            Defaults to True.
        border_width (int | None, optional): Width of the card border in pixels.
            Defaults to None (no border).
        border_color (str | None, optional): Color of the card border. Accepts CSS color
            values. Defaults to None.
        border_style (str | None, optional): Style of the card border (e.g., "solid",
            "dashed", "dotted"). Defaults to None.
        badge_color (str, optional): Color theme for the badge. Options: "red", "orange",
            "yellow", "blue", "green", "violet", "gray", "grey", "primary".
            Defaults to "primary".
        title_font_size (int | None, optional): Font size for the title in pixels.
            Defaults to None (theme default).
        title_font_weight (str | None, optional): Font weight for the title (e.g., "bold",
            "normal", "light"). Defaults to None.
        title_color (str | None, optional): Color of the title text. Accepts CSS color
            values. Defaults to None (theme default).
        text_font_size (int | None, optional): Font size for the text content in pixels.
            Defaults to None (theme default).
        text_font_weight (str | None, optional): Font weight for the text content.
            Defaults to None.
        text_color (str | None, optional): Color of the text content. Accepts CSS color
            values. Defaults to None (theme default).
        key (str | None, optional): Unique key for the component. If None, a key will be
            auto-generated. Defaults to None.

    Returns:
        ste.container: A styled container object configured as a badge card that can be
            used with a context manager to add additional content.

    Example:
        >>> badge_card_one(
        ...     badge_text="NEW",
        ...     title="Special Feature",
        ...     text="Check out our latest feature!",
        ...     badge_icon=":material/star:",
        ...     badge_color="yellow",
        ...     width=250
        ... )

    Note:
        Styling parameters are validated unless validation is bypassed via
        ValidationConfig. The card uses the card_base component for consistent
        styling across card components.
    """

    # Check if validation should be bypassed
    bypass_validation = ValidationConfig.is_validation_bypassed()
    strict_mode = ValidationConfig.get_strict_mode()

    # Set default background color from theme or fallback
    background_color = (
        background_color or st.get_option("theme.secondaryBackgroundColor") or "#f0f2f6"
    )
    base_radius = st.get_option("theme.baseRadius") or "0.5rem"

    # Prepare styling kwargs for validation
    css_kwargs = {
        "background_color": background_color,
        "border_width": border_width,
        "border_color": border_color,
        "border_style": border_style,
    }

    title_css_kwargs = {
        "font_size": title_font_size,
        "font_weight": title_font_weight,
        "color": title_color,
    }

    text_css_kwargs = {
        "font_size": text_font_size,
        "font_weight": text_font_weight,
        "color": text_color,
    }

    # Validate styling parameters if not bypassed
    if not bypass_validation:
        css_kwargs = validate_styling_kwargs(
            component_type="badge_card_1",
            kwargs=css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

        title_css_kwargs = validate_styling_kwargs(
            component_type="badge_card_1_title",
            kwargs=title_css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

        text_css_kwargs = validate_styling_kwargs(
            component_type="badge_card_1_text",
            kwargs=text_css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

    # Generate unique key for component
    key = key or generate_component_key(type="custom_component")

    title_key = f"{key}_title"
    text_key = f"{key}_text"

    # Configure card shadow
    if card_shadow:
        box_shadow = "2px 2px rgba(0, 0, 0, 0.1)"
    else:
        box_shadow = "none"

    # Add custom CSS to adjust badge spacing
    st.html(
        f"""
        <style>
        .st-key-{key} p:has(.stMarkdownBadge) {{
            margin-bottom: 8px;
        }}
        </style>
        """
    )

    # Create base card container with styling
    cont = card_base(
        key=key,
        width=width,
        height=height,
        background_color=css_kwargs["background_color"],
        border_width=css_kwargs["border_width"],
        border_color=css_kwargs["border_color"],
        border_style=css_kwargs["border_style"],
        box_shadow=box_shadow,
        padding="1rem",
        border_radius=base_radius,
        gap="0.5rem",
    )

    # Populate card with badge, title, and text
    with cont:
        ste.badge(badge_text, icon=badge_icon, color=badge_color)
        ste.subheader(title, **title_css_kwargs, key=title_key)
        ste.markdown(text, **text_css_kwargs, key=text_key)

    return cont


if __name__ == "__main__":
    # If this file is run directly, we can test our component in a simple
    # Streamlit app.

    badge_text = "NEW"
    title = "Boat Trips"
    text = "Boats. Boats. Boats."
