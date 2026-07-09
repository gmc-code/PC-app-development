import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk Button question")
root.geometry("350x100")

# 1. Create a Style object
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')

# 2. Configure a custom style layout for TButton
style.configure(
    "Custom.TButton",
    font=("Arial", 14),
    width=15,
    padding=(10, 5) # horizontal, vertical
)

# Note: Modern ttk uses dynamic maps for states like active/pressed
style.map(
    "Custom.TButton",
    foreground=[("pressed", "white"), ("active", "white")],
    # Add 'active' to the background list
    background=[("pressed", "black"), ("active", "#333333")]
)

# 3. Apply the custom style to the ttk.Button
button = ttk.Button(
    root,
    text="Click Me",
    style="Custom.TButton"
)

button.pack(padx=20, pady=20)

root.mainloop()
