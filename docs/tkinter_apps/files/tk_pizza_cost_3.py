import tkinter as tk

# Dictionary of pizza names and costs
pizza_prices = {
    "Margherita": 8.99,
    "Pepperoni": 10.99,
    "Vegetarian": 9.49,
    "Supreme": 11.99,
}

def calculate_total_cost(*args):
    total_cost = 0
    for pizza_row in pizza_rows:
        selected_pizza = pizza_row["var"].get()
        num_pizzas = int(pizza_row["spinbox"].get())
        pizza_cost = pizza_prices.get(selected_pizza, 0)
        total_cost += pizza_cost * num_pizzas
    total_cost_label.config(text=f"Total Cost: ${total_cost:.2f}")

window = tk.Tk()
window.title("Pizza Order App")
window.geometry("400x200")

# Create three rows of pizza selection
pizza_rows = []
for i, pizza_name in enumerate(["Margherita", "Pepperoni", "Vegetarian"]):
    row_frame = tk.Frame(window)
    row_frame.grid(row=i, column=0, padx=10)

    pizza_var = tk.StringVar(row_frame)
    pizza_var.set(pizza_name)  # Default pizza
    pizza_optionmenu = tk.OptionMenu(row_frame,
                                     pizza_var,
                                     *pizza_prices.keys(),
                                     command=calculate_total_cost)
    pizza_optionmenu.config(width=20)
    pizza_optionmenu.grid(row=0, column=0)

    pizza_spinbox = tk.Spinbox(row_frame,
                               from_=1,
                               to=10,
                               width=5,
                               command=calculate_total_cost)
    pizza_spinbox.grid(row=0, column=1)
    pizza_spinbox.delete(0, "end")  # Clear the default value
    pizza_spinbox.insert(0, "0")  # Set initial value to 1

    pizza_rows.append({"var": pizza_var, "spinbox": pizza_spinbox})

# Total cost label
total_cost_label = tk.Label(window, text="Total Cost: $0.00")
total_cost_label.grid(row=len(pizza_rows), column=0, padx=10)

window.mainloop()
