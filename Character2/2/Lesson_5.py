def input_int(calculator):
    while True:
        try:
            result = int(input(calculator))
        except ValueError:
            print("Число!")
        except ValueError:
            print("ЧИСЛО!!!")
        else:
            return result



one = input_int("Введіть число :")
two = input_int("Введіть число :")

try:
        print(f'{one} / {two} = {one} / {two}')
except ZeroDivisionError:
    print("Не можешь жилити на нуль!")
except:
    print("Щось Пішло не так")

print(f"Ок {one} + {two} =")
print(one + two)
print(f"Або {one} - {two} =")
print(one - two)
print(f"Або {one} * {two} =")
print(one * two)
print(f"Або {one} / {two} =")
print(one / two)
print(f"АБО! {one} + {two} * {one} - {two} / {one} =")
print(one / two)
