==================================
Python Tkinter TTK Button Widget
==================================

| In Python's **Tkinter** library, the ``ttk.Button`` widget represents a standard clickable push button provided by the *Themed Tkinter* (TTK) module.
| Unlike basic classic Tkinter buttons, ``ttk.Button`` widgets automatically adapt their look and feel to match the native operating system (Windows, macOS, or Linux).
| Buttons trigger specific actions or execute Python functions when clicked by the user.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("TTK Button Example")

    def my_action():
        print("Button was clicked!")

    # Creating a native TTK Button linked to a function
    btn = ttk.Button(root, text="Click Me", command=my_action)
    btn.pack(padx=20, pady=20)

    root.mainloop()

----

Basic TTK Buttons and Commands (text, command, state)
=====================================================

The ``ttk.Button`` widget uses essential parameters to control text display, click events, and availability:

- **The text Parameter**: Defines the human-readable label displayed on the surface of the button.
- **The command Parameter**: Binds a Python function or callback to execute when the button is clicked (without parentheses).
- **The state Parameter**: Controls whether a button is active or non-interactive: ``"normal"`` (default) or ``"disabled"``.
- **Dynamic State Handling**: Button states can be updated dynamically using the ``.config()`` or ``.state()`` methods.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()

    def handle_submit():
        print("Form submitted successfully!")
        submit_btn.config(state="disabled")  # Disable button after click

    # Interactive button definition
    submit_btn = ttk.Button(root, text="Submit Form", command=handle_submit)
    submit_btn.pack(padx=10, pady=10)

    # Pre-disabled button example
    disabled_btn = ttk.Button(root, text="Unavailable Action", state="disabled")
    disabled_btn.pack(padx=10, pady=10)

    root.mainloop()

Quiz: Basic TTK Buttons and Commands
------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To import themed widgets in Tkinter, use `from tkinter import @@ttk@@`.
    2. The parameter used to pass a function to a button is @@command@@.
    3. To prevent a user from clicking a button, set its `state` parameter to @@"disabled"@@.
    4. When assigning a function to `command`, you must omit the @@parentheses@@ `()`.
    5. The string parameter that specifies the visible label on a button is @@text@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a callback function and bind it to a TTK Button.

.. ordering::

    import tkinter as tk
    from tkinter import ttk

    def say_hello():
        print("Hello World!")

    root = tk.Tk()
    btn = ttk.Button(root, text="Greet", command=say_hello)
    btn.pack()

----

**Example 2:** Create a disabled TTK button and enable it dynamically.

.. ordering::

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    btn = ttk.Button(root, text="Process", state="disabled")
    btn.pack()
    btn.config(state="normal")

----

**Example 3:** Construct two buttons side by side using grid layout.

