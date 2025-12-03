"""Parameter validation for styling properties."""

import re
from typing import Any, Dict, List, Optional, Tuple
import warnings
import os


class ValidationError(ValueError):
    """Raised when validation fails for styling parameters."""


class ValidationWarning(UserWarning):
    """Warning for potential issues with styling parameters."""


class CSSValidator:
    """Comprehensive CSS property value validator."""

    # Common CSS color formats (improved patterns)
    COLOR_PATTERNS = {
        "hex_short": re.compile(r"^#[0-9a-fA-F]{3}$"),
        "hex_long": re.compile(r"^#[0-9a-fA-F]{6}$"),
        "hex_long_alpha": re.compile(r"^#[0-9a-fA-F]{8}$"),
        "rgb": re.compile(
            r"^rgb\(\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*\)$"
        ),
        "rgba": re.compile(
            r"^rgba\(\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(0(\.\d+)?|1(\.0)?)\s*\)$"
        ),
        "hsl": re.compile(r"^hsl\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*\)$"),
        "hsla": re.compile(
            r"^hsla\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*,\s*(0(\.\d+)?|1(\.0)?)\s*\)$"
        ),
    }

    # CSS named colors (expanded set including CSS keywords) CSS4 colors
    NAMED_COLORS = {
        "aliceblue",
        "antiquewhite",
        "aqua",
        "aquamarine",
        "azure",
        "beige",
        "bisque",
        "black",
        "blanchedalmond",
        "blue",
        "blueviolet",
        "brown",
        "burlywood",
        "cadetblue",
        "chartreuse",
        "chocolate",
        "coral",
        "cornflowerblue",
        "cornsilk",
        "crimson",
        "cyan",
        "darkblue",
        "darkcyan",
        "darkgoldenrod",
        "darkgray",
        "darkgreen",
        "darkgrey",
        "darkkhaki",
        "darkmagenta",
        "darkolivegreen",
        "darkorange",
        "darkorchid",
        "darkred",
        "darksalmon",
        "darkseagreen",
        "darkslateblue",
        "darkslategray",
        "darkslategrey",
        "darkturquoise",
        "darkviolet",
        "deeppink",
        "deepskyblue",
        "dimgray",
        "dimgrey",
        "dodgerblue",
        "firebrick",
        "floralwhite",
        "forestgreen",
        "fuchsia",
        "gainsboro",
        "ghostwhite",
        "gold",
        "goldenrod",
        "gray",
        "green",
        "greenyellow",
        "grey",
        "honeydew",
        "hotpink",
        "indianred",
        "indigo",
        "ivory",
        "khaki",
        "lavender",
        "lavenderblush",
        "lawngreen",
        "lemonchiffon",
        "lightblue",
        "lightcoral",
        "lightcyan",
        "lightgoldenrodyellow",
        "lightgray",
        "lightgreen",
        "lightgrey",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightslategray",
        "lightslategrey",
        "lightsteelblue",
        "lightyellow",
        "lime",
        "limegreen",
        "linen",
        "magenta",
        "maroon",
        "mediumaquamarine",
        "mediumblue",
        "mediumorchid",
        "mediumpurple",
        "mediumseagreen",
        "mediumslateblue",
        "mediumspringgreen",
        "mediumturquoise",
        "mediumvioletred",
        "midnightblue",
        "mintcream",
        "mistyrose",
        "moccasin",
        "navajowhite",
        "navy",
        "oldlace",
        "olive",
        "olivedrab",
        "orange",
        "orangered",
        "orchid",
        "palegoldenrod",
        "palegreen",
        "paleturquoise",
        "palevioletred",
        "papayawhip",
        "peachpuff",
        "peru",
        "pink",
        "plum",
        "powderblue",
        "purple",
        "red",
        "rosybrown",
        "royalblue",
        "saddlebrown",
        "salmon",
        "sandybrown",
        "seagreen",
        "seashell",
        "sienna",
        "silver",
        "skyblue",
        "slateblue",
        "slategray",
        "slategrey",
        "snow",
        "springgreen",
        "steelblue",
        "tan",
        "teal",
        "thistle",
        "tomato",
        "turquoise",
        "violet",
        "wheat",
        "white",
        "whitesmoke",
        "yellow",
        "yellowgreen",
        "transparent",
    }

    # CSS units
    LENGTH_UNITS = {
        "px",
        "em",
        "rem",
        "%",
        "vh",
        "vw",
        "pt",
        "cm",
        "mm",
        "in",
        "pc",
        "ex",
        "ch",
    }

    # CSS border styles
    BORDER_STYLES = {
        "none",
        "solid",
        "dashed",
        "dotted",
        "double",
        "groove",
        "ridge",
        "inset",
        "outset",
    }

    # CSS font weights
    FONT_WEIGHTS = {
        "thin": "100",
        "extra-light": "200",
        "light": "300",
        "normal": "400",
        "medium": "500",
        "semi-bold": "600",
        "bold": "700",
        "extra-bold": "800",
        "black": "900",
        "100": "100",
        "200": "200",
        "300": "300",
        "400": "400",
        "500": "500",
        "600": "600",
        "700": "700",
        "800": "800",
        "900": "900",
    }

    # CSS text align values
    TEXT_ALIGN_VALUES = {"left", "center", "right", "justify", "start", "end"}

    # CSS display values
    DISPLAY_VALUES = {
        "block",
        "inline",
        "inline-block",
        "flex",
        "inline-flex",
        "grid",
        "inline-grid",
        "none",
    }

    # CSS position values
    POSITION_VALUES = {"static", "relative", "absolute", "fixed", "sticky"}

    @staticmethod
    def is_valid_color(value: str) -> bool:
        """Validate CSS color value."""
        if not isinstance(value, str):
            return False

        value = value.strip().lower()

        # Check named colors
        if value in CSSValidator.NAMED_COLORS:
            return True

        # Check color patterns
        for pattern in CSSValidator.COLOR_PATTERNS.values():
            if pattern.match(value):
                return True

        return False

    @staticmethod
    def is_valid_length(value: str) -> bool:
        """Validate CSS length value (including space-separated values for properties like padding/margin)."""
        if not isinstance(value, str):
            return False

        value = value.strip()

        # Handle space-separated values (e.g., "10px 20px", "5px 10px 15px 20px")
        parts = value.split()
        if len(parts) > 1:
            # For properties like padding/margin, validate each part
            return all(CSSValidator.is_valid_length(part) for part in parts)

        # Check for 0 (unitless)
        if value == "0":
            return True

        # Check for number with unit
        length_pattern = re.compile(
            r"^-?\d*\.?\d+(" + "|".join(CSSValidator.LENGTH_UNITS) + ")$"
        )
        return bool(length_pattern.match(value))

    @staticmethod
    def is_valid_border_style(value: str) -> bool:
        """Validate CSS border style value."""
        if not isinstance(value, str):
            return False

        value = value.strip()

        return value.lower() in CSSValidator.BORDER_STYLES

    @staticmethod
    def is_valid_font_weight(value: str) -> bool:
        """Validate CSS font-weight value."""
        if not isinstance(value, str):
            return False
        return value.strip().lower() in CSSValidator.FONT_WEIGHTS

    @staticmethod
    def is_valid_text_align(value: str) -> bool:
        """Validate CSS text-align value."""
        if not isinstance(value, str):
            return False
        return value.strip().lower() in CSSValidator.TEXT_ALIGN_VALUES

    @staticmethod
    def is_valid_display(value: str) -> bool:
        """Validate CSS display value."""
        if not isinstance(value, str):
            return False
        return value.strip().lower() in CSSValidator.DISPLAY_VALUES

    @staticmethod
    def is_valid_position(value: str) -> bool:
        """Validate CSS position value."""
        if not isinstance(value, str):
            return False
        return value.strip().lower() in CSSValidator.POSITION_VALUES


