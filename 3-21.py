def is_subset(subset_candidate, main_array):
    for element in subset_candidate:
        if element not in main_array:
            return False
    return True

print("--- Sprawdzanie Podzbioru ---")

arr1 = [3, 7]
arr2 = [1, 3, 9, 7, 5]

if is_subset(arr1, arr2):
    print(f"Tablica {arr1} JEST podzbiorem tablicy {arr2}")
else:
    print(f"Tablica {arr1} NIE JEST podzbiorem tablicy {arr2}")

arr3 = [10, 2]
arr4 = [1, 2, 3]

if is_subset(arr3, arr4):
    print(f"Tablica {arr3} JEST podzbiorem tablicy {arr4}")
else:
    print(f"Tablica {arr3} NIE JEST podzbiorem tablicy {arr4}")