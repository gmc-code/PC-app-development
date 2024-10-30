import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits and grid size
ax.set_xlim(0, 4)  # Number of columns
ax.set_ylim(0, 7)  # Number of rows

# Set ticks at the edges (for grid lines)
ax.set_xticks(range(5))  # At 0, 1, 2, 3, 4 (edges)
ax.set_yticks(range(8))  # At 0, 1, 2, 3, 4, 5, 6, 7 (edges)

# Set the tick labels (offset manually)
for i in range(4):
    ax.text(i + 0.5, -0.1, str(i), ha='center', va='center', transform=ax.transData)  # X labels
for j in range(7):
    ax.text(-0.1, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)

# Define updated widget placements and properties
widgets = [
    {"name": "Customer Name", "xy": (0, 0), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "customer_entry", "xy": (1, 0), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "Pizza Type", "xy": (0, 1), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "pizza_frame", "xy": (1, 1), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "Pizza Size", "xy": (0, 2), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "size_frame", "xy": (1, 2), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "Quantity", "xy": (0, 3), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "quantity_menu", "xy": (1, 3), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "Cost per pizza", "xy": (1, 4), "width": 1, "height": 1, "color": "lightyellow"},
    {"name": "Order cost", "xy": (1, 5), "width": 1, "height": 1, "color": "lightyellow"},
    {"name": "Add Order", "xy": (1, 6), "width": 1, "height": 1, "color": "#5bd85b"},
    {"name": "Orders_label", "xy": (2, 0), "width": 2, "height": 1, "color": "lightblue"},
    {"name": "Orders", "xy": (2, 1), "width": 2, "height": 5, "color": "#c0f0c0"},
    {"name": "Delete Selected \n Pizza", "xy": (2, 6), "width": 1,"height" : 1,"color":"#ffdae0"},
    {"name":"Cancel Orders","xy" :(3 ,6),"width" : 1,"height" : 1,"color":"#ffdae0"}
]

# entry_bg = "#ffffff"  # white
# text_bg = "#f0f0f0"  # Very light gray
# text_fg = "#000000"  # black

# quantity_bg = "#93ccea"  # Very soft blue
# quantity_hover_bg = "#53aede"  # soft blue

# order_list_total_bg = "#c0f0c0"  # Very soft lime green
# order_list_total_selected_bg = "#5bd85b"  # moderate lime green

# add_button_bg = "#c0f0c0"  # Very soft lime green
# add_button_fg = "#000000"  # black
# add_button_hover_bg = "#5bd85b"  # moderate lime green

# delete_button_bg = "#ffdae0"  # very pale red
# delete_button_fg = "#000000"  # black
# delete_button_hover_bg = "#ffc1cb"  # very pale red

# Add rectangles and labels to the plot for each widget
for widget in widgets:
    rect = patches.Rectangle(widget["xy"], widget["width"], widget["height"],
                             linewidth=1, edgecolor='black', facecolor=widget["color"])
    ax.add_patch(rect)
    ax.text(
        widget["xy"][0] + widget["width"] / 2,
        widget["xy"][1] + widget["height"] / 2,
        widget["name"], ha='center', va='center'
    )

# Move the xlabel to the top
ax.xaxis.set_label_coords(0.5, 1.09)
plt.xlabel('Column')

# Move the ylabel to the left side
ax.yaxis.set_label_coords(-0.05, 0.5)
plt.ylabel('Row')

# Invert y-axis for correct orientation
plt.gca().invert_yaxis()

# Hide original tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Show the plot
plt.show()
