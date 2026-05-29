"""Generate per-theme Streamlit config files from st_yled theme templates.

This script uses the existing theming helpers in ``st_yled.styler`` to populate the
built-in ``template_config.toml`` for each theme found in ``constants.THEMES``.

Output layout:
    src/st_yled/themes/<theme_name>/config.toml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from st_yled import constants  # noqa: E402
from st_yled.styler import (  # noqa: E402
    _build_updated_themes,
    _extract_theme_sections,
    set_config_toml,
)


def generate_theme_configs(disable_light_dark_mode: bool = False) -> int:
    """Generate one config.toml file per built-in theme.

    Args:
        disable_light_dark_mode: If True, only fill ``[theme]`` and
            ``[theme.sidebar]`` from each theme's ``defaultTheme`` variant.

    Returns:
        Number of generated config files.
    """

    themes_root = SRC_PATH / "st_yled" / "themes"
    generated_count = 0

    for theme_name, theme_data in sorted(constants.THEMES.items()):
        updated_themes = _build_updated_themes(theme_data, disable_light_dark_mode)
        rendered_template = set_config_toml(constants.TEMPLATE_CONFIG_TOML, updated_themes)

        # Keep full template content for generated files so non-theme sections
        # remain available for users as placeholders/documentation.
        output_text = rendered_template.rstrip() + "\n"

        theme_dir = themes_root / theme_name
        theme_dir.mkdir(parents=True, exist_ok=True)
        output_path = theme_dir / "config.toml"
        output_path.write_text(output_text, encoding="utf-8")

        generated_count += 1

        # Also surface how much theme content was populated for quick visibility.
        theme_sections = _extract_theme_sections(rendered_template)
        section_line_count = len(theme_sections.splitlines()) if theme_sections else 0
        print(f"Generated {output_path} ({section_line_count} themed lines)")

    return generated_count


def main() -> None:
    """CLI entrypoint."""

    parser = argparse.ArgumentParser(
        description=(
            "Generate config.toml files for all built-in themes under "
            "src/st_yled/themes/<theme_name>/config.toml"
        )
    )
    parser.add_argument(
        "--disable-light-dark-mode",
        action="store_true",
        help=(
            "Populate only [theme] and [theme.sidebar] from each theme's "
            "defaultTheme variant"
        ),
    )
    args = parser.parse_args()

    generated_count = generate_theme_configs(
        disable_light_dark_mode=args.disable_light_dark_mode
    )
    print(f"Done. Generated {generated_count} theme config files.")


if __name__ == "__main__":
    main()
