import tkinter as tk


def update_label():
    # Update the label with the current value of the Spinbox
    label.config(text=f"Current Value: {int_var.get()}")


root = tk.Tk()
root.title("Spinbox Example 2")
root.geometry("300x200")

# Create an IntVar with an initial value
int_var = tk.IntVar(value=0)

# Create a Spinbox and associate it with the IntVar
spinbox = tk.Spinbox(root, from_=-10, to=10, increment=2, font=("Helvetica", 16), width=5, textvariable=int_var, command=update_label)
spinbox.pack(pady=5)

# Create a Label to display the current value of the Spinbox
label = tk.Label(root, text=f"Current Value: {int_var.get()}", font=("Helvetica", 16))
label.pack(pady=5)

root.mainloop()
