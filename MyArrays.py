def bubblesort(arr):
    n = len(arr)
    sorted_arr = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr

def second_largest(arr):
    sorted_arr = bubblesort(arr)
    return sorted_arr[-2]

def difference_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return max_val - min_val

def median(arr):
    sorted_arr = bubblesort(arr)
    n = len(sorted_arr)
    mid_index = n // 2

    if n % 2 != 0:
        return sorted_arr[mid_index]
    else:
        left = sorted_arr[mid_index - 1]
        right = sorted_arr[mid_index]
        return (left + right) / 2
    
def min_max_array(arr):
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return [min_val, max_val]   

def array_to_string(arr):
    result = ""
    for i in range(len(arr)):
        result += str(arr[i])
        if i < len(arr) - 1:
            result += "-"
    return result 