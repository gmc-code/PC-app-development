import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()

# Get the theme currently in use
current = style.theme_use()
print(f"Current active theme: {current}")

all_themes = style.theme_names()
print(f"Available themes: {all_themes}")


'''
Current active theme: vista
Available themes: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
'''

# Switch the application's appearance to the 'clam' theme
style.theme_use("clam")

# Create a button to see the new theme in action
button = ttk.Button(root, text="Themed Button")
button.pack(padx=20, pady=20)

root.mainloop()