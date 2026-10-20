import tkinter as tk

root = tk.Tk()

variable = tk.StringVar(value="One")
option_menu = tk.OptionMenu(root, variable, "One", "Two")

for option in option_menu.keys():
    print(f"{option}: {option_menu.cget(option)}")


'''
activebackground: SystemButtonFace
activeforeground: SystemButtonText
anchor: center
background: SystemButtonFace
bd: 2
bg: SystemButtonFace
bitmap:
borderwidth: 2
cursor:
direction: below
disabledforeground: SystemDisabledText
fg: SystemButtonText
font: TkDefaultFont
foreground: SystemButtonText
height: 0
highlightbackground: SystemButtonFace
highlightcolor: SystemWindowFrame
highlightthickness: 2
image:
indicatoron: 1
justify: center
menu: .!optionmenu.menu
padx: 5
pady: 4
relief: raised
compound: none
state: normal
takefocus: 0
text:
textvariable: PY_VAR0
underline: -1
width: 0
wraplength: 0
'''
