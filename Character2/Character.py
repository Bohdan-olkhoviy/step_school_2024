
class character:
    name = ' '
    Health = 100
    damage = 5
    Defendse = 90

    def __init__(self, name, health, damage, Defendse):
        self.name = name
        self.health = health
        self.damage = damage
        self.Defends = Defendse

        def show_stats(self):
            print(self)

        def __str__(self):
            return f"-- {self.name} -- \nЗдоровья: {self.health}\n" \
                  f"Шкода: {self.damage}\nЗахист: {self.defendse}"

            def take_damage(self, damage):
                self.health = max(self.health - damage, 0)