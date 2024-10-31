import tkinter as tk

def show_selection(*args):
    selected_fruit = fruit_var.get()
    text_widget.delete(1.0, 'end')
    text_widget.insert(tk.END, f"You selected: \n{selected_fruit}")

# Create the main window
window = tk.Tk()
window.title("Fruit Selector")

# Define a variable to hold the selected option
fruit_var = tk.StringVar(window)
fruit_var.trace("w", show_selection)  # Trace the variable to call show_selection on change

# Define the options for the OptionMenu
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Set the default value for the OptionMenu
fruit_var.set(fruits[0])

# Create the OptionMenu widget
option_menu = tk.OptionMenu(window, fruit_var, *fruits)
option_menu.pack(pady=10)

# Create a text widget to display the selected option with increased space
text_widget = tk.Text(window, height=2, width=20, bg="white", fg="black", font=("Helvetica", 12), bd=2, relief="solid")
text_widget.pack(pady=10, padx=20)

# Run the main event loop
window.mainloop()
