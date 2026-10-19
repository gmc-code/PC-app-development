import tkinter as tk

# Dictionary of pizza names and costs
pizza_prices = {
    "Margherita": 8.99,
    "Pepperoni": 10.99,
    "Vegetarian": 9.49,
    "Supreme": 11.99,
}

def calculate_total_cost(*args):
    selected_pizza = pizza_var.get()
    num_pizzas = int(pizza_spinbox.get())
    pizza_cost = pizza_prices.get(selected_pizza, 0)
    total_cost = pizza_cost * num_pizzas
    total_cost_label.config(text=f"Price: ${total_cost:.2f}")

root = tk.Tk()
root.title("Pizza Order App")
root.geometry("400x100")

# Pizza selection
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")  # Default pizza
pizza_optionmenu = tk.OptionMenu(root,
                                 pizza_var,
                                 *pizza_prices.keys(),
                                 command=calculate_total_cost)
pizza_optionmenu.config(width=20)
pizza_optionmenu.grid(row=0, column=0, padx=10)

# Number of pizzas
pizza_spinbox = tk.Spinbox(root, from_=1, to=10, width=5, command=calculate_total_cost)
pizza_spinbox.grid(row=0, column=1, padx=10)
pizza_spinbox.delete(0, "end")  # Clear the default value
pizza_spinbox.insert(0, "0")  # Set initial value to 1

# Total cost label
total_cost_label = tk.Label(root, text="Price: $0.00")
total_cost_label.grid(row=0, column=2, padx=10)

root.mainloop()
