# tk Frame - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Frames")

button_row = tk.Frame(root)
button_row.pack(pady=20)

tk.Button(button_row, text="Red").pack(side="left", padx=5)
tk.Button(button_row, text="Green").pack(side="left", padx=5)
tk.Button(button_row, text="Blue").pack(side="left", padx=5)

root.mainloop()
