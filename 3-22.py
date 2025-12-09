import random

def rand_elem(array):
    return random.choice(array)

print("--- Losowanie Elementów ---")
my_array = [10, 20, 30, 40, 50, 60, 70]
print(f"Tablica: {my_array}\n")

print(f"Wylosowany element 1: {rand_elem(my_array)}")
print(f"Wylosowany element 2: {rand_elem(my_array)}")
print(f"Wylosowany element 3: {rand_elem(my_array)}")