====================================================
tk text
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-label/?ref=lbp

The `tkinter.Text` widget provides a versatile multi-line text area that you can use for various purposes.
| To create a multi-line text widget the general syntax is:

.. py:function:: text_widget  = tk.Text(parent, option=value)

    | There are number of options which are used to change the format of the text. 
    | Number of options can be passed as parameters separated by commas. Some of them are listed below.


.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("400x250")  # Set window size


 
Options for the `Text` widget in Tkinter, including their default values and examples of use:

1. **autoseparators**:
   - **Default Value**: `False`
   - **Description**: Determines whether separators (such as line breaks) are automatically added to the undo stack after each insertion or deletion.
   - **Use Case Example**: In a collaborative document editor, enabling `autoseparators=True` ensures that undo actions group changes logically (e.g., undoing a whole paragraph instead of individual characters).

2. **background (bg)**:
   - **Default Value**: System-dependent (usually white)
   - **Description**: Sets the background color of the text widget.
   - **Use Case Example**: You're creating a notes app, and you want the background to be light yellow. Set `bg="lightyellow"`.

3. **bd (borderwidth)**:
   - **Default Value**: 2
   - **Description**: Specifies the width of the border around the widget.
   - **Use Case Example**: You're designing a chat input box, and you want a thin border. Set `bd=1`.

4. **blockcursor**:
   - **Default Value**: `False`
   - **Description**: Controls the cursor style when it's over the text. If set to `True`, the cursor is a block; if `False`, it's a line.
   - **Use Case Example**: In a code editor, set `blockcursor=True` to make the cursor more visible.

5. **cursor**:
   - **Default Value**: System-dependent (usually an arrow)
   - **Description**: Sets the cursor type (e.g., arrow, cross, etc.) when hovering over the widget.
   - **Use Case Example**: In a drawing app, set `cursor="cross"` to indicate that users can draw freehand shapes.

6. **endline**:
   - **Default Value**: ""
   - **Description**: Specifies the character(s) to be displayed at the end of each line.
   - **Use Case Example**: You're building a chat interface, and you want to add a smiley face (`":)"`) at the end of each message line.

7. **exportselection**:
   - **Default Value**: `True`
   - **Description**: Determines whether the selected text is automatically copied to the clipboard.
   - **Use Case Example**: Set `exportselection=False` for a password input field to prevent the password from being copied.

8. **fg (foreground)**:
   - **Default Value**: System-dependent (usually black)
   - **Description**: Sets the text color.
   - **Use Case Example**: For warning messages, set `fg="red"` to make them stand out.

9. **font**:
   - **Default Value**: System-dependent (usually a default font)
   - **Description**: Defines the font used for the text.
   - **Use Case Example**: Create a rich text editor with a specific font family and size: `font=("Arial", 12)`.

10. **height**:
    - **Default Value**: 24 (number of lines)
    - **Description**: Specifies the number of visible lines in the widget.
    - **Use Case Example**: In a log viewer, set `height=10` to display a limited number of log entries at once.

11. **highlightbackground**:
    - **Default Value**: System-dependent (usually gray)
    - **Description**: Sets the color of the focus highlight when the widget is not focused.
    - **Use Case Example**: Customize the focus highlight color to match your app's theme.

12. **highlightcolor**:
    - **Default Value**: System-dependent (usually black)
    - **Description**: Determines the color of the focus highlight when the widget is focused.
    - **Use Case Example**: Set `highlightcolor="blue"` for a noticeable focus highlight.

13. **highlightthickness**:
    - **Default Value**: 1 (pixel width)
    - **Description**: Sets the thickness of the focus highlight (border).
    - **Use Case Example**: Increase `highlightthickness` for a more prominent focus border.

14. **inactiveselectbackground**:
    - **Default Value**: System-dependent (usually gray)
    - **Description**: Color of the selected text when the widget is not active (not in focus).
    - **Use Case Example**: Customize the appearance of selected text when the widget is not in focus.

15. **insertbackground**:
    - **Default Value**: System-dependent (usually black)
    - **Description**: Color of the insertion cursor (caret).
    - **Use Case Example**: Set `insertbackground="green"` to make the cursor stand out.

