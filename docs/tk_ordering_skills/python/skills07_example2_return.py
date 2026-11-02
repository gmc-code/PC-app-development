juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}
sizes = {"Small": 0.00, "Regular": 1.00, "Large": 2.00}

juice = "Mango"
size = "Large"


def get_juice_price():
    """Adds up the juice and size prices for one juice."""
    price = juices[juice] + sizes[size]
    return price


price = get_juice_price()
print(f"Price: ${price:.2f}")       # prints Price: $8.00
