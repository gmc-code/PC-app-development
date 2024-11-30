import tkinter as tk


root = tk.Tk()
window.title("Text Widget Example")

# Create a Text widget
text = tk.Text(root, height=24, width=40, wrap="word", font=("Helvetica", 12))
text.pack(padx=10, pady=10)

# Insert initial content
text.insert("1.0", "Welcome \nto \nthe Text Widget!\nFeel free to edit this text.")

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
    pady=10,yscrollcommand="True")

window.mainloop()