16. **insertborderwidth**:
    - **Default Value**: 1
    - **Description**: Width of the insertion cursor's border.
    - **Use Case Example**: Increase `insertborderwidth

17. **insertofftime**:
    - **Default Value**: 300 (milliseconds)
    - **Description**: Specifies the time (in milliseconds) before the insertion cursor disappears when the widget loses focus.
    - **Use Case Example**: You're building a chat application, and you want the insertion cursor to remain visible for a longer duration after the user clicks outside the text box. Set `insertofftime=1000` (1 second).

18. **insertontime**:
    - **Default Value**: 600 (milliseconds)
    - **Description**: Specifies the time (in milliseconds) before the insertion cursor appears when the widget gains focus.
    - **Use Case Example**: In a search input field, set `insertontime=200` to make the cursor appear quickly when the user clicks inside the field.

19. **insertunfocussed**:
    - **Default Value**: `True`
    - **Description**: Determines whether the insertion cursor is visible when the widget is not focused.
    - **Use Case Example**: If you're creating a read-only display area, set `insertunfocussed=False` to hide the insertion cursor.

20. **insertwidth**:
    - **Default Value**: 2 (pixels)
    - **Description**: Width of the insertion cursor.
    - **Use Case Example**: For a code editor, set `insertwidth=3` to make the cursor wider and more noticeable.

21. **maxundo**:
    - **Default Value**: `-1` (unlimited)
    - **Description**: Maximum number of undo steps allowed.
    - **Use Case Example**: In a collaborative document editor, set `maxundo=50` to limit the number of undo steps per session.

22. **padx** and **pady**:
    - **Default Value**: 0
    - **Description**: Padding (horizontal and vertical) inside the widget.
    - **Use Case Example**: Add some space around the text content by setting `padx=5` and `pady=5`.

23. **relief**:
    - **Default Value**: `"flat"`
    - **Description**: Border style (e.g., `"flat"`, `"raised"`, `"sunken"`).
    - **Use Case Example**: Customize the appearance of the text widget border. For a raised effect, set `relief="raised"`.

24. **selectbackground**:
    - **Default Value**: System-dependent (usually blue)
    - **Description**: Background color of selected text.
    - **Use Case Example**: Set `selectbackground="yellow"` to highlight selected text with a yellow background.

25. **selectborderwidth**:
    - **Default Value**: 1
    - **Description**: Width of the selection border.
    - **Use Case Example**: Increase `selectborderwidth` to make the selection border more prominent.

26. **selectforeground**:
    - **Default Value**: System-dependent (usually white)
    - **Description**: Text color of selected text.
    - **Use Case Example**: Set `selectforeground="black"` to ensure good contrast for selected text.

27. **setgrid**:
    - **Default Value**: `False`
    - **Description**: Enables or disables grid alignment.
    - **Use Case Example**: If you're creating a crossword puzzle app, set `setgrid=True` to align text within grid cells.

28. **spacing1**, **spacing2**, **spacing3**:
    - **Default Value**: 0
    - **Description**: Line spacing parameters.
    - **Use Case Example**: Adjust line spacing for better readability. For example, set `spacing1=2` to add extra space between lines.

29. **startline**:
    - **Default Value**: 1
    - **Description**: Determines the first visible line.
    - **Use Case Example**: If you're displaying a long document, set `startline=10` to start showing content from the 10th line.

30. **state**:
    - **Default Value**: `"normal"` (editable)
    - **Description**: Sets the state of the widget (e.g., `"normal"`, `"disabled"`).
    - **Use Case Example**: Disable editing by setting `state="disabled"` for a read-only display.

31. **tabs**:
    - **Default Value**: System-dependent (usually 8 spaces)
    - **Description**: Defines tab stops.
    - **Use Case Example**: Customize tab behavior by setting specific tab stops (e.g., `tabs=(20, 40, 60)`).

32. **tabstyle**:
    - **Default Value**: `"wordprocessor"`
    - **Description**: Specifies the tab style (e.g., `"wordprocessor"`).
    - **Use Case Example**: Set `tabstyle="tabular"` for a more structured tab behavior.
  
33. **takefocus**:
    - **Default Value**: `True`
    - **Description**: Determines whether the widget can receive focus.
    - **Use Case Example**: If you have a search box, set `takefocus=False` to prevent it from receiving focus when navigating with the keyboard.

34. **undo**:
    - **Default Value**: `False`
    - **Description**: Enables or disables undo functionality.
    - **Use Case Example**: In a text editor, set `undo=True` to allow users to undo their changes.

35. **width**:
    - **Default Value**: System-dependent (usually 20 characters wide)
    - **Description**: Specifies the width of the widget in characters.
    - **Use Case Example**: Create a narrow input field by setting `width=10`.

36. **wrap**:
    - **Default Value**: `"none"`
    - **Description**: Controls text wrapping within the widget ("none," "char," or "word").
    - **Use Case Example**: For a chat message box, set `wrap="word"` to wrap text at word boundaries.

37. **xscrollcommand** and **yscrollcommand**:
    - **Default Value**: `None`
    - **Description**: Scrollbar commands for horizontal and vertical scrolling.
    - **Use Case Example**: Connect the text widget to horizontal and vertical scrollbars using these options.
