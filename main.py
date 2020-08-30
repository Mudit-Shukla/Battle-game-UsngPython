from classes.game import Person,bcolors

magic = [{"name": "Fire","cost": 10,"dmg": 60},
         {"name": "thunder","cost": 10,"dmg": 60},
         {"name": "blizzard","cost": 10,"dmg": 60}]

player = Person(460,65, 60, 34, magic)
enemy = Person(1200, 65, 45, 24, magic)

running = True

i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy Attacks" + bcolors.END)      # colours the text "Enemy attacks" the last attribute cancels the effect of the last applied effects.

while running:
    print("======================================")
    player.choose_action()
    choice = int(input("Enter your choice"))
    index = choice - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print("You attacked for ", str(damage) + "points of damage. Enemy hit points ", enemy.get_hp())
    enemy_choice = 1
    damage = enemy.generate_damage()
    player.take_damage(damage)
    if player.get_hp() == 0:
        print("You are dead")
        break
    else:
        print("Enemy attacked for", str(damage) + " points of damage. Your hit points ", player.get_hp())

