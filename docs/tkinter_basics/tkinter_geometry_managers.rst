====================================================
tk geometry managers
====================================================

| The grid geometry manager allows you to arrange widgets within a window.
| See: https://tkdocs.com/tutorial/grid.html
| See: https://www.geeksforgeeks.org/python-pack-method-in-tkinter/?ref=lbp

| Pack: see https://www.youtube.com/watch?v=rbW1iJO1psk
| Pack with frames: https://www.youtube.com/watch?v=SsjEAWT-SMc

| place: see https://www.youtube.com/watch?v=bx0YmWFfsEI

| grid: see https://www.youtube.com/watch?v=IJ-iVnN09-8

| pack is responsive to window size changes.

| place is not responsive to window size changes.
| Place uses absolute positioning. 

| grid is not responsive to window size changes.
| For grid, empty rows or columns are not allocated screen space.

1. **Relative Positioning:**
   - In relative positioning, you place the widget using relative coordinates using the `relx` and `rely` parameters.
   - For example, the following code places the widget in the center of its parent:
     ```python
     widget.place(relx=0.5, rely=0.5, anchor='center')
     ```

2. **Width and Height:**
   - You can set the width and height of the widget using the `width` and `height` parameters:
     ```python
     widget.place(width=120, height=60)
     ```
   - Alternatively, you can use relative sizing concerning the parent container. For instance, the following code sets the widget's width and height to 50% of the parent's dimensions:
     ```python
     widget.place(relwidth=0.5, relheight=0.5)
     ```

3. **Anchor:**
   - The `anchor` parameter determines which part of the widget is positioned at the given coordinates.
   - Common anchor values include:
     - `'n'`, `'ne'`, `'e'`, `'se'`, `'sw'`, `'w'`, `'nw'`: These constants represent the cardinal and intercardinal directions (north, northeast, east, southeast, south, southwest, west, northwest).
     - `'center'`: Positions the center of the widget at the specified coordinates (default anchor).
   - Example:
     ```python
     widget.place(relx=0.5, rely=0.5, anchor='center')
     ```

Source: Conversation with Copilot, 28/05/2024
(1) Tkinter Place Geometry Manager Explained By Examples - Python Tutorial. https://www.pythontutorial.net/tkinter/tkinter-place/.
(2) Place Geometry Manager in Tkinter (Place Layout) - Python Lobby. https://pythonlobby.com/geometry-manager-in-tkinter-place-layout-python-tkinter-tutorial/.
(3) Tkinter place() : Your Tool for Precise Widget Placement. https://ultrapythonic.com/tkinter-place/.

