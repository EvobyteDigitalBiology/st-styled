# Component Showcase

Explore additional custom component examples demonstrating advanced use cases and interaction patterns.

---

## Split Button Component

The split button component is perfect for actions with multiple options, combining a primary action with related variations.

### Example: Document Export Options

```python
import streamlit as st
import st_yled

st_yled.init()

st_yled.header("📄 Document Actions")

# Split button for export options
export_action = st_yled.split_button(
    label="Export Report",
    options=["Export as PDF", "Export as CSV", "Export as Excel", "Export as JSON"],
    icon=":material/download:",
    background_color="#3498db",
    color="#ffffff",
    radius="8px",
    key="export-split"
)

if export_action:
    st.success(f"✅ Exporting document: {export_action}")

# Split button for save variations
save_action = st_yled.split_button(
    label="Save",
    options=["Save Draft", "Save & Continue", "Save & Close", "Save & New"],
    icon=":material/save:",
    background_color="#27ae60",
    color="#ffffff",
    radius="8px",
    key="save-split"
)

if save_action:
    st.info(f"💾 Action selected: {save_action}")
```

### Use Cases for Split Buttons

**Export Functionality:**
```python
export = st_yled.split_button(
    label="Download",
    options=["PDF", "Excel", "CSV", "JSON"],
    icon=":material/file_download:",
    background_color="#3498db"
)
```

**Save Workflows:**
```python
save = st_yled.split_button(
    label="Save",
    options=["Save", "Save & Close", "Save as Draft"],
    icon=":material/save:",
    background_color="#27ae60"
)
```

**Bulk Actions:**
```python
action = st_yled.split_button(
    label="Actions",
    options=["Delete Selected", "Archive Selected", "Export Selected"],
    icon=":material/more_vert:",
    background_color="#95a5a6"
)
```

---

## Navigation with Redirect

The redirect component enables programmatic navigation to internal pages or external URLs.

### Example: Authentication Flow

```python
import streamlit as st
import st_yled

st_yled.init()

st_yled.title("🔐 User Authentication")

# Login form
with st.form("login_form"):
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    remember = st.checkbox("Remember me")

    submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        if username == "demo" and password == "demo":
            st.success("✅ Login successful! Redirecting to dashboard...")
            # Redirect to dashboard after successful login
            st_yled.redirect("https://example.com/dashboard")
        else:
            st.error("❌ Invalid credentials. Please try again.")

st.divider()

# Quick actions with redirect
st_yled.subheader("Quick Access")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📚 Documentation", use_container_width=True):
        st_yled.redirect("https://st-styled.evo-byte.com/")

with col2:
    if st.button("🎨 Studio", use_container_width=True):
        st_yled.redirect("https://styled-studio.streamlit.app/")

with col3:
    if st.button("💬 Support", use_container_width=True):
        st_yled.redirect("https://www.evo-byte.com")
```

### Use Cases for Redirect

**Post-Form Submission:**
```python
with st.form("registration"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submit = st.form_submit_button("Register")

    if submit:
        # Process registration
        st.success("Registration complete!")
        st_yled.redirect("/welcome")
```

**Conditional Navigation:**
```python
if not st.session_state.get('authenticated'):
    st.warning("Please login to continue")
    if st.button("Go to Login"):
        st_yled.redirect("/login")
```

**External Links:**
```python
col1, col2 = st.columns(2)
with col1:
    if st.button("View on GitHub"):
        st_yled.redirect("https://github.com/your-repo")

with col2:
    if st.button("Read Blog Post"):
        st_yled.redirect("https://blog.example.com/post")
```

---

## Advanced Component Combinations

### Example: Action Panel with Multiple Components

Combine different components for rich interaction patterns:

