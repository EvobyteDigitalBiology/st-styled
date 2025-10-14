"""Tests for st_yled package initialization."""
import pytest


def test_package_imports():
    """Test that the package can be imported."""
    try:
        import st_yled
        assert st_yled is not None
    except ImportError:
        pytest.fail("Failed to import st_yled package")


def test_main_modules_importable():
    """Test that main modules can be imported."""
    try:
        from st_yled import components, styler
        assert components is not None
        assert styler is not None
    except ImportError as e:
        pytest.fail(f"Failed to import main modules: {e}")


def test_version_available():
    """Test that version is available."""
    try:
        from st_yled import __version__
        assert __version__ is not None
        assert isinstance(__version__, str)
    except ImportError:
        pytest.fail("Version not available in package")
