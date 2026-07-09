import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("ttk Label padding")  # Set window title

# Create the label widget with 40 pixels left/right and 20 pixels top/bottom padding
label = ttk.Label(root, text="padded text", font=("Arial", 24), padding=(40, 20))

# Pack the label into the window
label.pack(pady=20)

# Run the main event loop
root.mainloop()