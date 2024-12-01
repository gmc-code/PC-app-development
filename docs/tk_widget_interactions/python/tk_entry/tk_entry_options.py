import tkinter as tk

root = tk.Tk()

widget = tk.Entry(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option


'''
background: SystemWindow
bd: 1
bg: SystemWindow
borderwidth: 1
cursor: xterm
disabledbackground: SystemButtonFace
disabledforeground: SystemDisabledText
exportselection: 1
fg: SystemWindowText
font: TkTextFont
foreground: SystemWindowText
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
insertbackground: SystemWindowText
insertborderwidth: 0
insertofftime: 300
insertontime: 600
insertwidth: 2
invalidcommand:
invcmd:
justify: left
readonlybackground: SystemButtonFace
relief: sunken
selectbackground: SystemHighlight
selectborderwidth: 0
selectforeground: SystemHighlightText
show:
state: normal
takefocus:
textvariable:
validate: none
validatecommand:
vcmd:
width: 20
xscrollcommand:
'''