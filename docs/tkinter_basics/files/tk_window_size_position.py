import tkinter as tk


window = tk.Tk()
window.title('Tkinter Window - size and position')

window_width = 400
window_height = 300
left_x = 200
top_y = 50
# set the size and position of the window
window.geometry(f'{window_width}x{window_height}+{left_x}+{top_y}')
# set window to stay topmost
window.attributes('-topmost', True)
# set window size to be static or un resizable
window.resizable(False, False)

window.mainloop()