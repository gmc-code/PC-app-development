====================================================
Importing tkinter
====================================================

tkinter recommended import
----------------------------------------

.. code-block:: python

    import tkinter as tk


- You need to prefix the objects with `tk.` to access them (e.g., `tk.Button`, `tk.Label`.).
- Provides better clarity and avoids potential naming conflicts.
- It's a good practice to be explicit about where your objects come from.

----

tkinter import everything
----------------------------------------

.. code-block:: python

    from tkinter import *


- This removes the need to prefix the objects with ``tkinter.`` to access them (e.g., ``Button`` instead of ``tkinter.Button``).
- This is poor practice. It makes it hard to tell what methods are from tkinter.

----

tkinter import
----------------------------------------


.. code-block:: python

    import tkinter


- You need to prefix the objects with ``tkinter`.` to access them (e.g., ``tkinter.Button``, ``tkinter.Label``.).
- This makes slightly longer code using ``tkinter.Button`` compared to ``tk.Button``

