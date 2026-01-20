import streamlit as st

__version__ = "0.1.0"


def redirect(url: str):
    """Redirect to a new URL

    redirect page to provided URL.
    Redirect inserts a `<meta>` tag in the page header to perform the redirect.

    Make sure not to include harmful URLs.

    unsafe_allow_html=True for underlying st.markdown

    Args:
        url (str): The URL to redirect to. External websites must contain protocol (http:// or https://)
    """
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True
    )
