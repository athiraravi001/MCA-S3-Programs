# a) Create a numpy array of shape (2,3)

import numpy as np
arr = np.array([[1, 2, 3], [5, 6, 7]])
print("Marix : \n", arr)
print("Shape : ", arr.shape)
print("\n====================\n")

# b) Create a list with 4 members and convert it into a numpy array of shape(2,2) and print the shape.

import numpy as np
l = [1, 2, 3, 4]
arr = np.array(l).reshape(2,2)
print("Matrix : \n", arr)
print("Shape : ", arr.shape)
print("\n====================\n")

# c) Generates an array of numbers within the range (1,10)

import numpy as np
arr=np.arange(1,11)
print(arr)
print("\n====================\n")

# d) Increment the values of all the elements in the array by 2

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr += 2
print(arr)
print("\n====================\n")

# e) Create a 3x3 identity matrix

import numpy as np
identity_matrix=np.identity(3)
print("Identity matrix\n", identity_matrix)
print("\n====================\n")

# f) create Null array of size 10

import numpy as np
null_array=np.zeros(10)
print("Null array : ", null_array)
print("\n====================\n")

# g) Perform addition, subtraction, multiplication and elementwise multiplication on  2D arrays

import numpy as np
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
print("First matrix\n", a1)
print("Second matrix\n", a2)
print("Addition matrix\n", a1+a2)
print("Subtraction matrix\n", a1-a2)
print("Multiplication\n", np.dot(a1,a2))
print("Elementwise multiplication\n", a1*a2)
print("\n====================\n")

# h) Find the transpose of a matrix

import numpy as np
b = np.array([[1, 2, 3],[4, 5, 6]])
print("Before performing transpose operation\n", b)
trans = b.T
print("After performing transpose operation\n", trans)
print("\n====================\n")

# i) Find the determinant of a matrix

import numpy as np
c = np.array([[1, 2],[3, 4]])
detp=np.linalg.det(c)
print("Determinant of a matrix : ",detp)
print("\n====================\n")

# j) Find the inverse of a matrix

import numpy as np
d = np.array([[1, 2],[3, 4]])
invp=np.linalg.inv(d)
print("Inverse of a matrix\n",invp)
print("\n====================\n")

# k) Find the rank of a matrix

import numpy as np
e = np.array([[1, 2],[3, 4]])
rank=np.linalg.matrix_rank(e)
print("Rank of a matrix : ",rank)
print("\n====================\n")

# l) Generate a 3D array with random numbers of shape (2, 2, 3)

import numpy as np
f = np.random.rand(2,2,3)
print("3D array with random numbers\n",f)
print("\n====================\n")

# m) Create a numpy array of shape (3,3) and also find the mean and standard deviation of the array and find the column-wise mean and standard deviation of the array

import numpy as np
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
matrix_mean = matrix.mean()
print("Matrix mean : ", matrix_mean)
matrix_std = matrix.std()
print("Matrix standard deviation : ", matrix_std)
columnwise_mean = np.mean(arr, axis=0)
print("Column-wise mean : ", columnwise_mean)
columnwise_std = np.std(arr, axis=0)
print("Columnwise standard deviation : ", columnwise_std)