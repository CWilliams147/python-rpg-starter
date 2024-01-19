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

    def print_status(self):
        print("{} has {} health and {} power remaining.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

#self.power is subtracting whatever its value is from enemy
    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(hero.name, self.power, type(enemy).__name__))
        if enemy.health <= 0:
            print("The {} is dead.".format(goblin.name))

    
class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to you.".format(goblin.name, self.power))
        if enemy.health <= 0:
            print("You are dead.")
    
    # def print_status(self):
    #     print("The {} has {} health and {} power.".format(goblin.name, self.health, self.power))


hero = Hero("Spider-Man", 10, 5)
goblin = Goblin("Green Goblin", 6, 2)

def main():
    while goblin.alive() and hero.alive():
        print("------------------------------------")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(" ")
        hero.print_status()
        goblin.print_status()
        print(" ")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("------------------------------------")
        print("What do you want to do?")
        print("1. Go Web Go")
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
            print("With great power comes great responsibility")
            break
        else:
            print("Invalid input {}".format(user_input))

main()
