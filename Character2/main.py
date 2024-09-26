from Character import character

player1 = character("Gojo", 100, 5, 0)
player1.show_stats()

player2 = character("Sukuna", 100, 3, 2)
player2.show_stats

player1.attack(player2)

a = 3
b = 5

print(id(a))
print(id(b))
