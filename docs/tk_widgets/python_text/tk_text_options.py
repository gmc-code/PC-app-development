import tkinter as tk

root = tk.Tk()

widget = tk.Text(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option

'''
autoseparators: 1
background: SystemWindow
bd: 1
bg: SystemWindow
blockcursor: 0
borderwidth: 1
cursor: xterm
endline:
exportselection: 1
fg: SystemWindowText
font: TkFixedFont
foreground: SystemWindowText
height: 24
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
inactiveselectbackground:
insertbackground: SystemWindowText
insertborderwidth: 0
insertofftime: 300
insertontime: 600
insertunfocussed: none
insertwidth: 2
maxundo: 0
padx: 1
pady: 1
relief: sunken
selectbackground: SystemHighlight
selectborderwidth: 0
selectforeground: SystemHighlightText
setgrid: 0
spacing1: 0
spacing2: 0
spacing3: 0
startline:
state: normal
tabs:
tabstyle: tabular
takefocus:
undo: 0
width: 80
wrap: char
xscrollcommand:
yscrollcommand:
'''
