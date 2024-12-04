import tkinter as tk

root = tk.Tk()
root.title("Text Widget Questions")

# Create a Text widget
text = tk.Text(root, height=6, width=40, wrap="word", font=("Helvetica", 12))
text.pack(padx=10, pady=10)

# Insert initial content
text.insert(
    "1.0", "Welcome to \nthe Text Widget!\nIt has multiline text.")

# Customize options
text.config(
    bg="light yellow",  # Background color
    fg="dark green",  # Text color
    bd=2,  # Border width
    relief="groove",  # Border style
    insertbackground="dark green",  # Insertion cursor color
    state="disabled",  # Disable editing
    highlightthickness=1,
    highlightcolor="dark green",
    padx=10,
    pady=10,
    yscrollcommand="True",
)

root.mainloop()
