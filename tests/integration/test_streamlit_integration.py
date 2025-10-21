"""Integration tests for Streamlit integration."""
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src", "st_yled"))


@pytest.mark.integration()
def test_elements_integration(mock_streamlit_app):
    """Test elements integration with mocked Streamlit."""
    from st_yled.elements import button

    # Test that elements can be called without errors
    try:
        button("Test Button", key="test")
    except Exception as e:
        pytest.fail(f"styled_button failed with mocked Streamlit: {e}")
