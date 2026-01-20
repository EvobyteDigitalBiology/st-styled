import typing
import streamlit as st
from typing import List

from st_yled.styler import generate_component_key
from st_yled.validation import ValidationConfig, validate_styling_kwargs
from st_yled.colors import adjust_lightness
from st_yled.colors import to_hex
from st_yled.colors import update_opacity

__version__ = "0.1.0"


@typing.no_type_check
def split_button(
    label: str,
    options: List[str],
    icon: str | None = None,
    color: str | None = None,
    background_color: str | None = None,
    radius: int | str = "20px",
    key: str | None = None,
):
    """Create a split button component
    A split button is a combination of a primary action button and a dropdown menu.

    The primary action button is always visible, while the dropdown menu is hidden until the user interacts with the button.
    The button design is inspired by the Google Material Design 3 design system.

        The component returns the label of the button or the selected option from the dropdown menu, or None if no action has been taken.

    Args:
        label: The label of the primary action button (e.g. "Submit").
        options: A list of options for the dropdown menu (e.g. ["Option 1", "Option 2"]).
        icon: An optional icon to display on the primary action button. Identical to st.button icon parameter.
        color: The text color of the button and dropdown menu (CSS color value, e.g. "blue").
        background_color: The background color of the button and dropdown menu (CSS color value, e.g. "#FF5733").
        radius: The border radius of the button and dropdown menu (CSS value, e.g. "4px").
        key: An optional key to use for the component. If not provided, a default key will be used.

    Returns:
        The label of the button or the selected option from the dropdown menu, or None

    Raises:
        ValueError: If the options list is empty.
        ValdiationError: If any of the provided CSS values are invalid.
    """

    if len(options) == 0:
        msg = "The options list must contain at least one option."
        raise ValueError(msg)

    # Check if validation should be bypassed
    bypass_validation = ValidationConfig.is_validation_bypassed()
    strict_mode = ValidationConfig.get_strict_mode()

    return_value = None
    key = key or generate_component_key(type="custom_component")

    main_container = st.container(key=key)

    # Extract primary color from theme and calculated derived colors
    # Hover color is decreased lightness by 15%
    # Shadow color is primary color with 50% opacity
    # Must be fixed and aligned to accept all standard color formats

    primary_color = background_color or st.get_option("theme.primaryColor") or "#ff4b4b"
    color = color or st.get_option("theme.textColor") or "#FFFFFF"

    # Perform Validation for CSS values
    css_kwargs = {"background_color": primary_color, "color": color, "radius": radius}

    if not bypass_validation:
        css_kwargs = validate_styling_kwargs(
            component_type="split_button",
            kwargs=css_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

    primary_color = css_kwargs["background_color"]
    color = css_kwargs["color"]
    radius = css_kwargs["radius"]

    primary_color = to_hex(primary_color)
    primary_hover_color = adjust_lightness(primary_color, -0.15)
    primary_hover_shadow = update_opacity(primary_color, -0.5)

    # Apply CSS to style the button and selectbox to look like a split button
    st.html(
        f"""
    <style>
    .st-key-{key} {{
        display: flex;
        flex-direction: row;
        gap: 2px;
    }}

    .st-key-{key} button {{
        width: max-content;
        padding-left: 16px;
        padding-right: 12px;
        padding-top: 4px;
        padding-bottom: 4px;
        margin: 0px;
        border-top-right-radius: 4px;
        border-bottom-right-radius: 4px;
        border-top-left-radius: {radius};
        border-bottom-left-radius: {radius};
        background-color: {primary_color};
        border: none;
    }}

    .st-key-{key} button p,
    .st-key-{key} button span
    {{
        color: {color};
    }}

    .st-key-{key} button:hover {{
        background-color: {primary_hover_color};
    }}

    .st-key-{key}-selectbox {{
        width: max-content;
    }}

    .st-key-{key}-selectbox > div > div > div {{
        background-color: {primary_color};
        border-color: {primary_color};
        border-top-right-radius: {radius};
        border-bottom-right-radius: {radius};
        border-top-left-radius: 4px;
        border-bottom-left-radius: 4px;
    }}

    .st-key-{key}-selectbox > div > div > div:hover {{
        background-color: {primary_hover_color};
        border-color: {primary_hover_color};
    }}

    .st-key-{key}-selectbox > div > div > div:active {{
        background-color: {primary_color};
        border-color: {primary_color};
    }}

    .st-key-{key}-selectbox div[data-testid="stSelectbox"]:has(input:focus) > div > div {{
        box-shadow: {primary_hover_shadow} 0px 0px 0px 0.2rem;
        background-color: {primary_hover_color};
    }}

    .st-key-{key}-selectbox > div > div > div > div:has(svg) {{
        padding-right: 11px;
        padding-left: 9px;
    }}

    .st-key-{key}-selectbox svg {{
        color: {color};
    }}

    .st-key-{key}-selectbox svg[title="Clear value"]  {{
        display: none;
    }}

    .st-key-{key}-selectbox div[data-baseweb="select"] > div > div > div:not(:has(input))  {{
        display: none;
    }}

    .st-key-{key}-selectbox div[data-baseweb="select"] > div > div:has(input)  {{
        background-color: red;
        padding: 0px;
        width: 0px;
        min-width: 0px;
        flex-grow: 0;
    }}

    div[data-baseweb="popover"] div ul {{
       min-width: 160px;
    }}

    .st-key-{key}-selectbox div[data-testid="stSelectbox"]:has(input:disabled) > div > div {{
        background-color: transparent;
        border-color: {primary_hover_color};
    }}

    </style>
    """
    )

    # Place button and selectbox in a horizontal container
    with main_container:
        if st.button(
            label,
            icon=icon,
            use_container_width=False,
            key=f"{key}-button",
            type="primary",
        ):
            return_value = label

        select_value = st.selectbox(
            label="split-button",
            options=options,
            key=f"{key}-selectbox",
            label_visibility="collapsed",
            index=None,
        )

        if not return_value and select_value:
            return_value = select_value

    return return_value


if __name__ == "__main__":
    # If this file is run directly, we can test our component in a simple
    # Streamlit app.

    import st_yled

    st_yled.init()

    clicks = split_button(
        label="Hello", options=["Click Me 1", "Click Me 2", "Click Me 3"]
    )

    st.write(f"You clicked the option {clicks}.")

    clicks = split_button(
        label="Hello",
        icon=":material/home:",
        options=["Click Me 1", "Click Me 2", "Click Me 3"],
        key="test01",
        radius="8px",
    )

    st.write(f"You clicked the option {clicks}.")
