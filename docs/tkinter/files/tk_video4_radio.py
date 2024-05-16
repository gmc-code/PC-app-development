import tkinter

def radio_pressed():
    # print(radiovar.get())
    label.config(text=f"You chose {radiovar.get()}")

# Create the main application window
window = tkinter.Tk()
window.title("Tkinter radio tutorial")
window.geometry('600x400')

# Create an entry widget
radiovar = tkinter.StringVar()
radio1 = tkinter.Radiobutton(window, variable=radiovar, text="June", value="June month", font=('Arial', '32'), command=radio_pressed)
radio2 = tkinter.Radiobutton(window, variable=radiovar, text="July", value="July month", font=('Arial', '32'), command=radio_pressed)
radio3 = tkinter.Radiobutton(window, variable=radiovar, text="August", value="August month", font=('Arial', '32'), command=radio_pressed)
radio4 = tkinter.Radiobutton(window, variable=radiovar, text="September", value="September month", font=('Arial', '32'), command=radio_pressed)

radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()

# Create a label widget (not in video)
label = tkinter.Label(window, text="", bg="yellow", fg="blue", width=60, font=('Arial', '32'),)
label.pack()


# Start the Tkinter event loop
window.mainloop()
