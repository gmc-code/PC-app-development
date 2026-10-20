import tkinter as tk

root = tk.Tk()

widget = tk.Spinbox(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option



'''

activebackground: SystemButtonFace
background: SystemWindow
bd: 1
bg: SystemWindow
borderwidth: 1
buttonbackground: SystemButtonFace
buttoncursor:
buttondownrelief: raised
buttonuprelief: raised
command:
cursor: xterm
disabledbackground: SystemButtonFace
disabledforeground: SystemDisabledText
exportselection: 1
fg: SystemWindowText
font: TkTextFont
foreground: SystemWindowText
format:
from: 0.0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
increment: 1.0
insertbackground: SystemWindowText
insertborderwidth: 0
insertofftime: 300
insertontime: 600
insertwidth: 2
invalidcommand:
invcmd:
justify: left
relief: sunken
readonlybackground: SystemButtonFace
repeatdelay: 400
repeatinterval: 100
selectbackground: SystemHighlight
selectborderwidth: 0
selectforeground: SystemHighlightText
state: normal
takefocus:
textvariable:
to: 0.0
validate: none
validatecommand:
values:
vcmd:
width: 20
wrap: 0
xscrollcommand:

'''
