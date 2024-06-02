import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)

# Configuring the first column
frame.columnconfigure(0, weight=1, minsize=100, uniform="group1", pad=5)

# Configuring the second column
frame.columnconfigure(1, weight=2, minsize=50, uniform="group1", pad=10)

# Adding widgets to the frame
label1 = tk.Label(frame, text="Column 1")
label2 = tk.Label(frame, text="Column 2")

label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)

frame.pack()
root.mainloop()
