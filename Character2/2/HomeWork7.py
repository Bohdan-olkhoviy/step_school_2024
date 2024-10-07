result = []

def divider(a, b):
    if a < b:
        raise ValueError("The first number is greater than 2")
    if b > 100:
        raise IndexError("The second number is more than 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except Exception as e:
        print(f"ERROR DUDE {key}: {e}")

print(result)
