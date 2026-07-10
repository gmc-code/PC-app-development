import tkinter as tk

root = tk.Tk()
root.title("Text Widget Example")
root.geometry("300x200")

# Create a Text widget
text = tk.Text(root, height=6, width=40, wrap="word", font=("Arial", 12))
text.pack(padx=10, pady=10)

# Insert initial content
text.insert("1.0", "Welcome to \nthe Text Widget!\nIt has multiline text.")

# Customize options
text.config(
    bg="#fafafa",  # Background color
    fg="blue",  # Text color
    borderwidth=1,  # Border width
    relief="solid",  # Border style
    insertbackground="red",  # Insertion cursor color
    selectbackground="red",  # Selection background color
    state="normal",  # Enable editing (use "disabled" to disable)
    padx=10,
    pady=10
)

root.mainloop()
