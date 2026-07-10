import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Formatted Label Example")
root.geometry("500x300")

# Define the custom font
custom_font = ("Comic Sans MS", 20)

# Create the Label widget with the specified formatting, border, padding, and anchor options
label = tk.Label(root, text="This is a label widget.", font=custom_font, bg="#e0b0ff", fg="purple",
                 borderwidth=2, relief="raised", padx=10, pady=10, anchor="nw", width=30, height=2)
label.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
