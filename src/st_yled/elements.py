import streamlit as st

from st_yled import styler  # type: ignore
from st_yled import validation  # type: ignore
from st_yled import constants  # type: ignore

# ==============================================================================
# Display and Magic Components
# ==============================================================================


def apply_docstring(func: object, st_func: object, component_name: str) -> None:
    """Apply enhanced docstring with stylable properties to a function.

    Args:
        func: The function to apply the docstring to.
        st_func: The Streamlit function to copy docstring from.
        component_name: The component name for retrieving CSS properties.
    """
    orig_docstring = st_func.__doc__ or ""
    css_properties = constants.ELEMENT_STYLES.get(component_name, {}).get("css", {})
    property_names = sorted(css_properties.keys())

    # Split docstring into sections
    sections = orig_docstring.split("\n        Examples")

    # Build enhanced docstring with stylable properties
    property_names = [f"        - {prop}" for prop in property_names]
    stylable_props = "\n\n".join(property_names) if property_names else "None"
    stylable_section = "\n\n        Stylable Properties:"

    enhanced_docstring = "\n\n".join(
        [sections[0], stylable_section, stylable_props] + sections[1:]
    )
    func.__doc__ = enhanced_docstring


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


apply_docstring(write, st.write, "write")


def write_stream(*args, **kwargs):
    return st.write_stream(*args, **kwargs)


apply_docstring(write_stream, st.write_stream, "write_stream")

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


apply_docstring(markdown, st.markdown, "markdown")


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


apply_docstring(title, st.title, "title")


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


apply_docstring(header, st.header, "header")


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


apply_docstring(subheader, st.subheader, "subheader")


def badge(*args, **kwargs):
    return st.badge(*args, **kwargs)


apply_docstring(badge, st.badge, "badge")


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


apply_docstring(caption, st.caption, "caption")


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


apply_docstring(code, st.code, "code")


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


apply_docstring(latex, st.latex, "latex")


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


apply_docstring(text, st.text, "text")


def divider(*args, **kwargs):
    return st.divider(*args, **kwargs)


apply_docstring(divider, st.divider, "divider")


def html(*args, **kwargs):
    return st.html(*args, **kwargs)


apply_docstring(html, st.html, "html")


# ==============================================================================
# Data Elements
# ==============================================================================


def dataframe(*args, **kwargs):
    return st.dataframe(*args, **kwargs)


apply_docstring(dataframe, st.dataframe, "dataframe")


def data_editor(*args, **kwargs):
    return st.data_editor(*args, **kwargs)


apply_docstring(data_editor, st.data_editor, "data_editor")


def table(*args, **kwargs):
    kwargs = styler.apply_component_css("table", kwargs)
    key = kwargs.pop("key", None)
    cont = st.container(key=key)
    return cont.table(*args, **kwargs)


apply_docstring(table, st.table, "table")


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


apply_docstring(metric, st.metric, "metric")


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


apply_docstring(json, st.json, "json")


# ==============================================================================
# Chart Elements
# ==============================================================================


def area_chart(*args, **kwargs):
    return st.area_chart(*args, **kwargs)


apply_docstring(area_chart, st.area_chart, "area_chart")


def bar_chart(*args, **kwargs):
    return st.bar_chart(*args, **kwargs)


apply_docstring(bar_chart, st.bar_chart, "bar_chart")


def line_chart(*args, **kwargs):
    return st.line_chart(*args, **kwargs)


apply_docstring(line_chart, st.line_chart, "line_chart")


def scatter_chart(*args, **kwargs):
    return st.scatter_chart(*args, **kwargs)


apply_docstring(scatter_chart, st.scatter_chart, "scatter_chart")


def map(*args, **kwargs):
    return st.map(*args, **kwargs)


apply_docstring(map, st.map, "map")


def pyplot(*args, **kwargs):
    return st.pyplot(*args, **kwargs)


apply_docstring(pyplot, st.pyplot, "pyplot")


def altair_chart(*args, **kwargs):
    return st.altair_chart(*args, **kwargs)


apply_docstring(altair_chart, st.altair_chart, "altair_chart")


def vega_lite_chart(*args, **kwargs):
    return st.vega_lite_chart(*args, **kwargs)


apply_docstring(vega_lite_chart, st.vega_lite_chart, "vega_lite_chart")


def plotly_chart(*args, **kwargs):
    return st.plotly_chart(*args, **kwargs)


apply_docstring(plotly_chart, st.plotly_chart, "plotly_chart")


def bokeh_chart(*args, **kwargs):
    return st.bokeh_chart(*args, **kwargs)


apply_docstring(bokeh_chart, st.bokeh_chart, "bokeh_chart")


def pydeck_chart(*args, **kwargs):
    return st.pydeck_chart(*args, **kwargs)


apply_docstring(pydeck_chart, st.pydeck_chart, "pydeck_chart")


def graphviz_chart(*args, **kwargs):
    return st.graphviz_chart(*args, **kwargs)


apply_docstring(graphviz_chart, st.graphviz_chart, "graphviz_chart")


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


