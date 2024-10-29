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
window.title("place calc")
window.geometry("250x150")

#  create widgets in frame
price_per_item_label = tk.Label(window, text="Price per item")
price_per_item_entry = tk.Entry(window)

number_of_items_label = tk.Label(window, text="Number of items")
number_of_items_entry = tk.Entry(window)

total_price_label = tk.Label(window, text="Total price")
total_price_entry = tk.Entry(window)

calculate_button = tk.Button(window, text="Calculate total", bg="light blue", command=calculate_price)

# place widgets
price_per_item_label.place(x=0, y=0)
price_per_item_entry.place(x=100, y=0)
number_of_items_label.place(x=0, y=30)
number_of_items_entry.place(x=100, y=30)
calculate_button.place(x=0, y=60, width=230)
total_price_label.place(x=0, y=90)
total_price_entry.place(x=100, y=90)

# Start the main event loop
window.mainloop()
