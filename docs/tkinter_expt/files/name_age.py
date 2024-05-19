import tkinter as tk


window = tk.Tk()
window.title("Login form")
window.geometry('1000x300')
window.configure(bg='#FFFFFF')


def place_name_age():
    # get name
    name = name_entry.get()
    # get age
    age = age_entry.get()
    # clear name_age_text
    name_age_text.delete(1.0, tk.END)
    # insert name age
    name_age_text.insert(tk.INSERT, f'My name is {name}. \nI am {age} years old.')
    
    
#  create widgets
name_label = tk.Label(window, text="Name",
                            bg='#FFFFFF', fg='#444444', font=("Arial", 30))
age_label = tk.Label(window, text="Age",
                            bg='#FFFFFF', fg='#444444', font=("Arial", 30))
name_entry = tk.Entry(window, bg='#e5e5e5', fg='#444444', font=("Arial", 30))
age_entry = tk.Entry(window, bg='#e5e5e5', fg='#444444', font=("Arial", 30))

name_age_button =tk.Button(window, text="Name and Age",
                            bg='#FFFFFF', fg='#444444', font=("Arial", 30), command=place_name_age)
name_age_text = tk.Text(window, height=2, width=30, bg='#e5e5e5', fg='#444444', font=("Arial", 30))
# 

# place widgets on window
name_label.grid(row=0, column=0, sticky='e')
name_entry.grid(row=0, column=1, sticky='w')

age_label.grid(row=1, column=0, sticky='e')
age_entry.grid(row=1, column=1, sticky='w')

name_age_button.grid(row=2, column=0, columnspan=2)
name_age_text.grid(row=3, column=0, columnspan=2)



window.mainloop()
