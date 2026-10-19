import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(7, 5))

# The root window uses 1 column and 4 rows
ax.set_xlim(0, 1)  # Number of columns in root
ax.set_ylim(0, 4)  # Number of rows in root

# Set ticks at the edges (for grid lines)
ax.set_xticks([0, 1])
ax.set_yticks(range(5))

# Set the tick labels (offset manually)
ax.text(0.5, -0.1, "0", ha='center', va='center', transform=ax.transData)  # X label
for j in range(4):
    ax.text(-0.03, j + 0.5, str(j), ha='center', va='center', transform=ax.transData, rotation=90)  # Y labels

# Add grid lines
ax.grid(True)

# Rows 0, 1 and 2 each hold a row_frame.
# Inside each row_frame there is its own grid: the OptionMenu in column 0 and the Spinbox in column 1.
for i in range(3):
    frame = patches.Rectangle((0.02, i + 0.08), 0.96, 0.84, linewidth=1.5,
                              edgecolor='black', facecolor='lightyellow')
    ax.add_patch(frame)
    ax.text(0.05, i + 0.2, f"row_frame (row={i})", ha='left', va='center', fontsize=9)
    option = patches.Rectangle((0.06, i + 0.32), 0.56, 0.5, linewidth=1,
                               edgecolor='black', facecolor='lightgreen')
    spin = patches.Rectangle((0.66, i + 0.32), 0.28, 0.5, linewidth=1,
                             edgecolor='black', facecolor='lightgreen')
    ax.add_patch(option)
    ax.add_patch(spin)
    ax.text(0.34, i + 0.57, "pizza_optionmenu\n(row=0, column=0)", ha='center', va='center', fontsize=9)
    ax.text(0.80, i + 0.57, "pizza_spinbox\n(row=0, column=1)", ha='center', va='center', fontsize=9)

# Row 3 holds the total cost label
label = patches.Rectangle((0, 3), 1, 1, linewidth=1, edgecolor='black', facecolor='lightblue')
ax.add_patch(label)
ax.text(0.5, 3.5, "total_cost_label (row=len(pizza_rows) = 3)", ha='center', va='center')

# Move the xlabel to the top
ax.xaxis.set_label_coords(0.5, 1.08)  # Centered above the axis
plt.xlabel('Column (root)')

# Move the ylabel to the left side
ax.yaxis.set_label_coords(-0.06, 0.5)  # Slightly left of the axis
plt.ylabel('Row (root)')

# Invert y-axis for correct orientation
plt.gca().invert_yaxis()

# Hide original tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Show the plot
plt.show()
