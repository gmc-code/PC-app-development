# tk Scale - get

import tkinter as tk


def convert():
    celsius = temp_scale.get()
    fahrenheit = celsius * 9 / 5 + 32
    result_label.config(text=f"{celsius} °C = {fahrenheit} °F")


root = tk.Tk()
root.geometry("300x200")
root.title("get")

temp_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, label="°C")
temp_scale.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
