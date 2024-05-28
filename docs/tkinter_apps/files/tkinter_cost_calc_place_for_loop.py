import tkinter as tk

"""# based on https://www.youtube.com/watch?v=OKfra37r4D0&list=PLs3IFJPw3G9KL3huzPS7g-0PCbS7Auc7I&index=4
"""


def calculate_price():
    try:
        total = int(price_per_item_entry.get()) * int(number_of_items_entry.get())
        total_price_entry.delete(0, "end")
        total_price_entry.insert(0, string=str(total))
    except:
        pass


# Create the main window
window = tk.Tk()
window.title("Price calculator - place programmatically")
window.geometry("300x300")

#  create widgets in frame
price_per_item_label = tk.Label(window, text="Price per item")
price_per_item_entry = tk.Entry(window)

number_of_items_label = tk.Label(window, text="Number of items")
number_of_items_entry = tk.Entry(window)

total_price_label = tk.Label(window, text="Total price")
total_price_entry = tk.Entry(window)

calculate_button = tk.Button(window, text="Calculate total", bg="light blue", command=calculate_price)

# place widgets
# Create a list of widgets
widgets = [price_per_item_label, price_per_item_entry, number_of_items_label, number_of_items_entry,
            calculate_button, total_price_label, total_price_entry]
# Set the initial y-coordinate
y = 0
# Place the widgets using a for loop
for widget in widgets:
    widget.place(x=0, y=y)
    y += 25  # Increment y by 25 for each widget


window.mainloop()
