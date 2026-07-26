import tkinter as tk

def update_label():
    selected_value = int_var.get()
    if selected_value == 1:
        label.config(text="Option 1 selected")
    elif selected_value == 2:
        label.config(text="Option 2 selected")

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x200")

int_var = tk.IntVar()

radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=int_var, value=1, command=update_label)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=int_var, value=2, command=update_label)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

label = tk.Label(root, text="No option selected", font=("Helvetica", 16))
label.pack(pady=20)

root.mainloop()
