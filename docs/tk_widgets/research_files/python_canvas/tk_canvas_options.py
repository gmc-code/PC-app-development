import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root)

for option in canvas.keys():
    print(f"{option}: {canvas.cget(option)}")

# root.mainloop()



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
