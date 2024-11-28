import tkinter as tk

def validate_age(new_value):
    # Check if the new value is numeric and within the valid age range
    if new_value.isdigit():
        age = int(new_value)
        return 0 <= age <= 120
    return new_value == ""  # Allow empty string for clearing the entry

window = tk.Tk()
window.title("Age Validation Example")
window.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (window.register(validate_age), '%P')

entry = tk.Entry(window, validate='key', validatecommand=vcmd, font=("Arial",24))
entry.pack(pady=10)

window.mainloop()
