# Data Components

Data components are essential for displaying information, metrics, and datasets in your Streamlit applications. st_yled enhances these components with professional styling options for tables, metrics, charts, and data visualization.

## Available Elements

- [table](#table) - Static table display with enhanced styling
- [metric](#metric) - Display key performance indicators with custom styling
- [json](#json) - Display JSON data with syntax highlighting and styling

---

## Display Components

### table
**Streamlit equivalent:** `st.table()`

Static table display with enhanced styling.

```python
st_yled.table(df, background_color="#f8f9fa", color="#2c3e50")
```

**Supported Styling Properties:**

- `background_color` - Table background color
- `color` - Text color
- `font_size` - Text size in cells
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)
- `border_style` - Border style (solid, dashed, dotted)
- `border_color` - Border color
- `border_width` - Border width (px, rem, em, or integer as px)

---

## Metrics and KPIs

### metric
**Streamlit equivalent:** `st.metric()`

Display key performance indicators with custom styling.

```python
st_yled.metric("Revenue", "$12,345", "+15%", color="#2c3e50", font_size="18px")
```

**Supported Styling Properties:**

- `color` - Text color for label and value
- `font_size` - Text size for label and value
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

## Data Visualization

### json
**Streamlit equivalent:** `st.json()`

Display JSON data with syntax highlighting and styling.

```python
data = {"name": "John", "age": 30, "city": "New York"}
st_yled.json(data, color="#2c3e50", font_size="14px")
```

**Supported Styling Properties:**

- `color` - Text color
- `font_size` - Text size
- `font_weight` - Font weight (100-900, thin, extra-light, light, normal, medium, semi-bold, bold, extra-bold, black)

---

## Next Steps

Continue exploring st_yled components:

- **[Layout Components](layout-components.md)** - Containers and page structure
- **[Status Components](status-components.md)** - Alerts, progress, and feedback

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
