tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
for taco in tacos.keys():
    print(f"{taco} (${tacos[taco]:.2f})")
