def create_2d_arr(x, y):
    return [[0] * y for i in range(x)]

rows = 3
cols = 5

my_array = create_2d_arr(rows, cols)

print(f"Utworzono tablicę {rows}x{cols}:")

print(my_array)

for row in my_array:
    print(row)