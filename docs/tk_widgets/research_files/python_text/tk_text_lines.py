import tkinter as tk

root = tk.Tk()
root.title("Text Widget lines")
root.geometry("300x200")

# The Text widget supports multi-line content and line.column indexing
text_widget = tk.Text(root, height=5, width=30)
text_widget.pack()

# Inserting text at specific lines
# "1.0" means Line 1, Character 0
text_widget.insert("1.0", "Line 1: Hello\n")
text_widget.insert("2.0", "Line 2: World")


text_widget.tag_configure("heading",
                          font=("Arial", 16, "bold"),
                          foreground="red")
text_widget.insert("1.0", "Welcome\n", "heading")

# Retrieving text from a specific range (e.g., all of line 1)
# "1.0" to "1.end" covers the entire first line
line1_text = text_widget.get("1.0", "1.end")
print(f"Content of line 1: {line1_text}")

root.mainloop()
