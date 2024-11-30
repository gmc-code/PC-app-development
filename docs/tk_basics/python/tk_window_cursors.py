import tkinter as tk

# List of all Tkinter cursor styles
all_cursors = [
    "arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "man",
    "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target",
    "tcross", "trek", "watch", "X_cursor", "based_arrow_down", "based_arrow_up", "boat",
    "bogosity", "bottom_left_corner", "bottom_right_corner", "bottom_side", "bottom_tee",
    "box_spiral", "center_ptr", "coffee_mug", "cross_reverse", "crosshair", "diamond_cross",
    "dot", "double_arrow", "draft_large", "draft_small", "draped_box", "gobbler", "gumby",
    "hand1", "hand2", "icon", "iron_cross", "left_ptr", "left_side", "left_tee", "leftbutton",
    "ll_angle", "lr_angle", "middlebutton", "pencil", "question_arrow", "right_ptr", "right_side",
    "right_tee", "rightbutton", "rtl_logo", "sailboat", "sb_down_arrow", "sb_h_double_arrow",
    "sb_left_arrow", "sb_right_arrow", "sb_up_arrow", "sb_v_double_arrow", "top_left_arrow",
    "top_left_corner", "top_right_corner", "top_side", "top_tee", "ul_angle", "umbrella",
    "ur_angle", "xterm"
]

# standard_os_cursors
cursors= [
    "arrow", "cross", "hand2", "watch", "xterm", "circle",
    "fleur", "plus", "sizing"
]

# Initialize the main Tkinter window
root = tk.Tk()
root.geometry("300x200+800+500")
root.title("Cursor Demo")

# Label to show current cursor name
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=40)

# Function to iterate through each cursor
def cycle_cursors(index=0):
    if index < len(cursors):
        current_cursor = cursors[index]
        label.config(text=f"Cursor: {current_cursor}")
        root.configure(cursor=current_cursor)
        # Call the function again after set number of ms with the next cursor
        root.after(1000, cycle_cursors, index + 1)
    else:
        # Reset to default cursor after the cycle completes
        root.configure(cursor="arrow")
        label.config(text="Cycle complete")

# Start cycling through cursors
cycle_cursors()

# Run the Tkinter main loop
root.mainloop()
