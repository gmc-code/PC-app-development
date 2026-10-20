import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Message Question")
root.geometry("450x250")

message = tk.Message(
    root,
    text="The Message widget automatically wraps long text so that it fits inside the widget.",
    font=("Comic Sans MS", 18),
    bg="#fff8dc",
    fg="darkgreen",
    width=220
)

message.pack(padx=20, pady=20)

root.mainloop()