multiplication_table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(" Tablica przed zmianą")
for row in multiplication_table:
    print(row)

for i in range(len(multiplication_table)):
    for j in range(len(multiplication_table[i])):
        multiplication_table[i][j] = (i + 1) * (j + 1)

print("\nTabliczka Mnożenia")
for row in multiplication_table:
    for number in row:
        print(f"{number:2}", end=" ")
    print()