import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits and grid size
ax.set_xlim(0, 4)  # Number of columns
ax.set_ylim(0, 5)  # Number of rows

# Set ticks at the edges (for grid lines)
ax.set_xticks(range(5))  # At 0, 1, 2, 3, 4 (edges)
ax.set_yticks(range(5))  # At 0, 1, 2, 3, 4, (edges)

# Set the tick labels (offset manually)
for i in range(4):
    ax.text(i + 0.5, -0.1, str(i), ha='center', va='center', transform=ax.transData)  # X labels
for j in range(7):
    ax.text(-0.1, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)

# Define updated widget placements and properties
widgets = [
    {"name": "label1", "xy": (0, 0), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "label2", "xy": (1, 1), "width": 1, "height": 1, "color": "lightgreen"},
    {"name": "label3", "xy": (2, 2), "width": 1, "height": 1, "color": "lightblue"},
    {"name": "label4", "xy": (0, 3), "width": 3, "height": 1, "color": "lightgreen"}
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
