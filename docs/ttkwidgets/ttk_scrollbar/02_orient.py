# ttk Scrollbar - orient

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("orient")

across = ttk.Scrollbar(root, orient="horizontal")
across.pack(side="bottom", fill="x")

long_text = tk.Text(root, wrap="none", xscrollcommand=across.set)
long_text.pack(fill="both", expand=True)
across.config(command=long_text.xview)

long_text.insert("1.0", "This line is much too long to fit, so you need to scroll sideways "
                        "to read all of it. Keep going... nearly there... the end!")

root.mainloop()
