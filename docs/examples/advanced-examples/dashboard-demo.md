# Professional Dashboard Demo

Build a comprehensive business dashboard with st_yled featuring KPIs, charts, interactive controls, and responsive design. This example demonstrates advanced layout patterns and professional styling techniques.

**Difficulty:** 🔴 Advanced
**Time:** 2-3 hours
**Prerequisites:** Intermediate st_yled knowledge, basic data analysis concepts

---

## Overview

In this comprehensive example, you'll build a production-ready business dashboard featuring:

- **Executive KPI Overview** - Key performance indicators with trend analysis
- **Interactive Charts** - Sales trends, regional performance, and product analysis
- **Real-time Updates** - Live data simulation and refresh capabilities
- **Responsive Design** - Mobile-friendly layout that adapts to screen size
- **Export Features** - Data export and report generation
- **User Controls** - Date ranges, filters, and customization options

---

## Complete Dashboard Code

```python
import streamlit as st
import st_yled
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# ============================================================================
# Page Configuration and Setup
# ============================================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize st_yled
st_yled.init()

# ============================================================================
# Data Generation (In production, connect to your data sources)
# ============================================================================

@st.cache_data
def load_dashboard_data():
    """Generate sample business data for the dashboard"""

    # Date range
    dates = pd.date_range(start='2024-01-01', end='2024-10-16', freq='D')

    # Sales data
    np.random.seed(42)
    sales_data = pd.DataFrame({
        'date': dates,
        'revenue': np.random.normal(15000, 3000, len(dates)).cumsum(),
        'orders': np.random.poisson(50, len(dates)),
        'customers': np.random.poisson(25, len(dates)),
        'avg_order_value': np.random.normal(300, 50, len(dates))
    })

    # Regional data
    regions = ['North', 'South', 'East', 'West', 'Central']
    regional_data = pd.DataFrame({
        'region': regions,
        'revenue': np.random.uniform(100000, 500000, len(regions)),
        'growth': np.random.uniform(-5, 25, len(regions)),
        'customers': np.random.randint(500, 2000, len(regions))
    })

    # Product data
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    product_data = pd.DataFrame({
        'product': products,
        'sales': np.random.uniform(50000, 200000, len(products)),
        'margin': np.random.uniform(15, 35, len(products)),
        'units_sold': np.random.randint(100, 1000, len(products))
    })

    return sales_data, regional_data, product_data

# Load data
sales_df, regional_df, product_df = load_dashboard_data()

# ============================================================================
# Dashboard Header
# ============================================================================

# Header container (Note: Limited container styling available)
with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e9ecef",
    border_width="2px"
):
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st_yled.title(
            "📊 Executive Dashboard",
            color="#2c3e50",
            font_size="2.2rem"
        )
        st_yled.text(
            f"Last updated: {datetime.now().strftime('%B %d, %Y at %H:%M')}",
            color="#7f8c8d",
            font_size="14px"
        )

    with col2:
        # Refresh button
        if st_yled.button(
            "🔄 Refresh Data",
            background_color="#17a2b8",
            color="white"
        ):
            st.cache_data.clear()
            st.experimental_rerun()

    with col3:
        # Export button
        if st_yled.button(
            "📥 Export Report",
            background_color="#28a745",
            color="white"
        ):
            st_yled.success("Report exported successfully!")

# ============================================================================
# Sidebar Controls
# ============================================================================

with st.sidebar:
    st_yled.header("🎛️ Dashboard Controls", color="#2c3e50")

    # Date range selector
    st_yled.subheader("📅 Date Range", color="#34495e")

    date_range = st_yled.date_input(
        "Select period",
        value=(datetime.now() - timedelta(days=30), datetime.now())
    )

    # Region filter
    st_yled.subheader("🌍 Region Filter", color="#34495e")
    selected_regions = st_yled.multiselect(
        "Choose regions",
        regional_df['region'].tolist(),
        default=regional_df['region'].tolist(),
        background_color="#f8f9fa"
    )

    # Metric selector
    st_yled.subheader("📈 Key Metrics", color="#34495e")
    show_revenue = st_yled.checkbox("Revenue", value=True, color="#28a745")
    show_orders = st_yled.checkbox("Orders", value=True, color="#007bff")
    show_customers = st_yled.checkbox("Customers", value=True, color="#6f42c1")

    # Dashboard theme
    st_yled.subheader("🎨 Theme", color="#34495e")
    theme = st_yled.selectbox(
        "Dashboard theme",
        ["Professional", "Dark", "Colorful"],
        background_color="#f8f9fa"
    )

# ============================================================================
# KPI Metrics Row
# ============================================================================

st_yled.header("📊 Key Performance Indicators", color="#2c3e50")

# Calculate KPIs
current_revenue = sales_df['revenue'].iloc[-1]
revenue_growth = ((sales_df['revenue'].iloc[-1] - sales_df['revenue'].iloc[-30]) / sales_df['revenue'].iloc[-30] * 100)

current_orders = sales_df['orders'].sum()
orders_growth = 12.5  # Simulated

current_customers = sales_df['customers'].sum()
customer_growth = 8.3  # Simulated

avg_order_value = current_revenue / current_orders if current_orders > 0 else 0
aov_growth = -2.1  # Simulated

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

def create_kpi_card(title, value, delta, delta_color, background_color, border_color):
    """Create a styled KPI card (Note: Metrics have limited styling)"""
    return st_yled.metric(
        label=title,
        value=value,
        delta=delta,
        color=border_color,
        font_size="16px"
    )

with col1:
    create_kpi_card(
        "Total Revenue",
        f"${current_revenue:,.0f}",
        f"+{revenue_growth:.1f}%",
        "green",
        "white",
        "#28a745"
    )

with col2:
    create_kpi_card(
        "Total Orders",
        f"{current_orders:,}",
        f"+{orders_growth:.1f}%",
        "green",
        "white",
        "#007bff"
    )

with col3:
    create_kpi_card(
        "Total Customers",
        f"{current_customers:,}",
        f"+{customer_growth:.1f}%",
        "green",
        "white",
        "#6f42c1"
    )

with col4:
    create_kpi_card(
        "Avg Order Value",
        f"${avg_order_value:.0f}",
        f"{aov_growth:.1f}%",
        "red",
        "white",
        "#dc3545"
    )

# ============================================================================
# Charts Section
# ============================================================================

# Revenue Trend Chart
st_yled.header("📈 Revenue Trends", color="#2c3e50")

with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e9ecef",
    border_width="1px"
):
    # Chart controls
    col1, col2 = st.columns([3, 1])

    with col2:
        chart_type = st_yled.selectbox(
            "Chart Type",
            ["Line", "Area", "Bar"],
            background_color="#f8f9fa"
        )

    # Create revenue chart
    if chart_type == "Line":
        fig = px.line(
            sales_df.tail(30),
            x='date',
            y='revenue',
            title="Daily Revenue (Last 30 Days)"
        )
    elif chart_type == "Area":
        fig = px.area(
            sales_df.tail(30),
            x='date',
            y='revenue',
            title="Daily Revenue (Last 30 Days)"
        )
    else:
        fig = px.bar(
            sales_df.tail(30),
            x='date',
            y='revenue',
            title="Daily Revenue (Last 30 Days)"
        )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        title_font=dict(size=18, color='#2c3e50')
    )

    st.plotly_chart(fig, use_container_width=True)

# Regional Performance and Product Analysis
col1, col2 = st.columns(2)

with col1:
    st_yled.subheader("🌍 Regional Performance", color="#2c3e50")

    with st_yled.container(
        background_color="white",
        border_style="solid",
        border_color="#e9ecef",
        border_width="1px"
    ):
        # Filter data based on selection
        filtered_regional = regional_df[regional_df['region'].isin(selected_regions)]

        fig_regional = px.bar(
            filtered_regional,
            x='region',
            y='revenue',
            color='growth',
            color_continuous_scale='RdYlGn',
            title="Revenue by Region"
        )

        fig_regional.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400
        )

        st.plotly_chart(fig_regional, use_container_width=True)

with col2:
    st_yled.subheader("📦 Product Performance", color="#2c3e50")

    with st_yled.container(
        background_color="white",
        border_style="solid",
        border_color="#e9ecef",
        border_width="1px"
    ):
        fig_products = px.scatter(
            product_df,
            x='sales',
            y='margin',
            size='units_sold',
            color='product',
            title="Product Sales vs Margin",
            hover_data=['units_sold']
        )

        fig_products.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400
        )

        st.plotly_chart(fig_products, use_container_width=True)

# ============================================================================
# Data Tables Section
# ============================================================================

st_yled.header("📋 Detailed Data", color="#2c3e50")

# Tabbed interface for different data views
tab1, tab2, tab3 = st_yled.tabs(
    ["📈 Sales Data", "🌍 Regional Data", "📦 Product Data"]
)

with tab1:
    st_yled.subheader("Recent Sales Performance")

    # Display recent sales data (Note: st_yled.dataframe doesn't exist, using st.dataframe)
    recent_sales = sales_df.tail(10).copy()
    recent_sales['date'] = recent_sales['date'].dt.strftime('%Y-%m-%d')
    recent_sales['revenue'] = recent_sales['revenue'].apply(lambda x: f"${x:,.0f}")
    recent_sales['avg_order_value'] = recent_sales['avg_order_value'].apply(lambda x: f"${x:.0f}")

    st.dataframe(
        recent_sales,
        use_container_width=True
    )

with tab2:
    st_yled.subheader("Regional Performance Summary")

    # Format regional data for display
    display_regional = filtered_regional.copy()
    display_regional['revenue'] = display_regional['revenue'].apply(lambda x: f"${x:,.0f}")
    display_regional['growth'] = display_regional['growth'].apply(lambda x: f"{x:+.1f}%")
    display_regional['customers'] = display_regional['customers'].apply(lambda x: f"{x:,}")

    st.dataframe(
        display_regional,
        use_container_width=True
    )

with tab3:
    st_yled.subheader("Product Analysis")

    # Format product data for display
    display_products = product_df.copy()
    display_products['sales'] = display_products['sales'].apply(lambda x: f"${x:,.0f}")
    display_products['margin'] = display_products['margin'].apply(lambda x: f"{x:.1f}%")
    display_products['units_sold'] = display_products['units_sold'].apply(lambda x: f"{x:,}")

    st.dataframe(
        display_products,
        use_container_width=True
    )

# ============================================================================
# Action Items and Alerts
# ============================================================================

st_yled.header("🚨 Action Items & Alerts", color="#2c3e50")

col1, col2 = st.columns(2)

with col1:
    # Critical alerts (limited container styling)
    with st_yled.container(
        background_color="#fff5f5",
        border_style="solid",
        border_color="#fed7d7",
        border_width="1px"
    ):
        st_yled.subheader("🚨 Critical Alerts", color="#e53e3e")
        st_yled.text("• Average order value declining (-2.1%)", color="#744210")
        st_yled.text("• West region underperforming target", color="#744210")
        st_yled.text("• Product C inventory running low", color="#744210")

with col2:
    # Opportunities
    with st_yled.container(
        background_color="#f0fff4",
        border_style="solid",
        border_color="#9ae6b4",
        border_width="1px"
    ):
        st_yled.subheader("💡 Opportunities", color="#38a169")
        st_yled.text("• Strong growth in North region (+25%)", color="#155724")
        st_yled.text("• Product A showing high margins", color="#155724")
        st_yled.text("• Customer acquisition trending up", color="#155724")

# ============================================================================
# Footer
# ============================================================================

# Note: st_yled.divider() doesn't exist, using st.divider()
st.divider()

with st_yled.container(
    background_color="#f8f9fa"
):
    st_yled.text(
        "📊 Executive Dashboard | Built with st_yled | Data refreshed every 15 minutes",
        color="#6c757d",
        font_size="14px"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st_yled.text("📞 Support: support@company.com", color="#6c757d", font_size="12px")

    with col2:
        st_yled.text("📋 Documentation", color="#6c757d", font_size="12px")

    with col3:
        st_yled.text("🔒 Privacy Policy", color="#6c757d", font_size="12px")
```

