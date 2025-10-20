# Global Styling Guide

Learn how to create consistent themes and design systems across your entire Streamlit application using st_yled's global styling capabilities.

---

## What is Global Styling?

Global styling allows you to set default styles for all components of a specific type on an app page. Instead of styling each component individually, you define styles once and they apply automatically throughout your app page.

**Benefits:**

- **Consistency** - Uniform look across all components

- **Efficiency** - Set styles once, apply everywhere

- **Maintainability** - Easy theme changes and updates

- **Scalability** - Perfect for large applications

---

## Basic Global Styling

### Setting Global Styles

Use `st_yled.set()` to apply styles globally to component types:

**NOTE**: Global styling must be applied to each page of your app

```python
import st_yled

# Initialize st_yled
st_yled.init()

# Global button styling
st_yled.set("button", "background_color", "#3498db")
st_yled.set("button", "color", "white")
st_yled.set("button", "border_width", "2px")
st_yled.set("button", "border_style", "dotted")
st_yled.set("button", "border_color", "yellow")
st_yled.set("button", "font_size", "20px")

# Now all buttons will have these styles automatically
st_yled.button("Button 1")  # Styled with global settings
st_yled.button("Button 2")  # Also styled with global settings
st_yled.button("Button 3")  # All buttons look consistent
```

### Available Component Types

You can set global styles for any st_yled component:

```python

# Initialize st_yled
st_yled.init()

# Text components
st_yled.set("title", "color", "#2c3e50")
st_yled.set("header", "color", "#34495e")
st_yled.set("text", "font_size", "13px")

# Input components
st_yled.set("text_input", "background_color", "f8f9fa")
st_yled.set("selectbox", "background_color", "#f8f9fa")

# Container components
st_yled.set("container", "border_width", "4px")
st_yled.set("container", "border_color", "black")
st_yled.set("expander", "background_color", "#f6f6f6")
```

---

## Creating Design Systems

### 1. Color Theme System

Define a comprehensive color palette:

```python
# Define your brand colors
COLORS = {
    "primary": "#3498db",
    "secondary": "#2ecc71",
    "accent": "#e74c3c",
    "background": "#f8f9fa",
    "surface": "#ffffff",
    "text_primary": "#2c3e50",
    "text_secondary": "#7f8c8d",
    "border": "#e1e8ed"
}



# Apply color theme globally
def apply_color_theme():
    # Button themes
    st_yled.set("button", "background_color", COLORS["primary"])
    st_yled.set("button", "color", "white")

    # Text themes
    st_yled.set("title", "color", COLORS["text_primary"])
    st_yled.set("header", "color", COLORS["text_primary"])
    st_yled.set("text", "color", COLORS["text_secondary"])

    # Container themes
    st_yled.set("container", "background_color", COLORS["surface"])
    st_yled.set("container", "border_color", COLORS["border"])

# Initialize your theme
st_yled.init()
apply_color_theme()
```

---

## Theme Variations

### Light Theme

```python
def apply_light_theme():
    LIGHT_COLORS = {
        "background": "#ffffff",
        "surface": "#f8f9fa",
        "primary": "#007bff",
        "text": "#212529",
        "border": "#dee2e6"
    }

    st_yled.set("container", "background_color", LIGHT_COLORS["surface"])
    st_yled.set("text", "color", LIGHT_COLORS["text"])
    st_yled.set("button", "background_color", LIGHT_COLORS["primary"])
    st_yled.set("container", "border_color", LIGHT_COLORS["border"])
```

### Dark Theme

```python
def apply_dark_theme():
    DARK_COLORS = {
        "background": "#1a1a1a",
        "surface": "#2d2d2d",
        "primary": "#4dabf7",
        "text": "#ffffff",
        "text_secondary": "#b0b0b0",
        "border": "#404040"
    }

    st_yled.set("container", "background_color", DARK_COLORS["surface"])
    st_yled.set("text", "color", DARK_COLORS["text"])
    st_yled.set("header", "color", DARK_COLORS["text"])
    st_yled.set("title", "color", DARK_COLORS["text"])
    st_yled.set("button", "background_color", DARK_COLORS["primary"])
    st_yled.set("container", "border_color", DARK_COLORS["border"])
```

### Corporate Theme

```python
def apply_corporate_theme():
    CORPORATE_COLORS = {
        "primary": "#003366",    # Navy blue
        "secondary": "#0066cc",  # Medium blue
        "accent": "#ff6600",     # Orange
        "background": "#f5f5f5", # Light gray
        "text": "#333333"        # Dark gray
    }

    # Professional button styling
    st_yled.set("button", "background_color", CORPORATE_COLORS["primary"])
    st_yled.set("button", "color", "white")

    # Conservative typography
    st_yled.set("title", "color", CORPORATE_COLORS["primary"])
    st_yled.set("text", "color", CORPORATE_COLORS["text"])
```

---

## Advanced Global Styling

### Conditional Theme Application

Apply different themes based on user preferences or app state:

```python
def apply_theme(theme_name):
    """Apply theme based on user selection."""

    # Reset any existing styles
    st_yled.reset_global_styles()

    if theme_name == "light":
        apply_light_theme()
    elif theme_name == "dark":
        apply_dark_theme()
    elif theme_name == "corporate":
        apply_corporate_theme()
    else:
        apply_default_theme()

# Init st_yled
st_yled.init()

# Usage with user selection
theme_choice = st.selectbox("Choose Theme", ["light", "dark", "corporate"])
apply_theme(theme_choice)
```

---

## Troubleshooting Global Styles

### Common Issues

**Styles not applying:**
```python
# ❌ Forgot to initialize
st_yled.button("Button")  # No styling

# ✅ Initialize first
st_yled.init()
st_yled.set("button", "background_color", "#3498db")
st_yled.button("Button")  # Styled correctly
```

**Individual styles overriding global:**
```python
# Global style
st_yled.set("button", "background_color", "#3498db")

# Individual style takes precedence
st_yled.button("Button", background_color="#e74c3c")  # Red, not blue
```

**CSS specificity conflicts:**
```python
# More specific selectors may be needed
st_yled.set("button", "background_color", "#3498db !important")
```

### Debugging Tips

```python
# Check current global styles
current_styles = st_yled.get_global_styles()
st.write(current_styles)

# Reset all global styles if needed
st_yled.reset_global_styles()

# Apply styles step by step to isolate issues
st_yled.set("button", "background_color", "#3498db")
# Test...
st_yled.set("button", "border_radius", "6px")
# Test...
```

---

## Next Steps

Master global styling and ready for more advanced topics:

- **[Component Reference](../elements/index.md)** - Detailed styling options for each component type
- **[Advanced Examples](../examples/advanced-examples/custom-themes.md)** - Complex theme implementations
- **[API Reference](../api/index.md)** - Complete function documentation for global styling

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
