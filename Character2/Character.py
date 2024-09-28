class Character:
    def __init__(self, name, health, damage, defense=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def attack(self, other):
        print(f"{self.name} атакує {other.name}")
        other.take_damage(self.damage)

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        print(f"{self.name} отримав {actual_damage} шкоди, залишилось здоров'я: {self.health}")