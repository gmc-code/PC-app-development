import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Declare username as a global variable
username = None

# Login button
def login_action():
    messagebox.showinfo("Login", f"Logging in as {username.get()}")

def create_login_form():
    global username  # Declare username as global
    window = tk.Tk()
    window.geometry('300x110+200+300')
    window.resizable(0, 0)
    window.title('Login')

    # UI options
    paddings = {'padx': 5, 'pady': 5}
    ENTRY_FONT = {'font': ('Helvetica', 11)}

    username = tk.StringVar()

    # Username label
    username_label = ttk.Label(window, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.W, **paddings)

    # Username entry
    username_entry = ttk.Entry(window, textvariable=username, **ENTRY_FONT)
    username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)

    login_button = ttk.Button(window, text="Login", command=login_action)
    login_button.grid(column=1, row=1, sticky=tk.E, **paddings)

    window.mainloop()

create_login_form()
