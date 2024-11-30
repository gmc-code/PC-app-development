import tkinter as tk


def window_set_height(root, height):
    # Wait for the window to be fully initialized
    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{height}")


def window_set_width(root, width):
    # Wait for the window to be fully initialized
    root.update_idletasks()
    root.geometry(f"{width}x{root.winfo_height()}")


root = tk.Tk()
root.title("Tkinter Window - Center")

# set the top left position to 250,50
root.geometry(f"+{250}+{50}")
window_set_width(root, 1000)
window_set_height(root, 250)

root.mainloop()
