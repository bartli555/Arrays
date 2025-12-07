import random

# 1. Prosta lista
arr1 = [3, 7, 1, 0, 4]
print(f"arr1: {arr1}")

# 2. Lista dwuwymiarowa (lista list)
arr2 = [[2, 3], [7, 1], [0, 4]]
print(f"arr2: {arr2}")

# 3. Lista wypełniona tą samą wartością (7) pięć razy
# [wyrażenie for zmienna in zakres]
arr3 = [7 for i in range(5)]
print(f"arr3: {arr3}")

# 4. Lista liczb od 1 do 9
arr4 = [i for i in range(1, 10)]
print(f"arr4: {arr4}")

# 5. Lista liczb parzystych (każda liczba z zakresu pomnożona przez 2)
arr5 = [i * 2 for i in range(1, 10)]
print(f"arr5: {arr5}")

# 6. Lista 10 losowych liczb z zakresu 1-20
arr6 = [random.randint(1, 20) for i in range(10)]
print(f"arr6: {arr6}")

# 7. Lista zawierająca 5 pustych list
arr7 = [[] for i in range(5)]
print(f"arr7: {arr7}")

# 8. Tablica 2D (4 wiersze, 2 kolumny) wypełniona jedynkami
# Zewnętrzna pętla (j) tworzy wiersze, wewnętrzna (i) tworzy kolumny
arr8 = [[1 for i in range(2)] for j in range(4)]
print(f"arr8: {arr8}")

# 9. Tablica 2D (5 wierszy, 3 kolumny) z losowymi liczbami
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]
print(f"arr9: {arr9}")

# --- Dodatkowe zadania opisowe ---

# 10. Tablica z wartościami 4, 0, 3
arr10 = [4, 0, 3]
print(f"arr10: {arr10}")

# 11. 15-elementowa tablica wypełniona zerami
# Można użyć pętli: [0 for i in range(15)]
# Lub mnożenia listy (szybsze): [0] * 15
arr11 = [0] * 15
print(f"arr11: {arr11}")

# 12. Tablica z liczbami całkowitymi z zakresu <1, 30>
# range(1, 31) generuje liczby od 1 do 30 włącznie
arr12 = list(range(1, 31))
print(f"arr12: {arr12}")

# 13. 20-elementowa tablica wypełniona losowo 0 lub 1
arr13 = [random.randint(0, 1) for i in range(20)]
print(f"arr13: {arr13}")

# 14. Tablica dwuwymiarowa (5 wierszy, 2 kolumny) wypełniona False
# [False, False] powtórzone 5 razy
arr14 = [[False for i in range(2)] for j in range(5)]
print(f"arr14: {arr14}")