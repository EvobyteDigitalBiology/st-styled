"""Tests for styler module."""

import pytest


def test_styler_module_exists():
    """Test that styler module can be imported."""
    try:
        from st_yled import styler
        assert styler is not None
    except ImportError:
        pytest.fail("Failed to import styler module")
