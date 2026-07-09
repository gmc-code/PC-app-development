import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk.Button Widget Example")
root.geometry("300x150")

# 1. Create a Style object
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')

# 2. Configure a custom style layout for TButton
style.configure(
    "Custom.TButton",
    font=("Arial", 12),
    width=15,
    padding=(10, 5) # horizontal, vertical
)

# Note: Modern ttk uses dynamic maps for states like active/pressed
style.map(
    "Custom.TButton",
    foreground=[("pressed", "white"), ("active", "black")],
    background=[("pressed", "#0d6efd"), ("active", "#9eb6da")]
)

# 3. Apply the custom style to the ttk.Button
button = ttk.Button(
    root,
    text="Button",
    style="Custom.TButton"
)

button.pack(padx=20, pady=20)

root.mainloop()
