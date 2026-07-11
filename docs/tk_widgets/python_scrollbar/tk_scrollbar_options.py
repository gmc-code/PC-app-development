import tkinter as tk

root = tk.Tk()

widget = tk.Scrollbar(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option


'''

activebackground: SystemButtonFace
activerelief: raised
background: SystemButtonFace
bd: 0
bg: SystemButtonFace
borderwidth: 0
command:
cursor:
elementborderwidth: -1
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
jump: 0
orient: vertical
relief: sunken
repeatdelay: 300
repeatinterval: 100
takefocus:
troughcolor: SystemScrollbar
width: 17

'''
