# Slicing (List, Tuple and String)
listItem = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# listItem[start: stop: step]
print(listItem[0:5:2])  # [10, 30, 50]
print(listItem[::2])  # [10, 30, 50, 70, 90]
print(listItem[:5])  # [10, 20, 30, 40, 50]
print(listItem[6:1:-1])  # [70, 60, 50, 40, 30]
print(listItem[7:1:1])  # []
print(listItem[-1:-6:-1])  # [90, 80, 70, 60, 50]
print(listItem[::-1])  # [90, 80, 70, 60, 50, 40, 30, 20, 10]


# difference between slicing in (list, tuple, string)
l1 = [10, 20, 30]  # list
l2 = l1[:]
t1 = (10, 20, 30)  # tuple
t2 = t1[:]
s1 = "geeks"  # string
s2 = s1[:]
print(l1 is l2)  # False
print(t1 is t2)  # True
print(s1 is s2)  # True

# Comprehension in Python ----
list1 = [x for x in range(11) if x % 2 == 0]
print(list1)  # [0, 2, 4, 6, 8, 10]

list2 = [x for x in range(11) if x % 2 != 0]
print(list2)  # [1, 3, 5, 7, 9]

# Greater than X
arr1 = [12, 32, 54, 768, 7, 452, 4546, 876, 54, 35, 5365, 64, 43, 43, 64, 6, 74, 6]
x1 = 50
list3 = [x for x in arr1 if x < x1]
print(list3)  # [12, 32, 7, 35, 43, 43, 6, 6]
# Smaller than X
list4 = [x for x in arr1 if x > x1]
print(list4)  # [54, 768, 452, 4546, 876, 54, 5365, 64, 64, 74]

# Examples
s = "geekforgeeks"
l1 = [x for x in s if x in "aeiou"]
print(l1)  # ['e', 'e', 'o', 'e', 'e']

l2 = ["geek", "ide", "courses", "gfg"]
l3 = [x for x in l2 if x.startswith("g")]
print(l3)  # ['geek', 'gfg']

l4 = [x*2 for x in range(10)]
print(l4)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Examples
l1 = ["geeks", "idle", "for", "geek", "gfg", "ide"]
l2 = [x.upper() for x in l1 if x.startswith("g")]
print(l2)  # ['GEEKS', 'GEEK', 'GFG']

# Set comprehension from list
l1 = [10, 20, 3, 40, 5, 60, 7, 80, 90, 100]
s1 = {x for x in l1 if x % 2 == 0}
s2 = {x for x in l1 if x % 2 != 0}
print(s1)  # {100, 40, 10, 80, 20, 90, 60}
print(s2)  # {3, 5, 7}

# Dictionary Comprehension
l1 = [1, 3, 4, 2, 5]
d1 = {x: x**3 for x in l1}
print(d1)  # {1: 1, 3: 27, 4: 64, 2: 8, 5: 125}

d2 = {x: f"ID{x}" for x in range(5)}
print(d2)  # {0: 'ID0', 1: 'ID1', 2: 'ID2', 3: 'ID3', 4: 'ID4'}

l2 = [101, 102, 103]
l3 = ["gfg", "ide", "courses"]
d3 = {l2[i]: l3[i] for i in range(len(l2))}
print(d3)  # {101: 'gfg', 102: 'ide', 103: 'courses'}

d3 = dict(zip(l2, l3))  # Better way
print(d3)  # {101: 'gfg', 102: 'ide', 103: 'courses'}

# Inverting a Dictionary(Key becomes value and value become key)
d1 = {101: "gfg", 103: "practice", 102: "idle"}
d2 = {v: k for (k, v) in d1.items()}
print(d2)  # {'gfg': 101, 'practice': 103, 'idle': 102}
