# tk Text - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

text_box = tk.Text(root, width=30, height=6, relief="solid", borderwidth=2)
text_box.pack(pady=10)

root.mainloop()
