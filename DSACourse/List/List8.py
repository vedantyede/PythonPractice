# Rotate Left one time List

l1 = [10, 20, 30, 40]


def rotate_left1(list_element):
    list1 = list_element[1:] + list_element[0:1]
    return list1


def rotate_left2(list_element):
    list_element.append(list_element.pop(0))
    return list_element


def rotateByOne(list_element):
    n = list_element[0]
    for i in range(len(list_element)-1):
        list_element[i] = list_element[i+1]
    list_element[i-1] = n
    return list_element


print(rotate_left1(l1))
print(rotate_left2(l1))
print(rotateByOne(l1))
