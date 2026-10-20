import tkinter as tk

root = tk.Tk()

widget = tk.Menubutton(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option




'''

activebackground: SystemButtonFace
activeforeground: SystemButtonText
anchor: center
background: SystemButtonFace
bd: 1
bg: SystemButtonFace
bitmap:
borderwidth: 1
cursor:
direction: below
disabledforeground: SystemDisabledText
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
image:
indicatoron: 0
justify: center
menu:
padx: 5
pady: 4
relief: flat
compound: none
state: normal
takefocus: 0
text:
textvariable:
underline: -1
width: 0
wraplength: 0

'''
