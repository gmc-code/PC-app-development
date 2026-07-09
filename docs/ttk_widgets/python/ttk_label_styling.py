import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk Label Styling")
root.configure(bg="#f0f0f0")  # default

# 1. Create a Style object
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')

# Define the font within the style configuration
style.configure(
    "Custom.TLabel",
    foreground="#36454F",
    background="#f0f0f0",
    font=("Arial", 14),  # Font included here
    padding=(10, 10),
)

# Style applied here; no need to pass font= parameter
label = ttk.Label(root, text="Styled ttk Label", style="Custom.TLabel")
label.pack(pady=25)

root.mainloop()
