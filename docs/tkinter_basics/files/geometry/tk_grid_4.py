from tkinter import *



def create_rectangle_from_grid_bbox(canvas, bbox, **kwargs):
    # Unpack the bounding box tuple
    x0, y0, width, height = bbox
    
    # Calculate the coordinates of the bottom-right corner
    x1 = x0 + width -1
    y1 = y0 + height -1
    print(x0, y0, x1, y1)

    # Draw the rectangle on the canvas
    canvas.create_rectangle(x0, y0, x1, y1, **kwargs)

# Create a window
w = Tk()
w.title('Usage of grid_bbox')


# Create a transparent canvas
canvas = Canvas(w, highlightthickness=0)  # Remove border around the canvas
canvas.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="news")  # span across the labels

# Create labels
label_sticky = ""
label_padx = 100
label_pady = 100
label_ipadx = 100
label_ipady = 50

lab_1 = Label(w, text='row 0, column 0', font='Verdana 32', width=20, height=3, bg='red')
lab_1.grid(row=0, column=0, sticky=label_sticky, padx=label_padx, pady=label_pady)

lab_2 = Label(w, text='row 0, column 1', font='Verdana 16', width=20, height=3, bg='yellow')
lab_2.grid(row=0, column=1, sticky=label_sticky, padx=label_padx, pady=label_pady, ipadx=label_ipadx, ipady=label_ipady)

lab_3 = Label(w, text='row 1, column 0', font='Verdana 16', width=20, height=3, bg='green')
lab_3.grid(row=1, column=0, sticky=label_sticky, padx=label_padx, pady=label_pady)

lab_4 = Label(w, text='row 1, column 1', font='Verdana 16', width=20, height=3, bg='blue')
lab_4.grid(row=1, column=1, sticky=label_sticky, padx=label_padx, pady=label_pady)

w.update_idletasks()
# Get the bounding box
# w.grid_bbox(row, column, columnspan=1, rowspan=1) returns (x, y, width, height)
bb0111 = w.grid_bbox(0, 1, 1, 1)
bb1011 = w.grid_bbox(1, 0, 1, 1)
bb0011 = w.grid_bbox(0, 0, 1, 1)
bb1111 = w.grid_bbox(1, 1, 1, 1)
# Draw lines to mark the grid sizes
create_rectangle_from_grid_bbox(canvas, bb0111, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb1011, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb0011, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb1111, outline="blue", width=1)

# Start the main event loop
w.mainloop()
