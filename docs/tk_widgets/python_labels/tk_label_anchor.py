import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("500x200")  # Set window size
window.title("Label anchor")  # Set window title

# Create the label widget with options
label = tk.Label(text="anchor nw", font=("Arial", 24), fg="blue", bg="lightyellow",
                width=20, height=2, anchor="nw")

# Pack the label into the window
label.pack(pady=5)

# Create the label widget with options
label_2 = tk.Label(text="anchor nw padded", font=("Arial", 24), fg="purple", bg="lightgreen",
                width=20, height=2, anchor="nw", padx=20, pady=10)

# Pack the label into the window
label_2.pack()

# Run the main event loop
window.mainloop()
