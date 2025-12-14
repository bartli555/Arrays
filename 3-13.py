def occur(number, array):
    return number in array

my_array = [15, 38, 7, 23, 14]

try:
    number_str = input("Number: ")
    number = int(number_str)

    array_display = " ".join(map(str, my_array))
    print(f"Array: {array_display}")

    if occur(number, my_array):
        print(f"Result: number {number} appears in the array")
    else:
        print(f"Result: number {number} does NOT appear in the array")

except ValueError:
    print("Error: Please enter a valid integer.")
