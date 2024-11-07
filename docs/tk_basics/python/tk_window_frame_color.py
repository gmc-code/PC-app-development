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

# Create a frame with a light blue border and red highlight color
frame = tk.Frame(window, bg="lightyellow", bd=1, relief="solid", highlightbackground="lightblue", highlightcolor="red", highlightthickness=5)
frame.pack(expand=True, fill='both')

# Add a widget inside the frame to see the effect of the red highlight color
label = tk.Label(frame, text="Hello, World!", bg="lightyellow")
label.pack(pady=20)

# Set focus to the frame to see the red highlight color
frame.focus_set()

# Start the main event loop
window.mainloop()
