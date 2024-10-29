import tkinter as tk


def calculate_price():
    try:
        total = int(price_per_item_entry.get()) * int(number_of_items_entry.get())
        total_price_entry.delete(0, "end")
        total_price_entry.insert(0, string=str(total))
    except:
        pass


# Create the main window
window = tk.Tk()
window.title("grid calc")
window.geometry("250x150")

#  create widgets in frame
price_per_item_label = tk.Label(window, text="Price per item")
price_per_item_entry = tk.Entry(window)

number_of_items_label = tk.Label(window, text="Number of items")
number_of_items_entry = tk.Entry(window)

total_price_label = tk.Label(window, text="Total price")
total_price_entry = tk.Entry(window)

calculate_button = tk.Button(window, text="Calculate total", bg="light blue", command=calculate_price)

# # place widgets
price_per_item_label.grid(row=0, column=0)
price_per_item_entry.grid(row=0, column=1)
number_of_items_label.grid(row=1, column=0)
number_of_items_entry.grid(row=1, column=1)
# fill the horizontal space; x axis
calculate_button.grid(row=2, column=0, columnspan=2, ipadx=70)
total_price_label.grid(row=3, column=0)
total_price_entry.grid(row=3, column=1)

# Start the main event loop
window.mainloop()
