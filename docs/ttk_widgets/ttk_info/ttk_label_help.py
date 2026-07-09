import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')

# Query elements structure layout configurations
print("Label Layout Structure:", style.layout("TLabel"))

# Check default element options mapping configuration rules
print("label Options:", style.element_options("TLabel.label"))
print("padding Options:", style.element_options("TLabel.padding"))
print("border Options:", style.element_options("TLabel.border"))


print("All options:", TLabel.keys())
'''
Label Layout Structure: [('Label.border', {'sticky': 'nswe', 'border': '1', 'children': [('Label.padding', {'sticky': 'nswe', 'border': '1', 'children': [('Label.label', {'sticky': 'nswe'})]})]})]

label Options: ('compound', 'space', 'text', 'font', 'foreground', 'underline', 'width', 'anchor', 'justify', 'wraplength', 'embossed', 'image', 'stipple', 'background')

padding Options: ('padding', 'relief', 'shiftrelief')

border Options: ('bordercolor', 'lightcolor', 'darkcolor', 'relief', 'borderwidth')

'''