import tkinter as tk


def show_selection():
    selected_indices = listbox.curselection()
    selected_values = [listbox.get(i) for i in selected_indices]
    print(selected_indices,selected_values)
    # Insert the selected values into the text widget
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, ", ".join(selected_values))


root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x300")

string_var = tk.StringVar(value=["Item 1", "Item 2", "Item 3"])

listbox = tk.Listbox(root, listvariable=string_var)
listbox.pack()

button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack()

# Create a Text widget to display the selected values
text_widget = tk.Text(root, height=3, width=30)
text_widget.pack()

root.mainloop()
