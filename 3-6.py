arr = [15, 8, 31, 47, 2, 19]

suma = 0

i = 0

while i < len(arr):
    suma += arr[i]

    i += 1

srednia = suma / len(arr)

print(f'Tablica: {arr}')
print(f'Średnia: {srednia:.2f}')   