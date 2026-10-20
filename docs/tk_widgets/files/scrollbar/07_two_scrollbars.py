# tk Scrollbar - Two scrollbars

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Two scrollbars")

down_bar = tk.Scrollbar(root, orient="vertical")
down_bar.pack(side="right", fill="y")

across_bar = tk.Scrollbar(root, orient="horizontal")
across_bar.pack(side="bottom", fill="x")

grid_box = tk.Text(root, wrap="none",
                   yscrollcommand=down_bar.set, xscrollcommand=across_bar.set)
grid_box.pack(side="left", fill="both", expand=True)

down_bar.config(command=grid_box.yview)
across_bar.config(command=grid_box.xview)

for row in range(1, 41):
    grid_box.insert(tk.END, f"Row {row}: " + "x " * 60 + "\n")

root.mainloop()