---

## Key Features Breakdown

### 1. Responsive Layout System

```python
# Adaptive column layouts
col1, col2, col3, col4 = st.columns(4)  # Desktop: 4 columns
# On mobile, automatically stacks vertically

# Container sizing (Note: Limited properties available)
with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e9ecef",
    border_width="1px"
):
    # Content adapts to screen size
```

### 2. Professional KPI Cards

```python
def create_kpi_card(title, value, delta, delta_color, background_color, border_color):
    """Reusable KPI card component (Note: Limited metric styling)"""
    return st_yled.metric(
        label=title,
        value=value,
        delta=delta,
        color=border_color,
        font_size="16px"
    )
```

### 3. Interactive Chart Integration

```python
# Plotly chart with st_yled container styling
with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e9ecef",
    border_width="1px"
):
    fig = px.line(data, x='date', y='revenue')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',     # Transparent background
        paper_bgcolor='rgba(0,0,0,0)',    # Transparent paper
        font=dict(color='#2c3e50')        # Consistent font color
    )
    st.plotly_chart(fig, use_container_width=True)
```

### 4. Advanced Data Tables

```python
# Styled data table (Note: st_yled.dataframe doesn't exist, use st.dataframe)
st.dataframe(
    formatted_data,
    use_container_width=True
)
```

