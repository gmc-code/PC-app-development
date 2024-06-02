from tkinter import *

# Create a window
window = Tk()
window.title('Labels with Different Sticky Settings')
window.geometry("1000x200")

# Create labels
labels = []
sticky_settings = ["ne", "new", "nw", "ns", "se", "sew", "sw", "e", "ew", "w", "news" ]
for i, sticky in enumerate(sticky_settings):
    label = Label(window, text=f"{i+1} {sticky}", font='Verdana 12 bold', bg='lightgray')
    label.grid(row=0, column=i, sticky=sticky, padx=0, pady=0)
    labels.append(label)

# Configure row 0 to have equal weight for each label
window.grid_rowconfigure(0, weight=1)

# Configure columns to have equal weight
for i in range(len(sticky_settings)):
    window.grid_columnconfigure(i, weight=1)

# Start the main event loop
window.mainloop()
