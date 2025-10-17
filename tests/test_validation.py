"""Comprehensive tests for parameter validation."""

import pytest
import warnings
from unittest.mock import patch, Mock
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "st_yled"))

from st_yled.validation import (
    CSSValidator, StyleValidator, ValidationError, ValidationWarning,
    validate_styling_kwargs, ValidationConfig
)


class TestCSSValidator:
    """Test CSS property validators."""

    def test_valid_colors(self):
        """Test valid color validation."""
        valid_colors = [
            "#FF0000", "#fff", "#000000", "#abc",
            "red", "blue", "transparent",
            "rgb(255, 0, 0)", "rgba(255, 0, 0, 0.5)",
            "hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 0.5)"
        ]

        for color in valid_colors:
            assert CSSValidator.is_valid_color(color), f"Color '{color}' should be valid"

    def test_invalid_colors(self):
        """Test invalid color validation."""
        invalid_colors = [
            "#gggggg", "#ff", "#fffffff", "invalidcolor",
            "rgb(300, 0, 0)", "rgba(255, 0, 0, 2)", 123, None, ""
        ]

        for color in invalid_colors:
            assert not CSSValidator.is_valid_color(color), f"Color '{color}' should be invalid"

    def test_valid_lengths(self):
        """Test valid length validation."""
        valid_lengths = [
            "0", "10px", "2em", "1.5rem", "50%", "100vh", "75vw",
            "-10px", "0.5em", "12.5px", "100.0%"
        ]

        for length in valid_lengths:
            assert CSSValidator.is_valid_length(length), f"Length '{length}' should be valid"

    def test_invalid_lengths(self):
        """Test invalid length validation."""
        invalid_lengths = [
            "10", "px", "10 px", "invalid", None, 123, "", "10pxx", "10.px"
        ]

        for length in invalid_lengths:
            assert not CSSValidator.is_valid_length(length), f"Length '{length}' should be invalid"

    def test_valid_borders(self):
        """Test valid border validation."""
        valid_borders = [
            "solid", "solid", "none"
        ]

        for border in valid_borders:
            assert CSSValidator.is_valid_border_style(border), f"Border '{border}' should be valid"

    def test_invalid_borders(self):
        """Test invalid border validation."""
        invalid_borders = [
            "invalid", "1px solid red blue", "1px 2px 3px 4px",
            "", 123, "1px invalid red"
        ]

        for border in invalid_borders:
            assert not CSSValidator.is_valid_border_style(border), f"Border '{border}' should be invalid"

    def test_font_weights(self):
        """Test font weight validation."""
        valid_weights = ["normal", "bold", "100", "400", "700", "900"]
        invalid_weights = ["heavy", "1000", "50", None, 123]

        for weight in valid_weights:
            assert CSSValidator.is_valid_font_weight(weight)

        for weight in invalid_weights:
            assert not CSSValidator.is_valid_font_weight(weight)

    def test_text_align(self):
        """Test text align validation."""
        valid_aligns = ["left", "center", "right", "justify", "start", "end"]
        invalid_aligns = ["middle", "top", "bottom", None, 123]

        for align in valid_aligns:
            assert CSSValidator.is_valid_text_align(align)

        for align in invalid_aligns:
            assert not CSSValidator.is_valid_text_align(align)


