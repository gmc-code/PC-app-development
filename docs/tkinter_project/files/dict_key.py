car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

# key exists
value = car_dictionary["brand"]
print(value)

# key doesn't exist
try:
    value = car_dictionary["brands"]
    print(value)
except KeyError:
    print("not a valid key")
