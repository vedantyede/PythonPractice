# Pattern searching in Python

text = input("Enter the text")
pattern = input("Enter the pattern")

pos = text.find(pattern)

while pos >= 0:
    print(pos)
    pos = text.find(pattern, pos + 1)
