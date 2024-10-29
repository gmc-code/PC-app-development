====================================================
Importing tkinter
====================================================

tkinter recommended import
----------------------------------------

.. code-block:: python

    import tkinter as tk


- You need to prefix the objects with `tk.` to access them (e.g., `tk.Button`, `tk.Label`.).
- This makes it explicit about where tk objects come from.
- It provides better clarity and avoids potential naming conflicts.
- It's good practice.

----

tkinter import everything
----------------------------------------

.. code-block:: python

    from tkinter import *


- This removes the need to prefix the objects with ``tkinter.`` to access them (e.g., ``Button`` instead of ``tkinter.Button``).
- It makes it hard to tell what methods are from tkinter.
- This is poor practice.
  
----

tkinter import
----------------------------------------


.. code-block:: python

    import tkinter


- The ``tkinter.`` prefix is needed for tkinter objects.
- It makes slightly longer code by using ``tkinter.Button`` compared to ``tk.Button``

