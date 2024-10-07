from Character import Character

class Arena:
    def __init__(self, players_list=None):
        if players_list is None:
            players_list = []
        self.players_list = players_list

    def add_player(self, name, health, damage, defense):
        # Використовуємо Character з правильною назвою
        new_player = Character(name=name, health=health, damage=damage, defense=defense)
        self.players_list.append(new_player)
        print(f"Гравець {name} доданий до арени!")

    def show_players(self):
        print("Список гравців на арені:")
        for player in self.players_list:
            print(player)