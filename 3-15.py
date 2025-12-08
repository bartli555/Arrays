my_tuple = (10, 20, 30, 40, 50)

reversed_tuple = my_tuple[::-1]

tuple_str = ",".join(map(str, my_tuple))
reversed_str = ",".join(map(str, reversed_tuple))

print(f"Tuple: {tuple_str}")
print(f"Reverse order: {reversed_str}")