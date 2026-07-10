import tkinter as tk

root = tk.Tk()

labelframe = tk.LabelFrame(root)
labelframe_options = labelframe.keys()

for option in labelframe_options:
    print(f"{option}: {labelframe.cget(option)}")


'''
bd: 2
borderwidth: 2
class: Labelframe
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
labelanchor: nw
labelwidget:
relief: groove
text:
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
