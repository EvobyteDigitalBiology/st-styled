import json
import re
from st_yled import constants

class InvalidColorError(ValueError):
    """Raised when an invalid color value is provided."""
    pass


def _normalize_hex(color: str) -> str:
    """
    Expand 3-digit hex color to 6-digit format.

    Args:
        color: Short hex color (e.g., "#ABC")

    Returns:
        Expanded hex color (e.g., "#AABBCC")
    """
    if len(color) == 4:  # #RGB
        return f"#{color[1]}{color[1]}{color[2]}{color[2]}{color[3]}{color[3]}"
    return color


def _hsl_to_rgb(h: int, s: int, l: int) -> tuple[int, int, int]:
    """
    Convert HSL to RGB values.

    Args:
        h: Hue (0-360)
        s: Saturation percentage (0-100)
        l: Lightness percentage (0-100)

    Returns:
        Tuple of (r, g, b) values (0-255)
    """
    s = s / 100
    l = l / 100

    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (
        round((r + m) * 255),
        round((g + m) * 255),
        round((b + m) * 255)
    )


def rgb_to_hex(r: int, g: int, b: int, a: float | None = None) -> str:
    """
    Convert RGB(A) values to hex format.

    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)
        a: Optional alpha value (0.0-1.0)

    Returns:
        Hex color string (e.g., "#FF0000" or "#FF0000FF")

    Raises:
        InvalidColorError: If values are out of range
    """
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise InvalidColorError(f"RGB values must be in range 0-255: r={r}, g={g}, b={b}")

    if a is not None:
        if not (0 <= a <= 1):
            raise InvalidColorError(f"Alpha value must be in range 0-1: a={a}")
        alpha_hex = f"{round(a * 255):02X}"
        return f"#{r:02X}{g:02X}{b:02X}{alpha_hex}"

    return f"#{r:02X}{g:02X}{b:02X}"


def hsl_to_hex(h: int, s: int, l: int, a: float | None = None) -> str:
    """
    Convert HSL(A) values to hex format.

    Args:
        h: Hue (0-360)
        s: Saturation percentage (0-100)
        l: Lightness percentage (0-100)
        a: Optional alpha value (0.0-1.0)

    Returns:
        Hex color string (e.g., "#FF0000" or "#FF0000FF")

    Raises:
        InvalidColorError: If values are out of range
    """
    if not (0 <= h <= 360):
        raise InvalidColorError(f"Hue must be in range 0-360: h={h}")
    if not (0 <= s <= 100):
        raise InvalidColorError(f"Saturation must be in range 0-100: s={s}")
    if not (0 <= l <= 100):
        raise InvalidColorError(f"Lightness must be in range 0-100: l={l}")

    r, g, b = _hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b, a)


def named_to_hex(color: str) -> str:
    """
    Convert named CSS color to hex format.

    Args:
        color: CSS color name (case-insensitive)

    Returns:
        Hex color string (e.g., "#FF0000")

    Raises:
        InvalidColorError: If color name is not recognized
    """
    color_lower = color.lower()
    if color_lower not in constants.CSS_COLOR_NAMES_HEX:
        raise InvalidColorError(f"Unknown color name: {color}")

    hex_value = constants.CSS_COLOR_NAMES_HEX[color_lower]
    return hex_value.upper() if hex_value.startswith("#") else f"#{hex_value.upper()}"


def to_hex(color: str) -> str:
    """
    Convert any supported color format to hex format.

    Supported formats:
    - Hex: #RGB, #RRGGBB, #RRGGBBAA
    - RGB: rgb(r, g, b)
    - RGBA: rgba(r, g, b, a)
    - HSL: hsl(h, s%, l%)
    - HSLA: hsla(h, s%, l%, a)
    - Named colors (CSS4 color names)

    Args:
        color: Color string in any supported format

    Returns:
        Hex color string in uppercase (e.g., "#FF0000" or "#FF0000FF")
        Alpha channel is included only if present in input.

    Raises:
        InvalidColorError: If color format is invalid or unrecognized

    Examples:
        >>> to_hex("#abc")
        "#AABBCC"
        >>> to_hex("rgb(255, 0, 0)")
        "#FF0000"
        >>> to_hex("rgba(255, 0, 0, 0.5)")
        "#FF000080"
        >>> to_hex("hsl(0, 100%, 50%)")
        "#FF0000"
        >>> to_hex("red")
        "#FF0000"
    """
    color = color.strip()

    # Check hex formats
    if constants.COLOR_PATTERNS["hex_short"].match(color):
        return _normalize_hex(color).upper()

    if constants.COLOR_PATTERNS["hex_long"].match(color):
        return color.upper()

    if constants.COLOR_PATTERNS["hex_long_alpha"].match(color):
        return color.upper()

    # Check RGB format
    if constants.COLOR_PATTERNS["rgb"].match(color):
        # Extract RGB values
        values = re.findall(r"\d+", color)
        r, g, b = int(values[0]), int(values[1]), int(values[2])
        return rgb_to_hex(r, g, b)

    # Check RGBA format
    if constants.COLOR_PATTERNS["rgba"].match(color):
        # Extract RGBA values
        match = re.search(
            r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)",
            color
        )
        if match:
            r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
            a = float(match.group(4))
            return rgb_to_hex(r, g, b, a)

    # Check HSL format
    if constants.COLOR_PATTERNS["hsl"].match(color):
        # Extract HSL values
        match = re.search(r"hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)", color)
        if match:
            h, s, l = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return hsl_to_hex(h, s, l)

    # Check HSLA format
    if constants.COLOR_PATTERNS["hsla"].match(color):
        # Extract HSLA values
        match = re.search(
            r"hsla\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*,\s*([\d.]+)\s*\)",
            color
        )
        if match:
            h, s, l = int(match.group(1)), int(match.group(2)), int(match.group(3))
            a = float(match.group(4))
            return hsl_to_hex(h, s, l, a)

    # Check named colors (case-insensitive)
    if color.lower() in constants.CSS_COLOR_NAMES_HEX:
        return named_to_hex(color)

    # If no pattern matched, raise error
    raise InvalidColorError(
        f"Invalid color format: {color}. "
        "Supported formats: hex (#RGB, #RRGGBB, #RRGGBBAA), "
        "rgb(r,g,b), rgba(r,g,b,a), hsl(h,s%,l%), hsla(h,s%,l%,a), "
        "or CSS color names."
    )
