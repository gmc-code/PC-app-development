import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()

# Force a theme that uses manual engine shading to see all properties clearly
style.theme_use('clam')

# 1. Create a dummy entry to get all available direct keys
entry = ttk.Entry(root)
entry_options = entry.keys()

print("=== True Default Style Values for TEntry ===")
for option in entry_options:
    # Use style.lookup to find what the active theme is actually using
    default_value = style.lookup("TEntry", option)

    # If style.lookup returns nothing, fallback to the widget's native configuration
    if default_value == "":
        default_value = entry.cget(option)

    print(f"{option}: {default_value}")


'''
exportselection: 1
font: TkDefaultFont
invalidcommand:
justify: left
show:
state: normal
textvariable:
validate: none
validatecommand:
width: 20
xscrollcommand:
foreground: black
background: #dcdad5
takefocus: ttk::takefocus
cursor: ibeam
style:
class:


'''