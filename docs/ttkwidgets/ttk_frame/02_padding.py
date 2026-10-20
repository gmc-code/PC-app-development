# ttk Frame - padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("padding")

padded = ttk.Frame(root, padding=(40, 20), relief="solid", borderwidth=1)
padded.pack(pady=30)
ttk.Label(padded, text="Lots of space around me").pack()

root.mainloop()
