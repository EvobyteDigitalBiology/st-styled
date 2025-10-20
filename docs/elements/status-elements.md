# Status Components

Status components communicate application state, provide feedback, and guide users through processes. st_yled enhances these components with comprehensive styling options for alerts, progress indicators, and interactive feedback.

## Available Elements

- [success](#success) - Display success messages with custom styling
- [info](#info) - Display informational messages with styling options
- [warning](#warning) - Display warning messages with attention-grabbing styling
- [error](#error) - Display error messages with clear, attention-grabbing styling
- [progress](#progress) - Progress bars with custom styling and colors

---

## Alert Components

### success
**Streamlit equivalent:** `st.success()`

Display success messages with custom styling.

```python
st_yled.success("✅ Operation completed successfully!", color="#155724", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color
- `font_size` - Font size
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color
- `border_width` - Border width (px, rem, em, or integer as px)

### info
**Streamlit equivalent:** `st.info()`

Display informational messages with styling options.

```python
st_yled.info("ℹ️ This is important information", color="#0c5460", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color
- `font_size` - Font size
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color
- `border_width` - Border width (px, rem, em, or integer as px)

### warning
**Streamlit equivalent:** `st.warning()`

Display warning messages with attention-grabbing styling.

```python
st_yled.warning("⚠️ Please review your input", color="#856404", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color
- `font_size` - Font size
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color
- `border_width` - Border width (px, rem, em, or integer as px)

### error
**Streamlit equivalent:** `st.error()`

Display error messages with clear, attention-grabbing styling.

```python
st_yled.error("❌ An error occurred", color="#721c24", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color
- `font_size` - Font size
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Progress Components

### progress
**Streamlit equivalent:** `st.progress()`

Progress bars with custom styling and colors.

```python
progress_bar = st_yled.progress(0.7, background_color="#007bff")
```

**Supported Styling Properties:**

- `background_color` - Progress bar color

---

## Next Steps

Explore more st_yled features:

- **[Basic Styling Guide](../getting-started/basic-styling.md)** - CSS fundamentals
- **[Typography Examples](../examples/basic-examples/color-themes.md)** - Real-world text styling patterns

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
