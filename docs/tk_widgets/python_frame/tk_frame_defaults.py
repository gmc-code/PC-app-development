import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame_options = frame.keys()

for option in frame_options:
    print(f"{option}: {frame.cget(option)}")



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
