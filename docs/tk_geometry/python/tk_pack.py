import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('300x200')

label1 = tk.Label(master=root, text='x', bg='red', fg='black')
label2 = tk.Label(master=root, text='y', bg='light green', fg='black')
label3 = tk.Label(master=root, text='none', bg='light blue', fg='black')
label4 = tk.Label(master=root, text='both', bg='yellow', fg='black')

label1.pack(side='top', expand=False, fill="x")
label2.pack(side='top', expand=False, fill="y")
label3.pack(side='top', expand=False, fill="none")
label4.pack(side='top', expand=False, fill="both")


root.mainloop()
