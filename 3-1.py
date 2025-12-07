arr = [34, 7, 19, 4, 21, 8]

licznik_parzystych = 0

i = 0

print(arr)

while i < len(arr):
    if arr[i] % 2 == 0:
        licznik_parzystych += 1

    i += 1

print(f'Liczba parzystych: {licznik_parzystych}')