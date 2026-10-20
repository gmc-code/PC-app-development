import tkinter as tk

root = tk.Tk()

widget = tk.Scale(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option





'''

activebackground: SystemButtonFace
background: SystemButtonFace
bigincrement: 0.0
bd: 1
bg: SystemButtonFace
borderwidth: 1
command:
cursor:
digits: 0
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
from: 0.0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 2
label:
length: 100
orient: vertical
relief: flat
repeatdelay: 300
repeatinterval: 100
resolution: 1.0
showvalue: 1
sliderlength: 30
sliderrelief: raised
state: normal
takefocus:
tickinterval: 0.0
to: 100.0
troughcolor: SystemScrollbar
variable:
width: 15

'''
