def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False  # swapped variable
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # if already sorted it will return arr
            return arr
    return arr


arr_v = [3, 5, 2, 6, 8, 1, 4, 9, 7]
print(bubble_sort(arr_v))
