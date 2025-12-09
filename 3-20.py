arr = [7, 9, 2, 4, 5, 6]
print(f"Tablica oryginalna: {arr}")

even_numbers = []
odd_numbers = []

for number in arr:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

arr = even_numbers + odd_numbers

print(f"Tablica posortowana: {arr}")