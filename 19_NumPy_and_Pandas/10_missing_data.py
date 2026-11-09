
# ============================================================
# PANDAS MISSING DATA
# ============================================================

# Missing data means a value is absent or unavailable.
# Pandas commonly represents missing numeric values as NaN.
#
# Handling missing data is an important data-cleaning task.

import pandas as pd
import numpy as np


# ============================================================
# 1. CREATING DATA WITH MISSING VALUES
# ============================================================

data = {
    "Name": ["Ravi", "Priya", "Aman", "Sneha"],
    "Age": [22, np.nan, 21, 24],
    "Marks": [85, 92, np.nan, 88]
}

df = pd.DataFrame(data)

print(df)

# Output:
#     Name   Age  Marks
# 0   Ravi  22.0   85.0
# 1  Priya   NaN   92.0
# 2   Aman  21.0    NaN
# 3  Sneha  24.0   88.0


# ============================================================
# 2. CHECKING MISSING VALUES
# ============================================================

print(df.isna())

# True indicates a missing value.


# ============================================================
# 3. COUNTING MISSING VALUES
# ============================================================

print(df.isna().sum())

# Output:
# Name     0
# Age      1
# Marks    1
# dtype: int64


# ============================================================
# 4. CHECKING NON-MISSING VALUES
# ============================================================

print(df.notna())

# True indicates a value is present.


# ============================================================
# 5. DROPPING ROWS WITH MISSING VALUES
# ============================================================

result = df.dropna()

print(result)

# Output:
#     Name   Age  Marks
# 0   Ravi  22.0   85.0
# 3  Sneha  24.0   88.0

# dropna() returns a new DataFrame by default.


# ============================================================
# 6. DROPPING COLUMNS WITH MISSING VALUES
# ============================================================

result = df.dropna(axis=1)

print(result)

# Removes columns containing at least one missing value.
# Name is retained because it has no missing values.


# ============================================================
# 7. FILLING MISSING VALUES WITH A FIXED VALUE
# ============================================================

result = df.fillna(0)

print(result)

# Replaces missing values with 0.


# ============================================================
# 8. FILLING WITH THE MEAN
# ============================================================

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

# Missing Age is replaced with the mean of available ages.


# ============================================================
# 9. FILLING WITH THE MEDIAN
# ============================================================

df["Marks"] = df["Marks"].fillna(df["Marks"].median())

print(df)

# Missing Marks is replaced with the median of available marks.


# ============================================================
# 10. FILLING WITH A FIXED TEXT VALUE
# ============================================================

data = {
    "Name": ["Ravi", None, "Aman"],
    "City": ["Bangalore", "Mysore", None]
}

df = pd.DataFrame(data)

df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Not Provided")

print(df)

# Missing text values are replaced with meaningful labels.


# ============================================================
# 11. FORWARD FILL
# ============================================================

data = pd.Series([10, np.nan, np.nan, 40])

print(data.ffill())

# Output:
# 0    10.0
# 1    10.0
# 2    10.0
# 3    40.0
# dtype: float64

# ffill() uses the previous valid value.


# ============================================================
# 12. BACKWARD FILL
# ============================================================

data = pd.Series([10, np.nan, np.nan, 40])

print(data.bfill())

# Output:
# 0    10.0
# 1    40.0
# 2    40.0
# 3    40.0
# dtype: float64

# bfill() uses the next valid value.


# ============================================================
# 13. REPLACING SPECIAL VALUES
# ============================================================

data = pd.Series([10, -999, 30, -999, 50])

data = data.replace(-999, np.nan)

print(data)

# Output:
# 0    10.0
# 1     NaN
# 2    30.0
# 3     NaN
# 4    50.0
# dtype: float64


# ============================================================
# MISSING DATA QUICK REVISION
# ============================================================

# Detect missing values:
# df.isna()
#
# Count missing values:
# df.isna().sum()
#
# Detect present values:
# df.notna()
#
# Drop rows:
# df.dropna()
#
# Drop columns:
# df.dropna(axis=1)
#
# Fill with fixed value:
# df.fillna(0)
#
# Fill with mean:
# df["Age"].fillna(df["Age"].mean())
#
# Fill with median:
# df["Marks"].fillna(df["Marks"].median())
#
# Forward fill:
# df.ffill()
#
# Backward fill:
# df.bfill()
#
# Replace a value:
# df.replace(-999, np.nan)
