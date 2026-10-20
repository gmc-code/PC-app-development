# tk Toplevel - destroy

import tkinter as tk


def open_window():
    pop_up = tk.Toplevel(root)
    pop_up.title("Message")
    pop_up.geometry("250x120")
    tk.Label(pop_up, text="Your work has been saved.").pack(pady=20)
    tk.Button(pop_up, text="Close", command=pop_up.destroy).pack()


root = tk.Tk()
root.geometry("300x200")
root.title("destroy")

tk.Button(root, text="Save", command=open_window).pack(pady=60)

root.mainloop()
