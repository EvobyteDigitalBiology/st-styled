"""Comprehensive tests for all elements in elements module."""

import pytest
import sys
import os
from datetime import date, time
from unittest.mock import patch, Mock
import pandas as pd

# Add paths for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "st_yled"))

from st_yled import elements


class TestComponentImports:
    """Test that all component functions can be imported and are callable."""

    def test_elements_module_exists(self):
        """Test that elements module can be imported."""
        assert elements is not None
        assert hasattr(elements, 'button')
        assert hasattr(elements, 'selectbox')

    # Display and Magic elements
    def test_write_exists(self):
        assert callable(elements.write)

    def test_write_stream_exists(self):
        assert callable(elements.write_stream)

    # Text Elements
    def test_markdown_exists(self):
        assert callable(elements.markdown)

    def test_title_exists(self):
        assert callable(elements.title)

    def test_header_exists(self):
        assert callable(elements.header)

    def test_subheader_exists(self):
        assert callable(elements.subheader)

    def test_badge_exists(self):
        assert callable(elements.badge)

    def test_caption_exists(self):
        assert callable(elements.caption)

    def test_code_exists(self):
        assert callable(elements.code)

    def test_latex_exists(self):
        assert callable(elements.latex)

    def test_text_exists(self):
        assert callable(elements.text)

    def test_divider_exists(self):
        assert callable(elements.divider)

    def test_html_exists(self):
        assert callable(elements.html)

    # Data Elements
    def test_dataframe_exists(self):
        assert callable(elements.dataframe)

    def test_data_editor_exists(self):
        assert callable(elements.data_editor)

    def test_table_exists(self):
        assert callable(elements.table)

    def test_metric_exists(self):
        assert callable(elements.metric)

    def test_json_exists(self):
        assert callable(elements.json)

    # Chart Elements
    def test_area_chart_exists(self):
        assert callable(elements.area_chart)

    def test_bar_chart_exists(self):
        assert callable(elements.bar_chart)

    def test_line_chart_exists(self):
        assert callable(elements.line_chart)

    def test_scatter_chart_exists(self):
        assert callable(elements.scatter_chart)

    def test_map_exists(self):
        assert callable(elements.map)

    def test_pyplot_exists(self):
        assert callable(elements.pyplot)

    def test_altair_chart_exists(self):
        assert callable(elements.altair_chart)

    def test_vega_lite_chart_exists(self):
        assert callable(elements.vega_lite_chart)

    def test_plotly_chart_exists(self):
        assert callable(elements.plotly_chart)

    def test_bokeh_chart_exists(self):
        assert callable(elements.bokeh_chart)

    def test_pydeck_chart_exists(self):
        assert callable(elements.pydeck_chart)

    def test_graphviz_chart_exists(self):
        assert callable(elements.graphviz_chart)

    # Input Widgets
    def test_button_exists(self):
        assert callable(elements.button)

    def test_download_button_exists(self):
        assert callable(elements.download_button)

    def test_link_button_exists(self):
        assert callable(elements.link_button)

    def test_page_link_exists(self):
        assert callable(elements.page_link)

    def test_checkbox_exists(self):
        assert callable(elements.checkbox)

    def test_color_picker_exists(self):
        assert callable(elements.color_picker)

    def test_feedback_exists(self):
        assert callable(elements.feedback)

    def test_multiselect_exists(self):
        assert callable(elements.multiselect)

    def test_pills_exists(self):
        assert callable(elements.pills)

    def test_radio_exists(self):
        assert callable(elements.radio)

    def test_segmented_control_exists(self):
        assert callable(elements.segmented_control)

    def test_selectbox_exists(self):
        assert callable(elements.selectbox)

    def test_select_slider_exists(self):
        assert callable(elements.select_slider)

    def test_toggle_exists(self):
        assert callable(elements.toggle)

    def test_number_input_exists(self):
        assert callable(elements.number_input)

    def test_slider_exists(self):
        assert callable(elements.slider)

    def test_date_input_exists(self):
        assert callable(elements.date_input)

    def test_time_input_exists(self):
        assert callable(elements.time_input)

    def test_text_area_exists(self):
        assert callable(elements.text_area)

    def test_text_input_exists(self):
        assert callable(elements.text_input)

    def test_chat_input_exists(self):
        assert callable(elements.chat_input)

    def test_audio_input_exists(self):
        assert callable(elements.audio_input)

    def test_file_uploader_exists(self):
        assert callable(elements.file_uploader)

    def test_camera_input_exists(self):
        assert callable(elements.camera_input)

    # Media Elements
    def test_image_exists(self):
        assert callable(elements.image)

    def test_logo_exists(self):
        assert callable(elements.logo)

    def test_pdf_exists(self):
        assert callable(elements.pdf)

    def test_audio_exists(self):
        assert callable(elements.audio)

    def test_video_exists(self):
        assert callable(elements.video)

    # Layout and Container Elements
    def test_columns_exists(self):
        assert callable(elements.columns)

    def test_container_exists(self):
        assert callable(elements.container)

    def test_empty_exists(self):
        assert callable(elements.empty)

    def test_expander_exists(self):
        assert callable(elements.expander)

    def test_popover_exists(self):
        assert callable(elements.popover)

    def test_tabs_exists(self):
        assert callable(elements.tabs)

    # Chat Elements
    def test_chat_message_exists(self):
        assert callable(elements.chat_message)

    # Status Elements
    def test_progress_exists(self):
        assert callable(elements.progress)

    def test_spinner_exists(self):
        assert callable(elements.spinner)

    def test_status_exists(self):
        assert callable(elements.status)

    def test_toast_exists(self):
        assert callable(elements.toast)

    def test_balloons_exists(self):
        assert callable(elements.balloons)

    def test_snow_exists(self):
        assert callable(elements.snow)

    def test_success_exists(self):
        assert callable(elements.success)

    def test_info_exists(self):
        assert callable(elements.info)

    def test_warning_exists(self):
        assert callable(elements.warning)

    def test_error_exists(self):
        assert callable(elements.error)

    def test_exception_exists(self):
        assert callable(elements.exception)

    # Execution Flow
    def test_dialog_exists(self):
        assert callable(elements.dialog)

    def test_form_exists(self):
        assert callable(elements.form)

    def test_form_submit_button_exists(self):
        assert callable(elements.form_submit_button)

    def test_rerun_exists(self):
        assert callable(elements.rerun)

    def test_stop_exists(self):
        assert callable(elements.stop)

    # Navigation and Pages
    def test_navigation_exists(self):
        assert callable(elements.navigation)

    def test_switch_page_exists(self):
        assert callable(elements.switch_page)

    # Configuration
    def test_set_page_config_exists(self):
        assert callable(elements.set_page_config)

    def test_get_option_exists(self):
        assert callable(elements.get_option)

    def test_set_option_exists(self):
        assert callable(elements.set_option)

    # Utility Functions
    def test_help_exists(self):
        assert callable(elements.help)

    def test_echo_exists(self):
        assert callable(elements.echo)


