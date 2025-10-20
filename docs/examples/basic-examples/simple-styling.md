# Simple Styling

Learn the fundamentals of st_yled component styling with practical, easy-to-follow examples. This guide covers basic styling concepts that form the foundation for more advanced applications.

**Difficulty:** 🟢 Beginner
**Time:** 15-20 minutes
**Prerequisites:** Basic Streamlit knowledge

---

## Overview

In this example, you'll learn how to:

- Apply basic styling to common components using **available** properties
- Use color properties effectively
- Control text appearance with font sizing
- Create visual hierarchy with supported styling options

**Important:** This example only uses styling properties that are actually available in st_yled. Each component has specific supported properties - refer to the [Component Reference](../../elements/index.md) for complete details.

---

## Complete Example Code

```python
import streamlit as st
import st_yled

# Page configuration
st.set_page_config(page_title="Simple Styling Demo", page_icon="🎨")

# Initialize st_yled
st_yled.init()

# ============================================================================
# Header Section
# ============================================================================

st_yled.title(
    "🎨 Simple Styling Demo",
    color="#2c3e50",
    font_size="2.5rem"
)

st_yled.text(
    "Learn basic st_yled styling with these simple examples",
    color="#7f8c8d",
    font_size="1.2rem"
)

# ============================================================================
# Text Styling Examples
# ============================================================================

st_yled.header("📝 Text Styling", color="#3498db")

# Basic text colors
st_yled.text("This is primary text", color="#2c3e50")
st_yled.text("This is secondary text", color="#7f8c8d")
st_yled.text("This is success text", color="#27ae60")
st_yled.text("This is warning text", color="#f39c12")
st_yled.text("This is error text", color="#e74c3c")

# Font sizes
st_yled.subheader("Font Sizes", color="#34495e")
st_yled.text("Large text", font_size="20px", color="#2c3e50")
st_yled.text("Normal text", font_size="16px", color="#2c3e50")
st_yled.text("Small text", font_size="14px", color="#2c3e50")
st_yled.text("Extra small text", font_size="12px", color="#2c3e50")

# Available text styling (note: font_weight is not supported)
st_yled.subheader("Text Colors", color="#34495e")
st_yled.text("Dark text", color="#2c3e50")
st_yled.text("Medium text", color="#7f8c8d")
st_yled.text("Success text", color="#27ae60")
st_yled.text("Warning text", color="#f39c12")

# ============================================================================
# Button Styling Examples
# ============================================================================

st_yled.header("🔘 Button Styling", color="#9b59b6")

# Button color variations
col1, col2, col3 = st.columns(3)

with col1:
    st_yled.button(
        "Primary",
        background_color="#3498db",
        color="white"
    )

with col2:
    st_yled.button(
        "Success",
        background_color="#27ae60",
        color="white"
    )

with col3:
    st_yled.button(
        "Warning",
        background_color="#f39c12",
        color="white"
    )

# Button size variations
st_yled.subheader("Button Sizes", color="#34495e")

col1, col2, col3 = st.columns(3)

with col1:
    st_yled.button(
        "Small",
        background_color="#95a5a6",
        color="white",
        font_size="12px"
    )

with col2:
    st_yled.button(
        "Medium",
        background_color="#95a5a6",
        color="white",
        font_size="14px"
    )

with col3:
    st_yled.button(
        "Large",
        background_color="#95a5a6",
        color="white",
        font_size="16px"
    )

# Button borders (using border properties)
st_yled.subheader("Border Buttons", color="#34495e")

col1, col2 = st.columns(2)

with col1:
    st_yled.button(
        "Border Primary",
        background_color="white",
        color="#3498db",
        border_style="solid",
        border_color="#3498db",
        border_width="2px"
    )

with col2:
    st_yled.button(
        "Border Success",
        background_color="white",
        color="#27ae60",
        border_style="solid",
        border_color="#27ae60",
        border_width="2px"
    )

# ============================================================================
# Container Styling Examples (Note: Limited styling options available)
# ============================================================================

st_yled.header("📦 Container Styling", color="#e67e22")

# Basic container (only background_color and border properties supported)
with st_yled.container(
    background_color="#ecf0f1",
    border_style="solid",
    border_color="#bdc3c7",
    border_width="1px"
):
    st_yled.text("This is content inside a styled container", color="#2c3e50")
    st_yled.text("Containers support limited styling properties", color="#7f8c8d")

# Another container example
with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e1e8ed",
    border_width="2px"
):
    st_yled.subheader("Container Content", color="#2c3e50")
    st_yled.text("This container has a white background and border", color="#34495e")
    st_yled.button("Container Action", background_color="#3498db", color="white")

# ============================================================================
# Metric Styling Examples (Note: Only color and font_size supported)
# ============================================================================

st_yled.header("📊 Metric Styling", color="#8e44ad")

# Metric examples with available styling
col1, col2, col3 = st.columns(3)

with col1:
    st_yled.metric(
        "Total Sales",
        "$12,345",
        "+15%",
        color="#2c3e50",
        font_size="16px"
    )

with col2:
    st_yled.metric(
        "New Users",
        "1,234",
        "+8%",
        color="#27ae60",
        font_size="18px"
    )

with col3:
    st_yled.metric(
        "Revenue",
        "$45,678",
        "+22%",
        color="#e67e22",
        font_size="14px"
    )

# ============================================================================
# Interactive Example
# ============================================================================

st_yled.header("🎮 Interactive Example", color="#e74c3c")

# User inputs for customization
col1, col2 = st.columns(2)

with col1:
    button_color = st_yled.color_picker(
        "Choose button color",
        value="#3498db"
    )

    text_color = st_yled.selectbox(
        "Choose text color",
        ["#2c3e50", "#e74c3c", "#27ae60", "#f39c12"]
    )

with col2:
    border_radius = st_yled.slider(
        "Border radius",
        0, 20, 6,
        color="#3498db"
    )

    padding_size = st_yled.selectbox(
        "Padding size",
        ["8px 16px", "10px 20px", "12px 24px", "15px 30px"]
    )

# Live preview
st_yled.subheader("Live Preview", color="#34495e")

st_yled.button(
    "Preview Button",
    background_color=button_color,
    color="white",
    font_size="14px"
)

st_yled.text(
    "This text color changes based on your selection",
    color=text_color,
    font_size="16px"
)

# ============================================================================
# Footer
# ============================================================================

# Note: st_yled.divider() doesn't exist, using regular st.divider() instead
st.divider()

st_yled.text(
    "🎉 Congratulations! You've learned the basics of st_yled styling.",
    color="#27ae60",
    font_size="18px"
)

st_yled.text(
    "Ready for more advanced examples? Check out the Button Gallery and Color Themes!",
    color="#7f8c8d"
)
```

