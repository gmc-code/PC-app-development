import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.title('Layout intro')
root.geometry('600x400')

# widgets
label1 = ttk.Label(root, text = 'Label 1', background = 'red')
label2 = ttk.Label(root, text = 'Label 2', background = 'blue')

# pack
# label1.pack(side = 'left', expand = True, fill = 'y')
# label2.pack(side = 'left', expand = True, fill = 'both')

# grid
# root.columnconfigure(0, weight = 1)
# root.columnconfigure(1, weight = 1)
# root.columnconfigure(2, weight = 2)
# root.rowconfigure(0, weight = 1)
# root.rowconfigure(1, weight = 1)

# label1.grid(row = 0, column = 1, sticky = 'nsew')
# label2.grid(row = 1, column = 1, columnspan = 2, sticky = 'nsew')

# place
label1.place(x = 100 , y = 200, width = 200, height = 100)
label2.place(relx = 0.5, rely = 0.5, relwidth = 0.4, anchor = 'se')

# Start the main event loop
root.mainloop()