# tk Scale - label

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("label")

volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200,
                        label="Volume")
volume_scale.pack(pady=20)

root.mainloop()
