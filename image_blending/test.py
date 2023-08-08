import numpy as np

testcase = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [8, 9, 10, 11], [12, 13, 14, 15]])
mask = np.array([[1, 2, 3], [0, 0, 0], [-4, -5, -6]])

h, w = mask.shape
inverse_matrix = mask.copy()
for i in range(h // 2):
    inverse_matrix[i, :], inverse_matrix[h - 1 - i, :] = mask[h - 1 - i, :], mask[i, :]

print(inverse_matrix)
