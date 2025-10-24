# API Reference

Complete reference for all st_yled functions, parameters, and configuration options. This documentation covers the core API, styling system, validation framework, and advanced features.

---

## Core Functions

### st_yled.init()

Initialize the st_yled styling system and load CSS configurations.

```python
def init(css_path: Optional[str] = None,
         validation_mode: str = "strict",
         theme: Optional[str] = None) -> None
```

**Parameters:**

- `css_path` (str, optional) - Path to custom CSS file. If not provided, looks for `.streamlit/st-styled.css`
- `validation_mode` (str, default="strict") - Validation behavior: `"strict"`, `"permissive"`, or `"bypass"`
- `theme` (str, optional) - Pre-built theme to apply: `"light"`, `"dark"`, `"professional"`

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

# With validation mode
st_yled.init(validation_mode="permissive")

# With theme
st_yled.init(theme="dark")

# Full configuration
st_yled.init(
    css_path="styles/app.css",
    validation_mode="strict",
    theme="professional"
)
```

**Notes:**
- Must be called before using any st_yled components
- Can be called multiple times to reload CSS or change settings
- Automatically loads CSS from `.streamlit/st-styled.css` if it exists

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

### st_yled.get_global_styles()

Retrieve current global styling configuration.

```python
def get_global_styles() -> Dict[str, Dict[str, str]]
```

**Returns:** Dictionary of component types and their applied styles

**Example:**

```python
# Get all current global styles
styles = st_yled.get_global_styles()
print(styles)

# Output:
# {
#   "button": {
#     "background_color": "#007bff",
#     "color": "white",
#     "border_radius": "6px"
#   },
#   "text": {
#     "font_family": "Arial, sans-serif",
#     "color": "#2c3e50"
#   }
# }

# Check specific component styles
button_styles = styles.get("button", {})
if "background_color" in button_styles:
    print(f"Button color: {button_styles['background_color']}")
```

---

## Validation System

### Validation Modes

st_yled includes a comprehensive validation system for CSS properties:

#### Strict Mode (Default)

```python
st_yled.init(validation_mode="strict")

# Raises ValidationError for invalid properties
st_yled.button("Test", color="invalid-color")  # ❌ Raises error
```

#### Permissive Mode

```python
st_yled.init(validation_mode="permissive")

# Shows warning but continues execution
st_yled.button("Test", color="invalid-color")  # ⚠️ Shows warning
```

#### Bypass Mode

```python
st_yled.init(validation_mode="bypass")

# No validation performed (fastest performance)
st_yled.button("Test", color="invalid-color")  # ✅ No validation
```

### Validation Functions

#### validate_css_property()

```python
def validate_css_property(property_name: str,
                         value: str) -> Tuple[bool, str]
```

Validate a CSS property and value combination.

**Parameters:**
- `property_name` (str) - CSS property name
- `value` (str) - CSS property value

**Returns:** Tuple of (is_valid: bool, error_message: str)

**Example:**
```python
# Validate color property
is_valid, error = st_yled.validate_css_property("color", "#3498db")
print(f"Valid: {is_valid}")  # True

# Validate invalid property
is_valid, error = st_yled.validate_css_property("color", "invalid")
print(f"Valid: {is_valid}, Error: {error}")  # False, "Invalid color format"
```

#### get_supported_properties()

```python
def get_supported_properties() -> Dict[str, List[str]]
```

Get list of all supported CSS properties by category.

**Returns:** Dictionary mapping property categories to property lists

**Example:**
```python
properties = st_yled.get_supported_properties()

print("Color properties:", properties["color"])
# ['color', 'background_color', 'border_color']

print("Typography properties:", properties["typography"])
# ['font_size', 'font_weight', 'font_family', 'line_height']

