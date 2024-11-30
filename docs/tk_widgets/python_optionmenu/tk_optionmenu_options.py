import tkinter as tk

# Create the main window
root = tk.Tk()

# Define a variable to hold the selected option
selected_option = tk.StringVar(root)

# Define the options for the OptionMenu
options = ["Option 1", "Option 2", "Option 3"]

# Set the default value for the OptionMenu
selected_option.set(options[0])

# Create the OptionMenu widget
widget = tk.OptionMenu(root, selected_option, *options)

# Pack the widget into the window
widget.pack()

# Retrieve and print the current configuration options of the widget
widget_options = widget.keys()
for option in widget_options:
    print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option




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
text: Option 1
textvariable: PY_VAR0
underline: -1
width: 0
wraplength: 0
'''
