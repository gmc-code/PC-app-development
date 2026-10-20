# tk Scale - resolution

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("resolution")

fives_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200,
                       resolution=5, label="Steps of 5")
fives_scale.pack(pady=5)

tenths_scale = tk.Scale(root, from_=0, to=1, orient="horizontal", length=200,
                        resolution=0.1, label="Steps of 0.1")
tenths_scale.pack(pady=5)

root.mainloop()
