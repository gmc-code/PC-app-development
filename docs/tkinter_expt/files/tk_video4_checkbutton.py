import tkinter

def checkbutton_pressed():
    # print(spinvar.get())
    label.config(text=f"You chose: {checkvar.get()}")

# Create the main application window
window = tkinter.Tk()
window.title("Tkinter checkbutton tutorial")
window.geometry('600x400')

# Create an entry widget
checkvar = tkinter.StringVar()
check = tkinter.Checkbutton(window,
                       text="CHeck me!",
                       font=('Arial', '32'),
                       textvariable=checkvar,
                       onvalue="Yes",
                       offvalue="No",
                       width=50,
                       command=checkbutton_pressed)


check.pack()

# Create a label widget (not in video)
label = tkinter.Label(window, text="", bg="yellow", fg="blue", font=('Arial', '32'), width=50)
label.pack()


# Start the Tkinter event loop
window.mainloop()
