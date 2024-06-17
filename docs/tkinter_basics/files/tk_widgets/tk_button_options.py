import tkinter as tk

window = tk.Tk()
window.geometry("250x170")

# Create a Text widget
widget = tk.Button(window, text="Button")

# Get all the options and their values
options = widget.config()

# Print the options
for option, value in options.items():
    # print(f"{option}: {value}")
    print(f"{option}")

window.mainloop()

'''
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
command
compound
cursor
default
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
justify
overrelief
padx
pady
relief
repeatdelay
repeatinterval
state
takefocus
text
textvariable
underline
width
wraplength
'''
