# tk Button - activebackground and activeforeground

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("active colours")

button = tk.Button(
    root,
    text="Press and hold",
    font=("Arial", 16),
    bg="lightblue",             # Normal colour
    activebackground="navy",    # Colour while pressed
    activeforeground="white",   # Word colour while pressed
)
button.pack(pady=20)

root.mainloop()
