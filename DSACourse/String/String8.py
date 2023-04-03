# Check for Anagram

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return "Not an Anagram"
    if sorted(str1) == sorted(str2):
        print("Is Anagram")
    else:
        print("No an Anagram")


def is_anagram2(str1, str2):
    if len(str1) != len(str2):
        return "Not an anagram"
    count = [0] * 256
    for i in range(len(str1)):
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1
    for x in count:
        if x != 0:
            return "Not an anagram"
    return "Is Anagram"


s1 = "listen"
s2 = "silent"
print(is_anagram2(s1, s2))

s3 = "aacb"
s4 = "abca"
print(is_anagram2(s3, s4))

s5 = "aab"
s6 = "abb"
print(is_anagram2(s5, s6))
