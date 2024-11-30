import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x400")  # Set window size
root.title("Listbox Example")  # Set window title

# Function to get the selected item from the listbox and display it in the label
def get_selection():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    output_label.config(text=f"Selected items:\n{', '.join(selected_items)}")

# Create the listbox widget
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=('calibre', 14, 'normal'), width=30, height=7)
listbox.pack(pady=10)  # Add some padding to the top

# Add items to the listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Create a button to trigger the get_selection function
submit_button = tk.Button(root, text="Submit", font=('calibre', 14, 'normal'), command=get_selection)
submit_button.pack(pady=10)

# Create a label to display the output
output_label = tk.Label(root, text="", font=('calibre', 14, 'normal'), width=50, height=3, bd=2,  highlightthickness=2, highlightbackground="gray")
output_label.pack(pady=10, padx=10)

# Run the main event loop
root.mainloop()
