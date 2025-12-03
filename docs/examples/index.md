# Examples Gallery

Explore practical examples of st_yled in action. From basic styling patterns to complex applications, these examples demonstrate the full capabilities of st_yled for creating beautiful Streamlit applications.

---

## Learning Path

### [🌱 Basic Examples](basic-examples/simple-styling.md)
**Perfect for beginners** - Learn fundamental styling concepts with simple, focused examples.

**What you'll learn:**
- Component styling basics
- Color and typography application
- Simple layout patterns
- Global styling introduction

**Examples included:**

- [Simple Styling](basic-examples/simple-styling.md) - Basic component styling patterns

**Time to complete:** 30-45 minutes

---

### [🚀 Advanced Examples](advanced-examples/dashboard-demo.md)
**For experienced developers** - Complex implementations showcasing advanced st_yled features.

**What you'll learn:**
- Complex layout systems
- Advanced styling patterns
- Performance optimization
- Integration with external libraries

**Examples included:**
- [Dashboard Demo](advanced-examples/dashboard-demo.md) - Professional business dashboard

**Time to complete:** 1-2 hours

---

## Quick Start Examples

### 5-Minute Quick Wins

Get immediate results with these focused examples:

```python
# Styled Button Example
import st_yled

st_yled.init()

# Create professional buttons instantly
st_yled.button(
    "Primary Action",
    background_color="#007bff",
    color="white",
    border_width="2px",
)
```

```python
# Instant Theme Application
st_yled.set("button", "border_radius", "8px")
st_yled.set("text", "color", "#2c3e50")
st_yled.set("container", "background_color", "#f8f9fa")

# All components now use consistent styling
```

```python
# Professional Metrics Display
st_yled.metric(
    "Revenue",
    "$45,678",
    "+22%",
    background_color="white",
    border_left="4px solid #28a745",
    padding="20px",
    border_radius="8px"
)
```

---

## Example Categories

### By Difficulty Level

**🟢 Beginner** (10-30 minutes)
- Component styling basics
- Simple color applications
- Basic layout patterns

**🟡 Intermediate** (30-60 minutes)
- Global styling systems
- Multi-component layouts
- Responsive design basics

**🔴 Advanced** (1-3 hours)
- Complex dashboard layouts
- Custom theming systems
- Performance optimization

### By Application Type

**📊 Dashboards & Analytics**
- Executive dashboards
- KPI monitoring systems
- Data exploration tools
- Real-time monitoring

**📝 Forms & Data Entry**
- User registration forms
- Survey applications
- Data collection interfaces
- Validation systems

**🎨 Content & Presentation**
- Documentation sites
- Portfolio showcases
- Interactive presentations
- Educational content

**🏢 Business Applications**
- CRM interfaces
- Project management tools
- Financial reporting
- HR management systems

---

## Interactive Features

### Live Code Playground

Many examples include interactive code playgrounds where you can:

- **Edit code in real-time** and see results instantly
- **Experiment with styling** by changing parameters
- **Copy code snippets** directly to your projects
- **Download complete examples** as standalone files

---

## Featured Examples

### 🏆 Most Popular

#### [Professional Dashboard](advanced-examples/dashboard-demo.md)
Complete business dashboard with KPIs, charts, and interactive controls.

**Highlights:**
- 15+ styled components
- Responsive grid layout
- Real-time data updates
- Export functionality

**Technologies:** st_yled, Plotly, Pandas

---

## Usage Patterns

### Copy-Paste Ready

All examples are designed for immediate use:

```python
# 1. Copy the import
import st_yled

# 2. Copy the initialization
st_yled.init()

# 3. Copy the styled components
st_yled.button("My Button", background_color="#007bff", color="white")
```

### Modular Components

Examples are built with reusable components:

```python
# Extract reusable patterns
def create_metric_card(label, value, delta, color="#007bff"):
    return st_yled.metric(
        label, value, delta,
        background_color="white",
        border_left=f"4px solid {color}",
        padding="20px",
        border_radius="8px"
    )

# Use throughout your app
create_metric_card("Sales", "$45K", "+12%", "#28a745")
create_metric_card("Users", "1.2K", "+8%", "#007bff")
```

### Progressive Enhancement

Start simple and enhance:

```python
# Step 1: Basic component
st_yled.button("Click me")

# Step 2: Add styling
st_yled.button("Click me", background_color="#007bff")

# Step 3: Full enhancement
st_yled.button(
    "Click me",
    background_color="#007bff",
    color="white",
    border_radius="6px",
    padding="12px 24px",
    transition="all 0.3s ease"
)
```


## Getting Help

### Example-Specific Support

Each example includes:

- **Prerequisites** - What you need to know
- **Step-by-step instructions** - Detailed walkthrough
- **Troubleshooting** - Common issues and solutions
- **Variations** - Ways to customize and extend

### Community Resources

- **[GitHub Discussions](https://github.com/EvobyteDigitalBiology/st-styled/discussions)** - Q&A and feature requests

---

<br>

st_yled with ❤️ from [EVOBYTE](https://www.evo-byte.com)
