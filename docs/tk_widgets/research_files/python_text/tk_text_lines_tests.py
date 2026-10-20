import tkinter as tk

root = tk.Tk()
root.title("Text Widget Index Insertion Test")
root.geometry("400x250")

text_widget = tk.Text(root, height=10, width=40, font=("Arial", 11))
text_widget.pack(padx=10, pady=10)

# 1. Populating some base lines
text_widget.insert("1.0", "Line 1: Apples\n")
text_widget.insert("2.0", "Line 2: Bananas\n")
text_widget.insert("3.0", "Line 3: Cantaloupes\n")

# 2. Inserting words INTO existing lines
# Let's insert "Fresh " at Line 2, Column 8 (right before 'Bananas')
text_widget.insert("2.8", "Fresh ")


# 3. TEST: Inserting into a line number that DOES NOT exist
# Right now we only have 3 lines of text. Let's try to insert at line 10.
text_widget.insert("10.0", "\n[Line 10 Test: Dragonfruit]")


# Let's print the actual total text to the console to see what happened
total_content = text_widget.get("1.0", "end")
print("--- Current Text Buffer Contents ---")
print(total_content)
print("------------------------------------")

root.mainloop()