car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

# without default
value = car_dictionary.get("brand")
print(value)

# without default; returns None
value = car_dictionary.get("brands")
print(value)

# with default
value = car_dictionary.get("brands", "not a valid key")
print(value)