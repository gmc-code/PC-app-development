====================================================
Hailstone numbers
====================================================

A sequence is called a hailstone sequence because the values typically rise and fall, somewhat analogously to a hailstone inside a cloud.

----

References
------------------------------

#. https://www.dcode.fr/collatz-conjecture
#. https://goodcalculators.com/collatz-conjecture-calculator/
#. https://en.wikipedia.org/wiki/Collatz_conjecture

----

Design
---------

| Use an Column panel.
| Use 3 label fields to display the information content.
| Add a text box for teh start number.
| Add a button to generate the hailstone numbers.
| Add a text area to display the hailstone numbers.

.. image:: images/hailstone/Hailstone_numbers.png
    :scale: 100

----

Get started
------------------------------

#. Go to: https://anvil.works/new-build
#. Click: Blank App.
#. Choose: Material Design

----

Settings
------------------------------

#. Click on the cog icon to show thie settings tab.
#. Enter an App name. Hailstone_numbers
#. Enter an App title. Hailstone_numbers
#. Enter an App description. Hailstone_numbers are a sequence of odd and even positive integers.
#. Close the settings tab.

----

Build interface: title
------------------------------

| Drag and drop a *label* component onto the **Drop title here** container.
| In the properties panel: name section, set the **name** to **title**.
| In the properties panel: text section, set the **text** to **Hailstone numbers**.
| In the properties panel: text section, set the **font_size** to 24.

----

Column panel
----------------

| Drag and drop a *column panel* component onto the form.

----

Info
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **info**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

| Hailstone numbers are a sequence of odd and even positive integers.
| The values typically rise and fall, like a hailstone inside a cloud.
| e.g. 6, 3, 10, 5, 16, 8, 4, 2, 1

----

Rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

| The rules for producing hailstone numbers:
| * Start with a positive whole number (integer)
| * If the number is even, divide by 2.
| * If the number is odd, multiply by 3 and add 1.
| * Repeat for each new number and continue till 1 is reached.

----

Directions
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **directions**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

rules
----------------

| Drag and drop a *label* component onto the form.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

Code 
--------------------

| 

.. admonition:: Tasks

    #. Write code for the nested dictionary.   

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code for the nested dictionary. 

                    .. code-block:: python

                        