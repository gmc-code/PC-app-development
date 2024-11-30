import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.title('Grid')
root.geometry('600x400')

# widgets
label1 = ttk.Label(root, text = 'Label 1', background = 'red')
label2 = ttk.Label(root, text = 'Label 2', background = 'blue')
label3 = ttk.Label(root, text = 'Label 3', background = 'green')
label4 = ttk.Label(root, text = 'Label 4', background = 'yellow')
button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')
entry = ttk.Entry(root)

# define a grid
# root.columnconfigure((0,1,2), weight = 1, uniform = 'a')
# root.columnconfigure(3, weight = 2, uniform = 'a')
# root.rowconfigure(0, weight = 1, uniform = 'a')
# root.rowconfigure(1, weight = 1, uniform = 'a')
# root.rowconfigure(2, weight = 1, uniform = 'a')
# root.rowconfigure(3, weight = 3, uniform = 'a')

# place a widget
label1.grid(row = 0, column = 0, sticky = 'nsew')
label2.grid(row = 1, column = 1, rowspan = 3, sticky = 'nsew')
label3.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 20, pady = 10)
label4.grid(row = 3, column = 3, sticky = 'se')

# exercise
# add the buttons and the entry field
button1.grid(row = 0, column = 3, sticky = 'nesw')
button2.grid(row = 2, column = 2, sticky = 'nesw')
entry.grid(row = 2, column = 3, rowspan = 2, sticky = 'ew')


# run
root.mainloop()