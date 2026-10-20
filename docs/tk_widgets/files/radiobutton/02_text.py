# tk Radiobutton - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

answer = tk.StringVar(value="none")      # "none" matches no button, so nothing is chosen

yes_radio = tk.Radiobutton(root, text="Yes, please", variable=answer, value="yes")
yes_radio.pack()
no_radio = tk.Radiobutton(root, text="No, thank you", variable=answer, value="no")
no_radio.pack()

root.mainloop()
