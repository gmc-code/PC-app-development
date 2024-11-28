import tkinter as tk
from tkinter import messagebox
import re


def validate_password():
    password = password_var.get()
    if len(password) < 8:
        messagebox.showwarning("Validation Result", "Password must be at least 8 characters long.")
        return False
    if not re.search("[a-z]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one lowercase letter.")
        return False
    if not re.search("[A-Z]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one uppercase letter.")
        return False
    if not re.search("[0-9]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one digit.")
        return False
    if not re.search('[!@#$%^&*(),.?":{}|<>]', password):
        messagebox.showwarning("Validation Result", "Password must contain at least one special character.")
        return False
    messagebox.showinfo("Validation Result", "Password is valid!")
    return True


def on_validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if action == "1":  # Insert
        return validate_password()
    return True


window = tk.Tk()
window.title("Password Validator")
window.geometry("300x200")

password_var = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password_var, show="*", validate="key", validatecommand=(window.register(on_validate), "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W"))
password_entry.pack(pady=10)

validate_button = tk.Button(window, font=("Arial", 24), text="Validate Password", command=validate_password)
validate_button.pack(pady=10)

window.mainloop()
