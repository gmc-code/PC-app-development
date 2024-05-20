import tkinter as tk


# Create the main application window
window = tk.Tk()
window.title("Tkinter hello world")
window.geometry('600x400')

# define widgets
label = tk.Label(window, text="Hello World!")
button = tk.Button(window, text="Quit", command=window.destroy)

# place widgets
label.grid(column=0, row=0)
button.grid(column=1, row=0)

# Start the main event loop
window.mainloop()
