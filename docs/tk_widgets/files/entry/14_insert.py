# tk Entry - insert

import tkinter as tk


def fill_in():
    entry.delete(0, tk.END)         # Clear the box first
    entry.insert(0, "Parade")       # Then put in the new text


root = tk.Tk()
root.geometry("300x200")
root.title("insert")

entry = tk.Entry(root, font=("Arial", 16))
entry.insert(0, "Type here")        # Starting text
entry.pack(pady=20)

fill_button = tk.Button(root, text="Fill in", command=fill_in)
fill_button.pack()

root.mainloop()
