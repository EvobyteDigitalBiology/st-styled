# API Reference

Complete reference for all st_yled functions, parameters, and configuration options. This documentation covers the core API, styling system, validation framework, and advanced features.

---

## Core Functions

### st_yled.init()

Initialize the st_yled styling system and load CSS configurations.

```python
def init(css_path: Optional[str] = None,
         bypass_css_validation: bool = False,
         strict_css_validation: bool = False,
         reset_tracebacklimit: bool = True) -> None
```

**Parameters:**

- `css_path` (str, optional) - Path to custom CSS file. If not provided, looks for `.streamlit/st-styled.css`
- `bypass_css_validation` (bool, default=False) - Skip CSS value validation in `st_yled` when `True`
- `strict_css_validation` (bool, default=False) - Raise `ValidationError` for invalid CSS values when `True`
- `reset_tracebacklimit` (bool, default=True) - Reset traceback depth for clearer custom CSS path debugging

**Returns:** None

**Raises:**
- `FileNotFoundError` - If specified CSS file doesn't exist
- `ValidationError` - If CSS contains invalid properties (strict mode only)

**Examples:**

```python
# Basic initialization
st_yled.init()

# With custom CSS file
st_yled.init(css_path="styles/custom.css")

# Enable strict validation
st_yled.init(strict_css_validation=True)

# Full configuration
st_yled.init(
    css_path="styles/app.css",
    bypass_css_validation=False,
    strict_css_validation=True,
    reset_tracebacklimit=True,
)
```

**Notes:**

- Must be called before using any st_yled components

- Can be called multiple times to reload CSS or change settings

- Automatically loads CSS from `.streamlit/st-styled.css` if it exists

- Validation precedence is: environment variables > `init(...)` arguments > class defaults

- Environment variables: `ST_STYLED_BYPASS_VALIDATION`, `ST_STYLED_STRICT_VALIDATION`

---

### st_yled.set()

Apply global styling to all components of a specified type.

```python
def set(component_type: str,
        property_name: str,
        value: str) -> None
```

**Parameters:**

- `component_type` (str) - Target component type (e.g., "button", "text", "container")
- `property_name` (str) - CSS property name (e.g., "background_color", "font_size")
- `value` (str) - CSS property value (e.g., "#3498db", "16px", "bold")

**Returns:** None

**Raises:**

- `ValidationError` - If property name or value is invalid

- `ComponentError` - If component type is not supported

**Examples:**

```python
# Set global button styling
st_yled.set("button", "background_color", "#007bff")
st_yled.set("button", "color", "white")
st_yled.set("button", "border_radius", "6px")

# Set global text styling
st_yled.set("text", "font_family", "Arial, sans-serif")
st_yled.set("text", "color", "#2c3e50")

# Set container defaults
st_yled.set("container", "border_radius", "8px")
st_yled.set("container", "padding", "20px")
```

**Supported Component Types:**

| Component Type | Description | Examples |
|----------------|-------------|----------|
| `button` | All button components | `st_yled.button()`, `st_yled.download_button()` |
| `text` | Text components | `st_yled.text()`, `st_yled.markdown()` |
| `title` | Title components | `st_yled.title()` |
| `header` | Header components | `st_yled.header()`, `st_yled.subheader()` |
| `container` | Container components | `st_yled.container()`, `st_yled.expander()` |
| `metric` | Metric components | `st_yled.metric()` |
| `input` | Input components | `st_yled.text_input()`, `st_yled.selectbox()` |
| `table` | Table components | `st_yled.dataframe()`, `st_yled.table()` |
| `alert` | Alert components | `st_yled.success()`, `st_yled.error()` |

---

---

## Validation System

### Validation Modes

st_yled includes a comprehensive validation system for CSS properties:

---

## Configuration

### CSS File Loading

st_yled automatically looks for CSS files in these locations:

1. `.streamlit/st-styled.css` (default)
2. `styles/st-styled.css`
3. `css/st-styled.css`
4. Custom path specified in `init()`

**CSS File Format:**

```css
/* .streamlit/st-styled.css */

/* Global button styles */
.stButton > button {
    border-radius: 8px;
    border: none;
    font-weight: 600;
    transition: all 0.3s ease;
}

/* Global container styles */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Custom classes */
.custom-metric {
    background-color: #f8f9fa;
    border-left: 4px solid #007bff;
    padding: 20px;
}
```

### Environment Variables

Configure st_yled behavior with environment variables:

```bash
# CSS file path
export ST_STYLED_BYPASS_VALIDATION="true"

# Validation mode
export ST_STYLED_STRICT_VALIDATION="false"

```

**Using in Python:**

---

## Advanced Features


## Migration Guide

### From Streamlit to st_yled

Replace Streamlit components with st_yled equivalents:

```python
# Before (Streamlit)
st.title("My App")
st.button("Click me")
st.text("Some text")

# After (st_yled)
st_yled.init()  # Add initialization
st_yled.title("My App", color="#2c3e50")  # Add styling
st_yled.button("Click me", background_color="#007bff", color="white")
st_yled.text("Some text", font_size="16px")
```

### Version Compatibility

```python
# Check st_yled version
import st_yled
print(f"st_yled version: {st_yled.__version__}")

# Check compatibility with current Streamlit version
compatibility = st_yled.check_compatibility()
if not compatibility["is_compatible"]:
    st.warning(f"Compatibility issue: {compatibility['message']}")
```

---

## Examples and Best Practices

### Component Factory Pattern

```python
def create_styled_button(text, variant="primary"):
    """Factory function for consistent button styling"""

    variants = {
        "primary": {
            "background_color": "#007bff",
            "color": "white"
        },
        "secondary": {
            "background_color": "#6c757d",
            "color": "white"
        },
        "success": {
            "background_color": "#28a745",
            "color": "white"
        }
    }

    style = variants.get(variant, variants["primary"])

    return st_yled.button(
        text,
        border_radius="6px",
        padding="10px 20px",
        border="none",
        **style
    )

# Usage
create_styled_button("Save", "success")
create_styled_button("Cancel", "secondary")
```

---

## Next Steps

### Further Reading

- **[Elements Reference](../elements/index.md)** - Detailed component documentation
- **[Examples Gallery](../examples/index.md)** - Practical usage examples
- **[Getting Started Guide](../getting-started/installation.md)** - Basic setup and usage


### Community Resources

- **[GitHub Repository](https://github.com/EvobyteDigitalBiology/st-styled)** - Source code and issues

---

**API mastery achieved!** 🚀 You now have complete knowledge of st_yled's capabilities and can build sophisticated, beautifully styled Streamlit applications.
