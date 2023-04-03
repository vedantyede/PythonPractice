# Reverse of the String

def reverse_string(str):
    rev = ''
    for i in str:
        rev = i + rev
    print(rev)


def reverse_string2(str):
    print(str[::-1])


s = input("Enter the String: ")
reverse_string(s)
reverse_string2(s)
