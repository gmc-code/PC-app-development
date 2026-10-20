import tkinter as tk

root = tk.Tk()

widget = tk.Toplevel(root)

widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")


'''

bd: 0
borderwidth: 0
class: Toplevel
menu:
relief: flat
screen:
use:
background: SystemButtonFace
bg: SystemButtonFace
colormap:
container: 0
cursor:
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
padx: 0
pady: 0
takefocus: 0
visual:


'''
