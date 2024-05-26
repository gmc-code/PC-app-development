import tkinter as tk

window = tk.Tk()
window.geometry("250x170")

# Get all the options and their values
options = window.config()

# Print the options
for option, value in options.items():
    # print(f"{option}: {value}")
    print(f"{option}")

window.mainloop()

'''
bd
borderwidth
class
menu
relief
screen
use
background
bg
colormap
container
cursor
height
highlightbackground
highlightcolor
highlightthickness
padx
pady
takefocus
visual
width
'''
