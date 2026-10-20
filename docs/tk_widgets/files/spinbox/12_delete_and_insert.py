# tk Spinbox - delete and insert

import tkinter as tk


def reset():
    lives_spinbox.delete(0, tk.END)
    lives_spinbox.insert(0, "3")


root = tk.Tk()
root.geometry("300x200")
root.title("delete and insert")

lives_spinbox = tk.Spinbox(root, from_=0, to=9, width=5, font=("Arial", 16))
lives_spinbox.pack(pady=10)

reset_button = tk.Button(root, text="Reset to 3 lives", command=reset)
reset_button.pack()

root.mainloop()