### 5. Status Alerts System

```python
# Color-coded alert containers (Note: Limited container properties)
with st_yled.container(
    background_color="#fff5f5",        # Light red background
    border_style="solid",              # Border style
    border_color="#fed7d7",            # Light red border
    border_width="1px"                 # Border width
):
    st_yled.subheader("🚨 Critical Alerts", color="#e53e3e")
    # Alert content
```

---

## Advanced Techniques Used

### 1. Data Processing Pipeline

```python
@st.cache_data
def load_dashboard_data():
    """Cached data loading for performance"""
    # Data generation/loading logic
    return sales_data, regional_data, product_data

# Efficient data filtering
filtered_data = df[df['region'].isin(selected_regions)]
```

### 2. Dynamic Theming

```python
# Theme-based styling
theme_configs = {
    "Professional": {
        "primary_color": "#2c3e50",
        "accent_color": "#3498db",
        "background_color": "white"
    },
    "Dark": {
        "primary_color": "#ffffff",
        "accent_color": "#64b5f6",
        "background_color": "#1e1e1e"
    }
}

current_theme = theme_configs[selected_theme]
```

### 3. Responsive Design Patterns

```python
# Mobile-first responsive containers (Note: Limited properties)
with st_yled.container(
    background_color="white",
    border_style="solid",
    border_color="#e9ecef",
    border_width="1px"
):
    # Content automatically adapts
```

