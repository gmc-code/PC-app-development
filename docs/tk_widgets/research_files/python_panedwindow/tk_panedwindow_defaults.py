import tkinter as tk

root = tk.Tk()

widget = tk.PanedWindow(root)

widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option




'''


background: SystemButtonFace
bd: 1
bg: SystemButtonFace
borderwidth: 1
cursor:
handlepad: 8
handlesize: 8
height:
opaqueresize: 1
orient: horizontal
proxybackground:
proxyborderwidth: 2
proxyrelief: flat
relief: flat
sashcursor:
sashpad: 0
sashrelief: flat
sashwidth: 3
showhandle: 0
width:


'''
