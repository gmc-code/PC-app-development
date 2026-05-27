import tkinter as tk

def validate_phone(new_text):
    if new_text == "":
        return True
    # Check if it is a number AND has 10 or fewer digits
    if new_text.isdigit() and len(new_text) <= 10:
        return True
    else:
        return False

root = tk.Tk()
root.title("Phone Validator (Max 10 Digits)")
root.geometry("400x200")

vcmd = (root.register(validate_phone), '%P')

entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
entry.pack(pady=40)

root.mainloop()