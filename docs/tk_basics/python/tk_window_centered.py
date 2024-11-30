import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - Centered')

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen, using top left position
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.mainloop()