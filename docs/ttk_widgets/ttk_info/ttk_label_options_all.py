import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')

# The style we want to inspect
style_name = "TLabel"

def get_all_style_options(style_obj, name):
    options = set()

    # 1. Get the layout layout tree of the widget
    try:
        layout = style_obj.layout(name)
    except tk.TclError:
        print(f"Style '{name}' not found.")
        return []

    # 2. Helper function to recursively parse the layout tree
    def parse_layout(node):
        if not node:
            return
        for item in node:
            if isinstance(item, str):
                # Found an element name (e.g., 'Button.label')
                # Extract all options configurable for this specific element
                element_opts = style_obj.element_options(item)
                options.update(element_opts)
            elif isinstance(item, list) or isinstance(item, tuple):
                parse_layout(item)
            elif isinstance(item, dict):
                if 'children' in item:
                    parse_layout(item['children'])

    parse_layout(layout)
    return sorted(list(options))

# Get and print the complete list
all_options = get_all_style_options(style, style_name)

print(f"=== Complete List of Customization Options for {style_name} ===")
for opt in all_options:
    print(f" - {opt}")



'''

Label Layout Structure: [('Label.border', {'sticky': 'nswe', 'border': '1', 'children': [('Label.padding', {'sticky': 'nswe', 'border': '1', 'children': [('Label.label', {'sticky': 'nswe'})]})]})]

label Options: ('compound', 'space', 'text', 'font', 'foreground', 'underline', 'width', 'anchor', 'justify', 'wraplength', 'embossed', 'image', 'stipple', 'background')

padding Options: ('padding', 'relief', 'shiftrelief')

border Options: ('bordercolor', 'lightcolor', 'darkcolor', 'relief', 'borderwidth')


- anchor
- background
- bordercolor
- borderwidth
- compound
- darkcolor
- embossed
- font
- foreground
- image
- justify
- lightcolor
- padding
- relief
- shiftrelief
- space
- stipple
- text
- underline
- width
- wraplength
'''
