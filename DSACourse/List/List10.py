# Reverse list

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def reverse_list1(list_elements):
    rev_list = list_elements[::-1]
    return rev_list


def reverse_list2(list_elements):
    rev_list = list(reversed(list_elements))
    return rev_list


def reverse_list3(list_elements):
    i = 0
    j = len(list_elements)-1
    while i < j:
        start = list_elements[i]
        end = list_elements[j]
        list_elements[i] = end
        list_elements[j] = start
        i = i+1
        j = j-1
    return list_elements


print(reverse_list1(l1))
print(reverse_list2(l1))
print(reverse_list3(l1))
