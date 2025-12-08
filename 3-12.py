arr = [2, 3, 2, 5, 8, 1, 9, 8]
print("Array:", end=" ")
for item in arr:
    print(item, end=" ")
print()

print("Unique elements:", end=" ")

for number in arr:
    if arr.count(number) == 1:
        print(number, end=" ")