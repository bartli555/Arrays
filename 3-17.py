my_tuple = (50, 20, 40, 50, 30, 50)

value_to_count = 50

occurrences = my_tuple.count(value_to_count)

tuple_string = ",".join(map(str, my_tuple))

print(f"Tuple: {tuple_string}")
print(f"Value: {value_to_count}")
print(f"Number of occurrences: {occurrences}")