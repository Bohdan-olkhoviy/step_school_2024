import random
def choose_item():
    while True:
        choice = input('Ваш вибір: ').lower()
        if choice in ['к', 'н', 'п','я','с']:
            return choice
        else:
            print('Вибір некоректний. Спробуйте ще раз.')


def choose_winner(player, bot):
    if player == bot:
        return 0
    elif player == 'к' and bot == 'н' \
        or player == 'н' and bot == 'п' \
         or player == 'п' and bot == 'к' \
        or player == 'я' and bot == 'с'\
        or player == 'с' and bot == 'к'\
        or player == 'с' and bot == 'п'\
        or player == 'п' and bot == 'я'\
        or player == 'я' and bot == 'к'\
        or player == 'я' and bot == 'н'\
        or player == 'с' and bot == 'н'\
        or player == 'с' and bot == 'п'\
        or player == 'с' and bot == 'к':
        return 1
    elif player == 'п' and bot == 'н'\
        or player == 'н' and bot == 'к'\
        or player == 'к' and bot == 'п'\
        or player == 'с' and bot == 'я'\
        or player == 'к' and bot == 'с'\
        or player == 'п' and bot == 'с'\
        or player == 'я' and bot == 'п'\
        or player == 'к' and bot == 'я'\
        or player == 'н' and bot == 'я'\
        or player == 'п' and bot == 'с'\
        or player == 'к' and bot == 'с'\
        or player == 'н' and bot == 'с':
        return -1
    else:
        return None
'''
    к - каміння
    н - ножиці
    п - папір
    я - ящірка
    с - спок
'''
print('- КАМІННЯ. НОЖИЦІ. ПАПІР. ЯЩІРКА. СПОК -')
while True:
    print('\nДля гри Вам необхідно обрати один з трьох предметів:')
    print('к - каміння')
    print('н - ножиці')
    print('п - папір')

    player_choice = choose_item()
    bot_choice = random.choice('кнпяс')
    print()
    print(f'Ви обрали: {player_choice}')
    print(f'Комп\'ютер обрав: {bot_choice}')
    winner = choose_winner(player_choice, bot_choice)
    if winner == 0:
        print('Нічия')
    elif winner == 1:
        print('Ви перемогли ')
    elif winner == 1:
        print('Переміг Комп\'ютер')
    else:
        print('Переможця не всановити')

    player_answer = input('Чи бажаеш зіграти ще раз (т / н ):').lower()
    if player_answer == 'н':
        break