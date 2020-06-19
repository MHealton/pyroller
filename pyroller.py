import random

def roll(rolls, max_sides):
    total = 0
    for roll in range(rolls):
        total += random.randint(1,max_sides)
    return total

def threedsix():
    result = roll(3,6)
    return result

def print_scores():
    print("STR: ", threedsix())
    print("DEX: ", threedsix())
    print("CON: ", threedsix())
    print("INT: ", threedsix())
    print("WIS: ", threedsix())
    print("CHA: ", threedsix())

print_scores()
