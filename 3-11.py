def bubblesort(array):
    arr = array.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arrays_to_sort = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [-10, 0, 10, -5, 5]
]            

for arr in arrays_to_sort:
    print(f"\nOryginalna: {arr}")
    sorted_arr = bubblesort(arr)
    print(f"Posortowana: {sorted_arr}")