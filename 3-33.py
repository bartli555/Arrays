def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f"{item:2}", end=" ")
        print()

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Tablica PRZED zmianą")
print_matrix(matrix)

for row in matrix:
    # Wewnątrz każdego wiersza zamieniamy element pierwszy (indeks 0)
    # z elementem ostatnim (indeks -1)
    row[0], row[-1] = row[-1], row[0]

print("\nTablica PO zmianie")
print_matrix(matrix)