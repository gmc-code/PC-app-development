==========================
Ordering app skills
==========================

| These short lessons build up every skill you need for the :doc:`../tk_icecream_orders_tutorial/icecream_orders` tutorial.
| Each lesson teaches **one** skill with a small **Juice Bar** example, then gives you tasks to try.
| In the last lesson you put all the skills together to make a small Juice Bar ordering app.

----

How each lesson works
----------------------

#. Read the explanation and run the example code.
#. Do the **Tasks**. Check your answers in the drop-down under the tasks.
#. Do the **Quiz** and the **Fill in the gaps**.

----

The skills
----------------------

| This table shows each skill, the code it uses, and where the ice cream tutorial uses it.

.. list-table::
    :header-rows: 1
    :widths: 30 50 20

    * - Skill
      - Code you will use
      - Used in the ice cream tutorial
    * - :doc:`skills01_window`
      - | ``import tkinter as tk``
        | ``tk.Tk()``
        | ``title()``
        | ``geometry()``
        | ``mainloop()``
      - Lesson 1
    * - :doc:`skills02_labels_grid`
      - | ``tk.Label(root)``
        | ``grid(row=, column=, columnspan=, sticky=)``
        | ``config()``
      - Lessons 3 to 8
    * - :doc:`skills03_constants`
      - | ``BG_COLOUR = "#fff4e6"``
        | ``TITLE_FONT = ("Segoe UI", 22, "bold")``
      - Lesson 3
    * - :doc:`skills04_dictionaries`
      - | ``{"Orange": 5.00}``
        | ``juices["Orange"]``
        | ``for juice in juices.keys():``
      - Lessons 2, 4, 5 and 6
    * - :doc:`skills05_fstrings`
      - ``f"{juice} costs ${price:.2f}"``
      - Lessons 4, 6 and 7
    * - :doc:`skills06_lists`
      - | ``orders = []``
        | ``append()``
        | ``orders[0]``
        | ``del``
        | ``clear()``
      - Lessons 2, 7 and 8
    * - :doc:`skills07_functions`
      - | ``def``
        | docstrings
        | ``return``
      - Lessons 6, 7 and 8
    * - :doc:`skills08_buttons`
      - | ``tk.Button(root)``
        | ``config(command=add_juice)``
      - Lessons 7 and 8
    * - :doc:`skills09_radiobuttons`
      - | ``tk.StringVar(root)``
        | ``set()``
        | ``get()``
        | ``tk.Radiobutton``
        | ``tk.Frame``
      - Lesson 4
    * - :doc:`skills10_optionmenu`
      - | ``tk.OptionMenu``
        | ``["menu"]``
        | ``delete(0)``
        | ``add_radiobutton()``
      - Lesson 5
    * - :doc:`skills11_trace_add`
      - | ``trace_add("write", update_price)``
        | ``*args``
      - Lesson 6
    * - :doc:`skills12_listbox`
      - | ``tk.Listbox``
        | ``insert(tk.END, ...)``
        | ``curselection()``
        | ``messagebox``
      - Lessons 7 and 8
    * - :doc:`skills13_project`
      - Everything above, in one app
      - Lessons 1 to 9

----

Lesson outline
----------------------

| :doc:`skills01_window`
| :doc:`skills02_labels_grid`
| :doc:`skills03_constants`
| :doc:`skills04_dictionaries`
| :doc:`skills05_fstrings`
| :doc:`skills06_lists`
| :doc:`skills07_functions`
| :doc:`skills08_buttons`
| :doc:`skills09_radiobuttons`
| :doc:`skills10_optionmenu`
| :doc:`skills11_trace_add`
| :doc:`skills12_listbox`
| :doc:`skills13_project`
