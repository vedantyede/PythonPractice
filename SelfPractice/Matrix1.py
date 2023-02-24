# Create a Matrix with for loop

listItems = []
for i in range(3):
    for j in range(3):
        listItems.append(i * j)
print(listItems)  # [0, 0, 0, 0, 1, 2, 0, 2, 4]

listItems = [(i, j) for i in range(3) for j in range(3)]
print(i, j)  # 2 2
print(listItems)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

listItems = [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]
print(listItems)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
