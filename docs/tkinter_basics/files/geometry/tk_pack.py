import tkinter as tk

window = tk.Tk()
window.title('Tkinter Pack Layout')
window.geometry('600x400')

label1 = tk.Label(master=window, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(master=window,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(master=window, text='Fill',bg='blue', fg='white')
label4 = tk.Label(master=window, text='Demo',bg='purple', fg='white')

label1.pack(side='top', expand=True, fill=tk.X)
label2.pack(side='top', expand=True, fill=tk.Y)
label3.pack(side='top', expand=True, fill=tk.NONE)
label4.pack(side='top', expand=True, fill=tk.BOTH)


window.mainloop()
