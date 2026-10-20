# tk Entry - delete

import tkinter as tk


def clear():
    entry.delete(0, tk.END)     # Remove all the text


root = tk.Tk()
root.geometry("300x200")
root.title("delete")

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=20)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

root.mainloop()
