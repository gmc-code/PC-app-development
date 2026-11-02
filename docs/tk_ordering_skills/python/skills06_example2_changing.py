order = []                     # an empty list
order.append("Orange")         # ["Orange"]
order.append("Mango")          # ["Orange", "Mango"]
order.append("Apple")          # ["Orange", "Mango", "Apple"]
del order[1]                   # removes index 1: ["Orange", "Apple"]
print(order)
order.clear()                  # removes every item: []
print(order)
