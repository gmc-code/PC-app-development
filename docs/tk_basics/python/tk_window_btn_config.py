import tkinter as tk


root = tk.Tk()
root.title("button_config")
root.geometry("250x150")

button_1 = tk.Button(root, text="Button 1", fg="blue", bg="red")
button_1.pack()

button_2 = tk.Button(root, text="Button 2")
button_2.pack()

# Function to change the button's appearance
def change_button():
    button_2.config(fg="green", bg="yellow", font=("Arial", 24))

# Schedule the change_button function to run after 3000 milliseconds (3 seconds)
root.after(6000, change_button)

root.mainloop()