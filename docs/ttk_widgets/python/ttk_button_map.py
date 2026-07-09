import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Bootstrap Styled Button - Obvious Press State")
root.geometry("400x250")

style = ttk.Style()
style.theme_use('clam')

# 1. STATIC STATE (Bootstrap 'btn-primary' Defaults)
style.configure(
    "Task.TButton",
    background="#0d6efd",      # Bootstrap Primary Blue
    foreground="#ffffff",      # White text
    font=("Segoe UI", 11),
    padding=(20, 8),

    # === [Button.border] Bootstrap Colors ===
    bordercolor="#0d6efd",
    borderwidth=1,
    lightcolor="#0d6efd",
    darkcolor="#0d6efd",
    relief="flat",

    # === [Button.focus] Bootstrap Glow Accent ===
    focuscolor="#98c1fe",      # Translucent-style light blue focus ring
    focusthickness=3,
    focussolid=True
)

# 2. DYNAMIC STATES (With Max-Emphasis Pressed State)
style.map(
    "Task.TButton",
    background=[
        ('pressed', '#052c65'),  # Ultra-Dark Navy (Much more obvious than standard Bootstrap)
        ('active', '#0b5ed7')    # Bootstrap Hover state
    ],
    foreground=[
        ('pressed', '#ffffff'),
        ('disabled', '#ffffff')
    ],

    # === [Button.border] Dynamic Press Feedback ===
    bordercolor=[
        ('pressed', '#031634'),  # Deep dark border outline
        ('active', '#0a5cbf')
    ],
    borderwidth=[
        ('pressed', 2),          # Thicken border on click to make it feel compressed
        ('active', 1)
    ],
    lightcolor=[
        ('pressed', '#031634'),
        ('active', '#0a5cbf')
    ],
    darkcolor=[
        ('pressed', '#031634'),
        ('active', '#0a5cbf')
    ],
    relief=[
        ('pressed', 'sunken'),   # Force mechanical indent
        ('active', 'flat')
    ],

    # === [Button.padding] Physical Movement ===
    shiftrelief=[
        ('pressed', 1),          # Visually drops text/content by 1px on click
        ('!pressed', 0)
    ],

    # === [Button.focus] Dynamic Updates ===
    focuscolor=[
        ('active', '#98c1fe'),
        ('pressed', '#98c1fe')
    ]
)

btn = ttk.Button(root, text="Primary Button", style="Task.TButton")
btn.pack(padx=50, pady=50)
btn.focus_set()

root.mainloop()