import tkinter as tk


def window_set_height(window, height):
    # Wait for the window to be fully initialized
    window.update_idletasks()
    window.geometry(f"{window.winfo_width()}x{height}")


def window_set_width(window, width):
    # Wait for the window to be fully initialized
    window.update_idletasks()
    window.geometry(f"{width}x{window.winfo_height()}")


window = tk.Tk()
window.title("Tkinter Window - Center")

# set the top left position to 250,50
window.geometry(f"+{250}+{50}")
window_set_width(window, 1000)
window_set_height(window, 250)

window.mainloop()
