import tkinter as tk


def update_label():
    if int_var.get() == 1:
        label.config(text="Checked!")
    else:
        label.config(text="Unchecked!")


root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("300x200")

int_var = tk.IntVar()

checkbutton = tk.Checkbutton(root, text="Check me", font=("Helvetica", 16), variable=int_var, command=update_label)
checkbutton.pack(pady=10)

label = tk.Label(root, text="Unchecked", font=("Helvetica", 16))
label.pack(pady=10)

root.mainloop()
