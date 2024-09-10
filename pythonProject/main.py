import random
def choose_item():
    while True:
        choice = input('Ваш вибір: ')
        if choice in ['к', 'н', 'п']:
            return choice
        else:
            print('Вибір некоректний. Спробуйте ще раз.')
'''
    к - каміння
    н - ножиці
    п - папір
'''
while True:
    print('- КАМІННЯ. НОЖИЦІ. ПАПІР -')
    print('\nДля гри Вам необхідно обрати один з трьох предметів:')
    print('к - каміння')
    print('н - ножиці')
    print('п - папір')
    player_choice = choose_item()
    bot_choice = random.choice('кнп') # ['к', 'н', 'п']
    print()
    print(f'Ви обрали: {player_choice}')
    print(f'Комп\'ютер обрав: {bot_choice}')

    if player_choice == bot_choice:
        print('Ничья')
        print('Переможться встановити не вдалося')
    elif player_choice == 'п' and bot_choice == 'к'\
        or player_choice == 'н' and bot_choice == 'п' \
        or player_choice == 'к' and bot_choice == 'н':
        print('Ви перемогли')
    elif player_choice == 'н' and bot_choice == 'п' \
        or player_choice == 'к' and bot_choice == 'н' \
        or player_choice == 'п' and bot_choice == 'к':
        print('Переміг комп\'ютер')
    else:
        print('Переможться встановити не вдалося')

