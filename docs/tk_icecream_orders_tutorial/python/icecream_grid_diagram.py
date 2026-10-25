import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(9, 7))

# Set the limits and grid size
ax.set_xlim(0, 4)  # Number of columns
ax.set_ylim(0, 7)  # Number of rows

# Set ticks at the edges (for grid lines)
ax.set_xticks(range(5))  # At 0 to 4 (edges)
ax.set_yticks(range(8))  # At 0 to 7 (edges)

# Set the tick labels (offset manually)
for i in range(4):
    ax.text(i + 0.5, -0.12, str(i), ha='center', va='center', transform=ax.transData)  # X labels
for j in range(7):
    ax.text(-0.08, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)
ax.set_axisbelow(True)

# Colours for each type of widget
LABEL = "lightblue"
RADIO = "lightgreen"
MENU = "#ffd6e0"
LISTBOX = "lightyellow"
BUTTON = "#ffc58f"

# Define widget placements and properties
widgets = [
    {"name": "title_label\n(columnspan=2)", "xy": (0, 0), "width": 2, "height": 1, "color": LABEL},
    {"name": "flavour_label", "xy": (0, 1), "width": 1, "height": 1, "color": LABEL},
    {"name": "flavour_frame\n(radio buttons)", "xy": (1, 1), "width": 1, "height": 1, "color": RADIO},
    {"name": "container_label", "xy": (0, 2), "width": 1, "height": 1, "color": LABEL},
    {"name": "container_menu\n(drop-down)", "xy": (1, 2), "width": 1, "height": 1, "color": MENU},
    {"name": "topping_label", "xy": (0, 3), "width": 1, "height": 1, "color": LABEL},
    {"name": "topping_menu\n(drop-down)", "xy": (1, 3), "width": 1, "height": 1, "color": MENU},
    {"name": "price_label", "xy": (1, 4), "width": 1, "height": 1, "color": LABEL},
    {"name": "add_button", "xy": (1, 5), "width": 1, "height": 1, "color": BUTTON},
    {"name": "order_heading\n(columnspan=2)", "xy": (2, 0), "width": 2, "height": 1, "color": LABEL},
    {"name": "order_listbox\n(rowspan=4, columnspan=2)", "xy": (2, 1), "width": 2, "height": 4, "color": LISTBOX},
    {"name": "total_label\n(columnspan=2)", "xy": (2, 5), "width": 2, "height": 1, "color": LABEL},
    {"name": "remove_button", "xy": (2, 6), "width": 1, "height": 1, "color": BUTTON},
    {"name": "clear_button", "xy": (3, 6), "width": 1, "height": 1, "color": BUTTON},
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
ax.xaxis.set_label_coords(0.5, 1.06)
plt.xlabel('Column')

# Move the ylabel to the left side
ax.yaxis.set_label_coords(-0.05, 0.5)
plt.ylabel('Row')

# Invert y-axis for correct orientation
plt.gca().invert_yaxis()

# Hide original tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Key showing the colour for each type of widget
key = [patches.Patch(facecolor=c, edgecolor='black', label=n) for n, c in
       [("Label", LABEL), ("Frame of radio buttons", RADIO), ("OptionMenu (drop-down)", MENU),
        ("Listbox", LISTBOX), ("Button", BUTTON)]]
ax.legend(handles=key, loc='upper center', bbox_to_anchor=(0.5, -0.03), ncol=5, fontsize=8, frameon=False)

# Save and show the plot
plt.tight_layout()
plt.savefig("icecream_grid.png", dpi=100)
plt.show()
