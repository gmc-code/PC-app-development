====================================================
tk variables
====================================================

| In Tkinter, several widgets can have a variable associated with them.
| These variables are instances of `StringVar`, `IntVar`, `DoubleVar`, or `BooleanVar`.
| They allow you to link the widget's value to a variable that can be updated and accessed programmatically.
| Here are some common widgets that can have an associated variable:

----

StringVar
------------

| Purpose: Holds string values.
| Basic Initialization: string_var = tk.StringVar()
| Initialization with Initial Value: string_var = tk.StringVar(value="Hello, World!")
| Initialization with a list of strings for a listbox: string_var = tk.StringVar(value=["Item 1", "Item 2", "Item 3"])

----

IntVar
------------

| Purpose: Holds integer values.
| Basic Initialization: int_var = tk.IntVar()
| Initialization with Initial Value: int_var = tk.IntVar(value=10)

----

DoubleVar
------------

| Purpose: Holds floating-point values.
| Basic Initialization: double_var = tk.DoubleVar()
| Initialization with Initial Value: double_var = tk.DoubleVar(value=3.14)

----

BooleanVar
------------

| Purpose: Holds boolean values (True or False).
| Basic Initialization: bool_var = tk.BooleanVar()
| Initialization with Initial Value: bool_var = tk.BooleanVar(value=True)

----

Binding variables to widgets
-----------------------------------------

1. **Label**: Can display text that is linked to a variable.

.. py:attribute:: textvariable

   label = tk.Label(root, textvariable=string_var)


2. **Entry**: Can take user input and link it to a variable.

.. py:attribute:: textvariable

   entry = tk.Entry(root, textvariable=string_var)


3. **Checkbutton**: Can be linked to a variable to track its state (checked or unchecked).

.. py:attribute:: variable

   checkbutton = tk.Checkbutton(root, variable=int_var)


4. **Radiobutton**: Can be linked to a variable to track which radio button is selected.

.. py:attribute:: variable

   radiobutton = tk.Radiobutton(root, variable=int_var, value=1)


5. **Listbox**: Can be linked to a variable to track the selected item.

.. py:attribute:: listvariable

   listbox = tk.Listbox(root, listvariable=string_var)


6. **Spinbox**: Can be linked to a variable to track the current value.

.. py:attribute:: textvariable

   spinbox = tk.Spinbox(root, textvariable=int_var)


7. **Scale**: Can be linked to a variable to track the current value of the scale.

.. py:attribute:: variable

   scale = tk.Scale(root, variable=double_var)


----

Label
------------

This code uses the textvariable option to set the display text of the label.

.. code-block:: python

	import tkinter as tk

	root = tk.Tk()
	root.title("Label Example")
	root.geometry("300x200")

	string_var = tk.StringVar()
	string_var.set("Hello, Tkinter!")

	label = tk.Label(root, textvariable=string_var)
	label.pack()

	root.mainloop()


----

Entry
------------

| This code uses the textvariable option to set the display text of the entry widget.
| Click the button to get the entry widget text, via string_var, change it to upper case then set the string_var, which dynamically updates the displayed text.

.. code-block:: python

	import tkinter as tk

	root = tk.Tk()
	root.title("Entry Example")
	root.geometry("300x200")

	string_var = tk.StringVar()

	entry = tk.Entry(root, textvariable=string_var)
	entry.pack()

	def upper_case_text():
		string_var.set(string_var.get().upper())

	button = tk.Button(root, text="Upper case text", command=upper_case_text)
	button.pack()

	root.mainloop()

----

Checkbutton
------------

| This code uses the variable option to link the checkbutton status with int_var.
| When the Checkbutton is checked, int_var is set to 1.
| When the Checkbutton is unchecked, int_var is set to 0.

.. code-block:: python

	import tkinter as tk


	def update_label():
		if int_var.get() == 1:
			label.config(text="Checked!")
		else:
			label.config(text="Unchecked!")


	root = tk.Tk()
	root.title("Checkbutton Example")
	root.geometry("300x200")

	int_var = tk.IntVar()

	checkbutton = tk.Checkbutton(root, text="Check me", font=("Helvetica", 16), variable=int_var, command=update_label)
	checkbutton.pack(pady=10)

	label = tk.Label(root, text="Unchecked", font=("Helvetica", 16))
	label.pack(pady=10)

	root.mainloop()

----

Radiobutton
------------

| ``variable=int_var`` links the Radiobutton to a Tkinter variable, **int_var**. This variable will hold the value of the selected Radiobutton in the group. All Radiobuttons in the same group should share the same variable.
| ``value=1`` sets the value that **int_var** will take when this Radiobutton is selected. In this case, if radiobutton1 is selected, int_var will be set to 1.

