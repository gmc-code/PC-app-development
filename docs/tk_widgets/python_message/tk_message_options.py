import tkinter as tk

root = tk.Tk()

widget = tk.Message(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option


'''
anchor: center
aspect: 150
background: SystemButtonFace
bd: 1
bg: SystemButtonFace
borderwidth: 1
cursor:
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 0
justify: left
padx: -1
pady: -1
relief: flat
takefocus: 0
text:
textvariable:
width: 0
'''