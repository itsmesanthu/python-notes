
# ============================================================
# PANDAS SERIES
# ============================================================

import pandas as pd


# ============================================================
# 1. CREATING A SERIES
# ============================================================

marks = pd.Series([80, 90, 75, 88])

print(marks)

# Output:
# 0    80
# 1    90
# 2    75
# 3    88
# dtype: int64


# ============================================================
# 2. CUSTOM INDEX
# ============================================================

marks = pd.Series(
    [80, 90, 75],
    index=["Ravi", "Priya", "Aman"]
)

print(marks)

# Output:
# Ravi     80
# Priya    90
# Aman     75
# dtype: int64


# ============================================================
# 3. ACCESSING VALUES
# ============================================================

marks = pd.Series(
    [80, 90, 75],
    index=["Ravi", "Priya", "Aman"]
)

print(marks["Ravi"])
print(marks.iloc[1])

# Output:
# 80
# 90

# Label-based access:
# marks["Ravi"]
#
# Position-based access:
# marks.iloc[1]


# ============================================================
# 4. SERIES OPERATIONS
# ============================================================

marks = pd.Series([10, 20, 30])

print(marks + 5)
print(marks * 2)

# Output:
# 0    15
# 1    25
# 2    35
# dtype: int64
#
# 0    20
# 1    40
# 2    60
# dtype: int64


# ============================================================
# 5. SERIES STATISTICS
# ============================================================

marks = pd.Series([70, 80, 90, 100])

print(marks.sum())
print(marks.mean())
print(marks.min())
print(marks.max())

# Output:
# 340
# 85.0
# 70
# 100


# ============================================================
# 6. FILTERING A SERIES
# ============================================================

marks = pd.Series([45, 60, 75, 90, 35])

print(marks[marks >= 60])

# Output:
# 1    60
# 2    75
# 3    90
# dtype: int64


# ============================================================
# 7. CHECKING UNIQUE VALUES
# ============================================================

values = pd.Series([10, 20, 10, 30, 20, 40])

print(values.unique())
print(values.nunique())

# Output:
# [10 20 30 40]
# 4


# ============================================================
# 8. VALUE COUNTS
# ============================================================

colors = pd.Series(["Red", "Blue", "Red", "Green", "Blue", "Red"])

print(colors.value_counts())

# Output:
# Red      3
# Blue     2
# Green    1
# Name: count, dtype: int64

# Ordering and displayed formatting can vary by Pandas version.


# ============================================================
# PANDAS SERIES QUICK REVISION
# ============================================================

# Create:
# pd.Series([10, 20, 30])
#
# Custom index:
# pd.Series([10, 20], index=["A", "B"])
#
# Label access:
# series["A"]
#
# Position access:
# series.iloc[0]
#
# Sum:
# series.sum()
#
# Average:
# series.mean()
#
# Unique values:
# series.unique()
#
# Count unique values:
# series.nunique()
#
# Frequency:
# series.value_counts()
