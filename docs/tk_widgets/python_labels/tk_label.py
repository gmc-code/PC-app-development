import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("500x500")  # Set window size
root.title("Label border")  # Set window title

# Create the label widget with options
label = tk.Label(text="label text", font=("Arial", 24), fg="blue", bg="lightyellow",
                 padx=60, pady=20, width=18, height=3, anchor="sw",
                 relief="solid", borderwidth=1)

# Pack the label into the window
label.pack()

# Run the main event loop
root.mainloop()