print("Spacing properties:", properties["spacing"])
# ['margin', 'padding', 'margin_top', 'padding_left']
```

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
export ST_STYLED_CSS_PATH="path/to/custom.css"

# Validation mode
export ST_STYLED_VALIDATION_MODE="permissive"

# Default theme
export ST_STYLED_THEME="dark"

# Enable debug mode
export ST_STYLED_DEBUG="true"
```

**Using in Python:**

```python
import os

st_yled.init(
    css_path=os.getenv("ST_STYLED_CSS_PATH"),
    validation_mode=os.getenv("ST_STYLED_VALIDATION_MODE", "strict"),
    theme=os.getenv("ST_STYLED_THEME")
)
```

---

## Advanced Features

### Custom CSS Classes

Apply custom CSS classes to components:

```python
# Add custom CSS class
st_yled.text(
    "Custom styled text",
    css_class="my-custom-class",
    custom_css="""
    .my-custom-class {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    """
)
```

### Theme Management

```python
# Create custom theme
custom_theme = {
    "button": {
        "background_color": "#6366f1",
        "color": "white",
        "border_radius": "8px"
    },
    "text": {
        "color": "#1f2937",
        "font_family": "Inter, sans-serif"
    }
}

# Apply theme
st_yled.apply_theme(custom_theme)

# Save theme for reuse
st_yled.save_theme("my_theme", custom_theme)

# Load saved theme
st_yled.load_theme("my_theme")
```

### Performance Monitoring

```python
# Enable performance monitoring
st_yled.init(debug=True)

# Get performance metrics
metrics = st_yled.get_performance_metrics()
print(f"CSS injection time: {metrics['css_injection_time']}ms")
print(f"Components rendered: {metrics['components_rendered']}")
print(f"Validation time: {metrics['validation_time']}ms")
```

---

## Error Handling

### Exception Types

```python
from st_yled.exceptions import (
    ValidationError,
    ComponentError,
    CSSError,
    ThemeError
)

try:
    st_yled.button("Test", color="invalid-color")
except ValidationError as e:
    st_yled.error(f"Validation failed: {e}")
except ComponentError as e:
    st_yled.error(f"Component error: {e}")
```

### Error Recovery

```python
# Graceful error handling
def safe_styling(**kwargs):
    try:
        return kwargs
    except ValidationError:
        # Return default styling on validation error
        return {"background_color": "#f8f9fa", "color": "#2c3e50"}

# Usage
button_style = safe_styling(
    background_color=user_selected_color,
    color=user_selected_text_color
)

st_yled.button("Safe Button", **button_style)
```

---

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

### Responsive Design Helper

```python
def responsive_container(**kwargs):
    """Create responsive container with mobile-friendly defaults"""

    defaults = {
        "width": "100%",
        "max_width": "1200px",
        "margin": "0 auto",
        "padding": "clamp(16px, 4vw, 32px)"
    }

    # Merge user styles with defaults
    styles = {**defaults, **kwargs}

    return st_yled.container(**styles)

# Usage
with responsive_container(background_color="white"):
    st_yled.title("Responsive Content")
```

---

## Next Steps

### Further Reading

- **[Component Reference](../elements/index.md)** - Detailed component documentation
- **[Examples Gallery](../examples/index.md)** - Practical usage examples
- **[Getting Started Guide](../getting-started/installation.md)** - Basic setup and usage

### Advanced Topics

- **[Custom Theme Development](../examples/advanced-examples/custom-themes.md)**
- **[Performance Optimization](../examples/advanced-examples/dashboard-demo.md)**
- **[Integration Patterns](../examples/use-cases/business-dashboard.md)**

### Community Resources

- **[GitHub Repository](https://github.com/EvobyteDigitalBiology/st-styled)** - Source code and issues
- **[Community Forum](../community/index.md)** - Discussion and support
- **[Contributing Guide](../community/contributing.md)** - How to contribute

---

**API mastery achieved!** 🚀 You now have complete knowledge of st_yled's capabilities and can build sophisticated, beautifully styled Streamlit applications.
