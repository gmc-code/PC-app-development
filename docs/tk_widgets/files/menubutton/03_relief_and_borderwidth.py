# tk Menubutton - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

flat_button = tk.Menubutton(root, text="Flat (default)")
flat_button.pack(pady=10)

raised_button = tk.Menubutton(root, text="Raised", relief="raised", borderwidth=2)
raised_button.pack(pady=10)

root.mainloop()
