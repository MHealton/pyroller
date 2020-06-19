import random

def print_class_race():
    classes = ['Assassin','Cleric','Druid','Fighter','Illusionist','Magic User','Paladin','Ranger','Thief']
    races   = ['Dwarf','Elf','Gnome','Half Elf','Halfling','Half Orc', 'Human']
    class_choice = random.choice(classes)
    race_choice  = random.choice(races)
    if (race_choice == 'Elf'):
        print('Why not an', race_choice, class_choice, 'maybe?')
    else:
        print('Why not a', race_choice, class_choice, 'maybe?')

print_class_race()