.. ordering::

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    b1 = ttk.Button(root, text="Cancel").grid(row=0, column=0)
    b2 = ttk.Button(root, text="Save").grid(row=0, column=1)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How is the TTK module typically imported in a Python script?

        [x] from tkinter import ttk | Correct! The themed widgets module is imported using from tkinter import ttk.
        [ ] import ttk | Incorrect. ttk resides inside the main tkinter library package.
        [ ] import tkinter.button | Incorrect. Standard syntax requires importing ttk module.
        [ ] include tkinter.ttk | Incorrect. 'include' is C/C++ syntax, not Python.


    .. multichoice::

        What happens if you pass parentheses when assigning a command function (e.g., ``command=say_hello()``)?

        [x] The function executes immediately when the program starts rather than when clicked | Correct! Adding parentheses executes the function instantly during widget instantiation.
        [ ] Python raises a SyntaxError | Incorrect. It is valid syntax, but triggers instant execution during setup.
        [ ] The button gets permanently disabled | Incorrect. Command assignment dictates execution timing.
        [ ] The button label becomes empty | Incorrect. Text is handled by text parameter.


    .. multichoice::

        Which parameter sets the displayed text on a ``ttk.Button``?

        [x] text | Correct! The text parameter specifies button text.
        [ ] label | Incorrect. Parameter name is text.
        [ ] title | Incorrect. Parameter name is text.
        [ ] caption | Incorrect. Parameter name is text.


    .. multichoice::

        How do you disable a ``ttk.Button`` named ``btn1`` so it cannot be clicked?

        [x] btn1.config(state="disabled") | Correct! Setting state="disabled" deactivates click interaction.
        [ ] btn1.disable() | Incorrect. No native .disable() method exists.
        [ ] btn1.state = False | Incorrect. Use .config(state=...) or .state() methods.
        [ ] btn1.active(False) | Incorrect. Use state parameter.


    .. multichoice::

        What is a key benefit of using ``ttk.Button`` over a standard classic ``tk.Button``?

        [x] TTK buttons automatically match the native theme of the operating system | Correct! TTK provides native modern look-and-feel across desktop OS platforms.
        [ ] TTK buttons execute functions 10 times faster | Incorrect. Performance speed is identical.
        [ ] TTK buttons do not require a parent window | Incorrect. All widgets require a parent container.
        [ ] TTK buttons can only store numbers | Incorrect. Text and image rendering are fully supported.


    .. multichoice::

        What is the default state of a newly created ``ttk.Button``?

        [x] "normal" | Correct! Buttons default to active ("normal") state upon creation.
        [ ] "disabled" | Incorrect. Default state is active.
        [ ] "active" | Incorrect. Standard default string parameter value is "normal".
        [ ] "hidden" | Incorrect. Default state is visible and active.


    .. multichoice::

        Which statement accurately describes the ``command`` parameter in ``ttk.Button``?

        [x] It expects a reference to a callable function or lambda expression | Correct! Accepts uncalled function references or lambda functions.
        [ ] It expects a string containing Python code | Incorrect. Expects function references, not raw strings.
        [ ] It accepts multiple print statements separated by commas | Incorrect. Must be wrapped in a single function reference.
        [ ] It requires an integer status code | Incorrect. Requires a callable function reference.


    .. multichoice::

        How do you change the text of an existing ``ttk.Button`` instance ``btn`` to "Next"?

        [x] btn.config(text="Next") | Correct! .config(text="...") dynamically updates widget properties.
        [ ] btn.text = "Next" | Incorrect. Property mutation uses .config() or bracket assignment btn["text"] = "Next".
        [ ] btn.set_text("Next") | Incorrect. .config() or bracket dictionary access is required.
        [ ] btn.update("Next") | Incorrect. Standard parameter modification uses .config().


    .. multichoice::

        If you need a button to pass arguments to a function upon click, which syntax is correct?

        [x] command=lambda: my_func("Arg") | Correct! Using an anonymous lambda function defers execution until click.
        [ ] command=my_func("Arg") | Incorrect. Executes my_func("Arg") instantly during widget declaration.
        [ ] command="my_func('Arg')" | Incorrect. Commands do not accept raw string statements.
        [ ] command=my_func["Arg"] | Incorrect. Invalid syntax for function invocation.


    .. multichoice::

        What parameter value enables a previously disabled ``ttk.Button``?

        [x] state="normal" | Correct! Setting state="normal" re-enables interactive button clicking.
        [ ] state="enabled" | Incorrect. Valid string parameter is "normal".
        [ ] state="active" | Incorrect. Valid options are "normal" or "disabled".
        [ ] state=True | Incorrect. Uses string flags "normal" or "disabled".

----

Images, Styling, and Layout (image, compound, ttk.Style)
========================================================

``ttk.Button`` widgets can incorporate icons or custom visual styles using TTK styling mechanics:

- **The image Parameter**: Displays a ``PhotoImage`` icon on the surface of the button.
- **The compound Parameter**: Controls relative placement when combining both text and images: ``tk.LEFT``, ``tk.RIGHT``, ``tk.TOP``, ``tk.BOTTOM``, or ``tk.CENTER``.
- **TTK Styles (ttk.Style)**: TTK widgets use central style classes (e.g., ``TButton``) rather than direct background color options (``bg``/``fg``).
- **Image Persistence**: Image objects must maintain an active reference in memory to avoid garbage collection removal.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")

    # Custom styling using TTK Style manager
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12, "bold"))

    # Button combining text and an icon image
    icon = tk.PhotoImage(width=16, height=16)  # Blank placeholder image

    img_btn = ttk.Button(
        root,
        text="Download",
        image=icon,
        compound=tk.LEFT,        # Place icon to the LEFT of text
        style="Accent.TButton"
    )
    img_btn.pack(padx=20, pady=20)

    root.mainloop()

Quiz: Images, Styling, and Layout
---------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To render an icon on a button, pass a PhotoImage reference to the @@image@@ parameter.
    2. The @@compound@@ parameter dictates how text and images are positioned relative to each other.
    3. To place an icon image above the text label on a button, set `compound=tk.@@TOP@@`.
    4. Custom styling for TTK widgets is managed using the `ttk.@@Style@@()` class.
    5. Standard TTK buttons use the default style class name `"@@TButton@@"`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Load an image and attach it to a TTK button alongside text.

.. ordering::

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    img = tk.PhotoImage(file="icon.png")
    btn = ttk.Button(root, text="Open", image=img, compound=tk.LEFT)
    btn.pack()

----

**Example 2:** Apply a custom font using TTK Style configuration.

.. ordering::

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    style = ttk.Style()
    style.configure("Big.TButton", font=("Arial", 16))
    btn = ttk.Button(root, text="Large", style="Big.TButton")
    btn.pack()

----

**Example 3:** Create an image-only button centered inside a window.

