# tk Message - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Poem")

poem = tk.Message(root, text="Twinkle, twinkle, little star,\n"
                             "How I wonder what you are!\n"
                             "Up above the world so high,\n"
                             "Like a diamond in the sky.",
                  width=250, justify="center")
poem.pack(pady=10)

root.mainloop()
