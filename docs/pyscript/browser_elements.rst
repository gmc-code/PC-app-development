====================================================
Browser elements
====================================================

Getting and setting input and output elements
--------------------------------------------------------------------

| In general, you should use ``.value`` to get or set the value of an input element, and ``.innerText`` to get or set the text content of other types of elements.
| ``.value`` is used to get or set the value of an input element, such as a text input or a select element.
| For example, if you have an input element with an id of **input**, you can get its value using document.getElementById('input').value.
| ``.innerText`` is used to get or set the text content of an element, such as a <div> or a <p> element.
| For example, if you have a <div> element with an id of myDiv, you can get its text content using document.getElementById('myDiv').innerText.

----

`querySelector` v `getElementById`
------------------------------------------

From the python script, when working with JavaScript in the browser, the choice between `querySelector` and `getElementById` depends on your specific use case.

1. **getElementById**

- **Purpose:** Use `getElementById` when you need to select an element based on its unique ID attribute.
- **Efficiency:** It is more efficient because IDs must be unique within a page, so it always returns the correct element.
- **Context:** You can only use `getElementById` from the document context.
- **Example:**

| Let part of the html include an input field with a given id.


.. code-block:: html

	<input type="number" min="1" max="20" id="number" placeholder="1">

.. code-block:: python

	from pyscript import document

	input_text_element = document.getElementById("number")
	num = input_text_element.value


1. **querySelector**

- **Purpose:** Use `querySelector` when you need flexibility in selecting elements based on various criteria (e.g., CSS selectors).
- **Versatility:** It allows you to find elements using more complex rules that can't be expressed with `getElementById`.
- **Context:** You can use `querySelector` from any element context (not just the document).
- **Example:**

.. code-block:: python

	from pyscript import document

	input_text_element = document.querySelector("#first_initial")
	first_initial = input_text_element.value


----

when decorator in python
--------------------------

| Use the Python decorator, **when**, to handle specified events for selected elements.
| For info on using the decorator ``@when``, See: `<https://jeff.glass/post/whats-new-pyscript-2023-05-1/>`_
| The `@when` decorator in PyScript is used to handle events in a Pythonic way, similar to how you might use `addEventListener` in JavaScript. It allows you to specify a function to be called when a particular event occurs on a specified element.
| Examples:

  - Input Event: Handles changes in a text field.
  - Click Event: Responds to clicks on a submit button.
  - Keypress Event: Captures key presses in a textarea.
  - Change Event: Detects changes in a dropdown menu selection.
  - Mouseover Event: Triggers actions when the mouse hovers over an image.

.. py:decorator:: @when(event_type, selector)

	| The **event_type** should be the name of the browser event to handle as a string (e.g. "click", "input", "keypress", "change", "mouseover").
	| The **selector** should be a string containing a valid selector to indicate the target elements in the DOM whose events of event_type are of interest.
	| e.g. @when("click", "#start_button")
	| The function decorated with `@when` will be called whenever the specified event occurs on the target element.

----

Output to the browser window
--------------------------------------------------------------------

| Pyscript recommends using the display function to output to the browser window.

.. py:function:: display(*values, target=None, append=True)

    \*values (list) - the list of objects to be displayed. Can be any of the following MIME types:: "text/plain", "text/html", "image/png", "image/jpeg", "image/svg+xml", "application/json" or "application/javascript"

    target (str)- the ID of the html tag to output to. If none, output to the current <py-script> tag.

    append (boolean) if the output is going to be appended or not to the targeted element. It creates a <div> tag if True and a <py-script> tag with a random ID if False

.. code-block:: python

	from pyscript import document, display

	display("Enter initials.", target="#superhero", append=False)

