import json
import uuid
from pathlib import Path
from typing import Any, Optional

import streamlit as st

from st_yled.validation import validate_styling_kwargs  # type: ignore
from st_yled.validation import ValidationConfig  # type: ignore

dirpath = Path(__file__).parent

with (dirpath / "element_styles.json").open() as f:
    ELEMENT_STYLES = json.load(f)


def get_css_properties_from_args(
    component_type: str, component_kwargs: dict[str, Any]
) -> dict[str, dict[str, str]]:
    """Get CSS properties from component arguments."""
    css_properties: dict[str, dict[str, str]] = {}
    if component_type in ELEMENT_STYLES:
        # Return dict of css properties and selectors for component
        style_mappings = ELEMENT_STYLES[component_type]

        args_to_remove = []

        # Loop over component arguments and check if those are in style mappings
        for comp_arg in component_kwargs:
            # Comp arg eg.g background_color
            if comp_arg in style_mappings:
                args_to_remove.append(comp_arg)
                # Get css selectors for css property as a dict
                css_for_selectors = style_mappings[comp_arg]

                # [css_selector] > dict(css_property: css_value or None)
                for sel, sel_css in css_for_selectors.items():
                    # Update css values for selector. If css_value is set, then take over, else set comp_val
                    new_sel_css = {}
                    for k, v in sel_css.items():
                        if v is None:
                            new_sel_css[k] = component_kwargs[comp_arg]
                        else:
                            new_sel_css[k] = v

                    if sel in css_properties:
                        css_properties[sel].update(new_sel_css)
                    else:
                        css_properties[sel] = new_sel_css
    else:
        msg = f"Component type '{component_type}' not found. Are you sure this component exists?"
        raise ValueError(msg)

    # Remove any args that were used for styling
    for arg in args_to_remove:
        del component_kwargs[arg]

    return css_properties


def generate_component_css(
    component_type: str, component_kwargs: dict[str, Any], component_key: Optional[str]
) -> str:
    """Generate CSS for a component."""
    css_properties = get_css_properties_from_args(component_type, component_kwargs)

    if css_properties:
        css_rules = []
        for selector, properties in css_properties.items():
            if component_key is None:
                selector_plus_key = selector
            else:
                selector_plus_key = f".st-key-{component_key} {selector}"

            rules = [
                f"    {prop}: {val} !important;" for prop, val in properties.items()
            ]
            rules_str = "\n".join(rules)
            css_rule = f"{selector_plus_key} {{\n{rules_str}\n}}"
            css_rules.append(css_rule)

        return "\n".join(css_rules)
    return ""


def apply_component_css(component_type: str, kwargs: dict[str, Any]) -> dict[str, Any]:
    """
    Apply CSS to a specific component with parameter validation.

    Args:
        component_type: Type of component (e.g., 'button', 'text')
        kwargs: Component keyword arguments including styling properties

    Returns:
        Validated kwargs with CSS applied via st.html()

    Raises:
        ValidationError: If validation is in strict mode and validation fails
    """
    # Check if validation should be bypassed
    bypass_validation = ValidationConfig.is_validation_bypassed()
    strict_mode = ValidationConfig.get_strict_mode()

    # Validate styling parameters if not bypassed
    if not bypass_validation:
        # TODO: Cache validation results
        kwargs = validate_styling_kwargs(
            component_type=component_type,
            kwargs=kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )

    # Generate unique key if not provided
    if "key" not in kwargs:
        kwargs["key"] = f"st-yler-{uuid.uuid4()}"

    # Generate and apply CSS
    # component kwargs are removed of styling properties
    css = generate_component_css(component_type, kwargs, kwargs["key"])

    if css:
        st.html(f"<style>{css}</style>")

    return kwargs


def apply_component_css_global(
    component_type: str, component_kwargs: dict[str, Any]
) -> None:
    """
    Apply global CSS styles to all components with parameter validation.

    Args:
        component_type: Type of component to style globally
        component_kwargs: Styling properties to apply

    Raises:
        ValidationError: If validation fails in strict mode
        ValueError: If component type or properties are invalid
    """
    # Check if validation should be bypassed
    bypass_validation = ValidationConfig.is_validation_bypassed()
    strict_mode = ValidationConfig.get_strict_mode()

    # Validate styling parameters if not bypassed
    if not bypass_validation:
        validated_kwargs = validate_styling_kwargs(
            component_type=component_type,
            kwargs=component_kwargs,
            strict=strict_mode,
            bypass_validation=False,
        )
    else:
        validated_kwargs = component_kwargs

    for styled_prop, value in validated_kwargs.items():
        single_prop_kwargs = {styled_prop: value}
        css = generate_component_css(component_type, single_prop_kwargs, None)
        if css:
            # Apply CSS globally without key
            # This will affect all components of this type
            st.html(f"<style>{css}</style>")
        else:
            if "-" in styled_prop:
                did_you_mean_ext = styled_prop.replace("-", "_")
                did_you_mean_ext = f"Did you mean '{did_you_mean_ext}'?"
            else:
                did_you_mean_ext = ""

            msg = f"No st_yled property {styled_prop} found for component type '{component_type}'. {did_you_mean_ext}"
            raise ValueError(msg)
