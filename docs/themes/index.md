# Themes

Built-in st_yled themes let you apply a complete visual style from `st_yled.init(...)`.

Don't forget to run `st_yled.init(...)` on each of your app pages.

## Quick Example

```python
import st_yled

# Apply a built-in theme template
st_yled.init(theme="bauhaus")

# Disable light and dark mode selection for the user -
# serve only the "default" for a theme
st_yled.init(theme="bauhaus", disable_light_dark_mode = True)

```

When a theme template is selected, st_yled updates the Streamlit theme sections in `.streamlit/config.toml`.

## Available Themes

- [Bauhaus](bauhaus.md)
- [Luxury Fintec](luxury-fintec.md)
- [Newspaper](newspaper.md)
- [Playful Startup](playful-startup.md)
- [Scandinavian](scandinavian.md)

## How It Works

- st_yled loads theme definitions from `src/st_yled/themes/*.json`
- The selected template is translated into Streamlit theme keys
- Theme values are written into `.streamlit/config.toml`
- Light and dark mode are supported by each template

Use the pages below to preview each built-in theme and inspect source files.
