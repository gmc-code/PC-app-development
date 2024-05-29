import tkinter as tk


# Create the main application window
window = tk.Tk()
window.title("Tkinter hello world - pack")
window.geometry('600x400')

# define widgets
label = tk.Label(window, text="Hello World!")
button = tk.Button(window, text="Quit", command=window.destroy)

# place widgets using pack
label.pack()
button.pack()

# Start the main event loop
window.mainloop()
