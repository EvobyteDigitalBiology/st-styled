import streamlit as st
import styler

# ==============================================================================
# Display and Magic Components
# ==============================================================================

def write(*args, **kwargs):
    return st.write(*args, **kwargs)

def write_stream(*args, **kwargs):
    return st.write_stream(*args, **kwargs)

# ==============================================================================
# Text Elements
# ==============================================================================

def markdown(*args, **kwargs):
    return st.markdown(*args, **kwargs)

def title(*args, **kwargs):
    kwargs = styler.apply_component_css("title", kwargs)
    key = kwargs.pop("key", None)
    cont = st.container(key=key)
    return cont.title(*args, **kwargs)

def header(*args, **kwargs):
    return st.header(*args, **kwargs)

def subheader(*args, **kwargs):
    return st.subheader(*args, **kwargs)

def badge(*args, **kwargs):
    return st.badge(*args, **kwargs)

def caption(*args, **kwargs):
    return st.caption(*args, **kwargs)

def code(*args, **kwargs):
    return st.code(*args, **kwargs)

def latex(*args, **kwargs):
    return st.latex(*args, **kwargs)

def text(*args, **kwargs):
    return st.text(*args, **kwargs)

def divider(*args, **kwargs):
    return st.divider(*args, **kwargs)

def html(*args, **kwargs):
    return st.html(*args, **kwargs)

# ==============================================================================
# Data Elements
# ==============================================================================

def dataframe(*args, **kwargs):
    return st.dataframe(*args, **kwargs)

def data_editor(*args, **kwargs):
    return st.data_editor(*args, **kwargs)

def table(*args, **kwargs):
    kwargs = styler.apply_component_css("table", kwargs)
    key = kwargs.pop("key", None)
    cont = st.container(key=key)
    return cont.table(*args, **kwargs)

def metric(*args, **kwargs):
    return st.metric(*args, **kwargs)

def json(*args, **kwargs):
    return st.json(*args, **kwargs)

# ==============================================================================
# Chart Elements
# ==============================================================================

def area_chart(*args, **kwargs):
    return st.area_chart(*args, **kwargs)

def bar_chart(*args, **kwargs):
    return st.bar_chart(*args, **kwargs)

def line_chart(*args, **kwargs):
    return st.line_chart(*args, **kwargs)

def scatter_chart(*args, **kwargs):
    return st.scatter_chart(*args, **kwargs)

def map(*args, **kwargs):
    return st.map(*args, **kwargs)

def pyplot(*args, **kwargs):
    return st.pyplot(*args, **kwargs)

def altair_chart(*args, **kwargs):
    return st.altair_chart(*args, **kwargs)

def vega_lite_chart(*args, **kwargs):
    return st.vega_lite_chart(*args, **kwargs)

def plotly_chart(*args, **kwargs):
    return st.plotly_chart(*args, **kwargs)

def bokeh_chart(*args, **kwargs):
    return st.bokeh_chart(*args, **kwargs)

def pydeck_chart(*args, **kwargs):
    return st.pydeck_chart(*args, **kwargs)

def graphviz_chart(*args, **kwargs):
    return st.graphviz_chart(*args, **kwargs)

# ==============================================================================
# Input Widgets
# ==============================================================================

def button(*args, **kwargs):
    kwargs = styler.apply_component_css("button", kwargs)
    return st.button(*args, **kwargs)

def download_button(*args, **kwargs):
    kwargs = styler.apply_component_css("download_button", kwargs)
    return st.download_button(*args, **kwargs)

def link_button(*args, **kwargs):
    return st.link_button(*args, **kwargs)

def page_link(*args, **kwargs):
    return st.page_link(*args, **kwargs)

def checkbox(*args, **kwargs):
    return st.checkbox(*args, **kwargs)

def color_picker(*args, **kwargs):
    return st.color_picker(*args, **kwargs)

def feedback(*args, **kwargs):
    return st.feedback(*args, **kwargs)

def multiselect(*args, **kwargs):
    kwargs = styler.apply_component_css("multiselect", kwargs)
    return st.multiselect(*args, **kwargs)

def pills(*args, **kwargs):
    kwargs = styler.apply_component_css("pills", kwargs)
    return st.pills(*args, **kwargs)

def radio(*args, **kwargs):
    return st.radio(*args, **kwargs)

def segmented_control(*args, **kwargs):
    return st.segmented_control(*args, **kwargs)

def selectbox(*args, **kwargs):
    kwargs = styler.apply_component_css("selectbox", kwargs)
    return st.selectbox(*args, **kwargs)

