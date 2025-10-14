"""Tests for __init__.py module."""
from st_yled import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
