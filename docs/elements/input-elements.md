# Input Components

Interactive input components allow users to interact with your Streamlit application. st_yled enhances these components with comprehensive styling options while maintaining full functionality and event handling.

## Available Elements

- [button](#button) - Interactive buttons with extensive styling and state management
- [download_button](#download_button) - Download buttons with custom styling for file downloads
- [link_button](#link_button) - External link buttons with custom appearance
- [selectbox](#selectbox) - Dropdown selection with styling options
- [radio](#radio) - Radio button groups with custom styling
- [multiselect](#multiselect) - Multiple selection component with styling
- [checkbox](#checkbox) - Checkbox with custom styling options
- [text_input](#text_input) - Text input fields with comprehensive styling
- [text_area](#text_area) - Multi-line text input with styling options
- [number_input](#number_input) - Numeric input with custom styling
- [slider](#slider) - Range slider with custom styling
- [select_slider](#select_slider) - Selection slider with discrete values
- [date_input](#date_input) - Date picker with styling options
- [time_input](#time_input) - Time picker with custom styling
- [color_picker](#color_picker) - Color selection with styling options
- [file_uploader](#file_uploader) - File upload component with custom styling
- [camera_input](#camera_input) - Camera input with styling options

---

## Button Components

### button
**Streamlit equivalent:** `st.button()`

Interactive buttons with extensive styling and state management.

```python
clicked = st_yled.button("Click Me", background_color="#007bff", color="white")
```

**Supported Styling Properties:**

- `background_color` - Button background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
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

### download_button
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

### link_button
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
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

**Button Types:**

Link buttons support the same type variations as regular buttons:

- **Primary** (`type="primary"`)
- **Secondary** (`type="secondary"`) - Default
- **Tertiary** (`type="tertiary"`)


```python
st_yled.set("link_button_primary", "background_color", "lightblue")
st_yled.set("link_button_secondary", "background_color", "lightblue")
st_yled.set("link_button_tertiary", "background_color", "lightblue")
```

---

## Selection Components

### selectbox
**Streamlit equivalent:** `st.selectbox()`

Dropdown selection with styling options.

```python
option = st_yled.selectbox(
    "Choose option",
    ["A", "B", "C"],
    background_color="#f8f9fa",
    border_color="#007bff"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

### radio
**Streamlit equivalent:** `st.radio()`

Radio button groups with custom styling.

```python
choice = st_yled.radio(
    "Select option",
    ["Option 1", "Option 2", "Option 3"],
    color="#007bff"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

### multiselect
**Streamlit equivalent:** `st.multiselect()`

Multiple selection component with styling.

```python
selections = st_yled.multiselect(
    "Choose multiple",
    ["A", "B", "C", "D"],
    background_color="#ffffff",
    border_color="#ced4da"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

### checkbox
**Streamlit equivalent:** `st.checkbox()`

Checkbox with custom styling options.

```python
enabled = st_yled.checkbox(
    "Enable notifications",
    color="#28a745",
    font_size="16px"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Input Fields

### text_input
**Streamlit equivalent:** `st.text_input()`

Text input fields with comprehensive styling.

```python
name = st_yled.text_input(
    "Your name",
    placeholder="Enter your name...",
    background_color="#f8f9fa",
    border_color="#007bff"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

### text_area
**Streamlit equivalent:** `st.text_area()`

Multi-line text input with styling options.

```python
content = st_yled.text_area(
    "Your message",
    placeholder="Type your message here...",
    background_color="#f8f9fa",
    border_color="#6c757d"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

### number_input
**Streamlit equivalent:** `st.number_input()`

Numeric input with custom styling.

```python
value = st_yled.number_input(
    "Enter number",
    min_value=0,
    max_value=100,
    background_color="#ffffff",
    border_color="#17a2b8"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Slider Components

### slider
**Streamlit equivalent:** `st.slider()`

Range slider with custom styling.

```python
value = st_yled.slider(
    "Select value",
    0, 100, 50,
    color="#007bff",
    font_size="16px"
)
```

**Supported Styling Properties:**

- `color` - Text and track color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

### select_slider
**Streamlit equivalent:** `st.select_slider()`

Selection slider with discrete values.

```python
size = st_yled.select_slider(
    "Size",
    ["XS", "S", "M", "L", "XL"],
    value="M",
    color="#28a745"
)
```

**Supported Styling Properties:**

- `color` - Text and track color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

## Date and Time Components

### date_input
**Streamlit equivalent:** `st.date_input()`

Date picker with styling options.

```python
date = st_yled.date_input(
    "Select date",
    background_color="#ffffff",
    border_color="#007bff"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

### time_input
**Streamlit equivalent:** `st.time_input()`

Time picker with custom styling.

```python
time = st_yled.time_input(
    "Select time",
    background_color="#ffffff",
    border_color="#6c757d"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Specialized Input Components

### color_picker
**Streamlit equivalent:** `st.color_picker()`

Color selection with styling options.

```python
color = st_yled.color_picker(
    "Choose color",
    value="#FF0000",
    color="#2c3e50"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

### file_uploader
**Streamlit equivalent:** `st.file_uploader()`

File upload component with custom styling.

```python
file = st_yled.file_uploader(
    "Upload file",
    type=['csv', 'xlsx'],
    background_color="#f8f9fa",
    border_color="#6c757d"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

### camera_input
**Streamlit equivalent:** `st.camera_input()`

Camera input with styling options.

```python
photo = st_yled.camera_input(
    "Take a photo",
    color="#2c3e50",
    border_color="#007bff"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Next Steps

Continue exploring st_yled components:

- **[Layout Components](layout-components.md)** - Containers and page structure
- **[Status Components](status-components.md)** - Alerts, progress, and feedback

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
