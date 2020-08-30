from classes.game import Person,bcolors

magic = [{"name": "Fire","cost": 10,"dmg": 60},
         {"name": "thunder","cost": 10,"dmg": 60},
         {"name": "blizzard","cost": 10,"dmg": 60}]

player = Person(460,65, 60, 34, magic)
enemy = Person(1200, 65, 45, 24, magic)

running = True

i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy Attacks" + bcolors.END)      # colours the text "Enemy attacks" the last attribute cancels the effect of the last applied effects.
