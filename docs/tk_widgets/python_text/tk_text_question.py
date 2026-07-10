import tkinter as tk

root = tk.Tk()
root.title("Text Widget Question")
root.geometry("300x200")

# Create a Text widget
text = tk.Text(root, height=6, width=40, wrap="word", font=("Arial", 12))
text.pack(padx=10, pady=10)

# Insert initial content
text.insert("1.0", "Welcome to \nthe Text Widget!\nIt has multiline text.")

# Customize options
text.config(
    bg="light yellow",
    fg="dark green",
    borderwidth=2,
    relief="groove",
    insertbackground="red",
    selectbackground="purple",
    state="disabled",
    padx=10,
    pady=10
)

root.mainloop()
