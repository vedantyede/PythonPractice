# List Advantages: Random Access. Cache Friendly
# List Disadvantages: Insertion, Deletion are slow. Search is also slow for unsorted.

# How does Dynamic Size Work?
#


# Average of Mean of list:
def average(mean_list):
    add = 0
    for x in mean_list:
        add = add + x
    n = len(mean_list)
    return add / n


print(average([10, 20, 40, 60, 40, 20]))


# Separate Even and Odd:
def even_and_odd(arr):
    odd = []
    even = []
    for el in arr:
        if el % 2 == 0:
            odd.append(el)
        else:
            even.append(el)
    return odd, even


odd, even = even_and_odd([10, 21, 43, 60, 45, 20])
print(odd)
print(even)


# Get Smallest Element
def smallest_element(arr):
    smallest = arr[0]
    for item in arr:
        if item < smallest:
            smallest = item
    return smallest


print(smallest_element([12, 34, 756, 78, 234, 7, 43, 76, 4]))


# Get Smaller than Element
def get_smaller_element(arr, x):
    smaller = []
    for item in arr:
        if item < x:
            smaller.append(item)
    return smaller


print(get_smaller_element([12, 34, 756, 78, 234, 7, 43, 76, 4], 10))

