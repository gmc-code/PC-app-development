# import tkinter as tk

# root = tk.Tk()
# widget_options = root.keys()

# print("Available options for the widget:")
# for option in widget_options:
#     print(option)


import tkinter as tk

root = tk.Tk()
root.geometry("250x170")

# Get all the options and their values
options = root.config()

# Print the options
for option, value in options.items():
    print(f"{option}: {value}")
    #print(f"{option}")

#root.mainloop()

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
