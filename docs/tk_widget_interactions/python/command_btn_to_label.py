import tkinter as tk


def change_text():
    label.config(text="Button pressed!")


# Create the main window
root = tk.Tk()
root.geometry("200x100")  # Set window size
root.title("Button -> label Example")  # Set window title

button = tk.Button(root, text="Click me", command=change_text)
button.pack(pady=10)

label = tk.Label(root, text="Waiting...")
label.pack(pady=10)

root.mainloop()
