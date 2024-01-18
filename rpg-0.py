"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, type(enemy).__name__))
        if enemy.health <= 0:
            print("The {} is dead.".format(type(enemy).__name__))

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")
    
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))


hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():
    while goblin.alive() and hero.alive():
        print("------------------------------------")
        hero.print_status()
        goblin.print_status()
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print("------------------------------------")
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end="")
        user_input = input()
        if user_input == "1":
            # Call the attack method on the hero
            hero.attack(goblin)
            
        elif user_input == "2":
            # Call the attack method on the goblin
            goblin.attack(hero)
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(user_input))

main()
