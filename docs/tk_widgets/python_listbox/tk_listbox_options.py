import tkinter as tk

window = tk.Tk()

widget = tk.Listbox(window)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option

'''
activestyle: underline
background: SystemWindow
bd: 1
bg: SystemWindow
borderwidth: 1
cursor:
disabledforeground: SystemDisabledText
exportselection: 1
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
height: 10
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 1
justify: left
relief: sunken
selectbackground: SystemHighlight
selectborderwidth: 0
selectforeground: SystemHighlightText
selectmode: browse
setgrid: 0
state: normal
takefocus:
width: 20
xscrollcommand:
yscrollcommand:
listvariable:
'''