.. ordering::

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    img = tk.PhotoImage(file="play.png")
    play_btn = ttk.Button(root, image=img)
    play_btn.pack(expand=True)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What parameter specifies where an icon is positioned relative to text on a ``ttk.Button``?

        [x] compound | Correct! compound controls relative alignment between image and text.
        [ ] align | Incorrect. Alignment is managed via compound parameter.
        [ ] side | Incorrect. side is a pack() geometry manager parameter.
        [ ] position | Incorrect. Parameter name is compound.


    .. multichoice::

        Which object type is commonly used to load photo icons into Tkinter widgets?

        [x] tk.PhotoImage | Correct! tk.PhotoImage loads GIF, PNG, and PPM image files into memory.
        [ ] tk.ImageFile | Incorrect. Python uses tk.PhotoImage.
        [ ] tk.Picture | Incorrect. Correct class name is tk.PhotoImage.
        [ ] tk.Graphic | Incorrect. Correct class name is tk.PhotoImage.


    .. multichoice::

        Why might an image fail to display on a button even if the file path is correct?

        [x] The image object was garbage-collected because no permanent variable reference was retained | Correct! Python garbage collects unreferenced local image instances.
        [ ] TTK buttons do not support images | Incorrect. TTK buttons fully support image rendering.
        [ ] The image file is larger than 10 pixels | Incorrect. Image size does not prevent rendering.
        [ ] Images require setting state="disabled" | Incorrect. State does not control image loading.


    .. multichoice::

        How do you change background/font aesthetics on TTK widgets instead of using direct ``bg`` or ``fg`` properties?

        [x] Configure options using ttk.Style() instances | Correct! TTK widget visual properties are governed centrally by ttk.Style().
        [ ] Modify the operating system registry | Incorrect. Use ttk.Style() class inside Python.
        [ ] Edit raw C++ Tkinter header files | Incorrect. Controlled via ttk.Style().
        [ ] Use html CSS style sheets | Incorrect. Web stylesheets are not supported natively in Tkinter.


    .. multichoice::

        What is the default behavior if an ``image`` parameter is provided without setting ``compound``?

        [x] The image replaces the text completely so only the image is visible | Correct! By default image overrides text unless compound specifies dual layout.
        [ ] Python raises a LayoutError | Incorrect. Syntax is valid, text is hidden.
        [ ] The text renders over top of image | Incorrect. Requires setting compound=tk.CENTER.
        [ ] The program crashes | Incorrect. Image displays alone.


    .. multichoice::

        Which ``compound`` option places the text directly over top of the center of an image?

        [x] compound=tk.CENTER | Correct! tk.CENTER layers text directly in the middle of the image.
        [ ] compound=tk.TOP | Incorrect. Places image above text.
        [ ] compound=tk.OVER | Incorrect. Valid constant is tk.CENTER.
        [ ] compound=tk.BOTH | Incorrect. Use tk.CENTER.


    .. multichoice::

        What standard style identifier suffix is used for TTK buttons?

        [x] .TButton | Correct! Custom TTK button styles end with the suffix .TButton (e.g., Custom.TButton).
        [ ] .ttkButton | Incorrect. Standard naming convention uses .TButton.
        [ ] .Button | Incorrect. TTK style class names begin with 'T' (e.g., TButton, TLabel).
        [ ] .BtnStyle | Incorrect. Standard suffix is .TButton.


    .. multichoice::

        How do you apply a custom style named ``"Action.TButton"`` to a ``ttk.Button``?

        [x] ttk.Button(root, text="Go", style="Action.TButton") | Correct! The style parameter accepts custom TTK style names.
        [ ] ttk.Button(root, text="Go", class_name="Action.TButton") | Incorrect. Parameter name is style.
        [ ] ttk.Button(root, text="Go", theme="Action.TButton") | Incorrect. Parameter name is style.
        [ ] ttk.Button(root, text="Go", css="Action.TButton") | Incorrect. Parameter name is style.


    .. multichoice::

        Which parameter allows a button image to be displayed to the RIGHT of its text label?

        [x] compound=tk.RIGHT | Correct! tk.RIGHT places image to the right side of text.
        [ ] side=tk.RIGHT | Incorrect. side belongs to pack().
        [ ] anchor=tk.E | Incorrect. anchor sets alignment inside bounds, compound positions image relative to text.
        [ ] image_pos="right" | Incorrect. Use compound parameter.


    .. multichoice::

        Can a ``ttk.Button`` display BOTH an image and a text string simultaneously?

        [x] Yes, by setting the compound parameter to define their relative placement | Correct! Combining image, text, and compound enables simultaneous display.
        [ ] No, buttons can only display either text or an image | Incorrect. Dual display is supported.
        [ ] Yes, but only on Linux OS | Incorrect. Cross-platform feature support.
        [ ] No, unless two separate buttons are merged | Incorrect. A single button handles both.

