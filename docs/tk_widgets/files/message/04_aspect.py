# tk Message - aspect

import tkinter as tk

root = tk.Tk()
root.geometry("350x300")
root.title("aspect")

text = "The water cycle moves water from the ocean to the sky and back again."

tk.Message(root, text=text, aspect=400, bg="lightblue").pack(pady=5)
tk.Message(root, text=text, aspect=50, bg="lightgreen").pack(pady=5)

root.mainloop()
