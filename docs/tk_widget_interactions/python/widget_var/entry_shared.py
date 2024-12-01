import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Tkinter Widget Interaction Examples")

# Example 1: Variable Binding
shared_var = tk.StringVar()
entry = tk.Entry(root, font=("Helvetica", 16), justify="left", width=20, textvariable=shared_var)
entry.pack()
label = tk.Label(root, font=("Helvetica", 16), anchor="w", width=20, bg='yellow', textvariable=shared_var)
label.pack()


root.mainloop()