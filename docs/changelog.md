# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v0.4.1 - [2026-04-10]

### Added
- Add css validation options to the init() file
- Add stylable st.menu_button coming with Streamlit v1.56

### Bugfix
- Custom CSS path work with traceback
- Small width of menu in st_yled.split_button


## v0.4.0 - [2026-03-16]

### Added

- Components: Tooltip Component
- New styling option: Label formatting for input containers
- Docsstrings with styling hints

### Bugfix
- Background Segmented Control: Formatting for background


## v0.3.0 - [2026-01-20]

### Added

- Components: split-button, redirect, badge card one, image card one, sticky header
- New styling option: Padding for st_yled.container and st_yled.expander
- New styling option: Label / value formatting for st_yled.metric
- Color converted module to lighten or darken colors

### Changed

- Extracting caller path for component key navigation
- All constants are in a separate module
- CSS validation exceptions for height property for components which support height by default
- Add a button category in components category

- Fix: Align font to icon for toggle and checkbox
- Fix: st.text: Define color, font weight and font size

### Removed

## v0.2.1 - [2025-12-05]

### Added

- st_yled.datetime_input wrapper to align with Streamlit 1.52

### Changed

- Fix: CSS targeting for title, header, subheader

### Removed


## v0.2.0 - [2025-12-03]

### Added

- font_weight argument to customize the font weight for element text
- st_yled.space wrapper to align with Streamlit 1.51

### Changed

- Fix: Font color for st_yled.code

### Removed


## v0.1.0 - [2025-10-31]

### Added

- First release with elements and theme styling

### Changed

### Removed
