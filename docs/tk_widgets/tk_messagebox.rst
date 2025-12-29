====================================================
tk messagebox
====================================================

| See: `<https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/>`_

----

| The messagebox module is used to display different types of message boxes.
| Each function (showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel) displays a different type of message box.
| The responses from the question-type message boxes are printed to the console in the example below.

.. grid:: 3
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      showinfo
      ^^^
      .. image:: images/messagebox_showinfo.png
        :scale: 100%

   .. grid-item-card::

      showwarning
      ^^^
      .. image:: images/messagebox_showwarning.png
        :scale: 100%

   .. grid-item-card::

      showerror
      ^^^
      .. image:: images/messagebox_showerror.png
        :scale: 100%



.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      askquestion
      ^^^
      .. image:: images/messagebox_askquestion.png
        :scale: 100%

   .. grid-item-card::

      askokcancel
      ^^^
      .. image:: images/messagebox_askokcancel.png
        :scale: 100%

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      askyesno
      ^^^
      .. image:: images/messagebox_askyesno.png
        :scale: 100%

   .. grid-item-card::

      askretrycancel
      ^^^
      .. image:: images/messagebox_askretrycancel.png
        :scale: 100%


| The code below shows each messagebox type.

.. code-block:: python

    import tkinter as tk
    from tkinter import messagebox

    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show an information message box
    messagebox.showinfo("Information", "This is an info message box")

    # Show a warning message box
    messagebox.showwarning("Warning", "This is a warning message box")

    # Show an error message box
    messagebox.showerror("Error", "This is an error message box")

    # Show a question message box
    response = messagebox.askquestion("Question", "Do you want to continue?")
    print(f"Response: {response}")

    # Show an ok/cancel message box
    response = messagebox.askokcancel("Ok/Cancel", "Do you want to proceed?")
    print(f"Response: {response}")

    # Show a yes/no message box
    response = messagebox.askyesno("Yes/No", "Do you agree?")
    print(f"Response: {response}")

    # Show a retry/cancel message box
    response = messagebox.askretrycancel("Retry/Cancel", "Do you want to retry?")
    print(f"Response: {response}")

    # Run the main event loop
    root.mainloop()
