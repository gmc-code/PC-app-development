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
| Add a text box for the start number.
| Add a button to generate the hailstone numbers.
| Add a text area to display the hailstone numbers.

.. image:: images/hailstone/Hailstone_numbers.png
    :scale: 80

----

Get started
------------------------------

#. Go to: https://anvil.works/new-build
#. Click: Blank App.
#. Choose: Material Design

----

Settings
------------------------------

#. Click on the cog icon to show the settings tab.
#. Enter an App name. **Hailstone_numbers**
#. Enter an App title. **Hailstone_numbers**
#. Enter an App description. **Hailstone_numbers are a sequence of odd and even positive integers.**
#. Close the settings tab.

----

Build interface
-------------------

Title
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the **Drop title here** container.
| In the properties panel: name section, set the **name** to **title**.
| In the properties panel: text section, set the **text** to **Hailstone numbers**.
| In the properties panel: text section, set the **font_size** to 24.

----

Column panel
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *column panel* component onto the form.

----

Info
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel.
| In the properties panel: name section, set the **name** to **info**.
| In the properties panel: text section, set the **font_size** to 18.
| In the properties panel: text section, set the **text** to text below.

| Hailstone numbers are a sequence of odd and even positive integers.
| The values typically rise and fall, like a hailstone inside a cloud.
| e.g. 6, 3, 10, 5, 16, 8, 4, 2, 1

----

Rules
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel to the right of the **info** label.
| In the properties panel: name section, set the **name** to **rules**.
| In the properties panel: text section, set the **font_size** to 18.
| In the properties panel: text section, set the **text** to text below.

| The rules for producing hailstone numbers:
| * Start with a positive whole number (integer)
| * If the number is even, divide by 2.
| * If the number is odd, multiply by 3 and add 1.
| * Repeat for each new number and continue till 1 is reached.

----

Directions
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel.
| In the properties panel: name section, set the **name** to **directions**.
| In the properties panel: text section, set the **font_size** to 18.
| In the properties panel: text section, set the **text** to text below.

| Enter the start number (positive integer) and click Generate.

----

Hailstone_start 
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *TextBox* component onto the column panel.
| In the properties panel: name section, set the **name** to **hailstone_start**.
| In the properties panel: properties section, set the **placeholder** to **start number**.
| In the properties panel: properties section, set the **type** to **number**.
| In the properties panel: text section, set the **font_size** to 24.
| In the properties panel: Events section, click on the blue icon to the right of the **pressed_enter** label.
| This will add a default script, **hailstone_start_pressed_enter**, to the code. This will be coded later with the **Generate** button code.

----

Generate_hailstone button
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Drag and drop a *Button* component onto the column panel to the right of the hailstone_start textbox.
| In the properties panel: name section, set the **name** to **generate_hailstoneles**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: text section, set the **text** to text below.

----

Error field
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel.
| In the properties panel: name section, set the **name** to **error**.
| In the properties panel: text section, set the **font_size** to 16.
| In the properties panel: icon section, set the **icon** to **fa:exclamation-triangle**.

----

Length_label
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel.
| In the properties panel: name section, set the **name** to **length_label**.
| In the properties panel: text section, set the **font_size** to 18.
| In the properties panel: text section, set the **text** to **Length:**.

----

Length
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel to the right of the **length_label** label.
| Control click and drag the divider on the left of the label to the left to minimize the length_label.
| In the properties panel: name section, set the **name** to **length**.
| In the properties panel: text section, set the **font_size** to 18.
| In the properties panel: text section, set the **text** to ****.

----

Hailstone_numbers
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *TextArea* component onto the column panel.
| In the properties panel: name section, set the **name** to **hailstone_numbers**.
| In the properties panel: text section, set the **font_size** to 24.
| In the properties panel: properties section, set the **placeholder** to **Hailstone numbers**.

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

                        