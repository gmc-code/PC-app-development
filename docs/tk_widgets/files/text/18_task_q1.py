# tk Text - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Diary")

diary_box = tk.Text(root, width=40, height=10, wrap="word",
                    bg="lightyellow", font=("Arial", 12))
diary_box.pack(pady=10)

root.mainloop()
