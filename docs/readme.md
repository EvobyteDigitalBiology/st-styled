# st_yled - Advanced Streamlit Styling

[![CI](https://github.com/EvobyteDigitalBiology/st-styled/workflows/CI/badge.svg)](https://github.com/EvobyteDigitalBiology/st-styled/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/st-styled.svg)](https://badge.fury.io/py/st-styled)
[![Test Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen.svg)](htmlcov/index.html)

<br>

![st_yled Components Examples](assets/st_yled_font_weight_preview.png)

<br>

**st_yled** provides styling capabilities and improved components for Streamlit applications.
Style your Streamlit apps with custom themes and unique elements to match your personal tone or corporate brand.

> **Check the [st_yled studio](https://styled-studio.streamlit.app/) app to configure your layouts and custom elements.**


## ✨ Features

🎨 **CSS Integration** - Load custom CSS files and apply styles seamlessly

🎯 **Global Styling** - Apply consistent styles across all elements

🔧 **Enhanced Elements** - 44+ styled component wrappers with validation

⚡ **st_yled studio** - Use the accompanying app to test your layout styling

## 🚀 Quick Start

### Installation

```bash
pip install st-styled
```

### Basic Usage

```python
import streamlit as st
import st_yled

# Initialize st_yled (loads CSS from .streamlit/st-styled.css if available)
st_yled.init()

# Apply global styling to all buttons
st_yled.set("button", "background_color", "#ff6b6b")
st_yled.set("button", "border_style", "solid")

# Use enhanced components with styling
st_yled.button("Styled Button", background_color="#4ecdc4", color="white")
st_yled.text("Styled Text", color="#2c3e50", font_size="18px")
```

## 📚 Documentation


### Content

- [Installation & Setup](#installation) - Get started quickly
- [API Reference](#api-reference) - Core functions and usage
- [Component Examples](#enhanced-components) - Basic component styling
- [Styling Properties](#styling-properties) - Supported CSS properties
- [Configuration](#configuration) - Advanced configuration options

## <a name="api-reference"></a>📖 API Reference

### Core Functions

#### `st_yled.init(css_path=None)`

Initialize st_yled with CSS styling.

**Parameters:**
- `css_path` (str, optional): Path to custom CSS file. If not provided, looks for `.streamlit/st-styled.css`

**Example:**
```python
# Load default CSS file
st_yled.init()

# Load custom CSS file
st_yled.init("path/to/custom.css")
```

#### `st_yled.set(component, property, value)`

Apply global styling to all components of a specific type.

**Parameters:**
- `component` (str): Component type (e.g., "button", "text", "header")
- `property` (str): CSS property name (e.g., "background_color", "font_size")
- `value` (str): CSS property value (e.g., "#ff6b6b", "18px")

**Example:**
```python
# Style all buttons
st_yled.set("button", "background_color", "#3498db")
st_yled.set("button", "border_style", "solid")
st_yled.set("button", "color", "white")

# Style all headers
st_yled.set("header", "color", "#2c3e50")
st_yled.set("header", "font_size", "24px")
```

## <a name="enhanced-components"></a>🔧 Enhanced Components

St_yled provides enhanced versions of Streamlit components with additional styling parameters:

### Text Components
```python
st_yled.title("My Title", color="#2c3e50", font_size="2.5rem")
st_yled.header("Section Header", color="#3498db")
st_yled.subheader("Subsection", color="#7f8c8d", font_size="1.5rem")
st_yled.text("Regular text", font_size="16px", color="#2c3e50")
st_yled.markdown("**Bold text**", color="#e74c3c")
st_yled.caption("Small caption", color="#95a5a6", font_size="14px")
```

### Interactive Components
```python
st_yled.button("Click Me", background_color="#e74c3c", color="white")
st_yled.text_input("Name", background_color="#f8f9fa", color="#2c3e50")
st_yled.selectbox("Choose", options=["A", "B"], background_color="#f8f9fa")
st_yled.slider("Value", 0, 100, color="#2ecc71")
```

### Layout Components
```python
# Styled containers (only background_color and border properties supported)
with st_yled.container(
    background_color="#f8f9fa",
    border_style="solid",
    border_color="#dee2e6",
    border_width="1px"
):
    st.write("Content inside styled container")

# Standard columns (st_yled.columns doesn't exist, use st.columns)
col1, col2 = st.columns(2)
```

### Status Components
```python
# Status components with styling (only color property supported)
st_yled.success(
    "Success message",
    color="#155724"
)

st_yled.info(
    "Info message",
    color="#0c5460"
)

st_yled.warning(
    "Warning message",
    color="#856404"
)

st_yled.error(
    "Error message",
    color="#721c24"
)
```

## 🎨 Component Coverage

St_yled supports **43 styled components** with comprehensive CSS property support:

- **Text Components (9)**: title, header, subheader, text, markdown, caption, code, latex, json
- **Interactive Components (16)**: button, download_button, text_input, text_area, number_input, selectbox, multiselect, slider, select_slider, checkbox, radio, toggle, color_picker, file_uploader, pills, form_submit_button
- **Layout Components (3)**: container, expander, tabs
- **Status Components (4)**: success, info, warning, error
- **Data Components (4)**: table, metric, progress, status
- **Chat Components (1)**: chat_message

Check the [st_yled element docs](https://st-styled.evo-byte.com/elements/) for more information


## 🛡️ Validation System

St_yled includes a comprehensive parameter validation system:

### Validation Modes

- **Permissive Mode (default)**: Invalid properties removed with warnings
- **Strict Mode**: Invalid properties raise `ValidationError`
- **Bypass Mode**: No validation (for advanced users)

### Configuration

```python
import os

# Enable strict validation (recommended for development)
os.environ["ST_STYLED_STRICT_VALIDATION"] = "true"

# Bypass validation (for performance-critical applications)
os.environ["ST_STYLED_BYPASS_VALIDATION"] = "true"
```


## <a name="styling-properties">🎨 Styling Properties

### Color Properties
- **Valid formats:** Hex (`#ff0000`), RGB (`rgb(255,0,0)`), HSL (`hsl(0,100%,50%)`), Named (`red`)
- **Examples:** `color`, `background_color`, `border_color`

### Size Properties
- **Valid units:** `px`, `em`, `rem`
- **Examples:** `font_size`, `width`, `height`, `padding`, `margin`

### Border Properties
- **Styles:** `solid`, `dashed`, `dotted`, `double`, ...
- **Examples:** `border`, `border_radius`, `border_width`, `border_style`

> **See [Component Reference](https://st-styled.evo-byte.com/elements/) for complete property details.**

## 🚀 Advanced Usage

### Custom Themes

```python
def apply_dark_theme():
    st_yled.set("title", "color", "#ffffff")
    st_yled.set("container", "background_color", "#1f2937")
    st_yled.set("button", "background_color", "#3b82f6")
    st_yled.set("button", "color", "#ffffff")

apply_dark_theme()
```

### Dashboard Layouts

```python
# Professional metric cards
col1, col2, col3 = st.columns(3)

with col1:
    with st_yled.container(
        background_color="#f8fafc",
        border="1px solid #e2e8f0",
        border_radius="12px",
    ):
        st_yled.metric("Revenue", "$2.4M", "+12%", color="#059669")
```

## 🔧 Configuration

### CSS File Locations

St_yled looks for CSS files in the following order:

1. Custom path provided to `st_yled.init(css_path)`
2. `.streamlit/st-styled.css` in current working directory
3. `~/.streamlit/st-styled.css` in home directory

### Styling Priority

Styles are applied in priority order (highest to lowest):

1. Inline component styling parameters
2. Global styles set with `st_yled.set()`
3. CSS file styles
4. Default Streamlit styles

### Environment Variables

```bash
# Validation configuration
export ST_STYLED_STRICT_VALIDATION=true   # Enable strict validation
export ST_STYLED_BYPASS_VALIDATION=true   # Bypass all validation
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **🐙 Source Code:** [GitHub Repository](https://github.com/EvobyteDigitalBiology/st-styled)
- **🐛 Issue Tracker:** [GitHub Issues](https://github.com/EvobyteDigitalBiology/st-styled/issues)
- **📦 PyPI Package:** [st-styled](https://pypi.org/project/st-styled/)

## ❓ Support

If you encounter any issues or have questions:

1. 📖 Check the [comprehensive documentation](https://st-styled.evo-byte.com/)
2. 🔍 Search [existing issues](https://github.com/EvobyteDigitalBiology/st-styled/issues)
3. 💬 Create a [new issue](https://github.com/EvobyteDigitalBiology/st-styled/issues/new)
4. 📧 Contact the maintainers

---

**Made with ❤️ by [EVOBYTE](https://www.evo-byte.com) for the Streamlit community**

*Transform your Streamlit apps with professional styling and comprehensive validation.*
