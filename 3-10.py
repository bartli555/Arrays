array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

print("Tablica 1:", array1)
print("Tablica 2:", array2)
print("Liczby z Tablicy 1, których nie ma w Tablicy 2:")

for number in array1:
    if number not in array2:
        print(number)