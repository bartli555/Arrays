matrix = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]
sum_last_col = 0

print("--- Tablica ---")
for row in matrix:
    print(row)

for row in matrix:
    last_value = row[-1]
    sum_last_col += last_value

print(f"Suma wartości w ostatniej kolumnie: {sum_last_col}")       