# tk Scale - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Rating")

rating_scale = tk.Scale(root, from_=1, to=10, orient="horizontal",
                        length=250, label="Rate this movie", tickinterval=1)
rating_scale.set(5)
rating_scale.pack(pady=10)

root.mainloop()
