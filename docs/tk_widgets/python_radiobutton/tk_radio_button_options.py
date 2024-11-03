import tkinter as tk

window = tk.Tk()

widget = tk.Radiobutton(window)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option




'''
activebackground: SystemButtonFace
activeforeground: SystemWindowText
anchor: center
background: SystemButtonFace
bd: 2
bg: SystemButtonFace
bitmap:
borderwidth: 2
command:
compound: none
cursor:
disabledforeground: SystemDisabledText
fg: SystemWindowText
font: TkDefaultFont
foreground: SystemWindowText
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 1
image:
indicatoron: 1
justify: center
offrelief: raised
overrelief:
padx: 1
pady: 1
relief: flat
selectcolor: SystemWindow
selectimage:
state: normal
takefocus:
text:
textvariable:
tristateimage:
tristatevalue:
underline: -1
value:
variable: selectedButton
width: 0
wraplength: 0
'''
