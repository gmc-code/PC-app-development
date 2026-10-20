import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Frame Question")
root.geometry("350x250")

# Create the Frame
frame = tk.Frame(
    root,
    bg="light blue",
    bd=4,
    relief="ridge",
    width=220,
    height=120,
    padx=15,
    pady=15
)

# Display the Frame
frame.pack(
    padx=30,
    pady=30
)

# Run the main event loop
root.mainloop()