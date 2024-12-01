import tkinter as tk


def validate_age(new_value):
    if new_value.isdigit():
        age = int(new_value)
        return 0 <= age <= 120  # Returns True if within range, otherwise False
    else:
        return new_value == ""  # Returns True if empty, otherwise False


root = tk.Tk()
root.title("Age Validation Example")
root.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (root.register(validate_age), "%P")

entry = tk.Entry(root, font=("Arial", 24), validate="key", validatecommand=vcmd)
entry.pack(pady=10)

root.mainloop()
