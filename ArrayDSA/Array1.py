# Reverse the array
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [4, 6, 8, 2, 4, 9, 2, 1, 0]
print(arr)
reverse_array(arr)
print(arr)
