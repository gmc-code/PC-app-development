# tk LabelFrame - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

warning = tk.LabelFrame(root, text="Warning", relief="solid", borderwidth=2,
                        fg="red", padx=10, pady=10)
warning.pack(pady=20)

tk.Label(warning, text="Save your work!").pack()

root.mainloop()
