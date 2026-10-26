
# ============================================================
# PANDAS BASICS
# ============================================================

# Pandas is a Python library used for data analysis.
# It helps us read, clean, filter, sort, and analyze data.
#
# Common uses:
# 1. Working with CSV and Excel files
# 2. Cleaning missing data
# 3. Filtering records
# 4. Sorting data
# 5. Calculating statistics
#
# Installation:
# pip install pandas

import pandas as pd


# ============================================================
# 1. IMPORTING PANDAS
# ============================================================

print(pd.__version__)

# Output: Your installed Pandas version


# ============================================================
# 2. CREATING A SIMPLE SERIES
# ============================================================

data = pd.Series([10, 20, 30, 40])

print(data)

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64


# ============================================================
# 3. CREATING A DATAFRAME
# ============================================================

data = {
    "Name": ["Ravi", "Priya", "Aman"],
    "Age": [22, 23, 21],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)

# Output:
#     Name  Age  Marks
# 0   Ravi   22     85
# 1  Priya   23     90
# 2   Aman   21     78


# ============================================================
# 4. VIEWING DATA
# ============================================================

print(df.head(2))

# Output:
#     Name  Age  Marks
# 0   Ravi   22     85
# 1  Priya   23     90


# ============================================================
# 5. DATAFRAME INFORMATION
# ============================================================

print(df.shape)

# Output:
# (3, 3)

df.info()

# Shows:
# - Column names
# - Number of non-missing values
# - Data types
# - Memory usage


# ============================================================
# 6. STATISTICAL SUMMARY
# ============================================================

print(df.describe())

# By default, describe() summarizes numeric columns.


# ============================================================
# 7. COLUMN NAMES
# ============================================================

print(df.columns)

# Output:
# Index(['Name', 'Age', 'Marks'], dtype='object')


# ============================================================
# 8. DATA TYPES
# ============================================================

print(df.dtypes)

# Output:
# Name     object
# Age       int64
# Marks     int64
# dtype: object

# Exact types may differ depending on the data.


# ============================================================
# PANDAS QUICK REVISION
# ============================================================

# Import:
# import pandas as pd
#
# Series:
# pd.Series([1, 2, 3])
#
# DataFrame:
# pd.DataFrame(data)
#
# First five rows:
# df.head()
#
# Last five rows:
# df.tail()
#
# Number of rows and columns:
# df.shape
#
# Column names:
# df.columns
#
# Data types:
# df.dtypes
#
# Data information:
# df.info()
#
# Statistics:
# df.describe()
