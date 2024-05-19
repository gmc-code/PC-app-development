
from tkinter import *


window = Tk()
window.title("Calculator")

# entry field
e = Entry(window, width=13, borderwidth=5, font=('Arial', 36))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

# button command
def button_click(number):
    curr_text = e.get()
    e.delete(0, END)
    e.insert(0, str(curr_text)+ str(number))

# clear command
def button_clear():
    e.delete(0, END)

# add command
def button_add():
    # get entry field number
    first_number = e.get()
    # declare a global so f_num can be used elsewhere
    global f_num
    # store number as an integer
    f_num = int(first_number)
    # clear entry field
    e.delete(0, END)

# add command
def button_subtract():
    # get entry field number
    first_number = e.get()
    # declare a global so f_num can be used elsewhere
    global f_num
    # store number as an integer
    f_num = int(first_number)
    # clear entry field
    e.delete(0, END)

# add command
def button_multiply():
    # get entry field number
    first_number = e.get()
    # declare a global so f_num can be used elsewhere
    global f_num
    # store number as an integer
    f_num = int(first_number)
    # clear entry field
    e.delete(0, END)

# add command
def button_divide():
    # get entry field number
    first_number = e.get()
    # declare a global so f_num can be used elsewhere
    global f_num
    # store number as an integer
    f_num = int(first_number)
    # clear entry field
    e.delete(0, END)

# equal command
def button_equal():
    # get entry field number
    second_number = e.get()
    # clear entry field
    e.delete(0, END)
    # declare a global so f_num can be used elsewhere
    global f_num
    # insert answer
    e.insert(0, f_num + int(second_number))

# equal command
def button_equal():
    # get entry field number
    second_number = e.get()
    # clear entry field
    e.delete(0, END)
    # declare a global so f_num can be used elsewhere
    global f_num
    # insert answer
    e.insert(0, f_num - int(second_number))

# equal command
def button_equal():
    # get entry field number
    second_number = e.get()
    # clear entry field
    e.delete(0, END)
    # declare a global so f_num can be used elsewhere
    global f_num
    # insert answer
    e.insert(0, f_num * int(second_number))

# equal command
def button_equal():
    # get entry field number
    second_number = e.get()
    # clear entry field
    e.delete(0, END)
    # declare a global so f_num can be used elsewhere
    global f_num
    # insert answer
    e.insert(0, f_num / int(second_number))

# define number buttons
button_1 = Button(window, text="1", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, font=('Arial', 25), command=lambda: button_click(0))



# define operator buttons
button_add = Button(window, text="+", padx=40, pady=20, font=('Arial', 25), command=button_add)
button_subtract = Button(window, text="-", padx=40, pady=20, font=('Arial', 25), command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, font=('Arial', 25), command=button_multiply)
button_divide = Button(window, text="/", padx=40, pady=20, font=('Arial', 25), command=button_divide)
button_equal = Button(window, text="=", padx=250, pady=20, bg='green', font=('Arial', 25), command=button_equal)
button_clear = Button(window, text="Clear", padx=75, pady=20, font=('Arial', 25), command=button_clear)


# place number buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

# place operator buttons
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=5, column=0, columnspan=6)
button_clear.grid(row=4, column=1, columnspan=2)

window.mainloop()

