import tkinter as tk

window = tk.Tk()

widget = tk.Label(window)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option

'''
activebackground: SystemButtonFace
activeforeground: SystemButtonText
anchor: center
background: SystemButtonFace
bd: 2
bg: SystemButtonFace
bitmap:
borderwidth: 2
compound: none
cursor:
disabledforeground: SystemDisabledText
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
image:
justify: center
padx: 1
pady: 1
relief: flat
state: normal
takefocus: 0
text:
textvariable:
underline: -1
width: 0
wraplength: 0
'''
