# Find the maximum and minimum element in an array

def max_min_element(arr):
    min_num = arr[0]
    max_num = 0
    for x in arr:
        if x > max_num:
            max_num = x

    for y in arr:
        if y < min_num:
            min_num = y

    return min_num, max_num


array = [10, 20, 60, 80, 70, 60, 87, 96, 74, 85, 32, 63, 41, 63, 47, 85]
min_number, max_number = max_min_element(array)
print(min_number)
print(max_number)
