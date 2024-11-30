====================================================
Browser elements
====================================================

Getting and setting input and output elements
--------------------------------------------------------------------

| In general, you should use ``.value`` to get or set the value of an input element, and ``.innerText`` to get or set the text content of other types of elements.
| ``.value`` is used to get or set the value of an input element, such as a text input or a select element.
| For example, if you have an input element with an id of myInput, you can get its value using document.getElementById('myInput').value.
| ``.innerText`` is used to get or set the text content of an element, such as a <div> or a <p> element.
| For example, if you have a <div> element with an id of myDiv, you can get its text content using document.getElementById('myDiv').innerText.

----

`querySelector` v `getElementById`
------------------------------------------

When working with JavaScript in the browser, the choice between `querySelector` and `getElementById` depends on your specific use case.

1. **`getElementById`:**

- **Purpose:** Use `getElementById` when you need to select an element based on its unique ID attribute.
- **Efficiency:** It is more efficient because IDs must be unique within a page, so it always returns the correct element.
- **Context:** You can only use `getElementById` from the document context.
- **Example:**

.. code-block:: javascript

	const element = document.getElementById("first_initial");
	const value = element.value;


2. **`querySelector`:**

- **Purpose:** Use `querySelector` when you need flexibility in selecting elements based on various criteria (e.g., CSS selectors).
- **Versatility:** It allows you to find elements using more complex rules that can't be expressed with `getElementById`.
- **Context:** You can use `querySelector` from any element context (not just the document).
- **Example:**

.. code-block:: javascript

	const element = document.querySelector("#first_initial");
	const value = element.value;


----

Output to the browser window
--------------------------------------------------------------------

| Pyscript recommends using the display function to output to the browser window.

.. py:function:: display(*values, target=None, append=True)

    *values (list) - the list of objects to be displayed. Can be any of the following MIME types:: "text/plain", "text/html", "image/png", "image/jpeg", "image/svg+xml", "application/json" or "application/javascript"

    target (str)- the ID of the html tag to output to. If none, output to the current <py-script> tag.

    append (boolean) if the output is going to be appended or not to the `target`ed element. It creates a <div> tag if True and a <py-script> tag with a random ID if False

.. code-block:: python

	from pyscript import document, display

	display("Enter initials.", target="#superhero", append=False)