from Character import Character
import random

class Assassin(Character):
    def __init__(self, name, health, damage, defense, crit_chance=0.1):
        super().__init__(name, health, damage, defense)
        self.crit_chance = crit_chance

    def attack(self, other):
        if random.random() < self.crit_chance:
            print(f"{self.name} завдає критичний удар!")
            other.take_damage(1000)
        else:
            super().attack(other)