# tk Scale - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Rating")

rating_scale = tk.Scale(root, from_=1, to=10, orient="horizontal",
                        length=250, label="Rate this movie")
rating_scale.pack(pady=10)

root.mainloop()
