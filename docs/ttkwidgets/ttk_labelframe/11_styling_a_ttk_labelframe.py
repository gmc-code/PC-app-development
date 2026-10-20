# ttk LabelFrame - Styling a ttk LabelFrame

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x220")
root.title("LabelFrame style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabelframe", background="lightyellow", bordercolor="orange")
style.configure("TLabelframe.Label", font=("Arial", 14, "bold"), foreground="darkorange",
                background="lightyellow")
style.configure("TLabel", background="lightyellow")

notes = ttk.LabelFrame(root, text="Notes", padding=15)
notes.pack(pady=30)
ttk.Label(notes, text="Bring a hat tomorrow").pack()

root.mainloop()
