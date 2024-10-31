import tkinter as tk
from tkinter import font

window = tk.Tk()

# Create a temporary button to get the system colors
button = tk.Button(window)

# Get the system-defined colors for `SystemButtonFace` and `SystemButtonText`
system_button_face = window.winfo_rgb(button.cget("background"))
system_button_text = window.winfo_rgb(button.cget("foreground"))
# Get the `highlightcolor` in system-defined color (e.g., SystemWindowFrame)
highlight_color = window.winfo_rgb(button.cget("highlightcolor"))
# Get the disabledforeground: SystemDisabledText
disabledforeground_color = window.winfo_rgb(button.cget("disabledforeground"))

# Convert the RGB values from 16-bit to 8-bit format
system_button_face_rgb = tuple(value // 256 for value in system_button_face)
system_button_text_rgb = tuple(value // 256 for value in system_button_text)
highlight_color_rgb = tuple(value // 256 for value in highlight_color)
disabledforeground_color_rgb =  tuple(value // 256 for value in disabledforeground_color)

print("SystemButtonFace RGB:", system_button_face_rgb)
print("SystemButtonText RGB:", system_button_text_rgb)
print("SystemWindowFrame (highlightcolor) RGB:", highlight_color_rgb)
print("SystemDisabledText (disabledforeground) RGB:", disabledforeground_color_rgb)

# Get the default font using the font module
default_font = font.nametofont("TkDefaultFont")

# Retrieve font properties
font_family = default_font.actual("family")
font_size = default_font.actual("size")
font_weight = default_font.actual("weight")
font_slant = default_font.actual("slant")

# Print out the default font properties
print("Default Font Family:", font_family)
print("Default Font Size:", font_size)
print("Default Font Weight:", font_weight)
print("Default Font Slant:", font_slant)

window.destroy()

''''
SystemButtonFace RGB: (240, 240, 240)
SystemButtonText RGB: (0, 0, 0)
SystemWindowFrame (highlightcolor) RGB: (100, 100, 100)
SystemDisabledText (disabledforeground) RGB: (109, 109, 109)

Default Font Family: Segoe UI
Default Font Size: 9
Default Font Weight: normal
Default Font Slant: roman

'''
