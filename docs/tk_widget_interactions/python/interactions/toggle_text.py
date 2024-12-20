import tkinter as tk


# Function to update the text
def update_text():
    if text_var.get() == "Initial Text":
        text_var.set("Updated Text")
    else:
        text_var.set("Initial Text")


# Create the main window
root = tk.Tk()
root.geometry("300x100")
root.title("Toggle Text")

# Create a StringVar to hold the text
text_var = tk.StringVar()
text_var.set("Initial Text")

# Create a Label widget with textvariable
label = tk.Label(root, textvariable=text_var, font=("Helvetica", 16))
label.pack(pady=10)

# Create a Button to trigger the text update
button = tk.Button(root, text="Toggle Text", command=update_text)
button.pack(pady=10)

# Run the application
root.mainloop()
