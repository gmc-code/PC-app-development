import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("LabelFrame Question")
root.geometry("320x220")

# Create the LabelFrame
settings = tk.LabelFrame(
    root,
    text="User Settings",
    font=("Arial", 12),
    padx=15,
    pady=15,
    bd=3,
    relief="groove"
)

# Display the LabelFrame
settings.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

# Run the main event loop
root.mainloop()