import tkinter as tk

def update_intensity(value):
    # Update the rectangle's intensity based on the Scale value
    intensity = int(float(value) * 255)
    color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
    canvas.itemconfig(rect, fill=color)

root = tk.Tk()
root.title("Scale Example")
root.geometry("300x200")

# Create a DoubleVar with an initial value
double_var = tk.DoubleVar(value=0.5)

# Create a Scale and associate it with the DoubleVar
scale = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, variable=double_var, command=update_intensity)
scale.pack()

# Create a Canvas to display the greyscale rectangle
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack(pady=20)

# Create a rectangle with initial intensity
initial_intensity = int(double_var.get() * 255)
rect = canvas.create_rectangle(0, 0, 200, 100, fill=f"#{initial_intensity:02x}{initial_intensity:02x}{initial_intensity:02x}")

root.mainloop()
