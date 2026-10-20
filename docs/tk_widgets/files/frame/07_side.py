# tk Frame - side

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("A row of buttons")

button_row = tk.Frame(root)
button_row.pack(pady=20)

tk.Button(button_row, text="Back", width=8).pack(side="left", padx=5)
tk.Button(button_row, text="Home", width=8).pack(side="left", padx=5)
tk.Button(button_row, text="Next", width=8).pack(side="left", padx=5)

root.mainloop()
