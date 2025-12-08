def star(n):
    return '*' * n

numbers = [2, 6, 4, 9, 7]

for number in numbers:
    stars_bar = star(number)
    print(f"{number}: {stars_bar}")