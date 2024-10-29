import tkinter as tk

window = tk.Tk()
window.geometry("250x170")

# Create a Text widget
widget = tk.Checkbutton(window, text="Checkbutton")

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
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
indicatoron
justify
offrelief
offvalue
onvalue
overrelief
padx
pady
relief
selectcolor
selectimage
state
takefocus
text
textvariable
tristateimage
tristatevalue
underline
variable
width
wraplength
'''
