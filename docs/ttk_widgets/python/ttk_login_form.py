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
    root = tk.Tk()
    root.geometry('300x110+200+300')
    root.resizable(0, 0)
    root.title('Login')

    # UI options
    paddings = {'padx': 5, 'pady': 5}
    ENTRY_FONT = {'font': ('Helvetica', 11)}

    username = tk.StringVar()

    # Username label
    username_label = ttk.Label(root, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.W, **paddings)

    # Username entry
    username_entry = ttk.Entry(root, textvariable=username, **ENTRY_FONT)
    username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)

    login_button = ttk.Button(root, text="Login", command=login_action)
    login_button.grid(column=1, row=1, sticky=tk.E, **paddings)

    root.mainloop()

create_login_form()
