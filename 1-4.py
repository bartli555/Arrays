###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Ostatnia wartość', arr[-1])
przedostatnia = len(arr) - 2
print('Przedostatnia wartość', arr[przedostatnia])
ostatni = len(arr) - 1
print('Suma pierwszego i ostatniego', arr[0] + arr[ostatni])
srednia = sum(arr) / len(arr)
print('Srednia', srednia)
print('Elementy oddzielone spacją', end=" ")
for wartosc in arr:
    print(wartosc,end=" ")