# import tkinter as tk

# window = tk.Tk()

# button = tk.Button(window)
# button_options = button.keys()

# for option in button_options:
#     print(option, end=", ")

"""
activebackground, activeforeground, anchor, background, bd, bg, bitmap, borderwidth, command, compound, cursor, default, disabledforeground, fg, font, foreground, height, highlightbackground, highlightcolor, highlightthickness, image, justify, overrelief, padx, pady, relief, repeatdelay, repeatinterval, state, takefocus, text, textvariable, underline, width, wraplength,
"""
import tkinter as tk

window = tk.Tk()

button = tk.Button(window)
button_options = button.keys()

for option in button_options:
    print(f"{option}: {button.cget(option)}")



# This also prints the default value for each option
''''
activebackground: SystemButtonFace
activeforeground: SystemButtonText
anchor: center
background: SystemButtonFace
bd: 2
bg: SystemButtonFace
bitmap:
borderwidth: 2
command:
compound: none
cursor:
default: disabled
disabledforeground: SystemDisabledText
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 1
image:
justify: center
overrelief:
padx: 1
pady: 1
relief: raised
repeatdelay: 0
repeatinterval: 0
state: normal
takefocus:
text:
textvariable:
underline: -1
width: 0
wraplength: 0
'''
