"""Test configuration and fixtures."""
import os
import tempfile

import pytest


@pytest.fixture()
def temp_css_file():
    """Create a temporary CSS file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".css", delete=False) as f:
        f.write("""
        .stButton > button {
            background-color: red !important;
        }
        """)
        f.flush()
        yield f.name
    os.unlink(f.name)


@pytest.fixture()
def mock_streamlit_app(monkeypatch):
    """Mock streamlit for testing without actual streamlit app context."""
    class MockStreamlit:
        def html(self, content):
            return content

        def button(self, *args, **kwargs):
            return False

    mock_st = MockStreamlit()
    monkeypatch.setattr("st_yled.components.st", mock_st)
    monkeypatch.setattr("st_yled.styler.st", mock_st)
    return mock_st
