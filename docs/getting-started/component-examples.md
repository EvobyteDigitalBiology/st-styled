# st_yled Components

Learn how to use st_yled's custom components to create rich, interactive UIs without writing complex code. This guide demonstrates practical examples of components you can use in your applications.

---

## Overview

st_yled provides pre-built custom components that extend Streamlit's functionality. These components are ready to use and fully customizable with styling options.

**Available Component Categories:**

- 🃏 **Cards** - Display content in beautiful containers

- 📐 **Layout** - Advanced layout controls like sticky headers

- 🧭 **Navigation** - Routing and redirection components

- 🎛️ **Input** - Enhanced input controls with multiple actions

---

## Example 1: Product Card Gallery

Create a beautiful product showcase using badge and image cards:

```python
import streamlit as st
import st_yled

# Initialize st_yled
st_yled.init()

st_yled.title("🛍️ Product Showcase")

# Create a 3-column layout for products
col1, col2, col3 = st.columns(3)

with col1:
    st_yled.badge_card_one(
        badge_text="Sale",
        badge_icon=":material/local_offer:",
        title="Premium Laptop",
        text="High-performance laptop with the latest specs. Save 20% today!",
        background_color="#ffffff",
        border_color="#e74c3c",
        border_style="solid",
        border_width=2,
        width=300,
        title_font_size=20
    )

    if st.button("Add to Cart", key="laptop", use_container_width=True):
        st.success("Added to cart!")

with col2:
    st_yled.image_card_one(
        image_path="https://picsum.photos/300/200?random=1",
        title="Wireless Headphones",
        text="Noise-canceling headphones with 30-hour battery life",
        width=300,
        card_shadow=True,
        border_color="#3498db",
        border_style="solid",
        border_width=1,
        title_font_size=20
    )

    if st.button("Add to Cart", key="headphones", use_container_width=True):
        st.success("Added to cart!")

with col3:
    st_yled.badge_card_one(
        badge_text="New",
        badge_icon=":material/star:",
        title="Smart Watch",
        text="Track your fitness goals with our latest smartwatch technology",
        background_color="#f0f8ff",
        border_color="#2ecc71",
        border_style="solid",
        border_width=2,
        width=300,
        title_font_size=20
    )

    if st.button("Add to Cart", key="watch", use_container_width=True):
        st.success("Added to cart!")
```

**What this does:**

- Creates a responsive product gallery with 3 columns

- Uses badge cards to highlight sales and new products

- Uses image cards for visual product display

- Adds interactive "Add to Cart" buttons below each product

---

## Example 2: Dashboard with Sticky Navigation

Build a professional dashboard with persistent navigation:

```python
import streamlit as st
import st_yled

# Initialize st_yled
st_yled.init()

# Create sticky header for navigation
with st_yled.sticky_header(
    height="60px",
    background_color="#2c3e50",
    padding="0px 32px",
    vertical_alignment="center"
):
    # Navigation layout
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([2, 1, 1, 1])

    with nav_col1:
        st_yled.text("📊 Analytics Dashboard", color="white", font_size="24px")

    with nav_col2:
        if st.button("Dashboard", key="nav_home", use_container_width=True):
            st.session_state.page = "dashboard"

    with nav_col3:
        if st.button("Reports", key="nav_reports", use_container_width=True):
            st.session_state.page = "reports"

    with nav_col4:
        if st.button("Settings", key="nav_settings", use_container_width=True):
            st.session_state.page = "settings"

# Add some space below header
st.write("")
st.write("")

# Main dashboard content
st_yled.header("Key Metrics")

# Metrics row
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st_yled.metric(
        "Total Revenue",
        "$45,231",
        "+12.5%",
        label_color="#7f8c8d",
        value_color="#2ecc71",
        value_font_size="32px"
    )

with metric_col2:
    st_yled.metric(
        "Active Users",
        "2,847",
        "+8.2%",
        label_color="#7f8c8d",
        value_color="#3498db",
        value_font_size="32px"
    )

with metric_col3:
    st_yled.metric(
        "Conversion Rate",
        "3.24%",
        "+0.8%",
        label_color="#7f8c8d",
        value_color="#9b59b6",
        value_font_size="32px"
    )

with metric_col4:
    st_yled.metric(
        "Avg. Order Value",
        "$156.80",
        "-2.4%",
        label_color="#7f8c8d",
        value_color="#e74c3c",
        value_font_size="32px"
    )

# Content area with cards
st_yled.header("Recent Activity")

activity_col1, activity_col2 = st.columns(2)

with activity_col1:
    st_yled.badge_card_one(
        badge_text="Live",
        badge_icon=":material/wifi:",
        title="Current Campaign",
        text="Summer Sale 2026 is performing 15% above target with 3 days remaining",
        background_color="#d4edda",
        border_color="#28a745",
        border_style="solid",
        border_width=1,
        width=500
    )

with activity_col2:
    st_yled.image_card_one(
        image_path="https://picsum.photos/500/200?random=2",
        title="Latest Report",
        text="Q4 2025 Performance Analysis - Download the full report for detailed insights",
        width=500,
        card_shadow=True
    )
```

**What this does:**
- Creates a sticky navigation header that remains visible while scrolling
- Displays key metrics with custom colored values
- Shows activity cards with real-time status
- Provides a professional dashboard layout

---

## Component Styling Tips

### Badge Cards
- Use contrasting `border_color` to make badges stand out
- Set `border_width=2` for emphasis on important items
- Match `background_color` with badge meaning (green for success, red for urgent)

### Image Cards
- Enable `card_shadow=True` for depth and separation
- Use consistent `width` values for uniform grid layouts
- Adjust `title_font_size` for hierarchy

### Sticky Headers
- Keep `height` between "56px" and "80px" for optimal UX
- Use dark `background_color` with light text for contrast
- Set appropriate `padding` for breathing room

---

## Next Steps

Ready to build with components?

- **[More Component Examples](../examples/component-showcase.md)** - Split buttons, navigation, and more
- **[Components Reference](../components/index.md)** - Complete component documentation
- **[Basic Styling](basic-styling.md)** - Learn styling fundamentals
- **[Advanced Examples](../examples/advanced-examples/dashboard-demo.md)** - Complex applications
- **[Element Reference](../elements/index.md)** - Explore all styled elements

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
