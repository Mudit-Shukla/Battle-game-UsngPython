from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Black magic

Fire = Spell("Fire", 10, 50, "black")
Thunder = Spell("Thunder", 15, 75, "black")
Blizzard = Spell("Blizzard", 20, 100, "black")
Meteor = Spell("Meteor", 25, 120, "black")
Quake = Spell("Quake", 30, 150, "black")

# White magic

cure_level1 = Spell("Cure", 15, 75, "White")
cure_level2 = Spell("Cure", 25, 125, "White")

# Adding Items

potion = Item("Potion", "potion", "Heals 50 HP", 50)
ultra_potion = Item("Ultra potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super potion", "potion", "Heals 150 HP", 150)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one of the party member", 9999)
mega_elixir = Item("Mega elixir", "elixir", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Attacks for 500 HP", 500)

player_spell = [Fire, Thunder, Blizzard, Meteor, Quake, cure_level1, cure_level2]
player_items = [{"item": potion, "quantity": 15}, {"item": ultra_potion, "quantity": 5},
                {"item": super_potion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": mega_elixir, "quantity": 2}, {"item": grenade, "quantity": 5}]

player = Person(460, 65, 60, 34, player_spell, player_items)  # creating player
enemy = Person(1200, 65, 45, 24, [], [])  # creating enemy

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
            player.reduce_mp(spell.cost)  # reduce magic points of player
            if spell.type == "White":
                magic_damage = -magic_damage
                player.take_damage(magic_damage)
                print(bcolors.WARNING + "Your magic points ", str(player.get_mp()) + bcolors.END)
                print(
                    bcolors.OKBLUE + "You gained " + str(-magic_damage) + " points of damage. Enemy hit points " + str(
                        enemy.get_hp()) + " and your hit points: " + str(player.get_hp()) + bcolors.END)
                continue
            else:
                damage_caused_by_magic = magic_damage  # generate damage and store in a variable
                enemy.take_damage(magic_damage)  # applying damage to enemy
                print(bcolors.WARNING + "Your magic points ", str(player.get_mp()) + bcolors.END)
                print(bcolors.OKBLUE + "You attacked for " + str(
                    magic_damage) + " points of damage. Enemy hit points " + str(enemy.get_hp()) + bcolors.END)
        else:
            print(bcolors.FAIL + "You do not have enough magic points to buy " + spell.name + bcolors.END)
            continue  # skip rest of steps and move back to the start of loop

    elif index == 3:
        player.choose_item()
        item_choice = int(input("Enter your choice of item")) -1

        item = player.items[item_choice]["item"]
        if player.items[item_choice]["quantity"] == 0:
            print("You do not have " + item.name)
            continue
        else:
            player.items[item_choice]["quantity"] -=1
            if item.type == "potion":
                player.take_damage(-item.property)
                print(bcolors.OKGREEN + item.name + " heals for " + str(item.property) , "HP" + bcolors.END)
            elif item.type == "elixir":
                player.hp = player.max_hp
                print(bcolors.OKGREEN + item.name + "restores all HP/MP" + bcolors.END)
            elif item.type == "attack":
                enemy.take_damage(item.property)
                print(bcolors.FAIL + "You attacked for " + str(item.property) + " points of damage. Enemy hit points" + str(enemy.get_hp()) + bcolors.END)



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
