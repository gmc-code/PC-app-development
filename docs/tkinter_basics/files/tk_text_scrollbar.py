import tkinter as tk


root = tk.Tk()
root.title("Text Widget with Vertical Scrollbar")

# Create a Text widget
text = tk.Text(root, height=10, width=40, wrap="word")
text.grid(row=0, column=0, padx=10, pady=10)

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")  # Place the scrollbar to the right

# Configure the Text widget to use the scrollbar
text.config(yscrollcommand=scrollbar.set)

# Insert some initial content
text.insert("1.0", "Sample text 12345.\n" * 14)

root.mainloop()