class TestComponentFunctionality:
    """Test that elements can be called and handle parameters correctly."""

    @pytest.fixture
    def mock_streamlit(self):
        """Mock streamlit module for testing component functionality."""
        with patch('st_yled.elements.st') as mock_st:
            # Create a proper container mock
            mock_container = Mock()

            # Configure individual component mocks on container
            for attr in ['markdown', 'title', 'header', 'subheader', 'caption', 'code',
                        'latex', 'text', 'table', 'metric', 'json', 'link_button', 'expander',
                        'popover', 'tabs', 'chat_message', 'progress', 'status', 'success',
                        'info', 'warning', 'error', 'form_submit_button']:
                setattr(mock_container, attr, Mock(return_value=f"mock_{attr}_result"))

            # Make sure container() returns the mock_container, not a string
            mock_st.container.return_value = mock_container

            # Configure elements that don't use containers (direct st.component calls)
            for attr in ['button', 'download_button', 'checkbox', 'color_picker', 'feedback',
                        'multiselect', 'pills', 'radio', 'segmented_control', 'selectbox',
                        'select_slider', 'toggle', 'number_input', 'slider', 'date_input',
                        'time_input', 'text_area', 'text_input', 'chat_input', 'audio_input',
                        'file_uploader', 'camera_input']:
                setattr(mock_st, attr, Mock(return_value=f"mock_{attr}_result"))

            # Configure non-styled elements
            for attr in ['write_stream', 'badge', 'divider', 'html', 'dataframe',
                        'data_editor', 'area_chart', 'bar_chart', 'line_chart', 'scatter_chart',
                        'map', 'pyplot', 'altair_chart', 'vega_lite_chart', 'plotly_chart',
                        'bokeh_chart', 'pydeck_chart', 'graphviz_chart', 'page_link', 'image',
                        'logo', 'pdf', 'audio', 'video', 'columns', 'empty',
                        'spinner', 'toast', 'balloons', 'snow', 'exception', 'dialog', 'form',
                        'rerun', 'stop', 'navigation', 'switch_page', 'set_page_config',
                        'get_option', 'set_option', 'help', 'echo']:
                setattr(mock_st, attr, Mock(return_value=f"mock_{attr}_result"))

            # Fix the container attribute to not return a string
            mock_st.container = Mock(return_value=mock_container)

            yield mock_st, mock_container

    @pytest.fixture
    def mock_styler(self):
        """Mock styler module for testing CSS application."""
        with patch('st_yled.elements.styler') as mock_styler:
            # Configure apply_component_css to return kwargs without styling properties
            def mock_apply_css(component_name, kwargs):
                # Remove common styling properties that would be processed
                styling_props = ['background_color', 'color', 'border_color', 'font_size',
                               'padding', 'margin', 'border_radius']
                filtered_kwargs = {k: v for k, v in kwargs.items() if k not in styling_props}
                return filtered_kwargs

            mock_styler.apply_component_css.side_effect = mock_apply_css
            yield mock_styler

    # Display and Text Elements Tests
    def test_markdown_component(self, mock_streamlit, mock_styler):
        """Test markdown component with styling."""
        mock_st, mock_container = mock_streamlit

        result = elements.markdown("# Hello World", color="#ff0000")

        # Should call styler for CSS processing
        mock_styler.apply_component_css.assert_called_once()
        # Should use container with key
        mock_st.container.assert_called_once()
        # Should call markdown on container
        mock_container.markdown.assert_called_once()

    def test_title_component(self, mock_streamlit, mock_styler):
        """Test title component."""
        mock_st, mock_container = mock_streamlit

        result = elements.title("Page Title", font_size="24px")

        mock_styler.apply_component_css.assert_called_with("title", {"font_size": "24px"})
        mock_container.title.assert_called_once_with("Page Title")

    def test_text_component(self, mock_streamlit, mock_styler):
        """Test text component."""
        mock_st, mock_container = mock_streamlit

        result = elements.text("Sample text", color="blue")

        mock_styler.apply_component_css.assert_called_with("text", {"color": "blue"})
        mock_container.text.assert_called_once_with("Sample text")

    # Input Widget Tests
    def test_button_component(self, mock_streamlit, mock_styler):
        """Test button component."""
        mock_st, mock_container = mock_streamlit

        result = elements.button("Click Me", background_color="red")

        mock_styler.apply_component_css.assert_called_with("button", {"background_color": "red"})
        mock_st.button.assert_called_once_with("Click Me")

    def test_selectbox_component(self, mock_streamlit, mock_styler):
        """Test selectbox component."""
        mock_st, mock_container = mock_streamlit

        options = ["Option 1", "Option 2", "Option 3"]
        result = elements.selectbox("Choose:", options, background_color="lightblue")

        mock_styler.apply_component_css.assert_called_with("selectbox", {"background_color": "lightblue"})
        mock_st.selectbox.assert_called_once_with("Choose:", options)

    def test_text_input_component(self, mock_streamlit, mock_styler):
        """Test text_input component."""
        mock_st, mock_container = mock_streamlit

        result = elements.text_input("Enter text:", placeholder="Type here...", border_color="green")

        # Styler receives all kwargs including streamlit parameters
        mock_styler.apply_component_css.assert_called_with("text_input",
                                                          {"placeholder": "Type here...", "border_color": "green"})
        mock_st.text_input.assert_called_once_with("Enter text:", placeholder="Type here...")

    def test_slider_component(self, mock_streamlit, mock_styler):
        """Test slider component."""
        mock_st, mock_container = mock_streamlit

        result = elements.slider("Select value:", min_value=0, max_value=100, value=50)

        # Styler receives all kwargs
        mock_styler.apply_component_css.assert_called_with("slider",
                                                          {"min_value": 0, "max_value": 100, "value": 50})
        mock_st.slider.assert_called_once_with("Select value:", min_value=0, max_value=100, value=50)

    # Data Element Tests
    def test_table_component(self, mock_streamlit, mock_styler):
        """Test table component with DataFrame."""
        mock_st, mock_container = mock_streamlit

        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = elements.table(df, border_color="black")

        mock_styler.apply_component_css.assert_called_with("table", {"border_color": "black"})
        mock_container.table.assert_called_once_with(df)

    def test_metric_component(self, mock_streamlit, mock_styler):
        """Test metric component."""
        mock_st, mock_container = mock_streamlit

        result = elements.metric("Revenue", "$1,000", delta="$100", color="green")

        mock_styler.apply_component_css.assert_called_with("metric", {"delta": "$100", "color": "green"})
        mock_container.metric.assert_called_once_with("Revenue", "$1,000", delta="$100")

    # Layout Element Tests
    def test_expander_component(self, mock_streamlit, mock_styler):
        """Test expander component."""
        mock_st, mock_container = mock_streamlit

        result = elements.expander("Show details", expanded=True, background_color="lightgray")

        mock_styler.apply_component_css.assert_called_with("expander", {"expanded": True, "background_color": "lightgray"})
        mock_container.expander.assert_called_once_with("Show details", expanded=True)

    # Status Element Tests
    def test_success_component(self, mock_streamlit, mock_styler):
        """Test success component."""
        mock_st, mock_container = mock_streamlit

        result = elements.success("Operation completed!", color="green")

        mock_styler.apply_component_css.assert_called_with("success", {"color": "green"})
        mock_container.success.assert_called_once_with("Operation completed!")

    def test_error_component(self, mock_streamlit, mock_styler):
        """Test error component."""
        mock_st, mock_container = mock_streamlit

        result = elements.error("Something went wrong!", background_color="red")

        mock_styler.apply_component_css.assert_called_with("error", {"background_color": "red"})
        mock_container.error.assert_called_once_with("Something went wrong!")

    # Non-styled Component Tests (Pass-through)
    def test_write_stream_component(self, mock_streamlit, mock_styler):
        """Test write_stream (non-styled) component."""
        mock_st, mock_container = mock_streamlit

        def text_generator():
            yield "Hello "
            yield "World!"

        result = elements.write_stream(text_generator())

        # Should not call styler for non-styled elements
        mock_styler.apply_component_css.assert_not_called()
        mock_st.write_stream.assert_called_once()

    def test_dataframe_component(self, mock_streamlit, mock_styler):
        """Test dataframe (non-styled) component."""
        mock_st, mock_container = mock_streamlit

        df = pd.DataFrame({'X': [1, 2], 'Y': [3, 4]})
        result = elements.dataframe(df, use_container_width=True)

        # Should not call styler for non-styled elements
        mock_styler.apply_component_css.assert_not_called()
        mock_st.dataframe.assert_called_once_with(df, use_container_width=True)

    def test_columns_component(self, mock_streamlit, mock_styler):
        """Test columns (non-styled) component."""
        mock_st, mock_container = mock_streamlit

        result = elements.columns(3, gap="medium")

        # Should not call styler for non-styled elements
        mock_styler.apply_component_css.assert_not_called()
        mock_st.columns.assert_called_once_with(3, gap="medium")

    # Test component parameter preservation
    def test_component_preserves_streamlit_parameters(self, mock_streamlit, mock_styler):
        """Test that elements preserve standard Streamlit parameters."""
        mock_st, mock_container = mock_streamlit

        # Test with checkbox which has standard Streamlit parameters
        result = elements.checkbox(
            "Enable feature",
            value=True,
            help="Check to enable",
            disabled=False,
            color="blue"  # styling parameter
        )

        # Styler should be called with all parameters including styling
        mock_styler.apply_component_css.assert_called_with("checkbox", {
            "value": True,
            "help": "Check to enable",
            "disabled": False,
            "color": "blue"
        })

        # Streamlit component should be called with preserved parameters (styling removed by styler mock)
        mock_st.checkbox.assert_called_once_with(
            "Enable feature",
            value=True,
            help="Check to enable",
            disabled=False
        )

    def test_component_with_key_handling(self, mock_streamlit, mock_styler):
        """Test that elements handle key parameters correctly."""
        mock_st, mock_container = mock_streamlit

        # Configure styler to return a key - need to reset since other tests might have changed it
        def mock_apply_css_with_key(component_name, kwargs):
            return {"key": "test_key_123"}

        mock_styler.apply_component_css.side_effect = mock_apply_css_with_key

        result = elements.markdown("# Test", color="red")

        # Should call container with the key from styler
        mock_st.container.assert_called_once_with(key="test_key_123")

        # Should call markdown without the key (key is handled by container)
        mock_container.markdown.assert_called_once_with("# Test")


