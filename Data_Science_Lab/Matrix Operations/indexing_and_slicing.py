# Create a 4x4 matrix and perform the following operations

"""
a) Slice the second and third row of the matrix
b) Slice the last row of the matrix
c) Slice the last column of the matrix
d) Slice the first and third columns of the matrix
"""

import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print("Matrix : \n", arr)
print("\n====================\n")
a = arr[1:3, :]
print("Sliced second and third row : \n", a)
print("\n====================\n")
b = arr[-1, :]
print("Sliced last row : \n", b)
print("\n====================\n")
c = arr[:, [3]]
print("Sliced last column : \n", c)
print("\n====================\n")
d = arr[:, [0, 2]]
print("Sliced first and third columns : \n", d)