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
root.state("zoomed")
# root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)

# Create a frame with a light blue border and red highlight color
frame = tk.Frame(root, bg="lightyellow", bd=1, relief="solid", highlightbackground="lightblue", highlightcolor="red", highlightthickness=5)
frame.pack(expand=True, fill='both')

# Add a widget inside the frame to see the effect of the red highlight color
label = tk.Label(frame, text="Hello, World!", bg="lightyellow")
label.pack(pady=20)

# Set focus to the frame to see the red highlight color
frame.focus_set()

# Start the main event loop
root.mainloop()
