import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if (self.hp < 0):
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp = self.hp + dmg
        if (self.hp > self.max_hp):
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp = self.mp - cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(bcolors.OKGREEN +"\n       " + self.name + bcolors.END)
        print(bcolors.OKBLUE + bcolors.BOLD + "       Actions\n" + bcolors.END)
        for item in self.actions:
            print("          " + str(i), ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "       Magics\n" + bcolors.END)
        for spell in self.magic:
            print("         " + str(i) + ":", spell.name + " cost : ", spell.cost)
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "       Items\n" + bcolors.END)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name + ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1
    def get_stats(self):
        print("                               _________________________            _______________")
        print(
            bcolors.BOLD + self.name + ":          " + str(self.hp) + "/" + str(self.max_hp) + "  |" + bcolors.OKGREEN + "███████████             " + bcolors.END + "|    "+ str(self.mp) + "/" + str(self.max_mp) + "  |" + bcolors.OKBLUE + "████████      " + bcolors.END + "|" + bcolors.END)

