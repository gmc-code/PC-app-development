import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("400x400")  # Set window size
window.title("Label Testing")  # Set window title

# Create the label widget
label = tk.Label(window, text="label text")

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
justify
padx
pady
relief
state
takefocus
text
textvariable
underline
width
wraplength
'''
