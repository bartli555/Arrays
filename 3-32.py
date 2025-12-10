def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f"{item:2}", end=" ")
        print()

matrix = [
    [1, 2, 3, 4, 5],      # Wiersz 0 (Pierwszy)
    [6, 7, 8, 9, 10],     # Wiersz 1 (Środkowy)
    [11, 12, 13, 14, 15]  # Wiersz 2 (Ostatni)
]

print("Tablica PRZED zmianą")
print_matrix(matrix)     
   
# Zamieniamy element pod indeksem 0 z elementem pod indeksem -1 (ostatnim)
matrix[0], matrix[-1] = matrix[-1], matrix[0]

print("\nTablica PO zmianie")
print_matrix(matrix)