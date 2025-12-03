import streamlit as st

from st_yled import styler  # type: ignore
from st_yled import validation  # type: ignore

# ==============================================================================
# Display and Magic Components
# ==============================================================================


def write(*args, **kwargs):
    kwargs = styler.apply_component_css("write", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.write(*args, **kwargs)


def write_stream(*args, **kwargs):
    return st.write_stream(*args, **kwargs)


# ==============================================================================
# Text Elements
# ==============================================================================


def markdown(*args, **kwargs):
    kwargs = styler.apply_component_css("markdown", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.markdown(*args, **kwargs)


def title(*args, **kwargs):
    kwargs = styler.apply_component_css("title", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.title(*args, **kwargs)


def header(*args, **kwargs):
    kwargs = styler.apply_component_css("header", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.header(*args, **kwargs)


def subheader(*args, **kwargs):
    kwargs = styler.apply_component_css("subheader", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.subheader(*args, **kwargs)


def badge(*args, **kwargs):
    return st.badge(*args, **kwargs)


def caption(*args, **kwargs):
    kwargs = styler.apply_component_css("caption", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.caption(*args, **kwargs)


def code(*args, **kwargs):
    kwargs = styler.apply_component_css("code", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.code(*args, **kwargs)


def latex(*args, **kwargs):
    kwargs = styler.apply_component_css("latex", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.latex(*args, **kwargs)


def text(*args, **kwargs):
    kwargs = styler.apply_component_css("text", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.text(*args, **kwargs)


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
    kwargs = styler.apply_component_css("metric", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.metric(*args, **kwargs)


def json(*args, **kwargs):
    kwargs = styler.apply_component_css("json", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.json(*args, **kwargs)


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
    if "type" in kwargs:
        btn_selector = f'button_{kwargs["type"]}'
    else:
        btn_selector = "button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)
    return st.button(*args, **kwargs)


def download_button(*args, **kwargs):
    if "type" in kwargs:
        btn_selector = f'download_button_{kwargs["type"]}'
    else:
        btn_selector = "download_button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)
    return st.download_button(*args, **kwargs)


def link_button(*args, **kwargs):
    if "type" in kwargs:
        btn_selector = f'link_button_{kwargs["type"]}'
    else:
        btn_selector = "link_button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)

    key = kwargs.pop("key", None)
    cont = st.container(key=key)
    return cont.link_button(*args, **kwargs)


def page_link(*args, **kwargs):
    return st.page_link(*args, **kwargs)


def checkbox(*args, **kwargs):
    kwargs = styler.apply_component_css("checkbox", kwargs)
    return st.checkbox(*args, **kwargs)


def color_picker(*args, **kwargs):
    kwargs = styler.apply_component_css("color_picker", kwargs)
    return st.color_picker(*args, **kwargs)


def feedback(*args, **kwargs):
    kwargs = styler.apply_component_css("feedback", kwargs)
    return st.feedback(*args, **kwargs)


def multiselect(*args, **kwargs):
    kwargs = styler.apply_component_css("multiselect", kwargs)
    return st.multiselect(*args, **kwargs)


def pills(*args, **kwargs):
    kwargs = styler.apply_component_css("pills", kwargs)
    return st.pills(*args, **kwargs)


def radio(*args, **kwargs):
    kwargs = styler.apply_component_css("radio", kwargs)
    return st.radio(*args, **kwargs)


def segmented_control(*args, **kwargs):
    kwargs = styler.apply_component_css("segmented_control", kwargs)
    return st.segmented_control(*args, **kwargs)


def selectbox(*args, **kwargs):
    kwargs = styler.apply_component_css("selectbox", kwargs)
    return st.selectbox(*args, **kwargs)


def select_slider(*args, **kwargs):
    kwargs = styler.apply_component_css("select_slider", kwargs)
    return st.select_slider(*args, **kwargs)


def toggle(*args, **kwargs):
    kwargs = styler.apply_component_css("toggle", kwargs)
    return st.toggle(*args, **kwargs)


def number_input(*args, **kwargs):
    kwargs = styler.apply_component_css("number_input", kwargs)
    return st.number_input(*args, **kwargs)


def slider(*args, **kwargs):
    kwargs = styler.apply_component_css("slider", kwargs)
    return st.slider(*args, **kwargs)


def date_input(*args, **kwargs):
    kwargs = styler.apply_component_css("date_input", kwargs)
    return st.date_input(*args, **kwargs)


def time_input(*args, **kwargs):
    kwargs = styler.apply_component_css("time_input", kwargs)
    return st.time_input(*args, **kwargs)


def text_area(*args, **kwargs):
    kwargs = styler.apply_component_css("text_area", kwargs)
    return st.text_area(*args, **kwargs)


def text_input(*args, **kwargs):
    kwargs = styler.apply_component_css("text_input", kwargs)
    return st.text_input(*args, **kwargs)


def chat_input(*args, **kwargs):
    kwargs = styler.apply_component_css("chat_input", kwargs)
    return st.chat_input(*args, **kwargs)


def audio_input(*args, **kwargs):
    kwargs = styler.apply_component_css("audio_input", kwargs)
    return st.audio_input(*args, **kwargs)


def file_uploader(*args, **kwargs):
    kwargs = styler.apply_component_css("file_uploader", kwargs)
    return st.file_uploader(*args, **kwargs)


def camera_input(*args, **kwargs):
    kwargs = styler.apply_component_css("camera_input", kwargs)
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
    kwargs = styler.apply_component_css("container", kwargs)
    return st.container(*args, **kwargs)


def empty(*args, **kwargs):
    return st.empty(*args, **kwargs)


def expander(*args, **kwargs):
    kwargs = styler.apply_component_css("expander", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.expander(*args, **kwargs)


def popover(*args, **kwargs):
    kwargs = styler.apply_component_css("popover", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        # If a valid width is provided, use it; otherwise, default to 'stretch'
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.popover(*args, **kwargs)


def tabs(*args, **kwargs):
    kwargs = styler.apply_component_css("tabs", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.tabs(*args, **kwargs)


def space(*args, **kwargs):
    return st.space(*args, **kwargs)


# ==============================================================================
# Chat Elements
# ==============================================================================


def chat_message(*args, **kwargs):
    kwargs = styler.apply_component_css("chat_message", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.chat_message(*args, **kwargs)


# ==============================================================================
# Status Elements
# ==============================================================================


def progress(*args, **kwargs):
    kwargs = styler.apply_component_css("progress", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.progress(*args, **kwargs)


def spinner(*args, **kwargs):
    return st.spinner(*args, **kwargs)


def status(*args, **kwargs):
    kwargs = styler.apply_component_css("status", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.status(*args, **kwargs)


def toast(*args, **kwargs):
    return st.toast(*args, **kwargs)


def balloons(*args, **kwargs):
    return st.balloons(*args, **kwargs)


def snow(*args, **kwargs):
    return st.snow(*args, **kwargs)


def success(*args, **kwargs):
    kwargs = styler.apply_component_css("success", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.success(*args, **kwargs)


def info(*args, **kwargs):
    kwargs = styler.apply_component_css("info", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.info(*args, **kwargs)


def warning(*args, **kwargs):
    kwargs = styler.apply_component_css("warning", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.warning(*args, **kwargs)


def error(*args, **kwargs):
    kwargs = styler.apply_component_css("error", kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.error(*args, **kwargs)


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
    if "type" in kwargs:
        btn_selector = f'form_submit_button_{kwargs["type"]}'
    else:
        btn_selector = "form_submit_button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)
    key = kwargs.pop("key", None)

    if "width" in kwargs:
        width_value = kwargs["width"]
        if validation.validate_container_width(width_value):
            container_width = width_value
        else:
            container_width = "stretch"  # set default
    else:
        container_width = "stretch"  # set default

    cont = st.container(key=key, width=container_width)
    return cont.form_submit_button(*args, **kwargs)


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
