import tkinter as tk

root = tk.Tk()

widget = tk.Menu(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option




'''

activebackground: SystemHighlight
activeborderwidth: 1
activeforeground: SystemHighlightText
background: SystemMenu
bd: 1
bg: SystemMenu
borderwidth: 1
cursor: arrow
disabledforeground: SystemDisabledText
fg: SystemMenuText
font: {Segoe UI} 9
foreground: SystemMenuText
postcommand:
relief: flat
selectcolor: SystemMenuText
takefocus: 0
tearoff: 1
tearoffcommand:
title:
type: normal

'''
