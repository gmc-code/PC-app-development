import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Message Example")
root.geometry("450x250")

# Create the Message widget
message = tk.Message(
    root,
    text="The Message widget automatically wraps long text so that it fits within the specified width.",
    width=250,
    font=("Arial", 16),
    bg="#f8f8f8",
    fg="navy"
)

message.pack(padx=20, pady=20)

# Run the main event loop
root.mainloop()