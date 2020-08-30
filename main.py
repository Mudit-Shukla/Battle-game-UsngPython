from classes.game import Person, bcolors
from classes.magic import Spell

# Black magic

Fire = Spell("Fire", 10, 50, "black")
Thunder = Spell("Thunder", 15, 75, "black")
Blizzard = Spell("Blizzard", 20, 100, "black")
Meteor = Spell("Meteor", 25, 120, "black")
Quake = Spell("Quake", 30, 150, "black")

# White magic

cure_level1 = Spell("Cure", 15, 75, "White")
cure_level2 = Spell("Cure", 25, 125, "White")

player = Person(460, 65, 60, 34, [Fire, Thunder, Blizzard, Meteor, Quake, cure_level1, cure_level2])  # creating player
enemy = Person(1200, 65, 45, 24, [])  # creating enemy

running = True

i = 0

print(
    bcolors.FAIL + bcolors.BOLD + "Enemy Attacks" + bcolors.END)  # colours the text "Enemy attacks" the last attribute cancels the effect of the last applied effects.

while running:
    print("\n======================================\n")
    player.choose_action()  # select action whether attack or use magic
    choice = int(input("Enter your choice"))
    index = choice

    if index == 1:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print(bcolors.OKBLUE + "You attacked for " + str(damage) + "points of damage. Enemy hit points " + str(
            enemy.get_hp()) + bcolors.END)
    elif index == 2:
        player.choose_magic()
        magic_choice = int(input("Enter magic choice")) - 1  # making compatible to array of magics

        spell = player.magic[magic_choice]  # getting name of spell
        magic_damage = spell.generate_spell_damage()  # getting cost of the same spell

        if player.get_mp() > spell.cost:  # checking if player has enough magic points

            if spell.type == "White":
                magic_damage = -magic_damage
                player.take_damage(magic_damage)
                player.reduce_mp(spell.cost)
                print(bcolors.WARNING + "Your magic points ", str(player.get_mp()) + bcolors.END)
                print(bcolors.OKBLUE + "You gained " + str(-magic_damage) + " points of damage. Enemy hit points " + str(enemy.get_hp()) + " and your hit points: " + str(player.get_hp()) + bcolors.END)
                continue
            else:
                damage_caused_by_magic = magic_damage  # generate damage and store in a variable
                enemy.take_damage(magic_damage)  # applying damage to enemy
                player.reduce_mp(spell.cost)  # reduce magic points of player
                print(bcolors.WARNING + "Your magic points ", str(player.get_mp()) + bcolors.END)
                print(bcolors.OKBLUE + "You attacked for " + str(magic_damage) + " points of damage. Enemy hit points " + str(enemy.get_hp()) + bcolors.END)
        else:
            print(bcolors.FAIL + "You do not have enough magic points to buy ", spell + bcolors.END)
            continue  # skip rest of steps and move back to the start of loop

    enemy_choice = 1  # declaring enemy choice as attack only (till now)
    damage = enemy.generate_damage()  # generating damage by enemy
    player.take_damage(damage)  # applying damage to player
    if player.get_hp() == 0:  # checking if player is dead
        print(bcolors.FAIL + "You are dead. You Lost" + bcolors.END)
        break
    elif enemy.get_hp() == 0:  # checking if enemy is dead
        print(bcolors.OKBLUE + "Enemy is dead. You Won!" + bcolors.END)
        break
    else:
        print(bcolors.WARNING + "Enemy attacked for" + str(damage) + " points of damage. Your hit points " + str(
            player.get_hp()) + bcolors.END)
