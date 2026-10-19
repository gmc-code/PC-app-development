import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits and grid size
ax.set_xlim(0, 3)  # Number of columns
ax.set_ylim(0, 4)  # Number of rows

# Set ticks at the edges (for grid lines)
ax.set_xticks(range(4))  # At 0, 1, 2, 3 (edges)
ax.set_yticks(range(5))  # At 0, 1, 2, 3, 4 (edges)

# Set the tick labels (offset manually)
for i in range(3):
    ax.text(i + 0.5, -0.1, str(i), ha='center', va='center', transform=ax.transData)  # X labels
for j in range(4):
    ax.text(-0.1, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)

# Add rectangles for each widget
widgets = [
    {"name": "inches_label", "xy": (0, 0), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "inches_entry", "xy": (1, 0), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "cm_label", "xy": (0, 2), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "cm_text", "xy": (1, 2), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "convert_button", "xy": (0, 1), "width": 2, "height": 1, "color": "lightcoral"}
]

for widget in widgets:
    rect = patches.Rectangle(widget["xy"], widget["width"], widget["height"], linewidth=1, edgecolor='black', facecolor=widget["color"])
    ax.add_patch(rect)
    ax.text(
        widget["xy"][0] + widget["width"] / 2,
        widget["xy"][1] + widget["height"] / 2,
        widget["name"], ha='center', va='center'
    ).
# widget["xy"][0] + widget["width"] / 2:
# This centers the x-coordinate of the text within the rectangle.

# widget["xy"][0] gives the x-coordinate of the bottom-left corner.
# Adding widget["width"] / 2 shifts the text to the horizontal center of the rectangle.
# widget["xy"][1] + widget["height"] / 2:
# Similarly, this centers the y-coordinate of the text within the rectangle.

# widget["xy"][1] gives the y-coordinate of the bottom-left corner.
# Adding widget["height"] / 2 shifts the text to the vertical center of the rectangle.


# Move the xlabel to the top
ax.xaxis.set_label_coords(0.5, 1.09)
# (0.5, 1.09):
# - 0.5 places the label horizontally centered (0 = left edge, 1 = right edge of the axis)
# - 1.09 moves it slightly above the top of the axis (1.0 is the top edge)

plt.xlabel('Column')  # Set the xlabel text

# Move the ylabel to the left side
ax.yaxis.set_label_coords(-0.05, 0.5)
# (-0.05, 0.5):
# - -0.05 shifts the label slightly to the left of the axis (0 = axis edge)
# - 0.5 centers the label vertically along the y-axis (0 = bottom, 1 = top)

plt.ylabel('Row')  # Set the ylabel text

# # Use suptitle to position the title above the plot
# fig.suptitle('Tkinter Widget Positioning via Grid Method', fontsize=16, y=0.98)  # Adjust the y position of the title
# # Adjust subplot to make space for title and labels
# plt.subplots_adjust(top=0.85)

# Invert y-axis for correct orientation
plt.gca().invert_yaxis()

# Hide original tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Show the plot
plt.show()
