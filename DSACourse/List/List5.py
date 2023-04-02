# Second-Largest Element in the List
l1 = [10, 30, 44, 54, 76, 34, 65, 45, 86, 46, 34]
l2 = [20, 20, 20]


def second_largest_element(list_element):
    first = -1
    second = -1
    for i in list_element:
        if i > first:
            first = i
    for i in list_element:
        if i > second and i != first:
            second = i
    print("Second Largest Number ", second)


second_largest_element(l1)
