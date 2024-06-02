====================================================
tk geometry pack
====================================================

| The pack geometry manager allows you to arrange widgets within a window.
| See: https://www.geeksforgeeks.org/python-pack-method-in-tkinter/?ref=lbp

| Layouts: https://www.youtube.com/watch?v=i577cFu8eBI&list=PLpMixYKO4EXflJFPhTvZOVAbs7lBdEBSa
| Pack: see https://www.youtube.com/watch?v=rbW1iJO1psk
| Pack with frames: https://www.youtube.com/watch?v=SsjEAWT-SMc

----

pack
--------------------

| Pack is responsive to window size changes.
| By default, the pack geometry manager places widgets in one direction vertically from top to bottom.

.. py:function:: widget.pack()

    | Use **pack()** method to pack a widget in one direction vertically from top to bottom.
    | e.g. widget.pack()

----

Certainly! Let's dive into the various options for the `pack()` geometry manager in Tkinter, along with examples for each one:

1. **Side**:
   - The `side` option determines the position of the widget within its parent container. It can take values like `LEFT`, `RIGHT`, `TOP`, or `BOTTOM`.
   - Example: To create four buttons positioned on different sides of a frame:
     ```python
     from tkinter import *

     root = Tk()
     root.geometry('250x150')

     button1 = Button(text="Left")
     button1.pack(side=LEFT)

     button2 = Button(text="Top")
     button2.pack(side=TOP)

     button3 = Button(text="Right")
     button3.pack(side=RIGHT)

     button4 = Button(text="Bottom")
     button4.pack(side=BOTTOM)

     root.mainloop()
     ```

2. **Expand**:
   - The `expand` option allows a widget to expand if the user resizes the frame.
   - Example: To make a widget expand when the frame is resized:
     ```python
     from tkinter import *

     root = Tk()
     root.geometry('200x150')

     label = Label(root, text="Expanding Label", bg="lightblue")
     label.pack(expand=True, fill=BOTH)

     root.mainloop()
     ```

3. **Fill**:
   - The `fill` option specifies how the widget should fill the available space. It can take values like `NONE`, `X`, `Y`, or `BOTH`.
   - Example: To create two labels with different fill options:
     ```python
     import tkinter as tk

     root = tk.Tk()

     label1 = tk.Label(root, text="Red", bg="red", fg="white")
     label1.pack(ipadx=30, ipady=6)

     label2 = tk.Label(root, text="Purple", bg="purple", fg="white")
     label2.pack(ipadx=8, ipady=12)

     root.mainloop()
     ```

4. **ipadx** and **ipady**:
   - These options control the internal padding (in pixels) along the x and y axes, respectively.
   - Example: The labels in the previous example demonstrate the use of `ipadx` and `ipady`.

5. **padx** and **pady**:
   - These options provide external padding (in pixels) along the x and y axes, respectively.
   - Example: You can add external padding to widgets using `padx` and `pady`.

6. **Anchor**:
   - The `anchor` option specifies the position of the widget within its allocated space. It can take values like `'nw'` (top-left), `'center'`, or `'se'` (bottom-right).
   - Example: To create labels anchored at different positions:
     ```python
     label1 = Label(root, text="Top-Left", bg="lightblue")
     label1.pack(anchor='nw')

     label2 = Label(root, text="Center", bg="lightgreen")
     label2.pack(anchor='center')

     label3 = Label(root, text="Bottom-Right", bg="lightpink")
     label3.pack(anchor='se')
     ```

Remember that the `pack()` method organizes widgets within a container based on these options. Feel free to adapt these examples to your specific needs! 😊

References:
1. [Learn how to use Pack in Tkinter - ActiveState](https://www.activestate.com/resources/quick-reads/how-to-use-pack-in-tkinter/)
2. [Difference between \"fill\" and \"expand\" options for tkinter pack method - Stack Overflow](https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method)
3. [Simplified Tkinter Pack Manager Tutorial - UltraPythonic](https://ultrapythonic.com/tkinter-pack/)
4. [Tkinter Pack Geometry Manager - Python Tutorial](https://www.pythontutorial.net/tkinter/tkinter-pack/)

Source: Conversation with Copilot, 02/06/2024
(1) Learn how to use Pack in Tkinter - three examples - ActiveState. https://www.activestate.com/resources/quick-reads/how-to-use-pack-in-tkinter/.
(2) Difference between "fill" and "expand" options for tkinter pack method. https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method.
(3) Simplified Tkinter Pack Manager Tutorial. https://ultrapythonic.com/tkinter-pack/.
(4) Tkinter Pack Geometry Manager - Python Tutorial. https://www.pythontutorial.net/tkinter/tkinter-pack/.
(5) github.com. https://github.com/Ninja-of-Physics/PhysicsOne/tree/d3c9171233bc262251452f7afd645d46c8716c27/tk_testing.py.