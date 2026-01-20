import re
import json
from pathlib import Path


dirpath = Path(__file__).parent

# Load elements
with (dirpath / "element_styles.json").open() as f:
    ELEMENT_STYLES = json.load(f)

with (dirpath / "css_color_names.json").open() as f:
    CSS_COLOR_NAMES_HEX = json.load(f)
    # Create lowercase version for case-insensitive matching
    CSS_COLOR_NAMES_HEX = {k.lower(): v for k, v in CSS_COLOR_NAMES_HEX.items()}

with (dirpath / "components.json").open() as f:
    COMPONENTS = json.load(f)

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