```python
import streamlit as st
import st_yled

st_yled.init()

st_yled.header("📊 Project Management Panel")

# Status card with badge
col1, col2, col3 = st.columns(3)

with col1:
    st_yled.badge_card_one(
        badge_text="Active",
        badge_icon=":material/check_circle:",
        title="Project Alpha",
        text="On track - 75% complete",
        background_color="#d4edda",
        border_color="#28a745",
        border_style="solid",
        border_width=2,
        width=300
    )

with col2:
    st_yled.badge_card_one(
        badge_text="Delayed",
        badge_icon=":material/warning:",
        title="Project Beta",
        text="Behind schedule - needs review",
        background_color="#fff3cd",
        border_color="#ffc107",
        border_style="solid",
        border_width=2,
        width=300
    )

with col3:
    st_yled.badge_card_one(
        badge_text="Planning",
        badge_icon=":material/pending:",
        title="Project Gamma",
        text="Requirements gathering phase",
        background_color="#cfe2ff",
        border_color="#0d6efd",
        border_style="solid",
        border_width=2,
        width=300
    )

st.divider()

# Action buttons
st_yled.subheader("Actions")

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:
    export = st_yled.split_button(
        label="Export",
        options=["Export All", "Export Active", "Export Reports"],
        icon=":material/download:",
        background_color="#3498db",
        color="#ffffff"
    )
    if export:
        st.info(f"Exporting: {export}")

with action_col2:
    project = st_yled.split_button(
        label="New Project",
        options=["Quick Start", "From Template", "Import Existing"],
        icon=":material/add:",
        background_color="#27ae60",
        color="#ffffff"
    )
    if project:
        st.success(f"Creating: {project}")

with action_col3:
    if st.button("View All Projects", use_container_width=True):
        st_yled.redirect("/projects")
```

### Example: E-commerce Product Actions

```python
import streamlit as st
import st_yled

st_yled.init()

# Product display with image card
st_yled.image_card_one(
    image_path="https://picsum.photos/600/400?random=10",
    title="Premium Wireless Headphones",
    text="High-fidelity audio with active noise cancellation. 30-hour battery life.",
    width=600,
    card_shadow=True,
    title_font_size=24
)

# Product actions
col1, col2, col3 = st.columns(3)

with col1:
    quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)

with col2:
    color = st.selectbox("Color", ["Black", "White", "Blue"])

with col3:
    size = st.selectbox("Size", ["Standard", "Large"])

# Split button for purchase options
purchase = st_yled.split_button(
    label="Add to Cart",
    options=["Add to Cart", "Buy Now", "Add to Wishlist", "Compare"],
    icon=":material/shopping_cart:",
    background_color="#ff6b6b",
    color="#ffffff",
    radius="8px"
)

if purchase == "Buy Now":
    st.success("Proceeding to checkout...")
    st_yled.redirect("/checkout")
elif purchase == "Add to Cart":
    st.success(f"Added {quantity} item(s) to cart")
elif purchase == "Add to Wishlist":
    st.info("Added to wishlist")
elif purchase == "Compare":
    st_yled.redirect("/compare")
```

---

## Component Best Practices

### Split Button Guidelines
- **Limit options to 3-7 items** - Too many options overwhelm users
- **Use clear action verbs** - "Export as PDF" vs. just "PDF"
- **Group related actions** - Export options together, save options together
- **Match colors to intent** - Blue for information, green for success, red for destructive actions

### Redirect Usage Tips
- **Provide user feedback** - Show a message before redirecting
- **Use for external links** - When linking to documentation, support, or external resources
- **Conditional navigation** - Check authentication, form validity, or state before redirecting
- **Avoid unexpected redirects** - Always trigger via user action (button click, form submission)

### Component Layout Tips
- **Use consistent widths** - Cards in the same row should have matching widths
- **Maintain spacing** - Use `st.divider()` or spacing columns between sections
- **Consider mobile** - Test component layouts on different screen sizes
- **Combine thoughtfully** - Don't overcrowd - give components breathing room

---

## Next Steps

Continue exploring st_yled:

- **[Component Reference](../components/index.md)** - Full component documentation
- **[Getting Started: Components](../getting-started/component-examples.md)** - Basic component examples
- **[Elements Reference](../elements/index.md)** - Explore styled elements
- **[Advanced Examples](advanced-examples/dashboard-demo.md)** - Complex applications

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
