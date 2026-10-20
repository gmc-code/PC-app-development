# tk Listbox - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

day_list = tk.Listbox(root, relief="solid", borderwidth=2, height=5)
for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
    day_list.insert(tk.END, day)
day_list.pack(pady=10)

root.mainloop()
