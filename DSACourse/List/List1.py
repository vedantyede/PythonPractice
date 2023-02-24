listItems = [10, 20, 30, 40, 50]
# list item excess
print(listItems[3])  # 40
print(listItems[-1])  # 50
print(listItems[0])  # 10

# append, insert, and search function
listItems.append(60)
print(listItems)  # [10, 20, 30, 40, 50, 60]
listItems.insert(1, 15)
print(listItems)  # [10, 15, 20, 30, 40, 50, 60]
print(15 in listItems)  # True
print(listItems.count(30))  # 1
print(listItems.index(30))  # 3
print(listItems.index(30, 0, 7))  # 3

# remove of items
listItems.remove(20)
print(listItems)  # [10, 15, 30, 40, 50, 60]
print(listItems.pop())  # 60
print(listItems)  # [10, 15, 30, 40, 50]
print(listItems.pop(2))  # 30
print(listItems)  # [10, 15, 40, 50]
del listItems[1]
print(listItems)  # [10, 40, 50]
del listItems[0:2]
print(listItems)  # [50]

# other list functions
listItems = [10, 20, 30, 40, 50]
print(max(listItems))  # 50
print(min(listItems))  # 10
print(sum(listItems))  # 150
listItems.reverse()
print(listItems)  # [50, 40, 30, 20, 10]
listItems.sort()
print(listItems)  # [10, 20, 30, 40, 50]
