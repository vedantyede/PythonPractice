# Rotate Left d time List

l1 = [10, 20, 30, 40]


def rotate_left1(list_element, d):
    for i in range(d):
        list1 = list_element[1:] + list_element[0:1]
        list_element = list1
    return list1


print(rotate_left1(l1, 2))