class StyleValidator:
    """Main styling parameter validator."""

    # Property validation mapping
    PROPERTY_VALIDATORS = {
        # Color properties
        "color": CSSValidator.is_valid_color,
        "background_color": CSSValidator.is_valid_color,
        "border_color": CSSValidator.is_valid_color,
        # Size/length properties (can handle space-separated values)
        "font_size": CSSValidator.is_valid_length,
        "font_weight": CSSValidator.is_valid_font_weight,
        "border_width": CSSValidator.is_valid_length,
        "border_style": CSSValidator.is_valid_border_style,
    }

    # Common property aliases/variations
    PROPERTY_ALIASES = {
        "bg_color": "background_color",
        "text_color": "color",
        "font_color": "color",
        "size": "font_size",
    }

    # Properties with default unit handling
    PROPERTY_DEFAULT_UNITS = {
        "font_size": "px",
        "border_width": "px",
    }

    @classmethod
    def set_default_int_unit(cls, prop_name: str, prop_value: Any) -> Any:
        """Convert integer property values to string with 'px' unit."""
        if (prop_name in cls.PROPERTY_DEFAULT_UNITS) and isinstance(prop_value, int):
            return f"{prop_value}px"
        return prop_value

    @classmethod
    def normalize_font_weight(cls, prop_name: str, prop_value: Any) -> str:
        """Normalize font-weight values."""
        if (prop_name == "font_weight") and (prop_value in CSSValidator.FONT_WEIGHTS):
            # Map font weight names to numeric
            return CSSValidator.FONT_WEIGHTS[prop_value]

        return prop_value

    @classmethod
    def validate_property(
        cls, prop_name: str, prop_value: Any, strict: bool = False
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate a single styling property.

        Args:
            prop_name: CSS property name
            prop_value: CSS property value to validate
            strict: If True, raise errors; if False, return warnings

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Skip validation for None values
        if prop_value is None:
            return True, None

        # Convert to string for validation
        if not isinstance(prop_value, str):
            prop_value = str(prop_value)

        # Get validator function
        validator = cls.PROPERTY_VALIDATORS.get(prop_name)

        if validator is None:
            # Unknown property - warn but allow
            warning_msg = f"Unknown CSS property '{prop_name}'. Value will be passed through without validation."
            return True, warning_msg if strict else None

        # Run validation
        try:
            is_valid = validator(prop_value)
            if not is_valid:
                error_msg = cls._get_validation_error_message(prop_name, prop_value)
                return False, error_msg
            return True, None
        except Exception as e:
            error_msg = f"Validation error for property '{prop_name}': {str(e)}"
            return False, error_msg

    @classmethod
    def _get_validation_error_message(cls, prop_name: str, prop_value: str) -> str:
        """Generate helpful error message for validation failure."""
        if "color" in prop_name:
            return (
                f"Invalid color value '{prop_value}' for property '{prop_name}'. "
                f"Expected formats: #hex (e.g., #FF0000), rgb(r,g,b), rgba(r,g,b,a), "
                f"hsl(h,s%,l%), or named colors (e.g., 'red', 'blue')."
            )
        elif prop_name in ["width", "height", "font_size", "border_radius"]:
            return (
                f"Invalid length value '{prop_value}' for property '{prop_name}'. "
                f"Expected formats: number with unit (e.g., '10px', '2em', '50%') or '0'."
            )
        elif prop_name in ["padding", "margin"]:
            return (
                f"Invalid length value '{prop_value}' for property '{prop_name}'. "
                f"Expected formats: single value ('10px') or space-separated values ('10px 20px')."
            )
        elif "border_style" in prop_name:
            return (
                f"Invalid value '{prop_value}' for property '{prop_name}'. "
                f"Expected format: 'style' (e.g., solid)."
            )
        elif "border_width" in prop_name:
            return (
                f"Invalid value '{prop_value}' for property '{prop_name}'. "
                f"Expected format: 'width' (e.g., 1px)."
            )
        elif prop_name == "font_weight":
            return (
                f"Invalid font-weight value '{prop_value}'. "
                f"Expected: {', '.join(sorted(CSSValidator.FONT_WEIGHTS.keys()))}."
            )
        else:
            return f"Invalid value '{prop_value}' for CSS property '{prop_name}'."

    @classmethod
    def validate_component_kwargs(
        cls,
        component_type: str,
        kwargs: Dict[str, Any],
        strict: bool = False,
        bypass_validation: bool = False,
    ) -> Dict[str, Any]:
        """
        Validate all styling properties in component kwargs.

        Args:
            component_type: Name of the component being styled
            kwargs: Component keyword arguments
            strict: If True, raise ValidationError on invalid properties
            bypass_validation: If True, skip all validation

        Returns:
            Validated kwargs (may be modified)

        Raises:
            ValidationError: If strict=True and validation fails
        """
        if bypass_validation:
            return kwargs

        validated_kwargs = kwargs.copy()
        errors = []
        warnings_list = []

        # Check each kwarg for styling properties
        for prop_name, prop_value in kwargs.items():
            # Skip non-styling properties (streamlit native params)

            # TODO: Better way to handle Streamlit native params
            if prop_name in {
                "key",
                "help",
                "disabled",
                "label_visibility",
                "on_change",
                "args",
                "kwargs",
            }:
                continue

            # Check property aliases
            prop_name = cls.PROPERTY_ALIASES.get(prop_name, prop_name)

            # Set default unit for certain properties
            prop_value = cls.set_default_int_unit(prop_name, prop_value)
            # Normalize font-weight values
            prop_value = cls.normalize_font_weight(prop_name, prop_value)

            is_valid, message = cls.validate_property(prop_name, prop_value, strict)

            if not is_valid:
                if strict:
                    errors.append(f"Component '{component_type}': {message}")
                else:
                    warnings_list.append(f"Component '{component_type}': {message}")
                    # Remove invalid property to prevent CSS errors
                    validated_kwargs.pop(prop_name, None)
            else:
                validated_kwargs[prop_name] = prop_value
                if message and not strict:
                    # Warning message for unknown property
                    warnings_list.append(f"Component '{component_type}': {message}")

        # Handle errors and warnings
        if errors:
            error_msg = "Styling validation failed:\n" + "\n".join(errors)
            raise ValidationError(error_msg)

        if warnings_list:
            warning_msg = "Styling validation warnings:\n" + "\n".join(warnings_list)
            warnings.warn(warning_msg, ValidationWarning)

        return validated_kwargs

    @classmethod
    def suggest_corrections(cls, prop_name: str) -> List[str]:
        """Suggest corrections for invalid property values."""
        suggestions = []

        if "color" in prop_name:
            suggestions.extend(
                [
                    "Try hex colors: '#FF0000', '#00FF00', '#0000FF'",
                    "Try RGB colors: 'rgb(255, 0, 0)', 'rgba(255, 0, 0, 0.5)'",
                    "Try named colors: 'red', 'blue', 'green', 'transparent'",
                ]
            )
        elif prop_name in ["width", "height", "padding", "margin"]:
            suggestions.extend(
                [
                    "Try pixel values: '10px', '20px', '100px'",
                    "Try percentage values: '50%', '100%'",
                    "Try relative units: '1em', '2rem'",
                    "Use '0' for zero values (no unit needed)",
                ]
            )
        elif "border" in prop_name:
            suggestions.extend(
                [
                    "Try: '1px solid #000000'",
                    "Try: '2px dashed red'",
                    "Try: '3px dotted blue'",
                ]
            )

        return suggestions


def validate_styling_kwargs(
    component_type: str,
    kwargs: Dict[str, Any],
    strict: bool = False,
    bypass_validation: bool = False,
) -> Dict[str, Any]:
    """
    Main validation function for component styling kwargs.

    This is the primary interface for validating styling parameters.

    Args:
        component_type: Name of the component (e.g., 'button', 'text')
        kwargs: Component keyword arguments to validate
        strict: If True, raise ValidationError on invalid properties;
                if False, warn and remove invalid properties
        bypass_validation: If True, skip all validation (for advanced users)

    Returns:
        Validated and potentially cleaned kwargs dictionary

    Raises:
        ValidationError: If strict=True and validation fails

    Example:
        >>> kwargs = {'background_color': '#FF0000', 'invalid_prop': 'bad_value'}
        >>> validated = validate_styling_kwargs('button', kwargs, strict=False)
        >>> print(validated)  # {'background_color': '#FF0000'}
    """
    return StyleValidator.validate_component_kwargs(
        component_type, kwargs, strict, bypass_validation
    )


# Configuration for validation behavior
class ValidationConfig:
    """Global configuration for styling validation."""

    # Default validation mode
    DEFAULT_STRICT_MODE = False

    # Whether to show validation warnings
    SHOW_WARNINGS = True

    # Environment variable to bypass validation
    BYPASS_ENV_VAR = "ST_STYLED_BYPASS_VALIDATION"

    @classmethod
    def is_validation_bypassed(cls) -> bool:
        """Check if validation should be bypassed based on environment."""
        return os.getenv(cls.BYPASS_ENV_VAR, "").lower() in ("true", "1", "yes")

    @classmethod
    def get_strict_mode(cls) -> bool:
        """Get current strict mode setting."""
        strict_env = os.getenv("ST_STYLED_STRICT_VALIDATION", "").lower()
        if strict_env in ("true", "1", "yes"):
            return True
        elif strict_env in ("false", "0", "no"):
            return False
        return cls.DEFAULT_STRICT_MODE


def validate_container_width(width_value: Any) -> bool:
    """
    Validate the container width value.

    Args:
        width_value: The width value to validate

    Returns:
        Tuple of (is_valid, error_message)
    """

    if isinstance(width_value, int):
        return True
    elif width_value == "stretch":
        return True
    else:
        return False
