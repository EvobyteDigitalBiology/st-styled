import json
import os
import streamlit as st
import uuid


dirpath = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dirpath, "component_styles.json")) as f:
    COMPONENT_STYLES = json.load(f)

def get_css_properties_from_args(component_type: str, component_kwargs: dict):

    css_properties = {}
    if component_type in COMPONENT_STYLES:
        
        # Return dict of css properties and selectors for component
        style_mappings = COMPONENT_STYLES[component_type]

        args_to_remove = []

        # Loop over component arguments and check if those are in style mappings
        for comp_arg, comp_val in component_kwargs.items():
            
            # Comp arg eg.g background_color
            if comp_arg in style_mappings:

                args_to_remove.append(comp_arg)
                # Get css selectors for css property as a dict
                # Return dict with selector and css properties like:
                # ".stButton > button": {
                #    "background-color": null
                #    }
                # [css_selector][css_property][css_value or None]

                css_for_selectors = style_mappings[comp_arg]

                # [css_selector] > dict(css_property: css_value or None)
                for sel, sel_css in css_for_selectors.items():
                    
                    # Update css values for selector. If css_value is set, then take over, else set comp_val
                    new_sel_css = {}
                    for k, v in sel_css.items():
                        if v is None:
                            new_sel_css[k] = component_kwargs[comp_arg]
                        else:
                            new_sel_css[k] = v

                    if sel in css_properties:
                        css_properties[sel].update(new_sel_css)
                    else:
                        css_properties[sel] = new_sel_css

    else:
        raise ValueError(f"Component type '{component_type}' not found. Are you sure this component exists?")

    # Remove any args that were used for styling
    for arg in args_to_remove:
        del component_kwargs[arg]

    return css_properties


def generate_component_css(component_type: str, component_kwargs: dict, component_key: str | None):
    
    css_properties = get_css_properties_from_args(component_type, component_kwargs)
    
    if css_properties:

        css_rules = []
        for selector, properties in css_properties.items():
            
            if component_key is None:
                selector_plus_key = selector
            else:
                selector_plus_key = '.st-key-' + component_key + ' ' + selector

            rules = [f"    {prop}: {val} !important;" for prop, val in properties.items()]
            rules_str = "\n".join(rules)
            css_rule = f"{selector_plus_key} {{\n{rules_str}\n}}"
            css_rules.append(css_rule)
        
        return "\n".join(css_rules)
    
    else:
        return ""


def apply_component_css(component_type: str, kwargs: dict):
    
    if "key" not in kwargs:
        kwargs["key"] = 'st-yler-' + str(uuid.uuid4())

    css = generate_component_css(component_type, kwargs, kwargs['key'])

    if css:
        st.html(f"<style>{css}</style>")

    return kwargs

def apply_component_css_global(component_type: str, component_kwargs: dict):
    """Apply global CSS styles to all components."""
    
    for styled_prop, value in component_kwargs.items():
        component_kwargs = {styled_prop: value}
        css = generate_component_css(component_type, component_kwargs, None)
        if css:
            # Apply CSS globally without key
            # This will affect all components of this type
            st.html(f"<style>{css}</style>")
        else:
            if '-' in styled_prop:
                did_you_mean_ext = styled_prop.replace('-', '_')
                did_you_mean_ext = f"Did you mean '{did_you_mean_ext}'?"
            else:
                did_you_mean_ext = ''

            raise ValueError(f"No st_yled property {styled_prop} found for component type '{component_type}'. {did_you_mean_ext}")