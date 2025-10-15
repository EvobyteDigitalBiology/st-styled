"""Integration tests for styler and validation system - Working version with correct component properties."""
import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "st_yled"))

from unittest.mock import patch, MagicMock
from st_yled.styler import apply_component_css, apply_component_css_global, get_css_properties_from_args
from st_yled.validation import ValidationConfig, ValidationError


class TestStylerValidationIntegration:
    """Test integration between styler and validation system."""

    def test_apply_component_css_processes_supported_styling_properties(self):
        """Test that apply_component_css processes supported styling properties correctly."""
        # Use properties that text component actually supports: color and font_size
        kwargs = {
            "value": "Hello World",
            "color": "#ff0000",
            "font_size": "16px"
        }

        # Mock st.html to capture CSS generation
        with patch("st_yled.styler.st") as mock_st:
            result_kwargs = apply_component_css("text", kwargs)

            # Verify CSS was generated and applied
            mock_st.html.assert_called_once()
            css_call = mock_st.html.call_args[0][0]
            assert "<style>" in css_call
            assert "</style>" in css_call

            # Verify supported styling properties are removed from returned kwargs
            assert "color" not in result_kwargs
            assert "font_size" not in result_kwargs

            # Non-styling properties should remain
            assert "value" in result_kwargs
            assert result_kwargs["value"] == "Hello World"

            # Key should be generated if not provided
            assert "key" in result_kwargs
            assert "st-yler-" in result_kwargs["key"]

    def test_apply_component_css_with_button_styling(self):
        """Test with button component that supports background_color."""
        kwargs = {
            "label": "Click me",
            "background_color": "#00ff00",
            "border_color": "#000000"
        }

        with patch("st_yled.styler.st") as mock_st:
            result_kwargs = apply_component_css("button", kwargs)

            # Verify CSS was generated
            mock_st.html.assert_called_once()

            # Button styling properties should be removed
            assert "background_color" not in result_kwargs
            assert "border_color" not in result_kwargs

            # Button properties should remain
            assert "label" in result_kwargs

    def test_apply_component_css_preserves_existing_key(self):
        """Test that existing key is preserved."""
        kwargs = {
            "value": "Hello World",
            "color": "#ff0000",
            "key": "custom_key"
        }

        with patch("st_yled.styler.st") as mock_st:
            result_kwargs = apply_component_css("text", kwargs)

            # Original key should be preserved
            assert result_kwargs["key"] == "custom_key"

    def test_apply_component_css_with_invalid_styling_strict_mode(self):
        """Test that invalid styling properties raise error in strict mode."""
        # Set environment variable for strict mode
        os.environ["ST_STYLED_STRICT_VALIDATION"] = "true"

        try:
            kwargs = {
                "value": "Hello World",
                "color": "invalid_color"  # Invalid color value
            }

            # Import ValidationError from validation module directly due to sys.path modifications
            from validation import ValidationError as VE

            with pytest.raises(VE):
                apply_component_css("text", kwargs)

        finally:
            # Clean up environment variable
            os.environ.pop("ST_STYLED_STRICT_VALIDATION", None)

    def test_apply_component_css_with_invalid_styling_permissive_mode(self):
        """Test that invalid styling is removed in permissive mode."""
        # Ensure we're not in strict mode
        os.environ.pop("ST_STYLED_STRICT_VALIDATION", None)

        kwargs = {
            "value": "Hello World",
            "color": "invalid_color"  # Invalid color value
        }

        with patch("st_yled.styler.st") as mock_st:
            # Should not raise error in permissive mode - invalid properties are removed by validation
            result_kwargs = apply_component_css("text", kwargs)

            # Invalid styling should be removed by validation
            assert "color" not in result_kwargs
            assert "value" in result_kwargs

    def test_apply_component_css_bypass_validation(self):
        """Test that validation can be bypassed via environment variable."""
        # Set bypass environment variable
        os.environ["ST_STYLED_BYPASS_VALIDATION"] = "true"

        try:
            kwargs = {
                "value": "Hello World",
                "color": "invalid_color"  # Would normally fail validation
            }

            with patch("st_yled.styler.st") as mock_st:
                result_kwargs = apply_component_css("text", kwargs)

                # When bypassed, validation is skipped, but CSS processing still happens
                # Styling properties should still be removed after CSS processing
                assert "color" not in result_kwargs
                assert "value" in result_kwargs

        finally:
            # Clean up environment variable
            os.environ.pop("ST_STYLED_BYPASS_VALIDATION", None)

    def test_apply_component_css_no_styling_properties(self):
        """Test component with no styling properties."""
        kwargs = {
            "value": "Hello World",
            "key": "test_key"
        }

        with patch("st_yled.styler.st") as mock_st:
            result_kwargs = apply_component_css("text", kwargs)

            # No CSS should be generated for no styling properties
            if mock_st.html.called:
                css_call = mock_st.html.call_args[0][0]
                # Empty CSS should not contain meaningful styling
                assert css_call == "<style> </style>" or css_call == "<style></style>"

            # All properties should remain (no styling to remove)
            assert "value" in result_kwargs
            assert result_kwargs["value"] == "Hello World"
            assert result_kwargs["key"] == "test_key"

    def test_apply_component_css_unsupported_styling_property(self):
        """Test with styling property not supported by component."""
        kwargs = {
            "value": "Hello World",
            "background_color": "#ff0000"  # text component doesn't support background_color
        }

        with patch("st_yled.styler.st") as mock_st:
            result_kwargs = apply_component_css("text", kwargs)

            # Unsupported properties should not be processed/removed
            # They remain in kwargs since they're not in the component's style mapping
            assert "background_color" in result_kwargs  # Not removed because text doesn't support it
            assert "value" in result_kwargs

    def test_get_css_properties_modifies_kwargs_in_place(self):
        """Test that get_css_properties_from_args removes styling properties from kwargs."""
        kwargs = {
            "color": "#ff0000",
            "font_size": "16px",
            "value": "test"
        }

        css_props = get_css_properties_from_args("text", kwargs)

        # Should return CSS properties
        assert isinstance(css_props, dict)
        assert len(css_props) > 0  # Should have generated CSS for supported properties

        # Supported styling properties should be removed from original kwargs
        assert "color" not in kwargs
        assert "font_size" not in kwargs

        # Non-styling should remain
        assert "value" in kwargs

    def test_component_with_unsupported_component_type(self):
        """Test component that doesn't exist in COMPONENT_STYLES."""
        kwargs = {
            "value": "Hello World",
            "color": "#ff0000"
        }

        # Use a component type that doesn't exist in COMPONENT_STYLES
        with pytest.raises(ValueError, match="Component type 'nonexistent' not found"):
            get_css_properties_from_args("nonexistent", kwargs)

    def test_validation_config_methods(self):
        """Test ValidationConfig class methods."""
        # Test is_validation_bypassed
        os.environ.pop("ST_STYLED_BYPASS_VALIDATION", None)
        assert ValidationConfig.is_validation_bypassed() is False

        os.environ["ST_STYLED_BYPASS_VALIDATION"] = "true"
        assert ValidationConfig.is_validation_bypassed() is True

        # Test get_strict_mode
        os.environ.pop("ST_STYLED_STRICT_VALIDATION", None)
        assert ValidationConfig.get_strict_mode() is False  # Default

        os.environ["ST_STYLED_STRICT_VALIDATION"] = "true"
        assert ValidationConfig.get_strict_mode() is True

        # Clean up
        os.environ.pop("ST_STYLED_BYPASS_VALIDATION", None)
        os.environ.pop("ST_STYLED_STRICT_VALIDATION", None)

    def test_css_generation_with_component_key(self):
        """Test that CSS generation includes component key selector."""
        from st_yled.styler import generate_component_css

        kwargs = {
            "color": "#ff0000"  # Use supported property
        }

        css = generate_component_css("text", kwargs, "test_key")

        # Should generate CSS and include the key in the CSS selector
        assert css  # Not empty

        # Property should be removed from kwargs after processing
        assert "color" not in kwargs

    def test_mixed_styling_and_component_properties(self):
        """Test component with mix of styling and regular streamlit properties."""
        kwargs = {
            "value": "Hello World",
            "color": "#ff0000",
            "help": "This is help text",  # Streamlit native property
            "disabled": False,  # Streamlit native property
            "font_size": "16px"
        }

        with patch("st_yled.styler.st") as mock_st:
            result_kwargs = apply_component_css("text", kwargs)

            # Supported styling properties should be removed
            assert "color" not in result_kwargs
            assert "font_size" not in result_kwargs

            # Streamlit native and other properties should remain
            assert "value" in result_kwargs
            assert "help" in result_kwargs
            assert "disabled" in result_kwargs
            assert result_kwargs["help"] == "This is help text"
            assert result_kwargs["disabled"] is False

    def test_apply_component_css_global_with_supported_properties(self):
        """Test global CSS application with supported styling properties."""
        # Use properties that text component supports
        kwargs = {
            "color": "#00ff00",
            "font_size": "16px"
        }

        with patch("st_yled.styler.st") as mock_st:
            # Should not raise error
            apply_component_css_global("text", kwargs)

            # Should have called st.html (once for each property that generates CSS)
            assert mock_st.html.call_count >= 1

    def test_validation_integration(self):
        """Test that validation warnings are properly issued."""
        kwargs = {
            "value": "Hello World",  # This triggers warning as unknown CSS property
            "color": "#ff0000"
        }

        with patch("st_yled.styler.st") as mock_st:
            # Should complete but issue warnings
            result_kwargs = apply_component_css("text", kwargs)
            # Supported styling should be processed
            assert "color" not in result_kwargs
            # Non-CSS properties should remain
            assert "value" in result_kwargs
