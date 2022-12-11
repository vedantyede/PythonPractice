# Largest Element in List
l1 = [10, 5, 20, 8]
l2 = [30, 30, 20]
l3 = [40]
print(max(l1))  # 20


def largest_element(list_element):
    largest_num = 0
    for x in list_element:
        if x > largest_num:
            largest_num = x
    return largest_num


print(largest_element(l1))  # 20
