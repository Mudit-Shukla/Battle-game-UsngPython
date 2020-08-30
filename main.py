from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 20, "dmg": 60},
         {"name": "thunder", "cost": 30, "dmg": 120},
         {"name": "blizzard", "cost": 40, "dmg": 180}]

player = Person(460, 65, 60, 34, magic)     # creating player
enemy = Person(1200, 65, 45, 24, magic)     # creating enemy

running = True

i = 0

print(
    bcolors.FAIL + bcolors.BOLD + "Enemy Attacks" + bcolors.END)  # colours the text "Enemy attacks" the last attribute cancels the effect of the last applied effects.

while running:
    print("======================================")
    player.choose_action()                  # select action whether attack or use magic
    choice = int(input("Enter your choice"))
    index = choice

    if index == 1:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print(bcolors.OKBLUE + "You attacked for " + str(damage) + "points of damage. Enemy hit points " + str(enemy.get_hp()) + bcolors.END)
    elif index == 2:
        player.choose_magic()
        magic_choice = int(input("Enter magic choice")) - 1         # making compatible to array of magics

        spell = player.get_spell_name(magic_choice)         # getting name of spell from game.py at entered choice
        cost_of_spell = player.get_spell_mp_cost(magic_choice)      # getting cost of the same spell

        if player.get_mp() > cost_of_spell:     # checking if player has enough magic points
            damage_caused_by_magic = player.generate_spell_damage(magic_choice)     # generate damage and store in a variable
            enemy.take_damage(damage_caused_by_magic)       # applying damage to enemy
            player.reduce_mp(player.get_spell_mp_cost(magic_choice))        # reduce magic points of player
            print(bcolors.WARNING + "Your magic points ", str(player.get_mp()) + bcolors.END)
            print(bcolors.OKBLUE + "You attacked for " + str(damage_caused_by_magic) + "points of damage. Enemy hit points " + str(enemy.get_hp()) + bcolors.END)
        else:
            print(bcolors.FAIL + "You do not have enough magic points to buy ", spell + bcolors.END)
            continue        # skip rest of steps and move back to the start of loop

    enemy_choice = 1        # declaring enemy choice as attack only (till now)
    damage = enemy.generate_damage()  # generating damage by enemy
    player.take_damage(damage)  # applying damage to player
    if player.get_hp() == 0:       # checking if player is dead
        print(bcolors.FAIL + "You are dead. You Lost" + bcolors.END)
        break
    elif enemy.get_hp() == 0:    # checking if enemy is dead
        print(bcolors.OKBLUE + "Enemy is dead. You Won!" + bcolors.END)
        break
    else:
        print(bcolors.WARNING + "Enemy attacked for" + str(damage) + " points of damage. Your hit points " + str(player.get_hp()) +bcolors.END)
