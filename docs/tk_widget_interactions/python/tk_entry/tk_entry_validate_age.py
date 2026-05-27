import tkinter as tk


def validate_age(new_text):
    if new_text == "":
        return True  # Allow deleting text completely
    if new_text.isdigit():
        age = int(new_text)
        # Only allow if the number is between 0 and 120
        return 0 <= age <= 120
    else:
        return False   # Reject letters

root = tk.Tk()
root.title("Age Validation Example")
root.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (root.register(validate_age), "%P")

entry = tk.Entry(root, font=("Arial", 24), validate="key", validatecommand=vcmd)
entry.pack(pady=10)

root.mainloop()
