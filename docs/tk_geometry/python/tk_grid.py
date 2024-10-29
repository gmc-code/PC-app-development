import tkinter as tk


# Create the main application window
window = tk.Tk()
window.title("grid")
window.geometry("200x150")

# define widgets
label1 = tk.Label(window, text="label 1", bg="light blue")
label2 = tk.Label(window, text="label 2", bg="light blue")
label3 = tk.Label(window, text="label 3", bg="light blue")
label4 = tk.Label(window, text="label 4", bg="light green")

# place widgets in grid layout
label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=2,column=2) 
label4.grid(row=3,column=0, columnspan=3, ipadx=60)

# Start the main event loop
window.mainloop()
