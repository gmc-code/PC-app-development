import tkinter as tk
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()
window.title("Text Widget Example")

# Create a Text widget with a scrollbar
text_frame = tk.Frame(root)
text_frame.pack(padx=10, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text = tk.Text(text_frame, height=10, width=40, wrap="word", font=("Helvetica", 12), yscrollcommand=scrollbar.set)
text.pack(padx=10, pady=10, fill="both", expand=True)

scrollbar.config(command=text.yview)

# Insert initial content
initial_content = "\n".join([f"Line {i+1}" for i in range(15)])
text.insert("1.0", initial_content)

# Customize options
text.config(
    bg="lightyellow",  # Background color
    fg="blue",  # Text color
    bd=2,  # Border width
    relief="solid",  # Border style
    insertbackground="blue",  # Insertion cursor color
    state="normal",  # Enable editing (use "disabled" to disable)
    highlightthickness=5,
    highlightcolor="red",
    padx=10,
    pady=10
)

# Run the main event loop
window.mainloop()
