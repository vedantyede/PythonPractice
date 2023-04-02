# Find the only odd

l1 = [10, 20, 20, 30, 10]
l2 = [40, 40]


def only_odd_in_list(list_elements):
    for i in list_elements:
        count = list_elements.count(i)
        if count % 2 != 0:
            return i
    return -1


def find_odd(list_elements):
    res = 0
    for x in list_elements:
        res = res ^ x
    return res


print(only_odd_in_list(l1))
print(find_odd(l1))
