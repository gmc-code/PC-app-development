import tkinter as tk

def validate_phone(new_value):
    # Check if the new value follows the pattern: 4 digits, a space, 3 digits, a space, 3 digits
    if len(new_value) == 0:
        return True
    if len(new_value) in [5, 9]:
        return new_value[-1] == ' '  # Ensure the 5th and 9th characters are spaces
    if len(new_value) in [1, 2, 3, 4, 6, 7, 8, 10, 11, 12]:
        return new_value[-1].isdigit()  # Ensure other positions are digits
    return False

window = tk.Tk()
window.title("Phone Number Validation Example")
window.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (window.register(validate_phone), '%P')

entry = tk.Entry(window, validate='key', validatecommand=vcmd, font=("Arial",24))
entry.pack(pady=10)

window.mainloop()
