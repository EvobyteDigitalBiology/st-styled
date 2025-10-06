import os
from components import *

def init(css_path: str = None):

    cwd = os.getcwd()

    if css_path:
        # Check if provided path exists
        if os.path.exists(css_path):
            st.html(css_path)
            return
        else:
            raise FileNotFoundError(f"CSS file not found at provided path: {css_path}")

    # Check if .streamlit/st-styled.css exists
    css_default_path = os.path.join(cwd, '.streamlit', 'st-styled.css')
    if os.path.exists(css_default_path):
        
        st.html(css_default_path)
        return

    # Check if directory in home exists
    home_dir = os.path.join(os.path.expanduser('~'), '.streamlit', 'st-styled.css')
    if os.path.exists(home_dir):
        st.html(home_dir)
        return

    # If no CSS file found, apply no styles
    # TODO: Potentially raise a warning here
