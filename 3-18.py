import MyArrays

numbers = [7, 3, 8, 5, 2]

numbers_str = ",".join(map(str, numbers))
print(f"Numbers: {numbers_str}")

sec_max = MyArrays.second_largest(numbers)
print(f"Second largest number: {sec_max}")

med = MyArrays.median(numbers)
print(f"Median: {med}")

min_max = MyArrays.min_max_array(numbers)
print(f"Smallest and largest number: {min_max[0]},{min_max[1]}")

str_representation = MyArrays.array_to_string(numbers)
print(f"Numbers as a string: {str_representation}")