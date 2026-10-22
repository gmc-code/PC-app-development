import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5.6, 7))

# Set the limits and grid size
ax.set_xlim(0, 2)  # Number of columns
ax.set_ylim(0, 9)  # Number of rows

# Set ticks at the edges (for grid lines)
ax.set_xticks(range(3))  # At 0, 1, 2 (edges)
ax.set_yticks(range(10))  # At 0 to 9 (edges)

# Set the tick labels (offset manually)
for i in range(2):
    ax.text(i + 0.5, -0.15, str(i), ha='center', va='center', transform=ax.transData)  # X labels
for j in range(9):
    ax.text(-0.08, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)

# Define widget placements and properties
widgets = [
    {"name": "title_label", "xy": (0, 0), "width": 2, "height": 1, "color": "lightblue"},
    {"name": "instructions_label", "xy": (0, 1), "width": 2, "height": 1, "color": "lightblue"},
    {"name": "item_entry", "xy": (0, 2), "width": 1, "height": 1, "color": "lightyellow"},
    {"name": "add_button", "xy": (1, 2), "width": 1, "height": 1, "color": "lightcoral"},
    {"name": "item_listbox\n(rowspan=4)", "xy": (0, 3), "width": 1, "height": 4, "color": "lightyellow"},
    {"name": "change_button", "xy": (1, 3), "width": 1, "height": 1, "color": "lightcoral"},
    {"name": "remove_button", "xy": (1, 4), "width": 1, "height": 1, "color": "lightcoral"},
    {"name": "sort_button", "xy": (1, 5), "width": 1, "height": 1, "color": "lightcoral"},
    {"name": "clear_button", "xy": (1, 6), "width": 1, "height": 1, "color": "lightcoral"},
    {"name": "count_label", "xy": (0, 7), "width": 2, "height": 1, "color": "lightblue"},
    {"name": "message_label", "xy": (0, 8), "width": 2, "height": 1, "color": "lightblue"},
]

# Add rectangles and labels to the plot for each widget
for widget in widgets:
    rect = patches.Rectangle(widget["xy"], widget["width"], widget["height"],
                             linewidth=1, edgecolor='black', facecolor=widget["color"])
    ax.add_patch(rect)
    ax.text(
        widget["xy"][0] + widget["width"] / 2,
        widget["xy"][1] + widget["height"] / 2,
        widget["name"], ha='center', va='center', fontsize=9
    )

# Move the xlabel to the top
ax.xaxis.set_label_coords(0.5, 1.06)  # Centered above the axis
plt.xlabel('Column')

# Move the ylabel to the left side
ax.yaxis.set_label_coords(-0.07, 0.5)  # Slightly left of the axis
plt.ylabel('Row')

# Invert y-axis for correct orientation
plt.gca().invert_yaxis()

# Hide original tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Show the plot
plt.show()
