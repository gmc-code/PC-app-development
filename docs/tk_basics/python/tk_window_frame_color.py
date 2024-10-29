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
window.state("zoomed")
# window.attributes('-alpha', 0.8)
window.attributes('-topmost', 1)

# Customize options
# window.config(
#     bg="lightyellow",  # Background color
#     bd=20,  # Border width
#     relief="solid"  # Border style
# )

# Create a frame with a light blue border
frame = tk.Frame(window, bg="lightyellow", bd=1, relief="solid", highlightbackground="lightblue", highlightcolor="lightgreen", highlightthickness=5)
frame.pack(expand=True, fill='both')

# Start the main event loop
window.mainloop()
