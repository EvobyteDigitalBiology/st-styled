import colorsys
import re
import typing
from st_yled import constants


class InvalidColorError(ValueError):
    """Raised when an invalid color value is provided."""


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


@typing.no_type_check
def _hsl_to_rgb(h: float, s: float, l: float) -> tuple[float, float, float]:
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

    return (round((r + m) * 255), round((g + m) * 255), round((b + m) * 255))


@typing.no_type_check
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
        msg = f"RGB values must be in range 0-255: r={r}, g={g}, b={b}"
        raise InvalidColorError(msg)

    if a is not None:
        if not (0 <= a <= 1):
            msg = f"Alpha value must be in range 0-1: a={a}"
            raise InvalidColorError(msg)
        alpha_hex = f"{round(a * 255):02X}"
        return f"#{r:02X}{g:02X}{b:02X}{alpha_hex}"

    return f"#{r:02X}{g:02X}{b:02X}"


def hsl_to_hex(h: float, s: float, l: int, a: float | None = None) -> str:
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
        msg = f"Hue must be in range 0-360: h={h}"
        raise InvalidColorError(msg)
    if not (0 <= s <= 100):
        msg = f"Saturation must be in range 0-100: s={s}"
        raise InvalidColorError(msg)
    if not (0 <= l <= 100):
        msg = f"Lightness must be in range 0-100: l={l}"
        raise InvalidColorError(msg)

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
        msg = f"Unknown color name: {color}"
        raise InvalidColorError(msg)

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
            r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)", color
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
            r"hsla\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*,\s*([\d.]+)\s*\)", color
        )
        if match:
            h, s, l = int(match.group(1)), int(match.group(2)), int(match.group(3))
            a = float(match.group(4))
            return hsl_to_hex(h, s, l, a)

    # Check named colors (case-insensitive)
    if color.lower() in constants.CSS_COLOR_NAMES_HEX:
        return named_to_hex(color)

    # If no pattern matched, raise error
    msg = f"Invalid color format: {color}. Supported formats: hex (#RGB, #RRGGBB, #RRGGBBAA), rgb(r,g,b), rgba(r,g,b,a), hsl(h,s%,l%), hsla(h,s%,l%,a), or CSS color names."
    raise InvalidColorError(msg)


@typing.no_type_check
def adjust_lightness(hex_color: str, factor: float) -> str:
    """
    Adjust the lightness of a hex color by a given factor.

    Args:
        color: Hex color string (e.g., "#FF0000" or "#FF0000FF")
        factor: Amount to adjust lightness (-1.0 to 1.0).
               Negative values decrease lightness, positive values increase it.
               For example, -0.15 decreases lightness by 15%.

    Returns:
        Hex color string with adjusted lightness, preserving alpha if present

    Raises:
        InvalidColorError: If color format is invalid or factor is out of range

    Examples:
        >>> adjust_lightness("#FF0000", -0.15)
        "#D90000"
        >>> adjust_lightness("#FF0000FF", -0.15)
        "#D90000FF"
        >>> adjust_lightness("#0080FF", 0.2)
        "#66B3FF"
    """
    if not -1.0 <= factor <= 1.0:
        msg = f"Factor must be in range -1.0 to 1.0: factor={factor}"
        raise InvalidColorError(msg)

    # Remove the # prefix
    hex_color = hex_color.lstrip("#")

    # Check if alpha channel is present
    has_alpha = len(hex_color) == 8

    # Extract RGB and optional alpha
    if has_alpha:
        r, g, b = (
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16),
        )
        alpha_hex = hex_color[6:8]
    else:
        r, g, b = (
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16),
        )
        alpha_hex = None

    # Convert RGB to HLS (Hue, Lightness, Saturation)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)

    # Adjust lightness
    l = max(0, min(1, l + factor))

    # Convert back to RGB
    r, g, b = colorsys.hls_to_rgb(h, l, s)

    # Convert to hex
    result = f"#{int(r * 255):02X}{int(g * 255):02X}{int(b * 255):02X}"

    # Append alpha if present
    if alpha_hex:
        result += alpha_hex

    return result


def update_opacity(color: str, factor: float) -> str:
    """
    Adjust the opacity (alpha) of a hex color by a given factor.

    Args:
        color: Hex color string (e.g., "#FF0000" or "#FF0000FF")
        factor: Amount to adjust opacity (-1.0 to 1.0).
               Positive values increase opacity, negative values decrease it.
               For example, 0.2 increases opacity by 20%, -0.3 decreases by 30%.

    Returns:
        Hex color string with alpha channel (e.g., "#FF000099")

    Raises:
        InvalidColorError: If color format is invalid or factor is out of range

    Examples:
        >>> update_opacity("#FF0000", 0.2)
        "#FF0000FF"
        >>> update_opacity("#FF000080", 0.2)
        "#FF0000A0"
        >>> update_opacity("#FF000080", -0.2)
        "#FF000060"
    """

    if not -1.0 <= factor <= 1.0:
        msg = f"Factor must be in range -1.0 to 1.0: factor={factor}"
        raise InvalidColorError(msg)

    # Remove the # prefix
    hex_color = color.lstrip("#")

    # Extract RGB and existing alpha
    if len(hex_color) == 8:
        rgb_hex = hex_color[:6]
        current_alpha = int(hex_color[6:8], 16) / 255
    elif len(hex_color) == 6:
        rgb_hex = hex_color
        current_alpha = 1.0  # Fully opaque if no alpha specified
    else:
        msg = f"Invalid hex color format: #{hex_color}"
        raise InvalidColorError(msg)

    # Adjust opacity and clamp to valid range
    new_opacity = max(0.0, min(1.0, current_alpha + factor))

    # Convert to hex
    alpha_value = round(new_opacity * 255)
    alpha_hex = f"{alpha_value:02X}"

    return f"#{rgb_hex.upper()}{alpha_hex}"
