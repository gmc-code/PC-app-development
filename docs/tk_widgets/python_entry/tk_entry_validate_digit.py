import tkinter as tk

def validate_input(new_value):
    # Check if the new value is numeric
    return new_value.isdigit() or new_value == ""

window = tk.Tk()
window.title("Validate Entry Example")
window.geometry("500x300")  # Set window size

# Register the validation function
vcmd = (window.register(validate_input), '%P')

entry = tk.Entry(window, validate='key', validatecommand=vcmd, font=("Arial",24))
entry.pack(pady=10)

window.mainloop()