class TestStyleValidator:
    """Test main style validator."""

    def test_valid_property_validation(self):
        """Test validation of valid properties."""
        test_cases = [
            ("color", "#FF0000"),
            ("background_color", "blue"),

        ]

        for prop_name, prop_value in test_cases:
            is_valid, message = StyleValidator.validate_property(prop_name, prop_value)
            assert is_valid, f"Property {prop_name}={prop_value} should be valid, got: {message}"
            assert message is None

    def test_invalid_property_validation(self):
        """Test validation of invalid properties."""
        test_cases = [
            ("color", "invalid_color"),
            ("background_color", "#gggggg"),
        ]

        for prop_name, prop_value in test_cases:
            is_valid, message = StyleValidator.validate_property(prop_name, prop_value, strict=True)
            assert not is_valid, f"Property {prop_name}={prop_value} should be invalid"
            assert message is not None
            assert "Invalid" in message

    def test_unknown_property_warning(self):
        """Test that unknown properties generate warnings."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            is_valid, message = StyleValidator.validate_property("unknown_prop", "some_value")

            assert is_valid  # Unknown properties are allowed

    def test_property_aliases(self):
        """Test property alias handling."""
        # bg_color should be treated as background_color
        is_valid, message = StyleValidator.validate_property("bg_color", "#FF0000")
        assert is_valid
        assert message is None

    def test_none_value_handling(self):
        """Test that None values are skipped."""
        is_valid, message = StyleValidator.validate_property("color", None)
        assert is_valid
        assert message is None

    def test_component_kwargs_validation_strict(self):
        """Test strict validation of component kwargs."""
        kwargs = {
            "background_color": "#FF0000",  # Valid
            "color": "invalid_color",       # Invalid
            "width": "100px",              # Valid
            "key": "test_key",             # Streamlit param - should be skipped
            "unknown_prop": "value"        # Unknown - should error in strict mode
        }

        # Should raise ValidationError in strict mode
        with pytest.raises(ValidationError) as exc_info:
            StyleValidator.validate_component_kwargs("button", kwargs, strict=True)

        assert "validation failed" in str(exc_info.value).lower()

    def test_component_kwargs_validation_lenient(self):
        """Test lenient validation of component kwargs."""
        kwargs = {
            "background_color": "#FF0000",  # Valid
            "color": "invalid_color",       # Invalid - should be removed
            "width": "100px",              # Valid
            "key": "test_key",             # Streamlit param - should be kept
            "unknown_prop": "value"        # Unknown - should generate warning
        }

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            validated = StyleValidator.validate_component_kwargs("button", kwargs, strict=False)

            # Invalid property should be removed
            assert "color" not in validated
            assert "background_color" in validated
            assert "width" in validated
            assert "key" in validated  # Streamlit params preserved

            # Should have warnings
            assert len(w) > 0

    def test_bypass_validation(self):
        """Test validation bypass functionality."""
        kwargs = {
            "color": "invalid_color",
            "unknown_prop": "invalid_value"
        }

        # Should return kwargs unchanged when bypassed
        validated = StyleValidator.validate_component_kwargs(
            "button", kwargs, bypass_validation=True
        )
        assert validated == kwargs


class TestValidationIntegration:
    """Test integration with main validation functions."""

    def test_validate_styling_kwargs_function(self):
        """Test main validate_styling_kwargs function."""
        kwargs = {
            "background_color": "#FF0000",
            "padding": "10px",
            "key": "test"
        }

        validated = validate_styling_kwargs("button", kwargs)

        assert "background_color" in validated
        assert "padding" in validated
        assert "key" in validated

    def test_validation_with_suggestions(self):
        """Test that validation provides helpful suggestions."""
        suggestions = StyleValidator.suggest_corrections("color")

        assert len(suggestions) > 0
        assert any("hex" in s.lower() for s in suggestions)
        assert any("rgb" in s.lower() for s in suggestions)

    def test_error_messages_are_helpful(self):
        """Test that error messages provide helpful information."""
        _, message = StyleValidator.validate_property("color", "invalid", strict=True)

        assert message is not None
        assert "Invalid color value" in message
        assert "Expected formats" in message
        assert "#hex" in message or "rgb" in message


class TestValidationConfig:
    """Test validation configuration."""

    def test_default_config(self):
        """Test default configuration values."""
        assert not ValidationConfig.DEFAULT_STRICT_MODE
        assert ValidationConfig.SHOW_WARNINGS
        assert ValidationConfig.BYPASS_ENV_VAR == "ST_STYLED_BYPASS_VALIDATION"

    def test_bypass_environment_detection(self):
        """Test bypass detection from environment variables."""
        # Test bypass enabled
        with patch.dict(os.environ, {"ST_STYLED_BYPASS_VALIDATION": "true"}):
            assert ValidationConfig.is_validation_bypassed()

        with patch.dict(os.environ, {"ST_STYLED_BYPASS_VALIDATION": "1"}):
            assert ValidationConfig.is_validation_bypassed()

        # Test bypass disabled
        with patch.dict(os.environ, {"ST_STYLED_BYPASS_VALIDATION": "false"}):
            assert not ValidationConfig.is_validation_bypassed()

        with patch.dict(os.environ, {}, clear=True):
            assert not ValidationConfig.is_validation_bypassed()

    def test_strict_mode_environment_detection(self):
        """Test strict mode detection from environment variables."""
        # Test strict mode enabled
        with patch.dict(os.environ, {"ST_STYLED_STRICT_VALIDATION": "true"}):
            assert ValidationConfig.get_strict_mode()

        # Test strict mode disabled
        with patch.dict(os.environ, {"ST_STYLED_STRICT_VALIDATION": "false"}):
            assert not ValidationConfig.get_strict_mode()

        # Test default behavior
        with patch.dict(os.environ, {}, clear=True):
            assert ValidationConfig.get_strict_mode() == ValidationConfig.DEFAULT_STRICT_MODE


class TestValidationErrorHandling:
    """Test error handling and edge cases."""

    def test_validation_error_inheritance(self):
        """Test that ValidationError is a ValueError."""
        error = ValidationError("test message")
        assert isinstance(error, ValueError)
        assert str(error) == "test message"

    def test_validation_warning_inheritance(self):
        """Test that ValidationWarning is a UserWarning."""
        warning = ValidationWarning("test message")
        assert isinstance(warning, UserWarning)

    def test_empty_kwargs_handling(self):
        """Test handling of empty kwargs."""
        result = validate_styling_kwargs("button", {})
        assert result == {}

    def test_large_kwargs_performance(self):
        """Test validation performance with many kwargs."""
        # Create kwargs with many properties
        large_kwargs = {f"prop_{i}": f"value_{i}" for i in range(100)}
        large_kwargs.update({
            "background_color": "#FF0000",
            "color": "blue",
            "width": "100px"
        })

        # Should complete quickly even with many properties
        import time
        start_time = time.time()
        validated = validate_styling_kwargs("button", large_kwargs, strict=False)
        end_time = time.time()

        # Should complete in reasonable time (< 1 second)
        assert end_time - start_time < 1.0

        # Valid properties should be preserved
        assert "background_color" in validated
        assert "color" in validated
        assert "width" in validated


class TestRealWorldScenarios:
    """Test real-world usage scenarios."""

    def test_common_button_styling(self):
        """Test common button styling scenarios."""
        button_kwargs = {
            "background_color": "#007BFF",
            "color": "white",
            "border": "1px solid #007BFF",
            "padding": "10px 20px",
            "border_radius": "5px",
            "font_weight": "bold"
        }

        validated = validate_styling_kwargs("button", button_kwargs)

        # All valid properties should be preserved
        for key, value in button_kwargs.items():
            assert key in validated
            assert validated[key] == value

    def test_dashboard_component_styling(self):
        """Test styling for dashboard-like elements."""
        metric_kwargs = {
            "background_color": "#f8f9fa",
            "border": "1px solid #dee2e6",
            "border_radius": "8px",
            "padding": "16px",
            "text_align": "center",
            "font_weight": "600"
        }

        validated = validate_styling_kwargs("metric", metric_kwargs)

        # Should validate without errors
        assert len(validated) == len(metric_kwargs)

    def test_mixed_valid_invalid_properties(self):
        """Test realistic mix of valid and invalid properties."""
        mixed_kwargs = {
            "background_color": "#FF0000",     # Valid
            "color": "blue",                   # Valid
            "custom_prop": "custom_value",    # Unknown but allowed
            "key": "component_key"            # Streamlit param
        }

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")

            validated = validate_styling_kwargs("text", mixed_kwargs, strict=False)

            # Valid properties should be preserved
            assert "background_color" in validated
            assert "color" in validated
            assert "key" in validated

            # Invalid properties should be removed
            assert "width" not in validated
            assert "border" not in validated
