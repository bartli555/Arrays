def flatten_2d_array(array_2d):
    array_1d = []

    for row in array_2d:
        for item in row:
            array_1d.append(item)
    return array_1d 

def print_arrays(original, flattened):
    print(f"2D: {original}")
    print(f"1D: {flattened}")
    print("-" * 30)

print("Konwersja Tablic 2D -> 1D\n")
matrix1 = [
    [2, 3],
    [1, 5]
]
matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]
matrix3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]
flat1 = flatten_2d_array(matrix1)
print_arrays(matrix1, flat1)

flat2 = flatten_2d_array(matrix2)
print_arrays(matrix2, flat2)

flat3 = flatten_2d_array(matrix3)
print_arrays(matrix3, flat3)