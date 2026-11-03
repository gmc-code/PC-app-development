import tkinter as tk

root = tk.Tk()
root.title("update_order args")
root.geometry("500x300")

sizes = {"Small": 4.00, "Medium": 5.50, "Large": 7.00}
juices = {"Orange": 0.00, "Mango": 0.50, "Berry": 1.00}

size_var = tk.StringVar(root, name="size")    # give each variable a name
juice_var = tk.StringVar(root, name="juice")
size_var.set("Small")
juice_var.set("Orange")

message_label = tk.Label(root, text="")
message_label.pack(padx=10, pady=10)
message_label.config(text="Pick a size and a juice")

price_label = tk.Label(root, text="")
price_label.pack(padx=10, pady=10)
price_label.config(text=f"Price: ${0:.2f}")

def update_order(*args):
    changed = args[0]    # the name of the variable that changed

    if changed == "size":
        message_label.config(text="You changed the size to " + size_var.get())
    elif changed == "juice":
        message_label.config(text="You changed the juice to " + juice_var.get())

    # The total uses both, so update it whichever one changed
    price = sizes[size_var.get()] + juices[juice_var.get()]
    price_label.config(text=f"Price: ${price:.2f}")


size_var.trace_add("write", update_order)     # both variables call
juice_var.trace_add("write", update_order)    # the same function

tk.OptionMenu(root, size_var, *sizes.keys()).pack(padx=10, pady=5)
tk.OptionMenu(root, juice_var, *juices.keys()).pack(padx=10, pady=5)

root.mainloop()