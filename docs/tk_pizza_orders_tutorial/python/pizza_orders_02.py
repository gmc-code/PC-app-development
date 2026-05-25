import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.geometry("900x600")

# --- LEFT SIDE: INPUT CONTROLS ---

# Customer name
customer_label = tk.Label(root, text="Customer Name:")
customer_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=3, sticky="w")

# Run the application
root.mainloop()
