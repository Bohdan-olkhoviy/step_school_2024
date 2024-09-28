import random
from Character import Character


class Ninja(Character):
    def __init__(self, name, health, damage, defense, dodge_chance=0.3):
        super().__init__(name, health, damage, defense)
        self.dodge_chance = dodge_chance

    # Обробляє отримання урона
    def take_damage(self, damage):
        if random.random() < self.dodge_chance:
            print(f"{self.name} ухилився від атаки!")
        else:
            super().take_damage(damage)

    def __str__(self):
        return (f'{self.name} -- \nЗдоров\'я: {self.health}\n'
                f'Шкода: {self.damage}\nЗахист: {self.defense}\n'
                f'Ймовірність ухилення: {self.dodge_chance * 100}%')
