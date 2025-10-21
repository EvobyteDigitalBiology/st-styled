# Text Elements

Text elements are the foundation of content display in Streamlit applications. st_yled enhances these elements with comprehensive typography controls, color options, and layout capabilities.

## Available Elements

- [title](#title) - Main page titles
- [header](#header) - Section headers
- [subheader](#subheader) - Subsection headers
- [text](#text) - General text content
- [markdown](#markdown) - Markdown content with styling
- [caption](#caption) - Small text and footnotes
- [code](#code) - Code display with syntax highlighting
- [latex](#latex) - Mathematical expressions

---

### title
**Streamlit equivalent:** `st.title()`

Display main page titles with customizable typography and styling.

```python
st_yled.title("Page Title",
            color="#2c3e50",
            font_size="2.5rem")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

<br>

### header
**Streamlit equivalent:** `st.header()`

Section headers for organizing content with clear visual hierarchy.

```python
st_yled.header("Section Header", color="#34495e", font_size="2rem")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

<br>

### subheader
**Streamlit equivalent:** `st.subheader()`

Subsection headers for detailed content organization.

```python
st_yled.subheader("Subsection Title", color="#7f8c8d", font_size="1.3rem")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

<br>

### text
**Streamlit equivalent:** `st.text()` or `st.write()`

General text content with comprehensive formatting options.

```python
st_yled.text("Body text content", color="#2c3e50", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

<br>

### markdown
**Streamlit equivalent:** `st.markdown()`

Render markdown content with enhanced styling options.

```python
st_yled.markdown("**Bold text** with *emphasis*", color="#2c3e50", font_size="16px")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

<br>

### caption
**Streamlit equivalent:** `st.caption()`

Small text for captions, footnotes, and secondary information.

```python
st_yled.caption("Figure 1: Sales data over time", color="#6c757d", font_size="12px")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)

---

<br>

### code
**Streamlit equivalent:** `st.code()`

Display code with syntax highlighting and custom styling.

```python
st_yled.code("print('Hello, World!')", language="python",
             background_color="#f8f9fa", color="#2c3e50")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)
- `background_color` - Background color (hex, rgb, named colors)
- `font_size` - Font size (px, rem, em, %, or integer as px)
- `border_style` - Border style (solid, dashed, dotted, none)
- `border_color` - Border color (hex, rgb, named colors)
- `border_width` - Border width (px, rem, em, or integer as px)

---

<br>

### latex
**Streamlit equivalent:** `st.latex()`

Render mathematical expressions with styling options.

```python
st_yled.latex(r"\sum_{i=1}^{n} x_i = \mu", color="#2c3e50")
```

**Supported Styling Properties:**

- `color` - Text color (hex, rgb, named colors)

---

## Next Steps

Explore more component categories:

- **[Input Elements](input-elements.md)** - Interactive form elements with styling
- **[Data Elements](data-elements.md)** - Tables, metrics, and data visualization
- **[Layout Elements](layout-elements.md)** - Containers and page structure

Or dive deeper into text styling:

- **[Basic Styling Guide](../getting-started/basic-styling.md)** - CSS fundamentals
- **[Typography Examples](../examples/basic-examples/color-themes.md)** - Real-world text styling patterns

---
