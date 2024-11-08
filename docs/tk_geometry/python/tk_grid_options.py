import tkinter as tk

def create_frame(window, title, row, column):
    frame = tk.LabelFrame(window, text=title, padx=10, pady=10)
    frame.grid(row=row, column=column, padx=10, pady=10)
    return frame

def add_label(frame, text, row, column, bg_color, **kwargs):
    label = tk.Label(frame, text=text, bg=bg_color)
    label.grid(row=row, column=column, **kwargs)
    return label

# Create the main window
window = tk.Tk()
window.title("Grid Options Examples")
# window.geometry("600x600")

# Rowspan example
frame1 = create_frame(window, "Rowspan Example", 0, 0)
add_label(frame1, "Rowspan 2", 0, 0, "lightblue", rowspan=2, sticky="ns")
add_label(frame1, "Label 1", 0, 1, "lightgreen")
add_label(frame1, "Label 2", 1, 1, "lightcoral")

# Columnspan example
frame2 = create_frame(window, "Columnspan Example", 0, 1)
add_label(frame2, "Columnspan 2", 0, 0, "lightblue", columnspan=2, sticky="ew")
add_label(frame2, "Label 1", 1, 0, "lightgreen")
add_label(frame2, "Label 2", 1, 1, "lightcoral")

# Padx example
frame3 = create_frame(window, "Padx Example", 1, 0)
add_label(frame3, "Padx 10", 0, 0, "lightblue", padx=10)
add_label(frame3, "Label 1", 0, 1, "lightgreen")

# Pady example
frame4 = create_frame(window, "Pady Example", 1, 1)
add_label(frame4, "Pady 10", 0, 0, "lightblue", pady=10)
add_label(frame4, "Label 1", 1, 0, "lightgreen")

# ipadx example
frame5 = create_frame(window, "ipadx Example", 2, 0)
add_label(frame5, "ipadx 10", 0, 0, "lightblue", ipadx=10)
add_label(frame5, "Label 1", 0, 1, "lightgreen")

# ipady example
frame6 = create_frame(window, "ipady Example", 2, 1)
add_label(frame6, "ipady 10", 0, 0, "lightblue", ipady=10)
add_label(frame6, "Label 1", 1, 0, "lightgreen")

# Start the main event loop
window.mainloop()
