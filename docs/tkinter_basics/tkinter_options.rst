====================================================
tkinter options
====================================================

Setting Options
----------------------------------------

| Options control things like the color and border width of a widget. 
| Options can be set in three ways:

| At object creation time, using keyword arguments
| button_1 = tk.Button(self, fg="red", bg="blue")

| After object creation, treating the option name like a dictionary index
| button_1["fg"] = "red"
| button_1["bg"] = "blue"

| Use the config() method to update multiple attributes subsequent to object creation
| button_1.config(fg="red", bg="blue")