def select_slider(*args, **kwargs):
    return st.select_slider(*args, **kwargs)

def toggle(*args, **kwargs):
    kwargs = styler.apply_component_css("toggle", kwargs)
    return st.toggle(*args, **kwargs)

def number_input(*args, **kwargs):
    kwargs = styler.apply_component_css("number_input", kwargs)
    return st.number_input(*args, **kwargs)

def slider(*args, **kwargs):
    return st.slider(*args, **kwargs)

def date_input(*args, **kwargs):
    return st.date_input(*args, **kwargs)

def time_input(*args, **kwargs):
    return st.time_input(*args, **kwargs)

def text_area(*args, **kwargs):
    kwargs = styler.apply_component_css("text_area", kwargs)
    return st.text_area(*args, **kwargs)

def text_input(*args, **kwargs):
    kwargs = styler.apply_component_css("text_input", kwargs)
    return st.text_input(*args, **kwargs)

def chat_input(*args, **kwargs):
    return st.chat_input(*args, **kwargs)

def audio_input(*args, **kwargs):
    return st.audio_input(*args, **kwargs)

def file_uploader(*args, **kwargs):
    return st.file_uploader(*args, **kwargs)

def camera_input(*args, **kwargs):
    return st.camera_input(*args, **kwargs)

# ==============================================================================
# Media Elements
# ==============================================================================

def image(*args, **kwargs):
    return st.image(*args, **kwargs)

def logo(*args, **kwargs):
    return st.logo(*args, **kwargs)

def pdf(*args, **kwargs):
    return st.pdf(*args, **kwargs)

def audio(*args, **kwargs):
    return st.audio(*args, **kwargs)

def video(*args, **kwargs):
    return st.video(*args, **kwargs)

# ==============================================================================
# Layout and Container Elements
# ==============================================================================

def columns(*args, **kwargs):
    return st.columns(*args, **kwargs)

def container(*args, **kwargs):
    return st.container(*args, **kwargs)

def empty(*args, **kwargs):
    return st.empty(*args, **kwargs)

def expander(*args, **kwargs):
    return st.expander(*args, **kwargs)

def popover(*args, **kwargs):
    return st.popover(*args, **kwargs)

def tabs(*args, **kwargs):
    return st.tabs(*args, **kwargs)

# ==============================================================================
# Chat Elements
# ==============================================================================

def chat_message(*args, **kwargs):
    return st.chat_message(*args, **kwargs)

# ==============================================================================
# Status Elements
# ==============================================================================

def progress(*args, **kwargs):
    return st.progress(*args, **kwargs)

def spinner(*args, **kwargs):
    return st.spinner(*args, **kwargs)

def status(*args, **kwargs):
    return st.status(*args, **kwargs)

def toast(*args, **kwargs):
    return st.toast(*args, **kwargs)

def balloons(*args, **kwargs):
    return st.balloons(*args, **kwargs)

def snow(*args, **kwargs):
    return st.snow(*args, **kwargs)

def success(*args, **kwargs):
    return st.success(*args, **kwargs)

def info(*args, **kwargs):
    return st.info(*args, **kwargs)

def warning(*args, **kwargs):
    return st.warning(*args, **kwargs)

def error(*args, **kwargs):
    return st.error(*args, **kwargs)

def exception(*args, **kwargs):
    return st.exception(*args, **kwargs)

# ==============================================================================
# Execution Flow
# ==============================================================================

def dialog(*args, **kwargs):
    return st.dialog(*args, **kwargs)

def form(*args, **kwargs):
    return st.form(*args, **kwargs)

def form_submit_button(*args, **kwargs):
    return st.form_submit_button(*args, **kwargs)

def rerun(*args, **kwargs):
    return st.rerun(*args, **kwargs)

def stop(*args, **kwargs):
    return st.stop(*args, **kwargs)

# ==============================================================================
# Navigation and Pages
# ==============================================================================

def navigation(*args, **kwargs):
    return st.navigation(*args, **kwargs)

def switch_page(*args, **kwargs):
    return st.switch_page(*args, **kwargs)

# ==============================================================================
# Configuration
# ==============================================================================

def set_page_config(*args, **kwargs):
    return st.set_page_config(*args, **kwargs)

def get_option(*args, **kwargs):
    return st.get_option(*args, **kwargs)

def set_option(*args, **kwargs):
    return st.set_option(*args, **kwargs)

# ==============================================================================
# Utility Functions
# ==============================================================================

def help(*args, **kwargs):
    return st.help(*args, **kwargs)

def echo(*args, **kwargs):
    return st.echo(*args, **kwargs)

