"""Tests for components module."""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "st_yled"))

def test_components_module_exists():
    """Test that components module can be imported."""
    try:
        from st_yled import components
        assert components is not None
    except ImportError:
        pytest.fail("Failed to import components module")


def test_styled_button_function_exists():
    """Test that styled_button function exists."""
    from st_yled.components import button
    assert callable(button)


def test_styled_selectbox_function_exists():
    """Test that styled_selectbox function exists."""
    from st_yled.components import selectbox
    assert callable(selectbox)
