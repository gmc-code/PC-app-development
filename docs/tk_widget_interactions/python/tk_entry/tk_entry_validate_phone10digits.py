import tkinter as tk


def validate_phone(new_value):
    # Check if the new value is numeric and has at most 10 digits
    return new_value.isdigit() and len(new_value) <= 10


root = tk.Tk()
root.title("Phone Number Validation Example")
root.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (root.register(validate_phone), "%P")

entry = tk.Entry(root, font=("Arial", 24), validate="key", validatecommand=vcmd)
entry.pack(pady=10)

root.mainloop()
