import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

# The style we want to inspect
style_name = "TButton"

def get_prefixed_style_options(style_obj, name):
    # Use a dictionary to map element prefixes to their respective options
    prefixed_options = {}

    # 1. Get the layout tree of the widget
    try:
        layout = style_obj.layout(name)
    except tk.TclError:
        print(f"Style '{name}' not found.")
        return {}

    # 2. Helper function to recursively parse the layout tree
    def parse_layout(node):
        if not node:
            return
        for item in node:
            if isinstance(item, str):
                # item is the element name, e.g., 'Button.border' or 'Button.label'
                element_opts = style_obj.element_options(item)
                if element_opts:
                    # Clean up or keep the exact element name as the prefix key
                    prefixed_options[item] = sorted(list(element_opts))

            elif isinstance(item, (list, tuple)):
                parse_layout(item)
            elif isinstance(item, dict):
                if 'children' in item:
                    parse_layout(item['children'])

    parse_layout(layout)
    return prefixed_options

# Get the dictionary of prefixed options
all_prefixed_options = get_prefixed_style_options(style, style_name)

print(f"=== Complete List of Customization Options for {style_name} ===")
for element_prefix, options in all_prefixed_options.items():
    print(f"\n[{element_prefix}]")
    for opt in options:
        print(f"  - {opt}")





'''
[Button.border]
  - bordercolor
  - borderwidth
  - darkcolor
  - lightcolor
  - relief

[Button.focus]
  - focuscolor
  - focussolid
  - focusthickness

[Button.padding]
  - padding
  - relief
  - shiftrelief

[Button.label]
  - anchor
  - background
  - compound
  - embossed
  - font
  - foreground
  - image
  - justify
  - space
  - stipple
  - text
  - underline
  - width
  - wraplength

'''

