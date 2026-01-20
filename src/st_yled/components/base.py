import typing
import streamlit as st
from typing import Literal


@typing.no_type_check
def card_base(
    key: str,
    width: Literal["stretch", "content"] | int = 300,
    height: Literal["stretch", "content"] | int = "content",
    background_color: str = "#f0f2f6",
    box_shadow: str = "2px 2px rgba(0, 0, 0, 0.1)",
    border_width: str = "0px",
    border_color: str = "black",
    border_style: str = "solid",
    padding: str = "0px",
    border_radius: str = "0.5rem",
    gap: str = "0px",
):
    cont_css = f"""<style>
    .st-key-{key} {{
        background-color: {background_color};
        box-shadow: {box_shadow};
        border-width: {border_width};
        border-color: {border_color};
        border-style: {border_style};
        border-radius: {border_radius};
        padding: {padding};
        gap: {gap};
    }}
    </style>"""

    st.html(cont_css)

    return st.container(key=key, width=width, height=height)