.. code-block:: python

	import tkinter as tk

	def update_label():
		selected_value = int_var.get()
		if selected_value == 1:
			label.config(text="Option 1 selected")
		elif selected_value == 2:
			label.config(text="Option 2 selected")

	root = tk.Tk()
	root.title("Radiobutton Example")
	root.geometry("300x200")

	int_var = tk.IntVar()

	radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=int_var, value=1, command=update_label)
	radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=int_var, value=2, command=update_label)
	radiobutton1.pack(pady=5)
	radiobutton2.pack(pady=5)

	label = tk.Label(root, text="No option selected", font=("Helvetica", 16))
	label.pack(pady=20)

	root.mainloop()

----

Listbox
------------

| This code uses the listvariable option to set the display text of the listbox widget.
| ``string_var = tk.StringVar(value=["Item 1", "Item 2", "Item 3"])`` sets the initial value of the StringVar to a list of strings: ["Item 1", "Item 2", "Item 3"]

.. code-block:: python

	import tkinter as tk


	def show_selection():
		selected_indices = listbox.curselection()
		selected_values = [listbox.get(i) for i in selected_indices]
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

----

Spinbox
------------

| This code uses the textvariable option for the spinbox widget.
| The Spinbox is created with a range from 0 to 10 and is associated with the IntVar named int_var.
| The update_label function updates the Label widget with the current value of the Spinbox whenever the value changes.
| The Label widget initially displays the value of int_var and updates dynamically as you change the value in the Spinbox.
| Clicking the up or down arrows on the Spinbox widget in Tkinter will automatically increment or decrement the associated variable by one, unless you specify a different increment value.

| This code increments by 1.

.. code-block:: python

	import tkinter as tk


	def update_label():
		# Update the label with the current value of the Spinbox
		label.config(text=f"Current Value: {int_var.get()}")


	root = tk.Tk()
	root.title("Spinbox Example")
	root.geometry("300x200")

	# Create an IntVar with an initial value
	int_var = tk.IntVar(value=5)

	# Create a Spinbox and associate it with the IntVar
	spinbox = tk.Spinbox(root, from_=0, to=10, font=("Helvetica", 16), width=5, textvariable=int_var, command=update_label)
	spinbox.pack(pady=5)

	# Create a Label to display the current value of the Spinbox
	label = tk.Label(root, text=f"Current Value: {int_var.get()}", font=("Helvetica", 16))
	label.pack(pady=5)

	root.mainloop()

| This code increments by 2.

.. code-block:: python

	import tkinter as tk


	def update_label():
		# Update the label with the current value of the Spinbox
		label.config(text=f"Current Value: {int_var.get()}")


	root = tk.Tk()
	root.title("Spinbox Example 2")
	root.geometry("300x200")

	# Create an IntVar with an initial value
	int_var = tk.IntVar(value=0)

	# Create a Spinbox and associate it with the IntVar
	spinbox = tk.Spinbox(root, from_=-10, to=10, increment=2, font=("Helvetica", 16), width=5, textvariable=int_var, command=update_label)
	spinbox.pack(pady=5)

	# Create a Label to display the current value of the Spinbox
	label = tk.Label(root, text=f"Current Value: {int_var.get()}", font=("Helvetica", 16))
	label.pack(pady=5)

	root.mainloop()


----

Scale
------------

| This code uses the variable option to associate the DoubleVar with the scale widget.
| The `Scale` widget allows the user to adjust the rectangle's color intensity dynamically

- **Defines `update_intensity` function**: Updates the rectangle's color intensity based on the `Scale` value.
- **Creates a `DoubleVar`**: Initializes with a value of 0.5.
- **Creates a `Scale` widget**: Horizontal, ranges from 0 to 1, linked to `DoubleVar`, calls `update_intensity` on change.
- **Creates a `Canvas` widget**: to enable displays of a rectangle.
- **Creates a rectangle on the `Canvas`**: Initial color intensity set based on `DoubleVar`.
- The expression {intensity:02x} is a Python string formatting operation that converts an integer to a two-digit hexadecimal string

.
```
.. code-block:: python

	import tkinter as tk

	def update_intensity(value):
		# Update the rectangle's intensity based on the Scale value
		intensity = int(float(value) * 255)
		color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
		canvas.itemconfig(rect, fill=color)

	root = tk.Tk()
	root.title("Scale Example")
	root.geometry("300x200")

	# Create a DoubleVar with an initial value
	double_var = tk.DoubleVar(value=0.5)

	# Create a Scale and associate it with the DoubleVar
	scale = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, variable=double_var, command=update_intensity)
	scale.pack()

	# Create a Canvas to display the greyscale rectangle
	canvas = tk.Canvas(root, width=200, height=100)
	canvas.pack(pady=20)

	# Create a rectangle with initial intensity
	initial_intensity = int(double_var.get() * 255)
	rect = canvas.create_rectangle(0, 0, 200, 100, fill=f"#{initial_intensity:02x}{initial_intensity:02x}{initial_intensity:02x}")

	root.mainloop()
