# ttk Checkbutton - Styling a ttk Checkbutton

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Checkbutton style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCheckbutton", font=("Arial", 14), foreground="navy",
                background="lightyellow", indicatorbackground="white")
style.map("TCheckbutton", foreground=[("selected", "green")],
          indicatorbackground=[("selected", "lightgreen")])

sports = []
for sport in ["Soccer", "Netball", "Tennis"]:
    choice = tk.IntVar()
    sports.append(choice)
    ttk.Checkbutton(root, text=sport, variable=choice).pack(pady=3)

root.mainloop()
