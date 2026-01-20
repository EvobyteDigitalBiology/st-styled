"""Image Card Component for Streamlit.

This module provides an image card component that displays an image at the top
with a title and text content below in a styled card container. The component
supports extensive customization of styling, colors, and typography.
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
def image_card_one(
    image_path: str,
    title: str,
    text: str,
    width: Literal["stretch", "content"] | int = 300,
    height: Literal["stretch", "content"] | int = "content",
    background_color: Optional[str] = None,
    card_shadow: bool = True,
    border_width: Optional[int] = None,
    border_color: Optional[str] = None,
    border_style: Optional[str] = None,
    title_font_size: Optional[int] = None,
    title_font_weight: Optional[str] = None,
    title_color: Optional[str] = None,
    text_font_size: Optional[int] = None,
    text_font_weight: Optional[str] = None,
    text_color: Optional[str] = None,
    key: Optional[str] = None,
):
    """Create an image card component with an image, title, and text content.

    This function creates a styled card container that displays an image at the top,
    followed by a title and text content in a separate section below. The card supports
    extensive customization including border styling, shadows, colors, and typography
    options for the text elements.

    Args:
        image_path (str): Path or URL to the image to display. Supports local file paths
            and remote URLs.
        title (str): Title text for the card, displayed below the image.
        text (str): Main content text for the card, displayed below the title.
        width (int | str, optional): Width of the card. Can be an integer (pixels),
            "stretch", or a CSS value string. Defaults to 300.
        height (int | str, optional): Height of the card. Can be an integer (pixels),
            "content", "stretch", or a CSS value string. Defaults to "content".
        background_color (str | None, optional): Background color of the card's text
            section. Accepts CSS color values (hex, rgb, named colors). Defaults to None,
            using theme's secondaryBackgroundColor.
        card_shadow (bool, optional): Whether to display a shadow on the card.
            Defaults to True.
        border_width (int | None, optional): Width of the card border in pixels.
            Defaults to None (no border).
        border_color (str | None, optional): Color of the card border. Accepts CSS color
            values. Defaults to None.
        border_style (str | None, optional): Style of the card border (e.g., "solid",
            "dashed", "dotted"). Defaults to None.
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
        ste.container: A styled container object configured as an image card that can be
            used with a context manager to add additional content.

    Example:
        >>> image_card_one(
        ...     image_path="https://example.com/image.jpg",
        ...     title="Beautiful Landscape",
        ...     text="Experience the beauty of nature in this stunning photograph.",
        ...     width=350,
        ...     border_width=1,
        ...     border_color="#cccccc"
        ... )

    Note:
        The image is displayed with width="stretch" to fill the card width. The text
        container below the image has rounded corners to match the card's border radius.
        Styling parameters are validated unless validation is bypassed via
        ValidationConfig.
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
            component_type="image_card_1",
            kwargs=css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

        title_css_kwargs = validate_styling_kwargs(
            component_type="image_card_1_title",
            kwargs=title_css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

        text_css_kwargs = validate_styling_kwargs(
            component_type="image_card_1_text",
            kwargs=text_css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

    # Generate unique keys for component and text container
    key = key or generate_component_key(type="custom_component")
    key_text_container = f"{key}-text-container"
    key_subheader = f"{key}_subheader"
    key_markdown = f"{key}_markdown"

    # Configure card shadow
    if card_shadow:
        box_shadow = "2px 2px rgba(0, 0, 0, 0.1)"
    else:
        box_shadow = "none"

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
        padding="0px",
        border_radius=base_radius,
        gap="0px",
    )

    # Add custom CSS to round the corners of the text container
    st.html(
        f"""
        <style>
        .st-key-{key_text_container} {{
            border-radius: {base_radius};
        }}
        </style>
        """
    )

    # Populate card with image and text content
    with cont:
        st.image(image_path, width="stretch")

        # Create text container with title and description
        with ste.container(
            background_color=background_color,
            padding="1rem",
            key=key_text_container,
            height="stretch",
        ):
            ste.subheader(title, **title_css_kwargs, key=key_subheader)
            ste.markdown(text, **text_css_kwargs, key=key_markdown)

    return cont


if __name__ == "__main__":
    # If this file is run directly, we can test our component in a simple
    # Streamlit app.

    title = "Boat Trips 2026"
    text = "Your adventure starts here! Book your boat trip now and explore the beautiful waterways with us. Don't miss out on an unforgettable experience."
