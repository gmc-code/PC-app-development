====================================================
tkinter constants
====================================================

Useful constants
----------------------------------------

| The common tkinter constants and their lowercase string equivalents are below.
| The lowercase versions are simpler to use.
| The constants require a reference to the tkinter module. e.g. tk.CENTER
| A full list of tkinter constants can be found at `<https://github.com/python/cpython/blob/main/Lib/tkinter/constants.py>`_

| The main ones used in this resource are `end` and the sticky constants: `n`, `s`, `e`, `w`, `center` and the sides: `left`, `right`, `top`, `bottom`.

----

Booleans
--------

- tk.NO=tk.FALSE=tk.OFF=0
- tk.YES=tk.TRUE=tk.ON=1

-anchor and -sticky
-------------------

- tk.N='n'
- tk.S='s'
- tk.W='w'
- tk.E='e'
- tk.NW='nw'
- tk.SW='sw'
- tk.NE='ne'
- tk.SE='se'
- tk.NS='ns'
- tk.EW='ew'
- tk.NSEW='nsew'
- tk.CENTER='center'

-fill
-----

- tk.NONE='none'
- tk.X='x'
- tk.Y='y'
- tk.BOTH='both'

-side
-----

- tk.LEFT='left'
- tk.TOP='top'
- tk.RIGHT='right'
- tk.BOTTOM='bottom'

-relief
-------

- tk.RAISED='raised'
- tk.SUNKEN='sunken'
- tk.FLAT='flat'
- tk.RIDGE='ridge'
- tk.GROOVE='groove'
- tk.SOLID='solid'

-orient
-------

- tk.HORIZONTAL='horizontal'
- tk.VERTICAL='vertical'

-tabs
----

- tk.NUMERIC='numeric'

-wrap
----

- tk.CHAR='char'
- tk.WORD='word'

-align
------

- tk.BASELINE='baseline'

-bordermode
-----------

- tk.INSIDE='inside'
- tk.OUTSIDE='outside'

Special tags, marks, and insert positions
-----------------------------------------

- tk.SEL='sel'
- tk.SEL_FIRST='sel.first'
- tk.SEL_LAST='sel.last'
- tk.END='end'
- tk.INSERT='insert'
- tk.CURRENT='current'
- tk.ANCHOR='anchor'
- tk.ALL='all' (e.g., Canvas.delete(ALL))

Text widget and button states
-----------------------------

- tk.NORMAL='normal'
- tk.DISABLED='disabled'
- tk.ACTIVE='active'

Canvas state
------------

- tk.HIDDEN='hidden'


----

Example usage
-----------------

| This script displays a visual grid demonstrating the most commonly used ``tkinter`` constants. Each constant is shown inside its own grid cell, together with a small widget that visually illustrates how the constant behaves.
| The grid includes demonstrations of:

- **Anchor constants**: ``N``, ``S``, ``E``, ``W``, ``CENTER``
  (controls text alignment inside a widget)

- **Sticky constants**: ``N``, ``S``, ``E``, ``W``, ``NSEW``
  (controls how widgets stretch inside a grid cell)

- **Side constants**: ``LEFT``, ``RIGHT``, ``TOP``, ``BOTTOM``
  (controls packing direction)

- **Fill constants**: ``X``, ``Y``, ``BOTH``
  (controls how widgets expand when packed)

- **Relief constants**: ``RAISED``, ``SUNKEN``, ``RIDGE``, ``GROOVE``,
  ``SOLID``, ``FLAT``
  (controls border style)

- **Orient constants**: ``HORIZONTAL``, ``VERTICAL``
  (used by widgets such as `Scale` and `Scrollbar`)

- **Wrap constants**: ``WORD``, ``CHAR``
  (controls text wrapping in `Text` widgets)

- **State constants**: ``NORMAL``, ``DISABLED``
  (controls widget interactivity)

- **Special text positions**: ``END``, ``INSERT``
  (used when inserting text into widgets such as `Text` and `Entry`)

----

SYntax
---------

.. py:data:: anchor=<tk.ANCHOR_CONSTANT>

    | Controls internal alignment of text or content inside a widget.
    | Valid values: ``tk.N``, ``tk.S``, ``tk.E``, ``tk.W``, ``tk.NE``, ``tk.NW``,
      ``tk.SE``, ``tk.SW``, ``tk.CENTER``.
    | Example: ``Label(root, text="Left", anchor=tk.W)``


.. py:data:: sticky=<tk.STICKY_CONSTANT>

    | Controls how a widget expands to fill its grid cell.
    | Valid values: ``tk.N``, ``tk.S``, ``tk.E``, ``tk.W``, or combinations such as ``"NS"``, ``"EW"``, ``"NSEW"``.
    | Example: ``frame.grid(row=0, column=0, sticky=tk.NSEW)``


.. py:data:: side=<tk.SIDE_CONSTANT>

    | Controls which side of the parent a widget is packed against.
    | Valid values: ``tk.LEFT``, ``tk.RIGHT``, ``tk.TOP``, ``tk.BOTTOM``.
    | Example: ``button.pack(side=tk.LEFT)``


.. py:data:: fill=<tk.FILL_CONSTANT>

    | Controls how a widget expands when packed.
    | Valid values: ``tk.X``, ``tk.Y``, ``tk.BOTH``, ``tk.NONE``.
    | Example: ``button.pack(fill=tk.X)``


.. py:data:: relief=<tk.RELIEF_CONSTANT>

    | Controls the 3D border style of a widget.
    | Valid values: ``tk.FLAT``, ``tk.RAISED``, ``tk.SUNKEN``, ``tk.GROOVE``,
      ``tk.RIDGE``, ``tk.SOLID``.
    | Example: ``Frame(root, relief=tk.RIDGE)``


.. py:data:: orient=<tk.ORIENT_CONSTANT>

    | Controls orientation of directional widgets such as ``Scale`` or ``Scrollbar``.
    | Valid values: ``tk.HORIZONTAL``, ``tk.VERTICAL``.
    | Example: ``Scale(root, orient=tk.VERTICAL)``


.. py:data:: wrap=<tk.WRAP_CONSTANT>

    | Controls text wrapping behavior in ``Text`` widgets.
    | Valid values: ``tk.WORD``, ``tk.CHAR``, ``tk.NONE``.
    | Example: ``Text(root, wrap=tk.WORD)``


.. py:data:: state=<tk.STATE_CONSTANT>

    | Controls widget interactivity.
    | Valid values: ``tk.NORMAL``, ``tk.DISABLED``, ``tk.ACTIVE`` (some widgets),
      ``tk.READONLY`` (Entry only).
    | Example: ``Entry(root, state=tk.DISABLED)``


.. py:data:: index=<tk.TEXT_INDEX>

    | Special text positions used when inserting or deleting text.
    | Valid values: ``tk.END``, ``tk.INSERT``, or explicit positions like ``"1.0"``.
    | Example: ``text.insert(tk.END, "Hello")``


----

| Each constant is demonstrated using a small widget placed inside a labelled frame, arranged in a multi-column grid for easy comparison.


.. image:: images/tk_constants.png
    :scale: 75%

.. literalinclude:: python/tk_constants.py
   :language: python
   :linenos:
