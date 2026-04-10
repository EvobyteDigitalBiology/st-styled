# Input Components

Enhanced input components with advanced functionality for your Streamlit applications.

---

## Split Button

A button with a dropdown menu for multiple actions.

![Split Button](https://evo-byte.com/wp-content/uploads/2026/01/split_button_expanded.webp)

### Description

A button with a dropdown menu for multiple actions, combining a primary action with related secondary options.

For Streamlit `>= 1.56`, `split_button` uses `st.menu_button` for the dropdown trigger. In `v0.4.1`, dropdown menu width behavior was refined to reduce overly narrow menus.

### Usage Pattern

Use this component when you have a primary action with related secondary options. Perfect for save/submit buttons with variations (Save Draft, Save & Close), export buttons with multiple formats, or any action where users frequently need to choose between similar operations.

### Basic Example

```python
import st_yled

st_yled.init()

st_yled.split_button(
    label="Save",
    options=["Save Draft", "Save & Close", "Save & New"],
    icon=":material/save:",
    color="#FFFFFF",
    background_color="#1976D2",
    radius="20px",
    key="split-button-1",
)
```

### Quick Start

```python
st_yled.split_button(label="", options=["1", "2"])
```

### Parameters

- `label` (str): Text displayed on the main button
- `options` (List[str]): List of dropdown menu options
- `icon` (str, optional): Material icon for the button
- `color` (str, optional): Text color
- `background_color` (str, optional): Button background color
- `radius` (int | str): Border radius (default: "20px")
- `key` (str, optional): Unique key for the component

### Usage Examples

**Export with Multiple Formats:**

```python
action = st_yled.split_button(
    label="Export",
    options=["Export as PDF", "Export as CSV", "Export as Excel"],
    icon=":material/download:",
    background_color="#4CAF50",
    key="export-button"
)

if action == "Export as PDF":
    # Handle PDF export
    pass
elif action == "Export as CSV":
    # Handle CSV export
    pass
```

**Save with Variations:**

```python
save_action = st_yled.split_button(
    label="Save",
    options=["Save Draft", "Save & Continue", "Save & Close"],
    icon=":material/save:",
    background_color="#2196F3",
    key="save-button"
)

if save_action:
    st.success(f"Action: {save_action}")
```

---

## Next Steps

Explore more component categories:

- **[Card Components](cards.md)** - Beautiful card layouts
- **[Layout Components](layout.md)** - Advanced layout controls
- **[Navigation Components](navigation.md)** - Routing and navigation

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
