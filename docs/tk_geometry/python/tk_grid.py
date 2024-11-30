import tkinter as tk


# Create the main application window
root = tk.Tk()
root.title("grid")
root.geometry("200x150")

# define widgets
label1 = tk.Label(root, text="label 1", bg="light blue")
label2 = tk.Label(root, text="label 2", bg="light blue")
label3 = tk.Label(root, text="label 3", bg="light blue")
label4 = tk.Label(root, text="label 4", bg="light green")

# place widgets in grid layout
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)
label4.grid(row=3, column=0, columnspan=3, sticky="ew")

# Start the main event loop
root.mainloop()
