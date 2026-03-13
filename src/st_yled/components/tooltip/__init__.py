"""Tooltip component for Streamlit.

This module provides a dismissible tooltip component rendered via inline
HTML/CSS/JS. The tooltip can be positioned on the page and optionally starts
hidden until shown.
"""

from typing import Optional
import typing
import html

import streamlit as st

from st_yled.styler import generate_component_key  # type: ignore

__version__ = "0.1.0"


@typing.no_type_check
def tooltip(
    title: str = "Tooltip Title",
    text: str = "This is a tooltip message. You can put anything here!",
    width: int = 230,
    top: str = "90px",
    left: str = "50px",
    background_color: str = "white",
    shadow: str = "0 4px 10px rgba(0, 0, 0, 0.2)",
    show: bool = True,
    key: Optional[str] = None,
) -> None:
    """Render a dismissible tooltip.

    Args:
        title: Tooltip header text.
        text: Tooltip body text.
        width: Tooltip width in pixels.
        top: CSS top offset (e.g., "90px", "2rem").
        left: CSS left offset (e.g., "50px", "10%").
        background_color: CSS background color.
        shadow: CSS box-shadow value.
        show: Whether the tooltip is initially visible.
        key: Optional unique key. Auto-generated when omitted.

    Returns:
        None
    """

    component_key = key or generate_component_key(type="custom_component")
    tooltip_id = f"tooltip-{component_key}"
    close_id = f"close-{component_key}"
    hidden_class = "" if show else "hidden"
    safe_title = html.escape(title)
    safe_text = html.escape(text)
    safe_component_key = "".join(
        char if char.isalnum() else "_" for char in component_key
    )
    component_name = f"st_yled_tooltip_{safe_component_key}"
    tooltip_class = f"st-yled-tooltip-{safe_component_key}"
    # app_font = st.get_option("theme.font") or "sans serif"
    # app_text_color = st.get_option("theme.textColor") or "#31333f"

    # # Streamlit theme uses names like "sans serif"; convert to valid CSS family.
    # if app_font == "sans serif":
    #   app_font = "sans-serif"

    css = f"""
    .{tooltip_class} {{
      position: fixed;
      top: {top};
      left: {left};
      width: {width}px;
      padding: 15px;
      border-radius: 8px;
      background: {background_color};
      box-shadow: {shadow};
      opacity: 0;
      transform: translateY(-5px);
      transition: opacity .25s ease, transform .25s ease;
      z-index: 999990;
    }}

    .{tooltip_class} .close-btn {{
      float: right;
      font-size: 16px;
      cursor: pointer;
      line-height: 1;
      width: 28px;
      height: 28px;
      border: 1px solid rgba(0, 0, 0, 0.25);
      border-radius: 999px;
      background: transparent;
      color: inherit;
      padding: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}

    .{tooltip_class} .close-btn:hover {{
      background: rgba(0, 0, 0, 0.06);
    }}

    .{tooltip_class}.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    .{tooltip_class}.hidden {{
      display: none;
    }}

    .{tooltip_class} h3 {{
      margin: 0 0 0.5rem 0;
      padding-right: 1.25rem;
    }}

    .{tooltip_class} p {{
      margin: 0;
    }}
    """

    html_block = f"""
    <div id=\"{tooltip_id}\" class=\"{tooltip_class} show {hidden_class}\">
      <button id=\"{close_id}\" class=\"close-btn\" aria-label=\"Close tooltip\">&times;</button>
      <h3>{safe_title}</h3>
      <p>{safe_text}</p>
    </div>
    """

    js = f"""
    export default function(component) {{
      const {{ parentElement }} = component;
      const closeButton = parentElement.querySelector("#{close_id}");
      const tooltipElement = parentElement.querySelector("#{tooltip_id}");
      const ownerDocument = parentElement.ownerDocument;
      const ownerWindow = ownerDocument.defaultView;

      const getMainBlock = () => {{
        const inCurrentDocument = parentElement.closest('[data-testid="stMainBlockContainer"]')
          || ownerDocument.querySelector('[data-testid="stMainBlockContainer"]')
          || ownerDocument.querySelector('.stMainBlockContainer')
          || ownerDocument.querySelector('.main .block-container')
          || ownerDocument.querySelector('.block-container');

        if (inCurrentDocument) return inCurrentDocument;

        try {{
          const parentDocument = ownerWindow?.parent?.document;
          if (!parentDocument) return null;
          return parentDocument.querySelector('[data-testid="stMainBlockContainer"]')
            || parentDocument.querySelector('.stMainBlockContainer')
            || parentDocument.querySelector('.main .block-container')
            || parentDocument.querySelector('.block-container');
        }} catch (error) {{
          return null;
        }}
      }};

      if (!closeButton || !tooltipElement) return;

      const anchorToMainBlock = () => {{
        const mainBlock = getMainBlock();
        if (!mainBlock) return;
        const rect = mainBlock.getBoundingClientRect();
        tooltipElement.style.top = `calc({top} + ${{rect.top}}px)`;
        tooltipElement.style.left = `calc({left} + ${{rect.left}}px)`;
      }};

      anchorToMainBlock();
      ownerWindow?.setTimeout(anchorToMainBlock, 0);
      ownerWindow?.requestAnimationFrame(anchorToMainBlock);
      ownerWindow?.addEventListener("resize", anchorToMainBlock);
      ownerWindow?.parent?.addEventListener("resize", anchorToMainBlock);
      ownerDocument.addEventListener("scroll", anchorToMainBlock, true);
      ownerWindow?.parent?.document?.addEventListener("scroll", anchorToMainBlock, true);

      closeButton.addEventListener("click", () => {{
        tooltipElement.classList.remove("show");
        tooltipElement.classList.add("hidden");
      }});
    }}
    """

    tooltip_component = st.components.v2.component(
      component_name,
      html=html_block,
      css=css,
      js=js,
      isolate_styles=False,
    )

    tooltip_component()
