import tkinter as tk

window = tk.Tk()
window.geometry("250x170")

# Create an Entry widget
entry_widget = tk.Entry(window)

# Get all the options and their values
options = entry_widget.config()

# Print the options
for option, value in options.items():
    # print(f"{option}: {value}")
    print(f"{option}")

window.mainloop()

'''
background
bd
bg
borderwidth        
cursor
disabledbackground 
disabledforeground 
exportselection    
fg
font
foreground
highlightbackground
highlightcolor     
highlightthickness 
insertbackground   
insertborderwidth  
insertofftime      
insertontime       
insertwidth        
invalidcommand
invcmd
justify
readonlybackground
relief
selectbackground
selectborderwidth
selectforeground
show
state
takefocus
textvariable
validate
validatecommand
vcmd
width
xscrollcommand
'''
