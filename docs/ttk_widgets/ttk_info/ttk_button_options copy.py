import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')

# Query elements structure layout configurations
print("Button Layout Structure:", style.layout("TButton"))

# Check default element options mapping configuration rules
print("Configured Options properties:", style.element_options("Button.label"))

'''

Button Layout Structure: [('Button.border', {'sticky': 'nswe', 'border': '1', 'children': [('Button.focus', {'sticky': 'nswe', 'children': [('Button.padding', {'sticky': 'nswe', 'children': [('Button.label', {'sticky': 'nswe'})]})]})]})]

Configured Options properties: ('compound', 'space', 'text', 'font', 'foreground', 'underline', 'width', 'anchor', 'justify', 'wraplength', 'embossed', 'image', 'stipple', 'background')
'''
