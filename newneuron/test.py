import numpy as np

mat1 = np.array([[1, 2, 3, 4], [4, 5, 6, 4], [7, 8, 9, 4], [2, 2, 4, 3]])
mat2 = np.array([[1, 2, 3, 4], [4, 5, 6, 4], [7, 8, 9, 4], [2, 2, 1, 4]])

mat3 = mat1 @ mat2

print(mat3)