
# ============================================================
# NUMPY ARRAYS
# ============================================================

import numpy as np


# ============================================================
# 1. ONE-DIMENSIONAL ARRAY
# ============================================================

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.ndim)

# Output:
# [10 20 30 40]
# 1


# ============================================================
# 2. TWO-DIMENSIONAL ARRAY
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
print(arr.ndim)
print(arr.shape)

# Output:
# [[1 2 3]
#  [4 5 6]]
# 2
# (2, 3)


# ============================================================
# 3. THREE-DIMENSIONAL ARRAY
# ============================================================

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr)
print(arr.ndim)
print(arr.shape)

# Output:
# 3
# (2, 2, 2)

# A three-dimensional array contains two-dimensional structures.


# ============================================================
# 4. ARRAY OF ZEROS
# ============================================================

arr = np.zeros(5)

print(arr)

# Output:
# [0. 0. 0. 0. 0.]


# ============================================================
# 5. ARRAY OF ONES
# ============================================================

arr = np.ones(4)

print(arr)

# Output:
# [1. 1. 1. 1.]


# ============================================================
# 6. ARRAY WITH A RANGE OF NUMBERS
# ============================================================

arr = np.arange(1, 11)

print(arr)

# Output:
# [ 1  2  3  4  5  6  7  8  9 10]


# ============================================================
# 7. ARRAY WITH A STEP VALUE
# ============================================================

arr = np.arange(0, 11, 2)

print(arr)

# Output:
# [ 0  2  4  6  8 10]

# Syntax:
# np.arange(start, stop, step)
# The stop value is excluded.


# ============================================================
# 8. EVENLY SPACED VALUES
# ============================================================

arr = np.linspace(0, 10, 5)

print(arr)

# Output:
# [ 0.   2.5  5.   7.5 10. ]

# linspace creates a specified number of evenly spaced values.


# ============================================================
# 9. CHANGING ARRAY DATA TYPE
# ============================================================

arr = np.array([1.2, 2.5, 3.8])

new_arr = arr.astype(int)

print(new_arr)

# Output:
# [1 2 3]

# Conversion to int truncates the decimal part.


# ============================================================
# 10. RESHAPING AN ARRAY
# ============================================================

arr = np.arange(1, 7)

new_arr = arr.reshape(2, 3)

print(new_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]

# The total element count must remain the same.


# ============================================================
# NUMPY ARRAYS QUICK REVISION
# ============================================================

# One-dimensional:
# np.array([1, 2, 3])
#
# Two-dimensional:
# np.array([[1, 2], [3, 4]])
#
# Zeros:
# np.zeros(5)
#
# Ones:
# np.ones(5)
#
# Range:
# np.arange(1, 10)
#
# Evenly spaced values:
# np.linspace(0, 10, 5)
#
# Change data type:
# arr.astype(int)
#
# Reshape:
# arr.reshape(2, 3)
