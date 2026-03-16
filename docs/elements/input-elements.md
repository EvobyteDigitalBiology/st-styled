# Input Components

Interactive input components allow users to interact with your Streamlit application. st_yled enhances these components with comprehensive styling options while maintaining full functionality and event handling.

## Available Elements

- [selectbox](#selectbox) - Dropdown selection with styling options
- [radio](#radio) - Radio button groups with custom styling
- [multiselect](#multiselect) - Multiple selection component with styling
- [pills](#pills) - Pill-style segmented choices with styling
- [segmented_control](#segmented_control) - Segmented selection control with styling
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
- [audio_input](#audio_input) - Audio recorder input with styling options

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

### pills
**Streamlit equivalent:** `st.pills()`

Pill-style segmented choices with custom styling.

```python
selection = st_yled.pills(
    "Choose",
    ["A", "B", "C"],
    color="#2c3e50",
    border_color="#007bff"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

### segmented_control
**Streamlit equivalent:** `st.segmented_control()`

Segmented selection control with custom styling.

```python
selection = st_yled.segmented_control(
    "Pick",
    ["X", "Y", "Z"],
    color="#2c3e50",
    background_color="#f8f9fa"
)
```

**Supported Styling Properties:**

- `background_color` - Background color (hex, rgb, named colors)
- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

## Slider Controls

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

### datetime_input
**Streamlit equivalent:** `st.datetime_input()`

Date and time picker with custom styling.

```python
datetime = st_yled.datetime_input(
    "Select date and time",
    background_color="#ffffff",
    border_color="#007bff"
)
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

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
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

### audio_input
**Streamlit equivalent:** `st.audio_input()`

Audio recorder input with styling options.

```python
audio = st_yled.audio_input(
    "Record audio",
    color="#2c3e50",
    border_color="#6c757d"
)
```

**Supported Styling Properties:**

- `color` - Text and icon color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)
- `label_color` - Label text color only (hex, rgb, named colors)
- `label_font_size` - Label text size only (px, rem, em, %, or integer as px)
- `label_font_weight` - Label font weight only (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

## Next Steps

Continue exploring st_yled components:

- **[Layout Components](layout-components.md)** - Containers and page structure
- **[Status Components](status-components.md)** - Alerts, progress, and feedback

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
