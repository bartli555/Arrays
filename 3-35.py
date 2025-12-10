def transpose_matrix(m):
    if not m:
        return []
    
    rows = len(m)
    cols = len(m[0])

    # Tworzymy nową macierz (transponowaną)
    # Będzie miała 'cols' wierszy i 'rows' kolumn.
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
             new_row.append(m[i][j])
        transposed.append(new_row)
    return transposed

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f"{item:2}", end=" ")
        print()

print("Transpozycja")

matrices = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ],
    [
        [5, 6, 7, 8]
    ]
]

for i, m in enumerate(matrices, 1):
    print(f"\nMacierz {i} (Oryginał):")
    print_matrix(m)
    
    transposed_m = transpose_matrix(m)
    
    print(f"Macierz {i} (Transponowana):")
    print_matrix(transposed_m)