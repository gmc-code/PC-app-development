import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter hello world")
root.geometry("600x400")
root.resizable(True, True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
min_width = 300
min_height = 200
root.minsize(min_width, min_height)
root.maxsize(screen_width, screen_height)
root.state=("zoomed")
root.attributes('-alpha',0.9)
root.attributes('-topmost', 1)

# Enable editing (use "disabled" to disable)
# screen_width = root.winfo_screenwidth() - 40
# screen_height = root.winfo_screenheight() -100
# x_coord = 20
# y_coord = 20
# root.geometry("{}x{}+{}+{}".format(screen_width, screen_height, x_coord, y_coord))

# Customize options
root.config(
    bg="lightyellow",  # Background color
    bd=2,  # Border width
    relief="solid",  # Border style
)

# Start the main event loop
root.mainloop()

