# tk Listbox - fg and bg (colours)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg and bg")

planet_list = tk.Listbox(root, fg="white", bg="darkblue", height=5)
for planet in ["Mercury", "Venus", "Earth", "Mars"]:
    planet_list.insert(tk.END, planet)
planet_list.pack(pady=10)

root.mainloop()
