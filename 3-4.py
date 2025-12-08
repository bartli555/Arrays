arr = [-15, 8, -31, 47, -2, 19]

print("Tablica:", arr)

min_number = arr[0]
max_number = arr[0]

for number in arr:
    if number < min_number:
        min_number = number

    if number > max_number:
        max_number = number

print(f"Liczba minimalna: {min_number}")
print(f"Liczba maksymalna: {max_number}")        