---

## Step-by-Step Breakdown

### 1. Basic Setup

```python
import streamlit as st
import st_yled

# Always initialize st_yled first
st_yled.init()
```

**Key concepts:**
- Import both `streamlit` and `st_yled`
- Call `st_yled.init()` before using any styled components
- Set page configuration for better presentation

### 2. Text Styling Fundamentals

```python
# Different text colors for different purposes
st_yled.text("Primary content", color="#2c3e50")     # Dark gray
st_yled.text("Secondary info", color="#7f8c8d")      # Light gray
st_yled.text("Success message", color="#27ae60")     # Green
st_yled.text("Warning", color="#f39c12")             # Orange
st_yled.text("Error", color="#e74c3c")               # Red
```

**Best practices:**
- Use consistent colors throughout your app
- Choose colors with good contrast for readability
- Reserve bright colors for important messages

### 3. Button Styling Patterns

```python
# Primary button pattern
st_yled.button(
    "Action",
    background_color="#3498db",  # Blue background
    color="white",               # White text
    border_style="solid",        # Border style
    border_color="#3498db",      # Border color
    border_width="2px",          # Border width
    font_size="14px"             # Font size
)
```

**Button variations:**
- **Solid buttons** - Filled background for primary actions
- **Border buttons** - Use border properties for outlined styles
- **Size variations** - Different font sizes for different button sizes
- **Color coding** - Different colors for different action types

**Available button properties:**
- `background_color` - Button background color
- `color` - Text color
- `font_size` - Text size
- `border_style` - Border style (solid, dashed, etc.)
- `border_color` - Border color
- `border_width` - Border thickness

### 4. Container Organization

```python
# Basic container (limited styling options)
with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e1e8ed",
    border_width="1px"
):
    # Content goes here
    st_yled.text("Card content")
```

**Container purposes:**
- **Organization** - Group related content
- **Visual separation** - Create distinct sections using background colors
- **Emphasis** - Highlight important information with borders
- **Layout control** - Structure your app's appearance

**Available container properties:**
- `background_color` - Container background color
- `border_style` - Border style (solid, dashed, etc.)
- `border_color` - Border color
- `border_width` - Border thickness

### 5. Metric Display

```python
# Professional metric styling
st_yled.metric(
    "Sales",                     # Label
    "$12,345",                   # Value
    "+15%",                      # Delta (change)
    color="#2c3e50",             # Text color
    font_size="16px"             # Font size
)
```

**Metric styling tips:**
- Use consistent colors across metrics for professional appearance
- Adjust font sizes for hierarchy and readability
- Color-code based on performance (green=good, red=bad)
- Keep styling minimal as metrics have limited style options

**Available metric properties:**
- `color` - Text color for label and value
- `font_size` - Font size for label and value

---

## What You Learned

✅ **Color Application** - How to apply colors consistently across components
✅ **Typography Control** - Managing font sizes and colors within supported limits
✅ **Button Styling** - Creating different button styles using available properties
✅ **Container Usage** - Organizing content with basic container styling
✅ **Metric Display** - Professional data presentation with color and font control
✅ **Property Limitations** - Understanding which CSS properties are actually supported
✅ **Interactive Elements** - Combining user input with available styling options

**Key Takeaway:** st_yled provides focused styling capabilities. Each component supports specific CSS properties - always check the [Element Reference](../../elements/index.md) for available options.

---

## Next Steps

Ready to explore more styling capabilities?

### Advanced Learning
- **[Dashboard Demo](../advanced-examples/dashboard-demo.md)** - Complex layout patterns
- **[Global Styling](../../getting-started/global-styling.md)** - Consistent styling across your app

### Practice Exercises

Try these modifications to reinforce your learning:

1. **Color Experiment** - Change all colors to create a dark theme
2. **Button Variations** - Create 5 different button styles
3. **Card Layout** - Organize the content into card-based sections
4. **Interactive Enhancement** - Add more user controls for customization

---

## Troubleshooting

### Common Issues

**Colors not showing:**
- Verify `st_yled.init()` is called first
- Check color format (use hex like `#3498db`)
- Ensure proper string quoting

**Styling not applying:**
- Check for typos in property names
- Verify component syntax matches examples
- Clear browser cache if changes don't appear

**Layout problems:**
- Use `st.columns()` for side-by-side elements
- Check container nesting and closing
- Verify margin and padding values

### Getting Help

- **[GitHub Issues](https://github.com/EvobyteDigitalBiology/st-styled/issues)** - Report problems

---

<br>

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
