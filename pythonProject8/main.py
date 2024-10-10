import random

class Character:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return f'{self.name}: Health = {self.health}, Damage = {self.damage}'

    def attack(self, other):
        damage_dealt = random.randint(0, self.damage)
        other.health -= damage_dealt
        print(f'{self.name} attacks {other.name} for {damage_dealt} damage!')

    def is_alive(self):
        return self.health > 0

# Основна частина
character1 = Character(name="Warrior", health=100, damage=20)
character2 = Character(name="Mage", health=80, damage=25)

while character1.is_alive() and character2.is_alive():
    character1.attack(character2)
    if not character2.is_alive():
        print(f'{character2.name} has fallen. {character1.name} wins!')
        break

    character2.attack(character1)
    if not character1.is_alive():
        print(f'{character1.name} has fallen. {character2.name} wins!')
        break

    print(character1)
    print(character2)
    print("-" * 30)