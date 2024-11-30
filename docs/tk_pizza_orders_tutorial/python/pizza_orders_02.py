import tkinter as tk

# Create the main window
root = tk.Tk()
window.title("Pizza Ordering System")
window.geometry("900x600")

# Customer name
tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
customer_entry = tk.Entry(root)
customer_entry.grid(row=0, column=1, padx=10, pady=5)

# Run the application
window.mainloop()
