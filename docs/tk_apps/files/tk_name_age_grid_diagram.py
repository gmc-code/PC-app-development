import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits and grid size (matches widget grid layout)
ax.set_xlim(0, 2)  # Number of columns
ax.set_ylim(0, 4)  # Number of rows

# Set ticks at the edges (for grid lines)
ax.set_xticks(range(3))  # At 0, 1, 2 (edges)
ax.set_yticks(range(5))  # At 0, 1, 2, 3, 4 (edges)

# Set tick labels (offset manually)
for i in range(2):
    ax.text(i + 0.5, -0.1, str(i), ha='center', va='center', transform=ax.transData)  # X labels
for j in range(4):
    ax.text(-0.1, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)

# Define updated widget placements and properties
widgets = [
    {"name": "name_label", "xy": (0, 0), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "name_entry", "xy": (1, 0), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "age_label", "xy": (0, 1), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "age_entry", "xy": (1, 1), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "name_age_button", "xy": (0, 2), "width": 2, "height": 1, "color": "lightcoral"},
    {"name": "name_age_text", "xy": (0, 3), "width": 2, "height": 1, "color": "lightyellow"},
]

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

# Move xlabel to the top
ax.xaxis.set_label_coords(0.5, 1.09)  # Centered above the axis
plt.xlabel('Column')

# Move ylabel to the left side
ax.yaxis.set_label_coords(-0.05, 0.5)  # Slightly left of the axis
plt.ylabel('Row')

# Invert y-axis for correct orientation
plt.gca().invert_yaxis()

# Hide original tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Show the plot
plt.show()

