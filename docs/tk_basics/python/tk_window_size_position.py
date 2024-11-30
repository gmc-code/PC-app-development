import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - size and position')

window_width = 400
window_height = 300
left_x = 200
top_y = 50
# set the size and position of the window
root.geometry(f'{window_width}x{window_height}+{left_x}+{top_y}')
# set window to stay topmost
root.attributes('-topmost', True)
# set window size to be static or un resizable
root.resizable(False, False)

root.mainloop()