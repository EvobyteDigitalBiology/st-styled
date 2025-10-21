# Basic Styling Concepts

Master the fundamentals of component styling with st_yled. Learn how to apply colors, fonts, spacing, and layouts to create beautiful Streamlit applications.

---

## Core Styling Philosophy

st_yled follows these key principles:

- **Intuitive Parameters** - Use familiar CSS property names
- **Comprehensive Validation** - Prevent styling errors with built-in checks
- **Consistent Behavior** - Same styling approach across all components
- **Progressive Enhancement** - Start simple, add complexity as needed

---

## CSS Property Basics

### Color Properties

st_yled supports multiple color formats for maximum flexibility:

```python
# Hex colors (recommended)
st_yled.title("Title", color="#3498db")

# RGB colors
st_yled.header("Header", color="rgb(52, 152, 219)")

# Named colors
st_yled.text("Text", color="blue")

# HSL colors
st_yled.button("Button", background_color="hsl(204, 70%, 53%)")
```

**Common Color Properties:**

- `color` - Text color

- `background_color` - Background color

- `border_color` - Border color

### Typography Properties

Control text appearance with typography properties:

```python
# Font size (pixels, rem, em, %)
st_yled.title("Large Title", font_size="48px")
st_yled.header("Medium Header", font_size="2rem")
st_yled.text("Small Text", font_size="0.9em")
st_yled.text("Very Small Text", font_size=7) # integer values are interpreted as px
```


### Border and Layout Properties

Add borders, shapes, and positioning:

```python
# Border properties
st_yled.container(
    border_color="#e74c3c",
    border_style="solid",
    border_width="2px "
)

```

---

## Component-Specific Styling

### Text Components

Text components support comprehensive typography styling:

```python
# Title with full styling
st_yled.title(
    "Styled Title",
    color="#2c3e50",
    font_size="2.5rem"
)

# Paragraph with line spacing
st_yled.text(
    "This is a styled paragraph with custom line height and spacing.",
    color="#34495e",
    font_size="16px",
)
```

### Button Components

Buttons support interactive and visual styling:

```python
# Primary button
st_yled.button(
    "Primary Action",
    background_color="#3498db",
    color="white",
    border_style="none",
    type="primary"
)

# Outline button
st_yled.button(
    "Secondary Action",
    background_color="transparent",
    border_color="#3498db",
    border_width = "2px",
    border_style = "solid"
)
```

### Container Components

Containers support layout and visual grouping:

```python
# Card-style container
st_yled.container(
    background_color="white",
    border_color="#3498db",
    border_width = 3,
    border_style = "solid"
)

# Highlighted container
st_yled.expander(
    "Expandable Section",
    background_color="#f8f9fa",
    border_color="#3498db",
)
```

---

## Validation System

st_yled validates all CSS properties to prevent errors and ensure compatibility:

### Valid Property Examples

```python
# These will work correctly
st_yled.title("Title", color="#3498db")  # Valid hex color
st_yled.text("Text", font_size="16px")   # Valid size with unit
st_yled.button("Button", padding="10px") # Valid padding value
```

### Validation Errors

```python
# These will show helpful error messages
st_yled.title("Title", color="invalid-color")  # ❌ Invalid color
st_yled.text("Text", font_size="16")          # ❌ Missing unit
st_yled.button("Button", padding="invalid")   # ❌ Invalid padding
```

### Property Validation Rules

| Property | Valid Values | Examples |
|----------|--------------|----------|
| `color` | Hex, RGB, named colors | `#ff0000`, `rgb(255,0,0)`, `red` |
| `font_size` | Size with units | `16px`, `1.2rem`, `100%` `12` (integer interpreted as px) |
| `background_color` | Color values | Same as `color` |

---

## Best Practices

### 1. Consistent Color Scheme

Define a color palette and use it consistently:

```python
# Define your color palette
PRIMARY_COLOR = "#3498db"
SECONDARY_COLOR = "#2ecc71"
ACCENT_COLOR = "#e74c3c"
BACKGROUND_COLOR = "#f8f9fa"
TEXT_COLOR = "#2c3e50"

# Use consistently throughout your app
st_yled.title("Title", color=PRIMARY_COLOR)
st_yled.button("Action", background_color=SECONDARY_COLOR)
st_yled.error("Error", color=ACCENT_COLOR)
```

### 2. Typography Hierarchy

Create clear visual hierarchy with consistent font sizes:

```python
# Typography scale
FONT_SIZES = {
    "hero": "3rem",
    "title": "2.5rem",
    "header": "2rem",
    "subheader": "1.5rem",
    "body": "1rem",
    "small": "0.875rem"
}

st_yled.title("Main Title", font_size=FONT_SIZES["title"])
st_yled.header("Section Header", font_size=FONT_SIZES["header"])
st_yled.text("Body text", font_size=FONT_SIZES["body"])
```

---

## Next Steps

Now that you understand basic styling concepts:

- **[Global Styling Guide](global-styling.md)** - Apply consistent themes across your entire app
- **[Component Reference](../elements/index.md)** - Explore styling options for specific components
- **[Advanced Examples](../examples/advanced-examples/responsive-design.md)** - See complex styling patterns in action

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
