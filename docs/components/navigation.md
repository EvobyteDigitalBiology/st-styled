# Navigation Components

Components for controlling navigation and routing in your Streamlit applications.

---

## Redirect

Programmatically redirect to a new URL through code.

![Redirect](https://evo-byte.com/wp-content/uploads/2026/01/redirect_logo.png)

### Description

Redirect to a new URL through code, enabling dynamic navigation based on user actions or application logic.

### Usage Pattern

Use this component when you need to programmatically redirect users to another page or external URL. Ideal for post-authentication flows, conditional navigation, redirecting after form submissions, or linking to external resources based on user actions.

### Basic Example

```python
import st_yled

st_yled.init()

# Simple redirect
st_yled.redirect("https://redirect-url.com")

# Conditional redirect
if st.button("Go to Dashboard"):
    st_yled.redirect("https://example.com/dashboard")

# Post-form submission redirect
with st.form("my_form"):
    name = st.text_input("Name")
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Process form data
        st.success(f"Welcome {name}!")
        # Redirect after 2 seconds
        st_yled.redirect("https://example.com/welcome")
```

### Quick Start

```python
st_yled.redirect("https://redirect-url.com")
```

### Parameters

- `url` (str): The URL to redirect to (must be a valid HTTP or HTTPS URL)

### Usage Notes

- The redirect happens immediately when the function is called
- Redirects work with both internal Streamlit pages and external URLs
- Use with conditional logic to control when redirection occurs
- Consider user experience - add messaging before redirecting

---

## Next Steps

Explore more component categories:

- **[Card Components](cards.md)** - Beautiful card layouts
- **[Layout Components](layout.md)** - Advanced layout controls
- **[Input Components](input.md)** - Enhanced input controls

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
