game_register = { 'googolplex': 100,
                'terminat0r': 27,
                'ace': 150,
                'teapot418' : 0 }

# print keys
keys = game_register.keys()
print("keys", keys)

# print values
values = game_register.values()
print("values", values)

# Access elements
value = game_register['ace']
print('ace', value)
value = game_register.get('ace')
print('ace', value)

# Retrieve a value for the key or default if not in dictionary
value = game_register.get('aced', 0)
print('aced', value)

# Add or update and existing entry
game_register['ace'] = 50
value = game_register['ace']
print('ace', value)

# Delete an entry
del game_register['ace']
value = game_register.get('ace', "no entry")
print('ace', value)

# check if key exists
key_exists = "googolplex" in game_register
print("googolplex", key_exists)
key_exists = "ace" in game_register
print("ace", key_exists)

# Delete all entries
game_register.clear()
dict_len = len(game_register)
print("dict length", dict_len)


# check if dictionary exists in local variables
try:
    game_register
    print("The game_register dictionary still exists.")
except NameError:
    print("The game_register dictionary has been deleted.")
# Delete the dictionary
del game_register
# check if dictionary exists in local variables
try:
    game_register
    print("The game_register dictionary still exists.")
except NameError:
    print("The game_register dictionary has been deleted.")
