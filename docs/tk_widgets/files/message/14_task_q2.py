# tk Message - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Instructions")

how_to = tk.Message(root, text="Roll the dice and move your piece. "
                               "If you land on a ladder, climb up. "
                               "If you land on a snake, slide down.",
                    width=250, font=("Arial", 12), bg="lightyellow",
                    relief="solid", borderwidth=1, padx=10, pady=10)
how_to.pack(pady=10)

root.mainloop()
