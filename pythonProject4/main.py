answer = 0

user = input('Яка країна найбільша? :')
if user == 'Україна':
    answer += 1
    print('Правильно')
else:
    print("Неправильно")
user = input('В якій країні зявилася китайська стіна :')
if user == 'Китай':
    answer += 1
    print('Правильно')
else:
    print('Неправильно')

user = input('Де ельфіва вежа :')
if user == 'Франция':
    answer += 1
    print('Правильно')
else:
    print('Неправильно')

user = input('Скільки Роблоку років :')
if user == '37':
    answer += 1
    print("Правильно")
else:
    print("Неправильно")

user = input("У якому місті Париж :")
if user == 'Франция':
    answer += 1
    print('Правильно')
else:
    print('Неправильно')

print("Правильних відповідей: ", answer)
