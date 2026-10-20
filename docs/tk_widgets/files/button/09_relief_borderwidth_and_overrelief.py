# tk Button - relief, borderwidth and overrelief

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

button = tk.Button(root, text="Hover over me", font=("Arial", 14),
                   relief="raised", borderwidth=4, overrelief="sunken")
button.pack(pady=20)

root.mainloop()
