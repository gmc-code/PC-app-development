import tkinter as tk


# Create the main application window
root = tk.Tk()
root.title("hello world - grid")
root.geometry("300x200")

# define widgets
label = tk.Label(root, text="Hello World!")
button = tk.Button(root, text="Quit", command=root.destroy)

# place widgets in grid layout
label.grid(row=0,column=0)
button.grid(row=1,column=0)

# Start the main event loop
root.mainloop()
