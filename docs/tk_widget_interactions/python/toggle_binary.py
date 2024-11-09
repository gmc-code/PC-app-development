import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Toggle Binary")

# Create a StringVar to hold the text
text_var = tk.StringVar()
text_var.set("0")

# Create a Label widget with textvariable
label = tk.Label(root, textvariable=text_var, font=("Helvetica", 16))
label.pack(pady=20)

# Function to update the text
def update_text():
    if text_var.get() == "0":
        text_var.set("1")
    else:
        text_var.set("0")

# Create a Button to trigger the text update
button = tk.Button(root, text="Toggle Binary", command=update_text)
button.pack(pady=20)

# Run the application
root.mainloop()
