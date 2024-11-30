import tkinter as tk


# Create the main application window
root = tk.Tk()
root.title("hello world - pack")
root.geometry("300x200")

# define widgets
label = tk.Label(root, text="Hello World!")
button = tk.Button(root, text="Quit", command=root.destroy)

# place widgets using pack
label.pack()
button.pack()

# Start the main event loop
root.mainloop()
