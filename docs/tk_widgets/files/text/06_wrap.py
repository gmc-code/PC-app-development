# tk Text - wrap

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("wrap")

text_box = tk.Text(root, width=25, height=5, wrap="word")
text_box.insert("1.0", "This sentence is too long for one line, so it wraps between words.")
text_box.pack(pady=10)

root.mainloop()
