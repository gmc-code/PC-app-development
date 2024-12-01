import tkinter as tk

root = tk.Tk()
root.title("Label Example")
root.geometry("300x200")

string_var = tk.StringVar()
string_var.set("Hello, Tkinter!")

label = tk.Label(root, textvariable=string_var)
label.pack()

root.mainloop()
