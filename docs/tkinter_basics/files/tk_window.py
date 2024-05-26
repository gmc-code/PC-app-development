import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Tkinter hello world")
window.geometry('600x400')
print(window.geometry)
# screen_width = window.winfo_screenwidth() - 40
# screen_height = window.winfo_screenheight() -100
# x_coord = 20
# y_coord = 20
# window.geometry("{}x{}+{}+{}".format(screen_width, screen_height, x_coord, y_coord))

# Start the main event loop
window.mainloop()
