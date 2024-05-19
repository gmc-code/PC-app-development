import tkinter


window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        print("logged in")
    else:
        print("Invalid login")


#  create frame widget for other widgets
frame = tkinter.Frame(bg='#333333')

#  create widgets in frame
login_label = tkinter.Label(frame, text="Login",
                            bg='#333333', fg='#FF3399', font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username",
                               bg='#333333', fg='#FFFFFF', font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password",
                               bg='#333333', fg='#FFFFFF', font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button =tkinter.Button(frame, text="Login",
                             bg='#FF3399', fg='#FFFFFF', font=("Arial", 16),
                             command=login)


# place widgets in frame
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

# place frame
frame.pack()








window.mainloop()
