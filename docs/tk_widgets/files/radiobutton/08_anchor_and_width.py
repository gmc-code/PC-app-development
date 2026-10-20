# tk Radiobutton - anchor and width

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("anchor and width")

sport = tk.StringVar(value="Soccer")

for choice in ["Soccer", "Netball", "Basketball", "Swimming"]:
    tk.Radiobutton(root, text=choice, variable=sport, value=choice,
                   width=15, anchor="w").pack()

root.mainloop()
