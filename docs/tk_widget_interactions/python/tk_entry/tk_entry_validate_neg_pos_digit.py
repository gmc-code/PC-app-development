import tkinter as tk

def validate_range(new_text):
    if new_text == "":
        return True  # Allow deleting text completely
    # Allow just a minus or plus sign so the user can start typing
    if new_text in ["-", "+"]:
        return True
    # Check if the text is a valid number
    try:
        num = int(new_text)
        # Only allow if the number is between -9 and +9
        return -9 <= num <= 9
    except ValueError:
        return False  # Reject letters or invalid symbols

root = tk.Tk()
root.title("Single Digit Validator (-9 to +9)")
root.geometry("400x200")

vcmd = (root.register(validate_range), '%P')

entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
entry.pack(pady=40)

root.mainloop()