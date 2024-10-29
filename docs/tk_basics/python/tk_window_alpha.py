import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Tkinter hello world")
window.geometry("600x400")
window.resizable(True, True)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
min_width = 300
min_height = 200
window.minsize(min_width, min_height)
window.maxsize(screen_width, screen_height)
window.state=("zoomed")
window.attributes('-alpha',0.9)
window.attributes('-topmost', 1)

# Enable editing (use "disabled" to disable)
# screen_width = window.winfo_screenwidth() - 40
# screen_height = window.winfo_screenheight() -100
# x_coord = 20
# y_coord = 20
# window.geometry("{}x{}+{}+{}".format(screen_width, screen_height, x_coord, y_coord))

# Customize options
window.config(
    bg="lightyellow",  # Background color
    bd=2,  # Border width
    relief="solid",  # Border style
)

# Start the main event loop
window.mainloop()

