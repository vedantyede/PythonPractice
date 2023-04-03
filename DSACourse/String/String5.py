# String Operations

s1 = 'VedantYede'
s2 = 'Vedant'
print(s1 in s2)
print(s2 in s1)
print(s1 not in s2)

s3 = 'Vedant'
s4 = 'Yede'
print(s3 + s4)
print("Welcome " + s3 + s4)

print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2, 0, 13))

print(len(s1))

s5 = s3.upper()
print(s5)

s6 = s4.lower()
print(s6)

print(s4.islower())
print(s6.islower())

print(s1.startswith("Vedant"))
print(s1.endswith("Yede"))
print(s1.startswith("Vedant", 1))
print(s1.endswith("Yede", 0, len(s1)))

s7 = "My name is Vedant"
print(s7.split())
s8 = "My,name,is,Vedant"
print(s8.split(","))

l1 = ["My", "Name", "Is", "Vedant"]
print(" ".join(l1))
print(",".join(l1))

s9 = "----Vedant Yede---"
print(s9.strip("-"))
print(s9.lstrip("-"))
print(s9.rstrip("-"))

s10 = "Yede"
print(s9.find(s10))
print(s9.find("Yedant"))
n = len(s9)
print(s1.find(s10, 1, n))

