import re
import json
from pathlib import Path
from typing import Any


dirpath = Path(__file__).parent
TEMPLATE_CONFIG_PATH = dirpath / "template_config.toml"

with TEMPLATE_CONFIG_PATH.open() as f:
    TEMPLATE_CONFIG_TOML = f.read()


def validate_theme_structure(theme_name: str, theme_data: dict[str, Any]) -> None:
    """Validate that a theme file matches the required schema."""

    required_root_keys = ("defaultTheme", "lightTheme", "darkTheme")
    for key in required_root_keys:
        if key not in theme_data:
            msg = f"Theme '{theme_name}' is missing required key '{key}'."
            raise ValueError(msg)

    if theme_data["defaultTheme"] not in {"lightTheme", "darkTheme"}:
        msg = (
            f"Theme '{theme_name}' has invalid defaultTheme "
            f"'{theme_data['defaultTheme']}'."
        )
        raise ValueError(msg)

    for variant_name in ("lightTheme", "darkTheme"):
        variant_data = theme_data[variant_name]
        if not isinstance(variant_data, dict):
            msg = f"Theme '{theme_name}' section '{variant_name}' must be a dictionary."
            raise ValueError(msg)

        for section_name in ("main", "sidebar", "components"):
            if section_name not in variant_data:
                msg = (
                    f"Theme '{theme_name}' section '{variant_name}' is missing "
                    f"required key '{section_name}'."
                )
                raise ValueError(msg)
            if not isinstance(variant_data[section_name], dict):
                msg = (
                    f"Theme '{theme_name}' section '{variant_name}.{section_name}' "
                    "must be a dictionary."
                )
                raise ValueError(msg)


def load_themes() -> dict[str, dict[str, Any]]:
    """Load built-in themes from the themes directory."""

    themes: dict[str, dict[str, Any]] = {}
    themes_dir = dirpath / "themes"

    if not themes_dir.exists():
        return themes

    for theme_path in sorted(themes_dir.glob("*.json")):
        with theme_path.open() as f:
            theme_data = json.load(f)

        validate_theme_structure(theme_path.stem, theme_data)
        themes[theme_path.stem] = theme_data

    return themes

# Load elements
with (dirpath / "element_styles.json").open() as f:
    ELEMENT_STYLES = json.load(f)

with (dirpath / "css_color_names.json").open() as f:
    CSS_COLOR_NAMES_HEX = json.load(f)
    # Create lowercase version for case-insensitive matching
    CSS_COLOR_NAMES_HEX = {k.lower(): v for k, v in CSS_COLOR_NAMES_HEX.items()}

with (dirpath / "components.json").open() as f:
    COMPONENTS = json.load(f)

THEMES = load_themes()

# Backwards-compatible alias while the rest of the package migrates.
STYLE_TEMPLATES = THEMES

# Color format patterns
COLOR_PATTERNS = {
    "hex_short": re.compile(r"^#[0-9a-fA-F]{3}$"),
    "hex_long": re.compile(r"^#[0-9a-fA-F]{6}$"),
    "hex_long_alpha": re.compile(r"^#[0-9a-fA-F]{8}$"),
    "rgb": re.compile(
        r"^rgb\(\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*\)$"
    ),
    "rgba": re.compile(
        r"^rgba\(\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,\s*(0(\.\d+)?|1(\.\d+)?)\s*\)$"
    ),
    "hsl": re.compile(r"^hsl\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*\)$"),
    "hsla": re.compile(
        r"^hsla\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*,\s*(0(\.\d+)?|1(\.\d+)?)\s*\)$"
    ),
}

CSS_NAMED_COLORS = set(list(CSS_COLOR_NAMES_HEX.keys()) + ["transparent"])

CSS_LENGTH_UNITS = {
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

CSS_BORDER_STYLES = {
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

CSS_FONT_WEIGHTS = {
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

CSS_TEXT_ALIGN_VALUES = {"left", "center", "right", "justify", "start", "end"}

CSS_DISPLAY_VALUES = {
    "block",
    "inline",
    "inline-block",
    "flex",
    "inline-flex",
    "grid",
    "inline-grid",
    "none",
}

CSS_POSITION_VALUES = {"static", "relative", "absolute", "fixed", "sticky"}

CSS_PRIORITY_TAGS = {"label_", "value_", "_left", "_right", "_top", "_bottom"}
