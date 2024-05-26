import tkinter as tk

window = tk.Tk()
window.geometry("250x170")

# Create a Text widget
text_widget = tk.Text(window, height=5, width=52)
text_widget.insert(tk.END, "Some sample text.")

# Get all the options and their values
options = text_widget.config()

# Print the options
for option, value in options.items():
    # print(f"{option}: {value}")
    print(f"{option}")

window.mainloop()

'''
autoseparators
background
bd
bg
blockcursor
borderwidth
cursor
endline
exportselection
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
inactiveselectbackground
insertbackground
insertborderwidth
insertofftime
insertontime
insertunfocussed
insertwidth
maxundo
padx
pady
relief
selectbackground
selectborderwidth
selectforeground
setgrid
spacing1
spacing2
spacing3
startline
state
tabs
tabstyle
takefocus
undo
width
wrap
xscrollcommand
yscrollcommand
'''
