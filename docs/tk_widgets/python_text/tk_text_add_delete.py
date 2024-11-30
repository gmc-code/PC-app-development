import tkinter as tk

# Create the main window
root = tk.Tk()
window.title("Interactive Text Widget Example")

# Create a StringVar to hold the text content
text_var = tk.StringVar()
text_var.set("This is a simple text widget example.")

# Create a Text widget
text = tk.Text(root, height=10, width=40, wrap="word", font=("Helvetica", 12))
text.pack(padx=10, pady=10, fill="both", expand=True)

# Insert initial content from StringVar
text.insert("1.0", text_var.get())

# Function to add text
def add_text():
    text.insert("end", "\nAdditional text added.")

# Function to remove text
def remove_text():
    text.delete("2.0", "end")

# Create buttons to add and remove text
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Text", command=add_text)
add_button.pack(side="left", padx=5)

remove_button = tk.Button(button_frame, text="Remove Text", command=remove_text)
remove_button.pack(side="left", padx=5)

# Run the main event loop
window.mainloop()
