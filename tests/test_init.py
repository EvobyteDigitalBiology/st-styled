"""Tests for st_yled package initialization."""
import os
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

import st_yled


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


def test_core_functions_available():
    """Test that core functions are available."""
    assert hasattr(st_yled, 'init')
    assert hasattr(st_yled, 'set')
    assert callable(st_yled.init)
    assert callable(st_yled.set)


@patch('st_yled.st.html')
def test_init_with_valid_css_path(mock_html):
    """Test init with a valid CSS file path."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.css', delete=False) as f:
        f.write('.test { color: red; }')
        f.flush()

        try:
            st_yled.init(f.name)
            mock_html.assert_called_once_with(f.name)
        finally:
            os.unlink(f.name)


def test_init_with_invalid_css_path():
    """Test init with an invalid CSS file path."""
    with pytest.raises(FileNotFoundError) as exc_info:
        st_yled.init("/nonexistent/path/style.css")

    assert "CSS file not found at provided path" in str(exc_info.value)


@patch('st_yled.st.html')
def test_init_with_default_css_file(mock_html, tmp_path):
    """Test init with default CSS file in .streamlit directory."""
    # Create a temporary directory structure
    streamlit_dir = tmp_path / ".streamlit"
    streamlit_dir.mkdir()
    css_file = streamlit_dir / "st-styled.css"
    css_file.write_text('.default { color: blue; }')

    with patch('st_yled.Path.cwd', return_value=tmp_path):
        st_yled.init()
        mock_html.assert_called_once_with(str(css_file))


@patch('st_yled.st.html')
def test_init_with_home_css_file(mock_html, tmp_path):
    """Test init with CSS file in home directory."""
    # Mock both cwd (no .streamlit/st-styled.css) and home directory
    with patch('st_yled.Path.cwd', return_value=tmp_path), \
         patch('st_yled.Path.home', return_value=tmp_path):

        # Create home directory CSS file
        streamlit_dir = tmp_path / ".streamlit"
        streamlit_dir.mkdir()
        css_file = streamlit_dir / "st-styled.css"
        css_file.write_text('.home { color: green; }')

        st_yled.init()
        mock_html.assert_called_once_with(str(css_file))


@patch('st_yled.st.html')
def test_init_no_css_file(mock_html, tmp_path):
    """Test init when no CSS file is found."""
    with patch('st_yled.Path.cwd', return_value=tmp_path), \
         patch('st_yled.Path.home', return_value=tmp_path):

        st_yled.init()
        mock_html.assert_not_called()


@patch('st_yled.styler.apply_component_css_global')
def test_set_function(mock_apply_css):
    """Test the set function calls styler correctly."""
    st_yled.set("button", "background_color", "#ff6b6b")

    mock_apply_css.assert_called_once_with("button", {"background_color": "#ff6b6b"})


@patch('st_yled.styler.apply_component_css_global')
def test_set_function_multiple_calls(mock_apply_css):
    """Test multiple calls to set function."""
    st_yled.set("button", "background_color", "#ff6b6b")
    st_yled.set("text", "font_size", "18px")

    assert mock_apply_css.call_count == 2
    mock_apply_css.assert_any_call("button", {"background_color": "#ff6b6b"})
    mock_apply_css.assert_any_call("text", {"font_size": "18px"})
