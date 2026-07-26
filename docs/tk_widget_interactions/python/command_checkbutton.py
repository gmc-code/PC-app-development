import tkinter as tk


def change_text():
    label.config(text="Button pressed!")


root = tk.Tk()
root.geometry("200x100")  # Set window size
root.title("Button -> label Example")  # Set window title

selected = tk.IntVar()

def update():
    if selected.get():
        label.config(text="Checked")
    else:
        label.config(text="Unchecked")

check = tk.Checkbutton(root,
                        text="Option",
                        variable=selected,
                        command=update)

label = tk.Label(root, text="Unchecked")

check.pack()
label.pack()

root.mainloop()
