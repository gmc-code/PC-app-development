import tkinter as tk

def check_number(new_text):
    # Allow the box to be empty, OR check if the new text is a number
    if new_text == "" or new_text.isdigit():
        return True   # True means "allow the change"
    else:
        return False  # False means "reject the keystroke"

root = tk.Tk()
root.title("Numbers Only")
root.geometry("400x200")

# Register our validation function with Tkinter
vcmd = (root.register(check_number), '%P')

# Create the entry box with validation turned on
entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
entry.pack(pady=40)

root.mainloop()