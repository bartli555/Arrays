macierz = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for row in macierz:
    print(row) #macierz oryginalna 

for i in range(len(macierz)):
    macierz[i][i] = 1

for row in macierz:
    for item in row:
        print(item, end=" ")
    print()