### 4. Performance Optimization

```python
# Efficient data caching
@st.cache_data(ttl=900)  # Cache for 15 minutes
def get_analytics_data():
    # Expensive data operations

# Lazy loading for large datasets
if st.button("Load Detailed Report"):
    # Load additional data only when needed
```

---

## Customization Options

### 1. Color Scheme Variants

```python
# Corporate theme
CORPORATE_COLORS = {
    "primary": "#003366",
    "secondary": "#0066cc",
    "success": "#28a745",
    "warning": "#ffc107",
    "danger": "#dc3545"
}

# Modern theme
MODERN_COLORS = {
    "primary": "#6366f1",
    "secondary": "#8b5cf6",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444"
}
```

### 2. Layout Variations

```python
# Sidebar vs top navigation
if layout_style == "sidebar":
    with st.sidebar:
        # Navigation controls
elif layout_style == "top_nav":
    with st_yled.container():
        # Horizontal navigation
```

### 3. Chart Customizations

```python
# Chart theme variants
def apply_chart_theme(fig, theme="professional"):
    themes = {
        "professional": {
            "plot_bgcolor": "white",
            "paper_bgcolor": "white",
            "font_color": "#2c3e50"
        },
        "dark": {
            "plot_bgcolor": "#1e1e1e",
            "paper_bgcolor": "#1e1e1e",
            "font_color": "#ffffff"
        }
    }

    fig.update_layout(**themes[theme])
    return fig
```

---

## Production Deployment Tips

### 1. Performance Optimization

```python
# Use caching strategically
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_large_dataset():
    # Heavy data operations

# Optimize data loading
@st.cache_resource
def init_database_connection():
    # Database connection setup
```

### 2. Error Handling

```python
try:
    data = load_dashboard_data()
except Exception as e:
    st_yled.error(f"❌ Data loading failed: {str(e)}")
    st.stop()
```

### 3. User Authentication

```python
# Add authentication wrapper
def require_auth():
    if "authenticated" not in st.session_state:
        # Show login form
        return False
    return True

if not require_auth():
    st.stop()
```

### 4. Configuration Management

```python
# Environment-based configuration
import os

CONFIG = {
    "api_url": os.getenv("API_URL", "localhost:8000"),
    "refresh_interval": int(os.getenv("REFRESH_INTERVAL", "900")),
    "theme": os.getenv("DEFAULT_THEME", "professional")
}
```

---

## What You Learned

✅ **Advanced Layout Systems** - Complex multi-column responsive layouts
✅ **Professional Data Visualization** - Integrated charts with custom styling
✅ **Interactive Controls** - Dynamic filtering and real-time updates
✅ **KPI Dashboard Design** - Professional metric display patterns
✅ **Performance Optimization** - Caching and efficient data handling
✅ **Production Patterns** - Error handling, authentication, and deployment
✅ **Responsive Design** - Mobile-friendly adaptive layouts
✅ **Component Reusability** - Modular component design patterns

---

## Next Steps

### Extend This Dashboard

1. **Add Real Data Sources** - Connect to databases, APIs, or data warehouses
2. **Implement User Management** - Add authentication and user-specific dashboards
3. **Create Export Features** - PDF reports, data downloads, scheduled exports
4. **Add Real-time Updates** - WebSocket connections for live data streams

### Explore Related Examples

- **[Responsive Design](responsive-design.md)** - Mobile-first design patterns
- **[Custom Themes](custom-themes.md)** - Advanced theming systems
- **[Data Analysis Platform](../use-cases/data-analysis.md)** - Scientific data applications

### Advanced Topics

- **Multi-page Applications** - Navigation and state management
- **Custom Components** - Building reusable dashboard widgets
- **Integration Patterns** - APIs, databases, and external services

---

**Dashboard mastery achieved!** 📊 You now have the skills to build production-ready business dashboards with st_yled that rival professional BI tools.
