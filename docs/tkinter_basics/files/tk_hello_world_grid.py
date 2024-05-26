import tkinter as tk


# Create the main application window
window = tk.Tk()
window.title("Tkinter hello world")
window.geometry('600x400')

# define widgets
label = tk.Label(window, text="Hello World!")
button = tk.Button(window, text="Quit", command=window.destroy)

# place widgets in grid layout
label.grid(row=0,column=0)
button.grid(row=1,column=0)

# Start the main event loop
window.mainloop()
