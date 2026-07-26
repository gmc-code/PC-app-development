import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x200")

string_var = tk.StringVar()

entry = tk.Entry(root, textvariable=string_var)
entry.pack()

def upper_case_text():
    string_var.set(string_var.get().upper())

button = tk.Button(root, text="Upper case text", command=upper_case_text)
button.pack()

root.mainloop()