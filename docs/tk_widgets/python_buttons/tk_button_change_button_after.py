import tkinter as tk


window = tk.Tk()
window.title("change button after delay")
window.geometry("250x150")

button_1 = tk.Button(window, text="Button 1", fg="blue", bg="red")
button_1.pack()

button_2 = tk.Button(window, text="Button 2")
button_2.pack()

# Function to change the button's appearance
def change_button():
    button_2.config(fg="green", bg="yellow", font=("Arial", 24))

# Schedule the change_button function to run after 3000 milliseconds (3 seconds)
window.after(3000, change_button)

window.mainloop()
