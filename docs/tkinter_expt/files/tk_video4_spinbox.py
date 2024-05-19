import tkinter

def spinbox_pressed():
    # print(spinvar.get())
    label.config(text=f"You chose: {spinvar.get()}")

# Create the main application window
window = tkinter.Tk()
window.title("Tkinter spinbox tutorial")
window.geometry('600x400')

# Create an entry widget
spinvar = tkinter.StringVar()
spin = tkinter.Spinbox(window,
                       values=["hello", "hi", "yes", "no"],
                       font=('Arial', '32'),
                       textvariable=spinvar, 
                       width=50,
                       command=spinbox_pressed)


spin.pack()

# Create a label widget (not in video)
label = tkinter.Label(window, text="", bg="yellow", fg="blue", font=('Arial', '32'), width=50)
label.pack()


# Start the Tkinter event loop
window.mainloop()
