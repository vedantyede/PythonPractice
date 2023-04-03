# Check for palindrome in python

def is_palindrome(str):
    if str == str[::-1]:
        return "Yes"
    else:
        return "No"



def is_palindrome2(str):
    low = 0
    high = len(str) - 1
    while low < high:
        if str[low] != str[high]:
            return "No"
        low = low + 1
        high = high - 1
    return "Yes"


print(is_palindrome("1001"))

print(is_palindrome("123"))
