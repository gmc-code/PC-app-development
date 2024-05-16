import tkinter

def print_hello():
    print(textntry.get())
    # Function to handle button click event
    # user_input = textntry.get()  # Get the text from the entry widget
    # label.config(text=f"Hello, {user_input}!")

# Create the main application window
window = tkinter.Tk()
window.title("Tkinter First App")
window.geometry('600x400')

# Create a label widget
label = tkinter.Label(window, text="Hello World", bg="red", fg="blue", width=50)
label.pack()

# Create an entry widget
textentry = tkinter.Entry(window, bg='#fdbce1', width=50)
textentry.pack()

# Create a button widget
#state=tkinter.DISABLED
button = tkinter.Button(window, text="Say Hello", bg='#cdfe34', 
                        activebackground='red', activeforeground='white', command=print_hello)
button.pack()

# Start the Tkinter event loop
window.mainloop()
