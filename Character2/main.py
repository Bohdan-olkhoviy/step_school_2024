from Character import Character
from berserk import Berserk
from assasin import Assassin
from ninja import Ninja

player1 = Character("Gojo", 101, 150, 0)
player2 = Berserk("Sukuna", 75, 75, 50)
player3 = Assassin("Toji", 125, 110, 2)
player4 = Ninja("Yuta", 250, 85, 99)


while (player1.health > 0 and (player2.health > 0 or player3.health > 0 or player4.health > 0)) or \
      (player2.health > 0 and (player1.health > 0 or player3.health > 0 or player4.health > 0)) or \
      (player3.health > 0 and (player1.health > 0 or player2.health > 0 or player4.health > 0)) or \
      (player4.health > 0 and (player1.health > 0 or player2.health > 0 or player3.health > 0)):

    if player1.health > 0:
        if player2.health > 0:
            player1.attack(player2)
        elif player3.health > 0:
            player1.attack(player3)
        elif player4.health > 0:
            player1.attack(player4)


    if player2.health > 0:
        if player1.health > 0:
            player2.attack(player1)
        elif player3.health > 0:
            player2.attack(player3)
        elif player4.health > 0:
            player2.attack(player4)

    if player3.health > 0:
        if player1.health > 0:
            player3.attack(player1)
        elif player2.health > 0:
            player3.attack(player2)
        elif player4.health > 0:
            player3.attack(player4)

    if player4.health > 0:
        if player1.health > 0:
            player4.attack(player1)
        elif player2.health > 0:
            player4.attack(player2)
        elif player3.health > 0:
            player4.attack(player3)

    alive_players = sum(1 for player in [player1, player2, player3, player4] if player.health > 0)
    if alive_players <= 1:
        break
