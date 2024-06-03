import tkinter as tk

# window
window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

# widgets 
label1 = tk.Label(window, text = 'Label 1', background = 'red')
label2 = tk.Label(window, text = 'Label 2', background = 'green')

# place
label1.place(x = 100 , y = 100, width = 200, height = 100)
label2.place(x = 200 , y = 200, width = 200, height = 100)

# run
window.mainloop()