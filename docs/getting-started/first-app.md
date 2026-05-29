# Your First Styled App

Create a beautiful Streamlit application with st_yled in just 10 minutes. This tutorial will guide you through building a complete app with professional styling.

---

## What We'll Build

A personal dashboard application featuring:

- Styled title and headers

- Custom button interactions

- Colorful metrics display

- Styled sidebar navigation

- Interactive components with validation

---

## Step 0: Expore Layouts in st_yled studio

Visit st_yled studio to easily try out and configure your app styling, which you can export. We will later load it into the example app.

Here is the [link to st_yled studio](https://styled-studio.streamlit.app/)


## Step 1: Create the Base App

Create a new file called `my_first_app.py`:

```python
import streamlit as st
import st_yled

# Initialize st_yled
st_yled.init()

# Page configuration
st.set_page_config(
    page_title="My Styled Dashboard",
    page_icon="🎨",
    layout="wide"
)

# App content placeholder
st_yled.title("My First Styled App")
```

Test your app:
```bash
streamlit run my_first_app.py
```

You should see a basic Streamlit app with a title.

For most elements `st_yled.` and `st.` module prefixes can be used interchangably. This means `st_yled.title("My Title")` and `st.title("My First Styled App")` will produce the same output, but `st_yled.` will accept custom styling attributes.

### Built-in Themes (v0.5)

You can apply a built-in theme template directly in `st_yled.init()`:

```python
import st_yled

st_yled.init(theme="bauhaus")
```

When a built-in theme is selected, st_yled updates the theme sections in `.streamlit/config.toml` so the app uses the template colors consistently.

---

## Step 2: Add a Styled Header

Replace the title with a styled header section:

```python
# Styled header section
st_yled.title(
    "🎨 Personal Dashboard",
    color="#4b68c8ff",
    font_size="3rem"
)


st_yled.chat_input("Say hello", background_color="#c9cfe5ff")

```

**What's happening here:**

- `color="#4b68c8ff"` - Dark blue-gray title color

- `font_size="3rem"` - Makes the title larger

- `background_color="#c9cfe5ff"` - Change background of chat input

---

## Step 3: Create a Styled Sidebar

Add navigation and controls in the sidebar:

```python
# Sidebar with styled navigation
with st.sidebar:
    st_yled.header("Navigation", color="#e74c3c")

    # Styled navigation buttons
    if st_yled.button("📊 Dashboard",
                      background_color="#3498db",
                      color="white",
                      width = 'stretch'):
        st.session_state.page = "dashboard"

    if st_yled.button("⚙️ Settings",
                      background_color="#95a5a6",
                      color="white",
                      width = 'stretch'):
        st.session_state.page = "settings"

    if st_yled.button("📈 Analytics",
                      background_color="#2ecc71",
                      color="white",
                      width = 'stretch'):
        st.session_state.page = "analytics"

    st_yled.divider()

    # Styled user info
    st_yled.info("👤 Logged in as: **Demo User**")
```

**Key styling concepts:**

- Different `background_color` for each button creates visual hierarchy

- `width="stretch"` makes buttons fill the sidebar width

- Consistent `color="white"` for button text readability

---

## Step 4: Interactive Components

Add some interactive styled components:

```python
st_yled.header("🎮 Interactive Controls", color="#8e44ad")

# Two-column layout for controls
col1, col2 = st.columns(2)

with col1:
    # Styled selectbox
    theme = st_yled.selectbox(
        "Choose Color Theme",
        ["Blue", "Green", "Purple", "Orange"],
        background_color="#f8f9fa",
        border_color="#6c757d"
    )

    # Styled slider
    value = st_yled.slider(
        "Adjust Value",
        0, 100, 50,
        color="#e74c3c"
    )

with col2:
    # Styled text input
    user_input = st_yled.text_input(
        "Enter your message",
        placeholder="Type something...",
        border_color="#3498db",
    )

    # Styled checkbox
    enabled = st_yled.checkbox(
        "Enable notifications",
        color="#2ecc71"
    )

# Display results with styling
if user_input:
    st_yled.success(f"✅ You entered: **{user_input}**")

if enabled:
    st_yled.info("🔔 Notifications are enabled")
```

---

## Step 5: Add Custom Components

Enhance your app with pre-built custom components:

```python
st_yled.header("✨ Custom Components", color="#16a085")

# Create columns for component display
comp_col1, comp_col2, comp_col3 = st.columns(3)

with comp_col1:
    # Badge card for featured content
    st_yled.badge_card_one(
        badge_text="New",
        badge_icon=":material/star:",
        title="Featured Item",
        text="Check out our latest feature with enhanced styling",
        background_color="#f8f9fa",
        border_color="#dee2e6",
        border_style="solid",
        border_width=1,
        width=280
    )

with comp_col2:
    # Image card for visual content
    st_yled.image_card_one(
        image_path="https://picsum.photos/300/200",
        title="Sample Project",
        text="Beautiful image cards for portfolios and galleries",
        width=280,
        card_shadow=True,
        title_font_size=18
    )

with comp_col3:
    # Another badge card with different styling
    st_yled.badge_card_one(
        badge_text="Hot",
        badge_icon=":material/local_fire_department:",
        title="Popular Choice",
        text="Most viewed item this week",
        background_color="#fff3cd",
        border_color="#ffc107",
        border_style="solid",
        border_width=2,
        width=280
    )
```

---

## Step 6: Add Global Styling

Apply consistent styling across all components on the page.
Global styled by `st_yled.set` will overwrite styling provided by a css file.

```python

# Initialize st_yled
st_yled.init()

# Global button styling
st_yled.set("button", "border", "none")
st_yled.set("button", "font_size", "20")

# Global text styling
st_yled.set("text", "color", "blue")

# Global container styling
st_yled.set("container", "backgroud_color", "grey")
```

**Global styling benefits:**

- Ensures consistent look across all components

- Easy to change theme by modifying global settings

- Reduces repetitive styling code


## What You've Learned

✅ **Basic st_yled setup** - Initialize and configure styling

✅ **Component styling** - Apply colors, sizes, and spacing

✅ **Global styling** - Set consistent themes across components

✅ **Layout techniques** - Use columns and containers effectively

✅ **Interactive components** - Handle user input with styled widgets

✅ **Sidebar patterns** - Apply custom styling to sidebar components

---

## Next Steps

Ready to explore more advanced features?

- **[Basic Styling Concepts](basic-styling.md)** - Understand CSS properties and validation
- **[Global Styling Guide](global-styling.md)** - Create consistent themes and design systems
- **[Component Reference](../elements/index.md)** - Explore all available styled components
- **[Advanced Examples](../examples/advanced-examples/dashboard-demo.md)** - Build complex applications

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
