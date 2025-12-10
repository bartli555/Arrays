array_2d = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_val = array_2d[0][0]
min_row = 0
min_col = 0

max_val = array_2d[0][0]
max_row = 0
max_col = 0

for row in array_2d:
    print(row)
    # i - indeks wiersza
    # row - lista reprezentująca wiersz
    for i in range(len(array_2d)):
        # j - indeks kolumny
        for j in range(len(array_2d[i])):
            current_val = array_2d[i][j]

            if current_val < min_val:
                min_val = current_val
                min_row = i
                min_col = j
            if current_val > max_val:
                max_val = current_val
                max_row = i
                max_col = j    

print(f"Najmniejsza wartość: {min_val}")
print(f"Pozycja: wiersz {min_row}, kolumna {min_col}")

print(f"Największa wartość: {max_val}")
print(f"Pozycja: wiersz {max_row}, kolumna {max_col}")