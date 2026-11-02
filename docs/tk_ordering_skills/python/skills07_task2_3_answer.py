tacos = {"Beef": 4.00, "Fish": 5.50}
extras = {"No extra": 0.00, "Cheese": 1.00}

taco = "Fish"
extra = "Cheese"


def get_taco_price():
    """Adds up the taco and extra prices."""
    price = tacos[taco] + extras[extra]
    return price


def show_taco_price():
    """Prints the price of the chosen taco."""
    price = get_taco_price()
    print(f"{taco}, {extra}: ${price:.2f}")


show_taco_price()
