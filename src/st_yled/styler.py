import json
from pathlib import Path
from typing import Any, Optional
import re
import warnings
import traceback

import streamlit as st

from st_yled.validation import validate_styling_kwargs  # type: ignore
from st_yled.validation import ValidationConfig  # type: ignore
from st_yled.validation import ValidationError  # type: ignore

dirpath = Path(__file__).parent

with (dirpath / "element_styles.json").open() as f:
    ELEMENT_STYLES = json.load(f)


def extract_caller_path_hash() -> str:
    traceback_stack = traceback.extract_stack()

    exec_line = False
    caller_path = ""
    # Traverse traceback in reverse order
    for line in traceback_stack[::-1]:
        if exec_line:
            caller_path = line.filename
            break
        if isinstance(line.line, str) and line.line.startswith(
            "exec(code, module.__dict__)"
        ):
            exec_line = True

    if caller_path == "":
        warnings.warn("Could not extract caller path from traceback.")

    return str(hash(caller_path))


def get_element_style(element_name: str) -> dict:
    """
    Get the style definition for a given element name.

    Args:
        element_name: The name of the element to retrieve the style for.

    Returns:
        A dictionary containing the style definition if found, else None.

    Example:
        >>> get_element_style("button")
        {
            "css": {
                ".stButton > button": {
                    "background-color": None
    """

    return ELEMENT_STYLES[element_name]


def get_stylable_elements(include_variants: bool = True) -> list[str]:
    """
    Get a list of all stylable component names from ELEMENT_STYLES.

    Args:
        include_variants: If True, includes variants like 'button_primary', 'button_secondary'.
                         If False, only returns base components like 'button'.

    Returns:
        Sorted list of component names that can be styled.

    Example:
        >>> get_stylable_elements(include_variants=False)
        ['button', 'caption', 'code', ...]
        >>> get_stylable_elements(include_variants=True)
        ['button', 'button_primary', 'button_secondary', 'caption', ...]
    """
    if include_variants:
        return sorted(ELEMENT_STYLES.keys())

    # Filter out variants ending with _primary, _secondary, _tertiary
    variant_pattern = re.compile(r".*_(primary|secondary|tertiary)$")
    base_elements = [
        key for key in ELEMENT_STYLES.keys() if not variant_pattern.match(key)
    ]
    return sorted(base_elements)


def get_stylable_elements_by_category() -> dict[str, dict[str, list[str]]]:
    """
    Get stylable components organized by category with variants.

    Args:
        include_variants: If True, includes variants like 'button_primary', 'button_secondary'.
                         If False, only returns base components with 'primary' as default variant.

    Returns:
        Nested dictionary structure:
        {
            'category': {
                'element': ['variant1', 'variant2', ...]
            }
        }

        If no variants are found for an element, defaults to ['primary'].

    Example:
        >>> get_stylable_elements_by_category(include_variants=True)
        {
            'input': {
                'button': ['primary', 'secondary', 'tertiary'],
                'checkbox': ['primary'],
                ...
            },
            'text': {
                'caption': ['primary'],
                'code': ['primary'],
                ...
            }
        }
    """
    # Get all elements (always include variants to find them)
    all_elements = sorted(ELEMENT_STYLES.keys())

    # Group by category and base element
    categories: dict[str, dict[str, list[str]]] = {}

    # Pattern to extract base element and variant
    variant_pattern = re.compile(
        r"^(?P<base>.+?)_(?P<variant>primary|secondary|tertiary)$"
    )

    for element in all_elements:
        if element not in ELEMENT_STYLES:
            continue

        category = ELEMENT_STYLES[element].get("category", "unknown")

        # Check if this is a variant or base element
        match = variant_pattern.match(element)
        if match:
            # This is a variant (e.g., button_primary)
            base_element = match.group("base")
            variant = match.group("variant")
        else:
            # This is a base element (e.g., button)
            base_element = element
            variant = "primary"  # Default variant

        # Initialize category if not exists
        if category not in categories:
            categories[category] = {}

        # Initialize base element if not exists
        if base_element not in categories[category]:
            categories[category][base_element] = []

        # Add variant if not already present
        if variant not in categories[category][base_element]:
            categories[category][base_element].append(variant)

    # Sort variants within each element and sort elements within each category
    for category in categories:
        # Sort elements in category
        sorted_elements = dict(sorted(categories[category].items()))
        # Sort variants for each element
        for element in sorted_elements:
            sorted_elements[element].sort()
        categories[category] = sorted_elements

    return dict(sorted(categories.items()))


def get_element_variants(element_name: str) -> list[str]:
    """
    Get all variants for a given element name.

    Args:
        element_name: The base name of the element (e.g., 'button').

    Returns:
        A list of variant names (e.g., ['primary', 'secondary', 'tertiary']).
    """
    variants = []
    if element_name not in ELEMENT_STYLES:
        value_error_msg = f"Element '{element_name}' not found in stylable elements."
        raise ValueError(value_error_msg)

    for element in ELEMENT_STYLES:
        if element.startswith(f"{element_name}_"):
            match = re.match(
                rf"{re.escape(element_name)}_(primary|secondary|tertiary)$", element
            )
            if match:
                variants.append(match.group(1))

    return variants


def generate_component_key() -> str:
    """Generate a unique component key for st_yled components."""

    caller_hash = extract_caller_path_hash()

    if f"st-yled-comp-{caller_hash}-counter" not in st.session_state:
        error_msg = "Session State not initialized for st_yled component key generation.\n\nWas st_yled.init() called?"
        raise ValidationError(error_msg)

    comp_counter = st.session_state[f"st-yled-comp-{caller_hash}-counter"]
    comp_key = f"st-yler-comp-{caller_hash}-{comp_counter}"

    st.session_state[f"st-yled-comp-{caller_hash}-counter"] += 1

    return comp_key


def get_css_properties_from_args(
    component_type: str, component_kwargs: dict[str, Any]
) -> dict[str, dict[str, str]]:
    """Get CSS properties from component arguments."""

    css_properties: dict[str, dict[str, str]] = {}

    if component_type in ELEMENT_STYLES:
        # Return dict of css properties and selectors for component
        style_mappings = ELEMENT_STYLES[component_type]["css"]

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
        kwargs["key"] = generate_component_key()

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
