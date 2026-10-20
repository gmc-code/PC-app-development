import tkinter as tk

root = tk.Tk()

widget1 = tk.Button(root)
widget2 = tk.Checkbutton(root)


print(widget1.widgetName)
in1 = set(widget1.configure().keys()) - set(widget2.configure().keys())
for option in in1:
    print(f"{option}: {widget1.cget(option)}")  # cget retrieves the current value of the option

print("\n\n" + widget2.widgetName)
in2 = set(widget2.configure().keys()) - set(widget1.configure().keys())
for option in in2:
    print(f"{option}: {widget2.cget(option)}")  # cget retrieves the current value of the option


