import tkinter as tk

def validate_phone(new_value):
    # Check if the new value is numeric and has at most 10 digits
    return new_value.isdigit() and len(new_value) <= 10

window = tk.Tk()
window.title("Phone Number Validation Example")
window.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (window.register(validate_phone), '%P')

entry = tk.Entry(window, validate='key', validatecommand=vcmd, font=("Arial",24))
entry.pack(pady=10)

window.mainloop()