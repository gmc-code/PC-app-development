# tk LabelFrame - bg (background colour)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("bg")

notes = tk.LabelFrame(root, text="Notes", bg="lightyellow", padx=10, pady=10)
notes.pack(pady=20)

tk.Label(notes, text="Bring a hat tomorrow", bg="lightyellow").pack()

root.mainloop()
