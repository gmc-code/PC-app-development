import tkinter as tk


def button_clicked():
    print("Button clicked!")


root = tk.Tk()

# Creating a button with specified options
button = tk.Button(
    window,
    text="Click Me",
    command=button_clicked,
    fg="black",  # Text color
    bg="lightblue",  # Background color
    activebackground="blue",  # Background color when clicked
    activeforeground="white",  # Text color when clicked
    font=("Arial", 12),
    padx=10,
    pady=5,
    width=15,
)

button.pack(padx=20, pady=20)

root.mainloop()
