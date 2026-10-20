# tk Label - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Score")

score_label = tk.Label(root, text="Score: 0", width=20, height=3,
                       bg="lightgreen", anchor="nw")
score_label.pack()

root.mainloop()
