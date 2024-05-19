import random

firstNames = {
    'A':'Angelic', 'B':'Blustery', 'C':'Cheery',
    'D':'Dancy', 'E':'Elfie', 'F':'Festive',
    'G':'Glistening', 'H':'Happy', 'I':'Icy',
    'J':'Jolly', 'K':'Kringle', 'L':'Lucky',
    'M':'Merry', 'N':'Naughty', 'O':'Oily',
    'P':'Pointy', 'Q':'Quirky', 'R':'Rosie',
    'S':'Snowy', 'T':'Tinsel', 'U':'Unity',
    'V':'Very Merry', 'W':'Wintry', 'X':'Xmasy',
    'Y':'Yule', 'Z':'Zippy'
}

lastNames = {
    'A':'Angel', 'B':'Bells', 'C':'Candy Cane',
    'D':'Dash', 'E':'Evergreen', 'F':'Feet',
    'G':'Gingerbread', 'H':'Holidays', 'I':'Icicles',
    'J':'Jingles', 'K':'Kringles', 'L':'Lights',
    'M':'McSnowface', 'N':'Noel', 'O':'Ornament',
    'P':'Peppermint', 'Q':'Quince Pie', 'R':'Ribbon',
    'S':'Snowball', 'T':'Toes', 'U':'Upatree',
    'V':'Vixen', 'W':'Wonderland', 'X':'Xmas',
    'Y':'Yuletide', 'Z':'Zest'
}


# while True:
#     firstInitial = (input("What is the first letter of your first name: ")).upper()
#     lastInitial = (input("What is the first letter of your last name: ")).upper()
#     elfName = firstNames [firstInitial] + " " + lastNames [lastInitial]
#     print ("Your elf name is: "+elfName)


# for i in range(20):
#     firstInitial = random.choice(list(firstNames.keys()))
#     lastInitial = random.choice(list(lastNames.keys()))
#     elfName = firstNames[firstInitial] + " " + lastNames[lastInitial]
#     print(i + 1, elfName)

def get_elves(num):
    elves = ""
    for i in range(int(num)):
        firstInitial = random.choice(list(firstNames.keys()))
        lastInitial = random.choice(list(lastNames.keys()))
        elfName = firstNames[firstInitial] + " " + lastNames[lastInitial]
        elves = elves + "\n" + elfName
    return elves


print(get_elves(input("How many elves?: ")))
