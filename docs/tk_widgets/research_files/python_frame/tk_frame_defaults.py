import tkinter as tk

root = tk.Tk()

widget = tk.Frame(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option


'''
bd: 0
borderwidth: 0
class: Frame
relief: flat
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
width: 0

'''
