
# ============================================================
# NUMPY BASICS
# ============================================================

# NumPy stands for Numerical Python.
# It is a Python library used for numerical calculations.
# It provides powerful arrays and mathematical operations.
#
# Installation:
# pip install numpy

import numpy as np


# ============================================================
# 1. IMPORTING NUMPY
# ============================================================

# np is the standard alias for NumPy.

print(np.__version__)

# Output: Your installed NumPy version


# ============================================================
# 2. BASIC PYTHON LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(type(numbers))

# Output:
# [10, 20, 30, 40, 50]
# <class 'list'>


# ============================================================
# 3. CREATING A NUMPY ARRAY
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print(type(arr))

# Output:
# [10 20 30 40 50]
# <class 'numpy.ndarray'>


# ============================================================
# 4. PYTHON LIST VS NUMPY ARRAY
# ============================================================

numbers = [1, 2, 3]
arr = np.array([1, 2, 3])

print(numbers * 2)
print(arr * 2)

# Output:
# [1, 2, 3, 1, 2, 3]
# [2 4 6]

# Explanation:
# List multiplication repeats the list.
# NumPy multiplication multiplies every element.


# ============================================================
# 5. NUMPY ARRAY DATA TYPE
# ============================================================

arr = np.array([10, 20, 30])

print(arr.dtype)

# Output: int64 or another integer type depending on platform


# ============================================================
# 6. ARRAY DIMENSION
# ============================================================

arr1 = np.array([10, 20, 30])
arr2 = np.array([[10, 20], [30, 40]])

print(arr1.ndim)
print(arr2.ndim)

# Output:
# 1
# 2


# ============================================================
# 7. ARRAY SHAPE
# ============================================================

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)

# Output:
# (2, 3)

# Explanation:
# 2 rows and 3 columns.


# ============================================================
# 8. ARRAY SIZE
# ============================================================

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.size)

# Output:
# 6

# size returns the total number of elements.


# ============================================================
# NUMPY QUICK REVISION
# ============================================================

# NumPy:
# Numerical Python library
#
# Import:
# import numpy as np
#
# Create array:
# np.array([1, 2, 3])
#
# Data type:
# arr.dtype
#
# Dimensions:
# arr.ndim
#
# Shape:
# arr.shape
#
# Total elements:
# arr.size
