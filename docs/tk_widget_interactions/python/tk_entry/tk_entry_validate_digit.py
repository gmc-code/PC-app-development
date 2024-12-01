import tkinter as tk

def validate_input(new_value):
    # Check if the new value is numeric
    return new_value.isdigit() or new_value == ""

root = tk.Tk()
root.title("Validate Entry Example")
root.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (root.register(validate_input), '%P')

entry = tk.Entry(root, font=("Arial",24), validate='key', validatecommand=vcmd)
entry.pack(pady=10)

root.mainloop()