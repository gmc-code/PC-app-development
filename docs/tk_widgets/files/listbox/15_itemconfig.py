# tk Listbox - itemconfig

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("itemconfig")

result_list = tk.Listbox(root, height=4)
for result in ["Maths: pass", "English: pass", "Science: fail"]:
    result_list.insert(tk.END, result)
result_list.itemconfig(2, fg="red")        # Make item 2 red
result_list.pack(pady=10)

root.mainloop()
