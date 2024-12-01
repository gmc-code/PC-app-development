import tkinter as tk
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email) or email == "":
        error_label.config(text="")
        return True
    else:
        error_label.config(text="Invalid email address")
        return False

root = tk.Tk()
root.title("Email Validation Example")
root.geometry("500x300")

# Register the validation function
vcmd = (root.register(validate_email), '%P')

entry = tk.Entry(root, font=("Arial", 24), validate="focusout", validatecommand=vcmd)
entry.pack(pady=10)

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

entry2 = tk.Entry(root, font=("Arial", 24))
entry2.pack(pady=10)

root.mainloop()
