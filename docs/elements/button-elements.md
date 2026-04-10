# Button Elements

Button elements provide interactive controls for user actions in your Streamlit application. st_yled enhances these components with comprehensive styling options while maintaining full functionality and event handling.

## Available Elements

- [button](#button) - Interactive buttons with extensive styling and state management
- [menu_button](#menu_button) - Menu button with stylable dropdown trigger
- [download_button](#download_button) - Download buttons with custom styling for file downloads
- [link_button](#link_button) - External link buttons with custom appearance
- [form_submit_button](#form_submit_button) - Form submission buttons with styling options

---

## button
**Streamlit equivalent:** `st.button()`

Interactive buttons with extensive styling and state management.

```python
clicked = st_yled.button("Click Me", background_color="#007bff", color="white")
```

**Supported Styling Properties:**

- `background_color` - Button background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

**Button Types:**

st_yled supports independent styling for different button types by using the `type` parameter:

- **Primary buttons** (`type="primary"`) - Main action buttons
- **Secondary buttons** (`type="secondary"`) - Default button style
- **Tertiary buttons** (`type="tertiary"`) - Subtle action buttons

```python
# Primary button
primary = st_yled.button(
    "Primary Action",
    type="primary",
    background_color="#007bff",
    color="white"
)

# Secondary button
secondary = st_yled.button(
    "Secondary Action",
    type="secondary",
    background_color="#6c757d",
    color="white"
)

# Tertiary button
tertiary = st_yled.button(
    "Tertiary Action",
    type="tertiary",
    background_color="transparent",
    color="#007bff"
)
```

For **global styling** of individual button types use the following accessors

```python
st_yled.set("button_primary", "background_color", "lightblue")
st_yled.set("button_secondary", "background_color", "lightblue")
st_yled.set("button_tertiary", "background_color", "lightblue")
```

---

## menu_button
**Streamlit equivalent:** `st.menu_button()`

Menu button for grouped actions with button-like styling support.

> Requires Streamlit `>= 1.56`.

```python
choice = st_yled.menu_button(
    "Actions",
    options=["Export CSV", "Export PDF", "Archive"],
    type="primary",
    background_color="#ff4b4b",
    color="#ffffff",
)
```

**Supported Styling Properties:**

- `background_color` - Button background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

For **global styling** of individual menu button types use:

```python
st_yled.set("menu_button_primary", "background_color", "lightblue")
st_yled.set("menu_button_secondary", "background_color", "lightblue")
st_yled.set("menu_button_tertiary", "background_color", "lightblue")
```

---

## download_button
**Streamlit equivalent:** `st.download_button()`

Download buttons with custom styling for file downloads.

```python
st_yled.download_button(
    "📄 Download Report",
    data=file_data,
    file_name="report.pdf",
    background_color="#17a2b8",
    color="white"
)
```

**Supported Styling Properties:**

- `background_color` - Button background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

**Button Types:**

Download buttons support the same type variations as regular buttons:

- **Primary** (`type="primary"`)
- **Secondary** (`type="secondary"`) - Default
- **Tertiary** (`type="tertiary"`)

For **global styling** of individual button types use the following accessors

```python
st_yled.set("download_button_primary", "background_color", "lightblue")
st_yled.set("download_button_secondary", "background_color", "lightblue")
st_yled.set("download_button_tertiary", "background_color", "lightblue")
```

---

## link_button
**Streamlit equivalent:** `st.link_button()`

External link buttons with custom appearance.

```python
st_yled.link_button(
    "🔗 Visit Website",
    url="https://example.com",
    background_color="#6f42c1",
    color="white"
)
```

**Supported Styling Properties:**

- `background_color` - Button background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

**Button Types:**

Link buttons support the same type variations as regular buttons:

- **Primary** (`type="primary"`)
- **Secondary** (`type="secondary"`) - Default
- **Tertiary** (`type="tertiary"`)

For **global styling** of individual button types use the following accessors

```python
st_yled.set("link_button_primary", "background_color", "lightblue")
st_yled.set("link_button_secondary", "background_color", "lightblue")
st_yled.set("link_button_tertiary", "background_color", "lightblue")
```

---

## form_submit_button
**Streamlit equivalent:** `st.form_submit_button()`

Form submission buttons with styling options. Must be used within a `st.form()` or `st_yled.form()` context.

```python
with st_yled.form("my_form"):
    st_yled.text_input("Name")
    st_yled.form_submit_button("Submit", background_color="#007bff", color="white")
```

**Supported Styling Properties:**

- `background_color` - Button background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Next Steps

Explore more component categories:

- **[Input Elements](input-elements.md)** - Text inputs, selections, and controls
- **[Layout Elements](layout-elements.md)** - Containers and page structure

Or dive deeper into styling:

- **[Basic Styling Guide](../getting-started/basic-styling.md)** - CSS fundamentals
- **[Global Styling](../getting-started/global-styling.md)** - Application-wide themes

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
