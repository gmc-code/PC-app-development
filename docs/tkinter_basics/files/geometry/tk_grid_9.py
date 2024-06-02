from tkinter import *

def create_rectangle_from_grid_bbox(canvas, bbox, **kwargs):
    # Unpack the bounding box tuple
    x0, y0, width, height = bbox
    
    # Calculate the coordinates of the bottom-right corner
    x1 = x0 + width - 1
    y1 = y0 + height - 1

    # Draw the rectangle on the canvas
    canvas.create_rectangle(x0, y0, x1, y1, **kwargs)

# Create a window
w = Tk()
w.title('Usage of grid_bbox')

# Create a transparent canvas
canvas = Canvas(w, highlightthickness=0)  # Remove border around the canvas
canvas.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="news")  # span across the labels

# Create labels
news_sticky = "news"
nw_sticky = "nw"
ne_sticky = "ne"

sw_sticky = "sw"
se_sticky = "se"

ns_sticky = "ns"
ew_sticky = "ew"

label_padx = 10
label_pady = 10
label_ipadx = 10
label_ipady = 10
corner_padx = 0
corner_pady = 0
corner_ipadx = 0
corner_ipady = 0


lab_1 = Label(w, text='row 0, column 0', font='Verdana 16', width=20, height=3, bg='red')
lab_1.grid(row=0, column=0, sticky=nw_sticky)

lab_2 = Label(w, text='row 0, column 1', font='Verdana 16', width=20, height=3, bg='yellow')
lab_2.grid(row=0, column=1, padx=label_padx, pady=label_pady, ipadx=label_ipadx, ipady=label_ipady)

lab_3 = Label(w, text='row 0, column 2', font='Verdana 16', width=20, height=3, bg='green')
lab_3.grid(row=0, column=2, sticky=ne_sticky)

lab_4 = Label(w, text='row 1, column 0', font='Verdana 16', width=20, height=3, bg='orange')
lab_4.grid(row=1, column=0, padx=label_padx, pady=label_pady, ipadx=label_ipadx, ipady=label_ipady)

lab_5 = Label(w, text='row 1, column 1', font='Verdana 16', width=20, height=3, bg='blue')
lab_5.grid(row=1, column=1, sticky=news_sticky)

lab_6 = Label(w, text='row 1, column 2', font='Verdana 16', width=20, height=3, bg='pink')
lab_6.grid(row=1, column=2, padx=label_padx, pady=label_pady, ipadx=label_ipadx, ipady=label_ipady)

lab_7 = Label(w, text='row 2, column 0', font='Verdana 16', width=20, height=3, bg='purple')
lab_7.grid(row=2, column=0, sticky=sw_sticky)

lab_8 = Label(w, text='row 2, column 1', font='Verdana 16', width=20, height=3, bg='cyan')
lab_8.grid(row=2, column=1, padx=label_padx, pady=label_pady, ipadx=label_ipadx, ipady=label_ipady)

lab_9 = Label(w, text='row 2, column 2', font='Verdana 16', width=20, height=3, bg='magenta')
lab_9.grid(row=2, column=2, sticky=se_sticky)

w.update_idletasks()

# Get the bounding boxes
bb0011 = w.grid_bbox(0, 0, 1, 1)
bb0111 = w.grid_bbox(0, 1, 1, 1)
bb0211 = w.grid_bbox(0, 2, 1, 1)
bb1011 = w.grid_bbox(1, 0, 1, 1)
bb1111 = w.grid_bbox(1, 1, 1, 1)
bb1211 = w.grid_bbox(1, 2, 1, 1)
bb2011 = w.grid_bbox(2, 0, 1, 1)
bb2111 = w.grid_bbox(2, 1, 1, 1)
bb2211 = w.grid_bbox(2, 2, 1, 1)

# Draw lines to mark the grid sizes
create_rectangle_from_grid_bbox(canvas, bb0011, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb0111, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb0211, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb1011, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb1111, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb1211, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb2011, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb2111, outline="blue", width=1)
create_rectangle_from_grid_bbox(canvas, bb2211, outline="blue", width=1)

# Start the main event loop
w.mainloop()
