# st_yled - Advanced Streamlit Styling

[![CI](https://github.com/EvobyteDigitalBiology/st-styled/workflows/CI/badge.svg)](https://github.com/EvobyteDigitalBiology/st-styled/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/st-styled.svg)](https://badge.fury.io/py/st-styled)

**st_yled** provides advanced styling capabilities and enhanced components for Streamlit applications. Style your Streamlit apps with CSS, create custom themes, and use enhanced component wrappers with built-in styling support.

## ✨ Features

- 🎨 **CSS Integration** - Load custom CSS files and apply styles to Streamlit components
- 🎯 **Global Styling** - Apply consistent styles across all components of the same type
- 🔧 **Component Wrappers** - Enhanced versions of 40+ Streamlit components with styling parameters
- 📱 **Responsive Design** - CSS-based responsive layouts and mobile-friendly styling
- ⚡ **Easy Setup** - Simple initialization and intuitive API
- 🎪 **Theme Support** - Create and apply custom themes to your applications

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
st_yled.set("button", "border_radius", "20px")

# Use enhanced components with styling
st_yled.button("Styled Button", background_color="#4ecdc4", color="white")
st_yled.text("Styled Text", color="#2c3e50", font_size="18px")
```

### CSS File Setup

Create a CSS file at `.streamlit/st-styled.css` in your project:

```css
/* Global button styling */
.stButton > button {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    border: none;
    border-radius: 25px;
    color: white;
    font-weight: bold;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

/* Custom text styling */
.custom-header {
    color: #2c3e50;
    font-family: 'Arial', sans-serif;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
}
```

## 📖 API Reference

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
st_yled.set("button", "border_radius", "10px")
st_yled.set("button", "color", "white")

# Style all headers
st_yled.set("header", "color", "#2c3e50")
st_yled.set("header", "font_family", "'Helvetica', sans-serif")
```

### Enhanced Components

All standard Streamlit components are available with additional styling parameters:

#### Text Components
```python
st_yled.title("My Title", color="#2c3e50", font_size="2.5rem")
st_yled.header("Section Header", color="#3498db", border_bottom="2px solid #3498db")
st_yled.subheader("Subsection", font_weight="normal", color="#7f8c8d")
st_yled.text("Regular text", font_size="16px", line_height="1.6")
st_yled.markdown("**Bold text**", color="#e74c3c")
st_yled.caption("Small caption", font_style="italic", color="#95a5a6")
```

#### Input Components
```python
st_yled.button("Click Me", background_color="#e74c3c", color="white", border_radius="5px")
st_yled.text_input("Name", border_color="#3498db", border_radius="5px")
st_yled.selectbox("Choose", options=["A", "B"], background_color="#f8f9fa")
st_yled.slider("Value", 0, 100, border_color="#2ecc71")
```

#### Data Components
```python
st_yled.dataframe(df, border="1px solid #ddd", border_radius="5px")
st_yled.metric("Sales", "1234", "+5%", color="#2ecc71")
st_yled.progress(0.75, color="#3498db")
```

### Styling Properties

Common CSS properties supported across components:

- **Colors:** `color`, `background_color`, `border_color`
- **Typography:** `font_size`, `font_family`, `font_weight`, `font_style`, `line_height`
- **Spacing:** `margin`, `padding`, `margin_top`, `padding_left`, etc.
- **Borders:** `border`, `border_radius`, `border_width`, `border_style`
- **Layout:** `width`, `height`, `display`, `text_align`
- **Effects:** `box_shadow`, `opacity`, `transform`

## 🎨 Examples

### Example 1: Custom Button Theme
```python
import streamlit as st
import st_yled

st_yled.init()

# Create a custom button theme
st_yled.set("button", "background", "linear-gradient(45deg, #FF6B6B, #4ECDC4)")
st_yled.set("button", "border", "none")
st_yled.set("button", "border_radius", "25px")
st_yled.set("button", "color", "white")
st_yled.set("button", "font_weight", "bold")

st.title("🎨 Custom Button Theme")
col1, col2, col3 = st.columns(3)

with col1:
    st_yled.button("Primary")
with col2:
    st_yled.button("Secondary")
with col3:
    st_yled.button("Tertiary")
```

### Example 2: Card Layout with Styling
```python
import streamlit as st
import st_yled

st_yled.init()

st.title("📊 Dashboard Cards")

# Create card-like containers
col1, col2, col3 = st.columns(3)

with col1:
    st_yled.container(
        border="1px solid #ddd",
        border_radius="10px",
        padding="20px",
        background_color="#f8f9fa"
    ):
        st_yled.metric("Revenue", "$12,345", "+8%", color="#2ecc71")

with col2:
    st_yled.container(
        border="1px solid #ddd",
        border_radius="10px",
        padding="20px",
        background_color="#f8f9fa"
    ):
        st_yled.metric("Users", "1,234", "+12%", color="#3498db")

with col3:
    st_yled.container(
        border="1px solid #ddd",
        border_radius="10px",
        padding="20px",
        background_color="#f8f9fa"
    ):
        st_yled.metric("Orders", "456", "-2%", color="#e74c3c")
```

### Example 3: Form with Custom Styling
```python
import streamlit as st
import st_yled

st_yled.init()

st.title("📝 Styled Contact Form")

# Apply form styling
st_yled.set("text_input", "border_radius", "8px")
st_yled.set("text_input", "border", "2px solid #e1e5e9")
st_yled.set("text_area", "border_radius", "8px")
st_yled.set("text_area", "border", "2px solid #e1e5e9")

with st.form("contact_form"):
    st_yled.text_input("Full Name", placeholder="Enter your full name")
    st_yled.text_input("Email", placeholder="Enter your email")
    st_yled.text_area("Message", placeholder="Enter your message")

    st_yled.form_submit_button(
        "Send Message",
        background_color="#2ecc71",
        color="white",
        border_radius="8px",
        width="100%"
    )
```

## 🛠️ Advanced Usage

### Custom CSS Classes

You can add custom CSS classes to components:

```python
st_yled.button("Custom Button", css_class="my-custom-button")
```

Then style in your CSS file:
```css
.my-custom-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    border-radius: 15px;
    color: white;
    padding: 12px 24px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
}

.my-custom-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}
```

### Responsive Design

Create responsive layouts using CSS:

```css
/* Mobile styles */
@media (max-width: 768px) {
    .stButton > button {
        width: 100%;
        margin-bottom: 10px;
    }

    .stColumns {
        flex-direction: column;
    }
}

/* Desktop styles */
@media (min-width: 769px) {
    .stButton > button {
        min-width: 150px;
    }
}
```

## 🔧 Configuration

### CSS File Locations

st_yled looks for CSS files in the following order:

1. Custom path provided to `st_yled.init(css_path)`
2. `.streamlit/st-styled.css` in current working directory
3. `~/.streamlit/st-styled.css` in home directory

### Styling Priority

Styles are applied in the following priority order (highest to lowest):

1. Inline component styling parameters
2. Global styles set with `st_yled.set()`
3. CSS file styles
4. Default Streamlit styles

## 🧪 Testing

Run the test suite:

```bash
# Install development dependencies
poetry install --with dev

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=st_yled
```

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

1. Fork and clone the repository
2. Install dependencies: `poetry install --with dev`
3. Install pre-commit hooks: `poetry run pre-commit install`
4. Make changes and run tests: `poetry run pytest`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation:** [GitHub README](https://github.com/EvobyteDigitalBiology/st-styled#readme)
- **Source Code:** [GitHub Repository](https://github.com/EvobyteDigitalBiology/st-styled)
- **Issue Tracker:** [GitHub Issues](https://github.com/EvobyteDigitalBiology/st-styled/issues)
- **PyPI Package:** [st-styled](https://pypi.org/project/st-styled/)

## ❓ Support

If you encounter any issues or have questions:

1. Check the [documentation](https://github.com/EvobyteDigitalBiology/st-styled#readme)
2. Search [existing issues](https://github.com/EvobyteDigitalBiology/st-styled/issues)
3. Create a [new issue](https://github.com/EvobyteDigitalBiology/st-styled/issues/new)

---

Made with ❤️ for the Streamlit community
