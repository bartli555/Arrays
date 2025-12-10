def identity_matrix(n):
    matrix = [[0] * n for i in range(n)]
    #Wstawiamy jedynki na przekątnej
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

sizes = [3, 5, 8]
for size in sizes:
    print(f"\nMacierz o wymiarach {size}x{size}:")
    my_identity_matrix = identity_matrix(size)
    print_matrix(my_identity_matrix)            