# Elements Overview

st_yled provides enhanced versions of many major Streamlit elements with built-in styling capabilities. Those elements support CSS properties for customization while maintaining full compatibility with their Streamlit equivalents.

Below you find an overview of Streamlit elements with styling options

FYI: All Streamlit Components can be accessed through the st_yled API, no matter if they can be styled or not.

```python
# The statements below have the same effect
st_yled.init()

st.title("Hello")
st_yled.title("Hello")

st.badge("Tag")
st_yled.badge("Tag")

st.toast("Hooray")
st_yled.toast("Hooray")
```

---

## Categories

### [📝 Text Elements](text-elements.md)
Display and format text, code and formulas with advanced styling options.

**Available Elements:**

- [`title`](text-elements.md#title)

- [`header`](text-elements.md#header)

- [`subheader`](text-elements.md#subheader)

- [`text`](text-elements.md#text)

- [`markdown`](text-elements.md#markdown)

- [`caption`](text-elements.md#caption)

- [`code`](text-elements.md#code)

- [`latex`](text-elements.md#latex)


---

### [🎛️ Input Elements](input-elements.md)
Interactive widgets for user input with enhanced visual styling.

**Available Elements:**

- [`button`](input-elements.md#button)

- [`download_button`](input-elements.md#download_button)

- [`link_button`](input-elements.md#link_button)

- [`selectbox`](input-elements.md#selectbox)

- [`radio`](input-elements.md#radio)

- [`multiselect`](input-elements.md#multiselect)

- [`checkbox`](input-elements.md#checkbox)

- [`text_input`](input-elements.md#text_input)

- [`text_area`](input-elements.md#text_area)

- [`number_input`](input-elements.md#number_input)

- [`slider`](input-elements.md#slider)

- [`select_slider`](input-elements.md#select_slider)

- [`date_input`](input-elements.md#date_input)

- [`time_input`](input-elements.md#time_input)

- [`color_picker`](input-elements.md#color_picker)

- [`file_uploader`](input-elements.md#file_uploader)

- [`camera_input`](input-elements.md#camera_input)

---

### [📊 Data Elements](data-elements.md)
Display data and metrics with professional styling options.

**Available Elements:**

- [`table`](data-elements.md#table)

- [`metric`](data-elements.md#metric)

- [`json`](data-elements.md#json)

---

### [🏗️ Layout Elements](layout-elements.md)
Structure your application with styled containers and layout elements.

**Available Elements:**

- [`container`](layout-elements.md#container)

- [`expander`](layout-elements.md#expander)

- [`tabs`](layout-elements.md#tabs)

- [`form`](layout-elements.md#form)

---

### [🎯 Status Elements](status-elements.md)
Communicate application state with styled alerts and messages.

**Available Elements:**

- [`success`](status-elements.md#success)

- [`info`](status-elements.md#info)

- [`warning`](status-elements.md#warning)

- [`error`](status-elements.md#error)

- [`progress`](status-elements.md#progress)

---

## Component Philosophy

### Enhanced, Not Replaced

st_yled elements are **enhanced versions** of Streamlit elements, not replacements:

```python
# Standard Streamlit
st.button("Click me")

# Enhanced with st_yled - same functionality + styling
st_yled.button("Click me", background_color="#3498db", color="white")
```

### Backward Compatibility

All st_yled elements accept the same parameters as their Streamlit equivalents:

```python
# All standard parameters work exactly the same
st_yled.selectbox(
    "Choose option",
    ["A", "B", "C"],
    index=1,
    help="Select an option",
    disabled=False,
    key="my_select"
)

# Plus additional styling parameters
st_yled.selectbox(
    "Styled option",
    ["A", "B", "C"],
    background_color="#f8f9fa",
    border_color="#007bff",
    border_radius="8px"
)
```

---

## Styling Patterns

### Individual Component Styling

Style elements individually for specific requirements:

```python
# Styled title
st_yled.title(
    "Dashboard Overview",
    color="#2c3e50",
    font_size="2.5rem",
    text_align="center",
    margin_bottom="30px"
)

# Styled button with hover effect
st_yled.button(
    "Primary Action",
    background_color="#007bff",
    color="white",
    border_radius="6px",
    padding="12px 24px",
    font_weight="bold"
)
```

### Global Styling

Apply consistent styles across all elements of the same type:

```python
# Set global button styles
st_yled.set("button", "border_radius", "8px")
st_yled.set("button", "font_weight", "600")
st_yled.set("button", "transition", "all 0.3s ease")

# All buttons will inherit these styles
st_yled.button("Button 1")  # Automatically styled
st_yled.button("Button 2")  # Also automatically styled
```

### Theme-Based Styling

Create cohesive visual themes:

```python
# Define theme colors
PRIMARY = "#3498db"
SECONDARY = "#2ecc71"
BACKGROUND = "#f8f9fa"

# Apply theme to multiple elements
st_yled.header("Section Title", color=PRIMARY)
st_yled.container(background_color=BACKGROUND, padding="20px")
st_yled.button("Action", background_color=SECONDARY, color="white")
```

---

## Validation and Error Handling

### CSS Property Validation

st_yled validates all styling properties to prevent errors:

```python
# ✅ Valid styling
st_yled.button("Button", color="#3498db")

# ❌ Invalid styling - helpful error message
st_yled.button("Button", color="invalid-color")
# Error: Invalid color value 'invalid-color'. Use hex (#ff0000), rgb(255,0,0), or named colors.
```

### Validation Modes

Control validation behavior based on your needs using environment variables

```bash
# Strict mode (default) - stops on validation errors
export ST_STYLED_STRICT_VALIDATION=True

# Bypass mode - no validation (performance optimized)
export ST_STYLED_BYPASS_VALIDATION=True
```

---

## Advanced Features

### Component State Styling

Style elements differently based on their state:

```python
# Button states
if st.session_state.get("success"):
    st_yled.button("Success!", background_color="#28a745")
else:
    st_yled.button("Try Again", background_color="#6c757d")

# Conditional container styling
status = "error" if error_occurred else "success"
background = "#ffe6e6" if status == "error" else "#e6ffe6"

st_yled.container(background_color=background, padding="15px")
```

### Component Composition

Combine multiple styled elements for complex layouts:

```python
# Card component composed of multiple st_yled elements
with st_yled.container(
    background_color="white",
    border_width="12px",
):
    st_yled.header("Card Title", color="#504c2cff", text_size="16")
    st_yled.text("Card content with styled text.", color="#51c786ff")
```

---

## Getting Help

### Component Documentation

Each component category has detailed documentation:

- **[Text Elements](text-elements.md)** - Typography and content display
- **[Input Elements](input-elements.md)** - Forms and user interaction
- **[Data Elements](data-elements.md)** - Tables, metrics, and data display
- **[Layout Elements](layout-elements.md)** - Containers and page structure
- **[Status Elements](status-elements.md)** - Alerts, progress, and feedback

### Quick Reference

- **[API Documentation](../api/index.md)** - Function signatures and parameters

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
