# What is NumPy?
# NumPy, short for Numerical Python, is a fundamental library for numerical and scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays. NumPy serves as the foundation for many data science and machine learning libraries, making it an essential tool for data analysis and scientific research in Python.

# Key aspects of NumPy in Python:
# Efficient data structures: NumPy introduces efficient array structures, which are faster and more memory-efficient than Python lists. This is crucial for handling large data sets.

# Multi-dimensional arrays: NumPy allows you to work with multi-dimensional arrays, enabling the representation of matrices and tensors. This is particularly useful in scientific computing.

# Element-wise operations: NumPy simplifies element-wise mathematical operations on arrays, making it easy to perform calculations on entire data sets in one go.

# Random number generation: It provides a wide range of functions for generating random numbers and random data, which is useful for simulations and statistical analysis.

# Integration with other libraries: NumPy seamlessly integrates with other data science libraries like SciPy, Pandas, and Matplotlib, enhancing its utility in various domains.

# Performance optimization: NumPy functions are implemented in low-level languages like C and Fortran, which significantly boosts their performance. It's a go-to choice when speed is essential.

import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Array attributes
print(arr_2d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.
# output : 2
print(arr_2d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.
# Output : (3, 3)
print(arr_2d.size) # size: Provides the total number of elements in the array.
# Output : 9

# Indexing and slicing
print(arr_1d[2])          # Accessing an element (3rd element)

print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)

print(arr_2d[1])          # Accessing a row (2nd row)

print(arr_2d[:, 1])       # Accessing a column (2nd column)

# Array addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # [5 7 9 ]

# Scalar multiplication
array = np.array([1, 2, 3])
result = array * 2 # each element of an array is multiplied by 2
print(result)  # [2 4 6]

# Element-wise multiplication (Hadamard product)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print(result)  # [4 10 18]

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result)
# [[19 22]
#  [43 50]]

