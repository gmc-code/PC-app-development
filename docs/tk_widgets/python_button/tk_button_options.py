import tkinter as tk

root = tk.Tk()

widget = tk.Button(root)
widget_options = widget.keys()

for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option

# widget2 = tk.Frame(root)
# in1 = set(widget.configure().keys()) - set(widget2.configure().keys())
# for option in in1:
#     print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option

# print(set(dir(widget)) - set(dir(widget2)))
# {'flash', 'invoke'}

''''
activebackground: SystemButtonFace
activeforeground: SystemButtonText
anchor: center
background: SystemButtonFace
bd: 2
bg: SystemButtonFace
bitmap:
borderwidth: 2
command:
compound: none
cursor:
default: disabled
disabledforeground: SystemDisabledText
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 1
image:
justify: center
overrelief:
padx: 1
pady: 1
relief: raised
repeatdelay: 0
repeatinterval: 0
state: normal
takefocus:
text:
textvariable:
underline: -1
width: 0
wraplength: 0
'''
