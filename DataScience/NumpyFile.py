import numpy as np

height = [1.73, 1.69, 1.8, 1.58, 1.56]
weight = [65.3, 66.2, 80, 50.5, 55]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)  # [1.73 1.69 1.8  1.58 1.56]
print(np_weight)  # [65.3 66.2 80.  50.5 55. ]

bmi = np_weight / np_height ** 2

print(bmi)  # [21.81830332 23.17846014 24.69135802 20.22912995 22.60026298]
print(np_height > 1.7)  # [ True False  True False False]

print(np_height[np_height > 1.7])  # [1.73 1.8 ]
