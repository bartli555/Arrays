arr = [15, 8, 31, 47, 2, 19]

suma = 0

for liczba in arr:
    suma += liczba

srednia = suma/len(arr)

print(f'Tablica: {arr}')
print(f'Średnia: {srednia:.2f}')