import tkinter as tk


def calculate_price():
    try:
        total = int(price_per_item_entry.get()) * int(number_of_items_entry.get())
        total_price_entry.delete(0, "end")
        total_price_entry.insert(0, string=str(total))
    except:
        pass


# Create the main window
root = tk.Tk()
root.title("pack calc")
root.geometry("250x150")

#  create widgets in frame
price_per_item_label = tk.Label(root, text="Price per item")
price_per_item_entry = tk.Entry(root)

number_of_items_label = tk.Label(root, text="Number of items")
number_of_items_entry = tk.Entry(root)

total_price_label = tk.Label(root, text="Total price")
total_price_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate total", bg="light blue", command=calculate_price)

# # place widgets
price_per_item_label.pack()
price_per_item_entry.pack()
number_of_items_label.pack()
number_of_items_entry.pack()
# fill the horizontal space; x axis
calculate_button.pack(fill="x", padx=10)
total_price_label.pack()
total_price_entry.pack()

# Start the main event loop
root.mainloop()
