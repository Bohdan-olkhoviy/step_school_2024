from Character import character
from berserk import Berserk

player1 = character("Gojo", 100, 5, 0)
print(player1)

player2 = Berserk("Sukuna", 100, 3, 2)
player2.show_stats

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

print(f'\n{player1}\n{player2}\n')