class TestComponentEdgeCases:
    """Test edge cases and error conditions for elements."""

    @pytest.fixture
    def mock_streamlit_error(self):
        """Mock streamlit that raises errors for testing."""
        with patch('st_yled.elements.st') as mock_st:
            mock_st.button.side_effect = Exception("Streamlit error")
            yield mock_st

    def test_component_handles_no_styling_parameters(self):
        """Test elements work without any styling parameters."""
        with patch('st_yled.elements.st') as mock_st, \
             patch('st_yled.elements.styler') as mock_styler:

            mock_container = Mock()
            mock_st.container.return_value = mock_container
            mock_styler.apply_component_css.return_value = {}

            result = elements.text("Plain text")  # No styling parameters

            mock_styler.apply_component_css.assert_called_with("text", {})
            mock_container.text.assert_called_once_with("Plain text")

    def test_component_with_only_styling_parameters(self):
        """Test elements with only styling parameters (no content)."""
        with patch('st_yled.elements.st') as mock_st, \
             patch('st_yled.elements.styler') as mock_styler:

            mock_container = Mock()
            mock_st.container.return_value = mock_container
            mock_styler.apply_component_css.return_value = {}

            result = elements.button(color="red")  # Only styling, no label

            mock_styler.apply_component_css.assert_called_with("button", {"color": "red"})
            mock_st.button.assert_called_once_with()

    def test_component_with_complex_data_structures(self):
        """Test elements can handle complex data structures."""
        with patch('st_yled.elements.st') as mock_st, \
             patch('st_yled.elements.styler') as mock_styler:

            mock_container = Mock()
            mock_st.container.return_value = mock_container
            mock_styler.apply_component_css.return_value = {}

            # Test with complex JSON data
            complex_data = {
                "users": [
                    {"id": 1, "name": "Alice", "settings": {"theme": "dark"}},
                    {"id": 2, "name": "Bob", "settings": {"theme": "light"}}
                ],
                "metadata": {"version": "1.0", "timestamp": "2024-01-01"}
            }

            result = elements.json(complex_data, background_color="white")

            mock_styler.apply_component_css.assert_called_with("json", {"background_color": "white"})
            mock_container.json.assert_called_once_with(complex_data)
