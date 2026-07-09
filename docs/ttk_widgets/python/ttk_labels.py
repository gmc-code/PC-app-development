import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("Inherited ttk Styling")

# 1. Create a Style object
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')


# 1. Base style: Defines shared properties (colors, relief, etc.)
style.configure(
    "Base.TLabel",
    foreground="#000000",
    background="#f0f0f0",
    font=("Arial", 12),
    padding=(10, 5),
)

# 2. Inherit and override: Each child overrides font AND the background color

style.configure("Medium.Base.TLabel", font=("Arial", 16))

style.configure("Large.Base.TLabel", font=("Arial", 20))

# 3. Apply the specific styles
label1 = ttk.Label(root, text="Base Label", style="Base.TLabel")
label1.pack(pady=10)

label2 = ttk.Label(root, text="Medium Label", style="Medium.Base.TLabel")
label2.pack(pady=10)

label3 = ttk.Label(root, text="Large Label", style="Large.Base.TLabel")
label3.pack(pady=10)

root.mainloop()
