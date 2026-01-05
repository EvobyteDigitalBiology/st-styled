# Layout Components

Layout components provide the structural foundation for your Streamlit applications. st_yled enhances these components with advanced styling options for containers, columns, and organizational elements.

## Available Elements

- [container](#container) - Flexible containers for grouping and styling content sections
- [expander](#expander) - Collapsible content sections with custom styling
- [tabs](#tabs) - Tabbed interface with custom styling options
- [form](#form) - Enhanced forms with styling and layout options

---

## Container Components

### container
**Streamlit equivalent:** `st.container()`

Flexible containers for grouping and styling content sections.

```python
with st_yled.container(
    background_color="#f8f9fa",
    border_color="#dee2e6",
    padding="20px"
):
    st_yled.text("Content inside styled container")
```

**Supported Styling Properties:**

- `background_color` - Container background color (hex, rgb, named colors)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `padding` - Inner padding for all sides (px, rem, em, or integer as px)
- `padding_left` - Left padding (px, rem, em, or integer as px)
- `padding_right` - Right padding (px, rem, em, or integer as px)
- `padding_top` - Top padding (px, rem, em, or integer as px)
- `padding_bottom` - Bottom padding (px, rem, em, or integer as px)

---

## Organizational Components

### expander
**Streamlit equivalent:** `st.expander()`

Collapsible content sections with custom styling.

```python
with st_yled.expander(
    "Click to expand",
    color="#2c3e50",
    background_color="#f8f9fa",
    padding="16px"
):
    st_yled.text("Hidden content here")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Header background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `padding` - Inner padding for expanded content, all sides (px, rem, em, or integer as px)
- `padding_left` - Left padding for expanded content (px, rem, em, or integer as px)
- `padding_right` - Right padding for expanded content (px, rem, em, or integer as px)
- `padding_top` - Top padding for expanded content (px, rem, em, or integer as px)
- `padding_bottom` - Bottom padding for expanded content (px, rem, em, or integer as px)

### tabs
**Streamlit equivalent:** `st.tabs()`

Tabbed interface with custom styling options.

```python
tab1, tab2, tab3 = st_yled.tabs(["Tab 1", "Tab 2", "Tab 3"], color="#007bff", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color
- `font_size` - Font size
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

## Form Components

### form
**Streamlit equivalent:** `st.form()` with `st.form_submit_button()`

Enhanced forms with styling and layout options.

```python
with st_yled.form("my_form"):
    st_yled.text_input("Name")
    st_yled.form_submit_button("Submit", background_color="#007bff", color="white")
```

**Form Submit Button Styling Properties:**

- `background_color` - Button background color
- `color` - Text color
- `font_size` - Font size
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Next Steps

Explore more component categories:

- **[Status Elements](status-elements.md)** - Progress indicators and status messages
- **[Button Elements](button-elements.md)** - Interactive buttons and controls

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
