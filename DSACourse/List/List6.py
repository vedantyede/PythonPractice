# Check if List is sorted

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l2 = [20, 40, 20, 10, 50, 40, 70, 80]


def is_list_sorted(list_element):
    for i in range(len(list_element)-1):
        i = i+1
        if list_element[i] < list_element[i-1]:
            return False
    return True


def is_Sorted(list_element):
    s1 = sorted(list_element)
    if s1 == list_element:
        return True
    return False


if is_list_sorted(l1):
    print("List is sorted")
else:
    print("List is not sorted")


if is_Sorted(l2):
    print("List is sorted")
else:
    print("List is not sorted")