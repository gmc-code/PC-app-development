====================================================
Displacement calculator
====================================================

This app calculates the displacement, S, given u, v, and t.

.. image:: images/kinematics/displacement_calculator.png

----

Get started
------------------------------

#. Go to: https://anvil.works/new-build
#. Click: Blank App.
#. Choose: Material Design

----

Design
------------------------------

| Use the diagram: :download:`rectangle diagram <images/kinematics/Speed_time_graph.png>`
| Use a spacer to the right of the dropdown so it is spaced from the right edge.
| Display the formula: S = ½(v + u)t

----

Key components
-------------------

| Name the input textboxes: **u**, **v** and **t**.
| Set each of the input textbox property **type** settings to **number**.

----

Decimal Places Dropdown Code 
------------------------------

| Name the dropdown: **decimal_places**.
| Set the dropdown items using: ``self.decimal_places.items = ['0', '1', '2', '3', '4'] ``
| The dropdown items list needs to be of strings. [0, 1, 2, 3, 4] can't be used.
| Set the initial decimal_places to '2' using: ``self.decimal_places.selected_value = '2'``
| Create an instance variable, **self.dp**, the number of deciomal places to use for formating the output.
| The int function is needed to turn the string into an integer.

.. code-block:: python

    class Form1(Form1Template):

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.decimal_places.items = ['0', '1', '2', '3', '4']   #requires list of strings
        self.decimal_places.selected_value = '2'
        self.dp = int(self.decimal_places.selected_value)
        
| In the properties panel: Events section, click on the blue icon to the right of the **change** label.
| This will add a default script, **decimal_places_change**, to the code.
| Add the code below to update **self.dp** when the dropdown is used.

.. code-block:: python

    def decimal_places_change(self, **event_args):
        self.dp = int(self.decimal_places.selected_value)

----

Calculation
--------------------

| A try-except block is used to make sure an **error** output is given when the inputs are not valid.
| Any time values of 0 or less are then detected: ``self.t.text < 0:``.
| Negative values for u and v are possible, as well as a negative final value for S.
| A negative S is equivalent to more area below the X axis then above it.

| f-stings allow convenient formatting to 2 decimal places.
| e.g. ``self.area.text = f'{val:.2f}''``

.. code-block:: python

    def calculate_click(self, **event_args):
        try:
            s = 0.5 * (self.u.text + self.v.text) * self.t.text
        except TypeError as error:
            self.s.text = 'error'
        except BaseException as error:
            self.s.text = 'error''
        else:
            if self.t.text < 0:
                self.s.text = 'error'
            else:
                self.s.text = f'{s:.{self.dp}f}'


----

Final  Code 
--------------------

| The full code is below.

.. code-block:: python

    from ._anvil_designer import Form1Template
    from anvil import *
    import anvil.tables as tables
    import anvil.tables.query as q
    from anvil.tables import app_tables

    class Form1(Form1Template):

        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)
            self.decimal_places.items = ['0', '1', '2', '3', '4']   #requires list of strings
            self.decimal_places.selected_value = '2'
            self.dp = int(self.decimal_places.selected_value)
            
        def decimal_places_change(self, **event_args):
            self.dp = int(self.decimal_places.selected_value)

        def calculate_click(self, **event_args):
            try:
                S = 0.5 * (self.u.text + self.v.text) * self.t.text
            except TypeError as error:
                self.S.text = 'error'
            except BaseException as error:
                self.S.text = 'error''
            else:
                if self.t.text < 0:
                    self.S.text = 'error'
                else:
                    self.S.text = f'{S:.{self.dp}f}'

----

.. admonition:: Tasks

    #. Write an app to calculate the acceleration given initial velocity, final velocity, and time.










