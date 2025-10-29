# Installation & Setup

Get st_yled up and running in your Streamlit application in just a few minutes.

---

## Prerequisites

- **Python 3.10+** - st_yled requires modern Python features
- **Streamlit 1.42+** - Latest Streamlit version for optimal compatibility
---

## Installation



### Option 1: Install from PyPI (Recommended)

```bash
pip install st-styled
```

### Option 3: Pip install from GitHub

```bash
pip install git+https://github.com/EvobyteDigitalBiology/st-styled
```

### Option 3: Install from source

```bash
# Clone the repository
git clone https://github.com/EvobyteDigitalBiology/st-styled.git
cd st-styled

# Install in development mode
pip install -e .
```

---

## Verify Installation

Create a simple test file to verify st_yled is working correctly:

```python
# test_installation.py
import streamlit as st
import st_yled

st.title("Testing st_yled Installation")

# Initialize st_yled
st_yled.init()

# Test basic functionality
st_yled.success("✅ st_yled is working correctly!")
st_yled.button("Test Button", background_color="#4CAF50", color="white")
```

Run the test:

```bash
streamlit run test_installation.py
```

If you see a green success message and a styled button, st_yled is installed correctly!

---

## Project Structure Setup

For best results, organize your Streamlit project with st_yled support:

```
your-streamlit-app/
├── .streamlit/
│   ├── config.toml          # Streamlit configuration (recommendend)
│   └── st-styled.css        # Your custom CSS (optional)
├── pages/                   # Multi-page app pages
├── requirements.txt         # Python dependencies
├── main.py                 # Main Streamlit app
└── ...                     # Additional folders, files, ...
```

---

## CSS File Setup (Optional)

The easiest way to define custom css for Streamlit is using st_yled studio, our free app to try and optimize your style and layout.

Here is the [link to st_yled studio](https://styled-studio.streamlit.app/).

st_yled will by default load CSS defined in `.streamlit/st-styled.css` once the `st_yled.init()` function is called.

You can adapt the path of the default css file by providing the path argument `st_yled.init('path/to/custom.css')`

```css
/* .streamlit/st-styled.css */

/* Global app styling */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Custom button styles */
.stButton > button {
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
```

---

## Troubleshooting

### Common Issues

**Styling not applied to multipage app**

- Make sure `st_yled.init()` is run in each app page.

- `st_yled.set()` must be run on each page where global styling should be applied.

**CSS not loading**

- Verify CSS file path: `.streamlit/st-styled.css`

- Try manual CSS loading: `st_yled.init(css_path="path/to/your.css")`

**ImportError: No module named 'st_yled'**

- Ensure st_yled is installed: `pip list | grep st-styled`

- Check you're using the correct Python environment

**Components not styling**

- Ensure `st_yled.init()` when using custom css from st_yled Studio

- Check if other css sources are used in your project, which may cause inconsistencies.

### Getting Help

- **GitHub Issues**: [Report bugs and request features](https://github.com/EvobyteDigitalBiology/st-styled/issues)
- **Documentation**: [Complete API reference](../api/index.md)
- **Examples**: [Working code examples](../examples/index.md)

---

## Next Steps

Now that st_yled is installed:

1. **[Create your first app](first-app.md)** - Build a simple styled application
2. **[Learn basic styling](basic-styling.md)** - Understand component styling fundamentals
3. **[Explore global styling](global-styling.md)** - Apply consistent themes across your app

---

**Installation complete!** 🎉 Ready to build beautiful Streamlit apps with st_yled.

<br>
<br>

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
