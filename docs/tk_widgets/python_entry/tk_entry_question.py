import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Entry Alphabet Example")
root.geometry("400x300")

# Define the custom font
custom_font=("Comic Sans MS", 20)

# First Entry widget
entry = tk.Entry(root, font=custom_font, bg="#fafafa", fg="#2f2f2f", borderwidth=2, relief="sunken", justify="left", width=20)
entry.pack(padx=20, pady=20, ipady=5)


# Run the Tkinter event loop
root.mainloop()