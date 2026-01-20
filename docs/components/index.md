# New Components

st_yled provides a collection of components that extend Streamlit's functionality with pre-built UI patterns and advanced interactions.

## Component Categories

### [🃏 Card Components](cards.md)
Beautiful card components for displaying content in organized, visually appealing containers.

**Available Components:**

- [Badge Card One](cards.md#badge-card-one) - Cards with customizable badges

- [Image Card One](cards.md#image-card-one) - Image-focused card layouts

---

### [📐 Layout Components](layout.md)
Advanced layout components for better page structure and navigation.

**Available Components:**

- [Sticky Header](layout.md#sticky-header) - Fixed headers that stay visible while scrolling

---

### [🧭 Navigation Components](navigation.md)
Components for controlling navigation and routing in your application.

**Available Components:**

- [Redirect](navigation.md#redirect) - Programmatic URL redirection

---

### [🎛️ Input Components](input.md)
Enhanced input components with advanced functionality.

**Available Components:**

- [Split Button](input.md#split-button) - Buttons with dropdown action menus

---

## Using Custom Components

All custom components are accessible through the `st_yled` namespace:

```python
import st_yled

# Initialize st_yled
st_yled.init()

# Use custom components
st_yled.badge_card_one(
    badge_text="New",
    title="Featured Item",
    text="Check out this amazing feature"
)
```

## Installation

Custom components are included with st_yled. No additional installation required:

```bash
pip install st-styled
```

---

## Next Steps

- Explore component categories above
- Check out [Basic Examples](../examples/basic-examples/simple-styling.md)
- Learn about [Element Styling](../elements/index.md)

---

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
