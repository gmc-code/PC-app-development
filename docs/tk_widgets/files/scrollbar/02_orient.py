# tk Scrollbar - orient

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("orient")

scrollbar = tk.Scrollbar(root, orient="horizontal")
scrollbar.pack(side="bottom", fill="x")             # Along the bottom, full width

long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
long_text.pack(fill="both", expand=True)

scrollbar.config(command=long_text.xview)

long_text.insert("1.0", "This line is much too long to fit in the window, "
                        "so you need to scroll sideways to read all of it.")

root.mainloop()
