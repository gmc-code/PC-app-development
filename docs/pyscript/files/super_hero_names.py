import random


first_names = {
    "A": "Atomic", "B": "Blazing", "C": "Cosmic",
    "D": "Daring", "E": "Electric", "F": "Furious",
    "G": "Galactic", "H": "Hyper", "I": "Invincible",
    "J": "Justice", "K": "Kinetic", "L": "Legendary",
    "M": "Mighty", "N": "Noble", "O": "Omega",
    "P": "Polaris", "Q": "Quantum", "R": "Radiant",
    "S": "Stealth", "T": "Titan", "U": "Unstoppable",
    "V": "Vigilant", "W": "Warrior", "X": "Xeno",
    "Y": "Yieldless", "Z": "Zephyr",
}

last_names = {
    "A": "Avenger", "B": "Blade", "C": "Crusader",
    "D": "Defender", "E": "Eagle", "F": "Falcon",
    "G": "Guardian", "H": "Hawk", "I": "Inferno",
    "J": "Jaguar", "K": "Knight", "L": "Lion",
    "M": "Marvel", "N": "Ninja", "O": "Oracle",
    "P": "Phantom", "Q": "Quicksilver", "R": "Ranger",
    "S": "Specter", "T": "Thunder", "U": "Ultra",
    "V": "Viper", "W": "Wolf", "X": "Xiphos",
    "Y": "Youngstorm", "Z": "Zoom",
}

def get_superhero():
    first_initial = (input("What is the first initial: ")).upper()
    last_initial = (input("What is the last initial: ")).upper()
    superhero_name = first_names[first_initial] + " " + last_names[last_initial]
    return superhero_name

print("Your super hero name is:", get_superhero())

# Find keys with the same values
# same_values = {k: first_names[k] for k in first_names if k in last_names and first_names[k] == last_names[k]}
# print(same_values)