apply_docstring(button, st.button, "button")


def menu_button(*args, **kwargs):
    if "type" in kwargs:
        btn_selector = f'menu_button_{kwargs["type"]}'
    else:
        btn_selector = "menu_button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)
    return st.menu_button(*args, **kwargs)


apply_docstring(menu_button, st.menu_button, "menu_button")


def download_button(*args, **kwargs):
    if "type" in kwargs:
        btn_selector = f'download_button_{kwargs["type"]}'
    else:
        btn_selector = "download_button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)
    return st.download_button(*args, **kwargs)


apply_docstring(download_button, st.download_button, "download_button")


def link_button(*args, **kwargs):
    if "type" in kwargs:
        btn_selector = f'link_button_{kwargs["type"]}'
    else:
        btn_selector = "link_button"

    kwargs = styler.apply_component_css(btn_selector, kwargs)

    key = kwargs.pop("key", None)
    cont = st.container(key=key)
    return cont.link_button(*args, **kwargs)


apply_docstring(link_button, st.link_button, "link_button")


def page_link(*args, **kwargs):
    return st.page_link(*args, **kwargs)


apply_docstring(page_link, st.page_link, "page_link")


def checkbox(*args, **kwargs):
    kwargs = styler.apply_component_css("checkbox", kwargs)
    return st.checkbox(*args, **kwargs)


apply_docstring(checkbox, st.checkbox, "checkbox")


def color_picker(*args, **kwargs):
    kwargs = styler.apply_component_css("color_picker", kwargs)
    return st.color_picker(*args, **kwargs)


apply_docstring(color_picker, st.color_picker, "color_picker")


def feedback(*args, **kwargs):
    kwargs = styler.apply_component_css("feedback", kwargs)
    return st.feedback(*args, **kwargs)


apply_docstring(feedback, st.feedback, "feedback")


def multiselect(*args, **kwargs):
    kwargs = styler.apply_component_css("multiselect", kwargs)
    return st.multiselect(*args, **kwargs)


apply_docstring(multiselect, st.multiselect, "multiselect")


def pills(*args, **kwargs):
    kwargs = styler.apply_component_css("pills", kwargs)
    return st.pills(*args, **kwargs)


apply_docstring(pills, st.pills, "pills")


def radio(*args, **kwargs):
    kwargs = styler.apply_component_css("radio", kwargs)
    return st.radio(*args, **kwargs)


apply_docstring(radio, st.radio, "radio")


def segmented_control(*args, **kwargs):
    kwargs = styler.apply_component_css("segmented_control", kwargs)
    return st.segmented_control(*args, **kwargs)


apply_docstring(segmented_control, st.segmented_control, "segmented_control")


def selectbox(*args, **kwargs):
    kwargs = styler.apply_component_css("selectbox", kwargs)
    return st.selectbox(*args, **kwargs)


apply_docstring(selectbox, st.selectbox, "selectbox")


def select_slider(*args, **kwargs):
    kwargs = styler.apply_component_css("select_slider", kwargs)
    return st.select_slider(*args, **kwargs)


apply_docstring(select_slider, st.select_slider, "select_slider")


def toggle(*args, **kwargs):
    kwargs = styler.apply_component_css("toggle", kwargs)
    return st.toggle(*args, **kwargs)


apply_docstring(toggle, st.toggle, "toggle")


def number_input(*args, **kwargs):
    kwargs = styler.apply_component_css("number_input", kwargs)
    return st.number_input(*args, **kwargs)


apply_docstring(number_input, st.number_input, "number_input")


def slider(*args, **kwargs):
    kwargs = styler.apply_component_css("slider", kwargs)
    return st.slider(*args, **kwargs)


apply_docstring(slider, st.slider, "slider")


def date_input(*args, **kwargs):
    kwargs = styler.apply_component_css("date_input", kwargs)
    return st.date_input(*args, **kwargs)


apply_docstring(date_input, st.date_input, "date_input")


def time_input(*args, **kwargs):
    kwargs = styler.apply_component_css("time_input", kwargs)
    return st.time_input(*args, **kwargs)


apply_docstring(time_input, st.time_input, "time_input")


def datetime_input(*args, **kwargs):
    kwargs = styler.apply_component_css("datetime_input", kwargs)
    return st.datetime_input(*args, **kwargs)


apply_docstring(datetime_input, st.datetime_input, "datetime_input")


def text_area(*args, **kwargs):
    kwargs = styler.apply_component_css("text_area", kwargs)
    return st.text_area(*args, **kwargs)


apply_docstring(text_area, st.text_area, "text_area")


def text_input(*args, **kwargs):
    kwargs = styler.apply_component_css("text_input", kwargs)
    return st.text_input(*args, **kwargs)


apply_docstring(text_input, st.text_input, "text_input")


def chat_input(*args, **kwargs):
    kwargs = styler.apply_component_css("chat_input", kwargs)
    return st.chat_input(*args, **kwargs)


apply_docstring(chat_input, st.chat_input, "chat_input")


