# tk Scale - tickinterval

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("tickinterval")

temp_scale = tk.Scale(root, from_=0, to=40, orient="horizontal", length=250,
                      tickinterval=10, label="Temperature")
temp_scale.pack(pady=20)

root.mainloop()
