import tkinter as tk


root = tk.Tk()
root.title("Text Widget Example")

# Create a Text widget
text = tk.Text(root, height=6, width=40, wrap="word", font=("Helvetica", 12))
text.pack(padx=10, pady=10)

# Insert initial content
text.insert(
    "1.0", "Welcome to \nthe Text Widget!\nIt has multiline text.")

# Customize options
text.config(
    bg="#fafafa",  # Background color
    fg="blue",  # Text color
    bd=1,  # Border width
    relief="solid",  # Border style
    insertbackground="blue",  # Insertion cursor color
    state="normal",  # Enable editing (use "disabled" to disable)
    highlightthickness=1,
    highlightcolor="blue",
    padx=10,
    pady=10,
    yscrollcommand="True",
)

root.mainloop()