def audio_input(*args, **kwargs):
    kwargs = styler.apply_component_css("audio_input", kwargs)
    return st.audio_input(*args, **kwargs)


apply_docstring(audio_input, st.audio_input, "audio_input")


def file_uploader(*args, **kwargs):
    kwargs = styler.apply_component_css("file_uploader", kwargs)
    return st.file_uploader(*args, **kwargs)


apply_docstring(file_uploader, st.file_uploader, "file_uploader")


def camera_input(*args, **kwargs):
    kwargs = styler.apply_component_css("camera_input", kwargs)
    return st.camera_input(*args, **kwargs)


apply_docstring(camera_input, st.camera_input, "camera_input")


# ==============================================================================
# Media Elements
# ==============================================================================


def image(*args, **kwargs):
    return st.image(*args, **kwargs)


apply_docstring(image, st.image, "image")


def logo(*args, **kwargs):
    return st.logo(*args, **kwargs)


apply_docstring(logo, st.logo, "logo")


def pdf(*args, **kwargs):
    return st.pdf(*args, **kwargs)


apply_docstring(pdf, st.pdf, "pdf")


def audio(*args, **kwargs):
    return st.audio(*args, **kwargs)


apply_docstring(audio, st.audio, "audio")


def video(*args, **kwargs):
    return st.video(*args, **kwargs)


apply_docstring(video, st.video, "video")


# ==============================================================================
# Layout and Container Elements
# ==============================================================================


def columns(*args, **kwargs):
    return st.columns(*args, **kwargs)


apply_docstring(columns, st.columns, "columns")


def container(*args, **kwargs):
    kwargs = styler.apply_component_css("container", kwargs)
    return st.container(*args, **kwargs)


apply_docstring(container, st.container, "container")


def empty(*args, **kwargs):
    return st.empty(*args, **kwargs)


apply_docstring(empty, st.empty, "empty")


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


apply_docstring(expander, st.expander, "expander")


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


apply_docstring(popover, st.popover, "popover")


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


apply_docstring(tabs, st.tabs, "tabs")


def space(*args, **kwargs):
    return st.space(*args, **kwargs)


apply_docstring(space, st.space, "space")


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


apply_docstring(chat_message, st.chat_message, "chat_message")


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


apply_docstring(progress, st.progress, "progress")


def spinner(*args, **kwargs):
    return st.spinner(*args, **kwargs)


apply_docstring(spinner, st.spinner, "spinner")


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


apply_docstring(status, st.status, "status")


def toast(*args, **kwargs):
    return st.toast(*args, **kwargs)


apply_docstring(toast, st.toast, "toast")


def balloons(*args, **kwargs):
    return st.balloons(*args, **kwargs)


apply_docstring(balloons, st.balloons, "balloons")


def snow(*args, **kwargs):
    return st.snow(*args, **kwargs)


apply_docstring(snow, st.snow, "snow")


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


apply_docstring(success, st.success, "success")


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


apply_docstring(info, st.info, "info")


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


apply_docstring(warning, st.warning, "warning")


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


apply_docstring(error, st.error, "error")


def exception(*args, **kwargs):
    return st.exception(*args, **kwargs)


apply_docstring(exception, st.exception, "exception")


# ==============================================================================
# Execution Flow
# ==============================================================================


def dialog(*args, **kwargs):
    return st.dialog(*args, **kwargs)


apply_docstring(dialog, st.dialog, "dialog")


def form(*args, **kwargs):
    return st.form(*args, **kwargs)


apply_docstring(form, st.form, "form")


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


apply_docstring(form_submit_button, st.form_submit_button, "form_submit_button")


def rerun(*args, **kwargs):
    return st.rerun(*args, **kwargs)


apply_docstring(rerun, st.rerun, "rerun")


def stop(*args, **kwargs):
    return st.stop(*args, **kwargs)


apply_docstring(stop, st.stop, "stop")


# ==============================================================================
# Navigation and Pages
# ==============================================================================


def navigation(*args, **kwargs):
    return st.navigation(*args, **kwargs)


apply_docstring(navigation, st.navigation, "navigation")


def switch_page(*args, **kwargs):
    return st.switch_page(*args, **kwargs)


apply_docstring(switch_page, st.switch_page, "switch_page")


# ==============================================================================
# Configuration
# ==============================================================================


def set_page_config(*args, **kwargs):
    return st.set_page_config(*args, **kwargs)


apply_docstring(set_page_config, st.set_page_config, "set_page_config")


def get_option(*args, **kwargs):
    return st.get_option(*args, **kwargs)


apply_docstring(get_option, st.get_option, "get_option")


def set_option(*args, **kwargs):
    return st.set_option(*args, **kwargs)


apply_docstring(set_option, st.set_option, "set_option")


# ==============================================================================
# Utility Functions
# ==============================================================================


def help(*args, **kwargs):
    return st.help(*args, **kwargs)


apply_docstring(help, st.help, "help")


def echo(*args, **kwargs):
    return st.echo(*args, **kwargs)


apply_docstring(echo, st.echo, "echo")
