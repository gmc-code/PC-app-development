import tkinter as tk


def greet(name):
    label.config(text=f"Hello {name}.")


# Create the main window
root = tk.Tk()
root.geometry("200x100")  # Set window size
root.title("Button lambda -> label Example")  # Set window title

button = tk.Button(root, text="Click", command=lambda: greet("Alice"))
button.pack(pady=10)

label = tk.Label(root, text="Waiting...")
label.pack(pady=10)

root.mainloop()
