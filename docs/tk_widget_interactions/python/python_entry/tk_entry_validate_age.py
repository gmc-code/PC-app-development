import tkinter as tk


def validate_age(new_value):
    if new_value.isdigit():
        age = int(new_value)
        return 0 <= age <= 120  # Returns True if within range, otherwise False
    else:
        return new_value == ""  # Returns True if empty, otherwise False


window = tk.Tk()
window.title("Age Validation Example")
window.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (window.register(validate_age), "%P")

entry = tk.Entry(window, font=("Arial", 24), validate="key", validatecommand=vcmd)
entry.pack(pady=10)

window.mainloop()
