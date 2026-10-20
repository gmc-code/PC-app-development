# tk Message - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

note = tk.Message(root, text="Dear class,\nPlease bring your laptop on Friday.\nThanks!")
note.pack(pady=10)

root.mainloop()
