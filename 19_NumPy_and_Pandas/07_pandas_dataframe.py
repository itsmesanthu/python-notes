
# ============================================================
# PANDAS DATAFRAME
# ============================================================

import pandas as pd


# ============================================================
# 1. CREATING A DATAFRAME
# ============================================================

data = {
    "Name": ["Ravi", "Priya", "Aman", "Sneha"],
    "Age": [22, 23, 21, 24],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df)

# Output:
#     Name  Age  Marks
# 0   Ravi   22     85
# 1  Priya   23     92
# 2   Aman   21     78
# 3  Sneha   24     88


# ============================================================
# 2. SELECTING ONE COLUMN
# ============================================================

print(df["Name"])

# Output:
# 0     Ravi
# 1    Priya
# 2     Aman
# 3    Sneha
# Name: Name, dtype: object


# ============================================================
# 3. SELECTING MULTIPLE COLUMNS
# ============================================================

print(df[["Name", "Marks"]])

# Output:
#     Name  Marks
# 0   Ravi     85
# 1  Priya     92
# 2   Aman     78
# 3  Sneha     88


# ============================================================
# 4. SELECTING ROWS WITH LOC
# ============================================================

print(df.loc[0])

# Selects the row with index label 0.


# ============================================================
# 5. SELECTING ROWS WITH ILOC
# ============================================================

print(df.iloc[1])

# Selects the second row by position.


# ============================================================
# 6. ADDING A NEW COLUMN
# ============================================================

df["Passed"] = df["Marks"] >= 40

print(df[["Name", "Passed"]])

# Output:
#     Name  Passed
# 0   Ravi    True
# 1  Priya    True
# 2   Aman    True
# 3  Sneha    True


# ============================================================
# 7. ADDING A NEW ROW
# ============================================================

new_row = pd.DataFrame([
    {"Name": "Kiran", "Age": 22, "Marks": 81, "Passed": True}
])

df = pd.concat([df, new_row], ignore_index=True)

print(df.tail(1))

# Adds a new row at the end.


# ============================================================
# 8. RENAMING COLUMNS
# ============================================================

df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Score"
})

print(df.columns)

# Output:
# Index(['Student_Name', 'Age', 'Score', 'Passed'], dtype='object')


# ============================================================
# 9. DROPPING A COLUMN
# ============================================================

df = df.drop(columns=["Passed"])

print(df.columns)

# Output:
# Index(['Student_Name', 'Age', 'Score'], dtype='object')


# ============================================================
# 10. DROPPING A ROW
# ============================================================

df = df.drop(index=0)

print(df.head())

# Removes the row whose index label is 0.


# ============================================================
# 11. ITERATING THROUGH ROWS
# ============================================================

data = {
    "Name": ["Ravi", "Priya"],
    "Marks": [85, 92]
}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    print(row["Name"], row["Marks"])

# Output:
# Ravi 85
# Priya 92


# ============================================================
# PANDAS DATAFRAME QUICK REVISION
# ============================================================

# Create:
# pd.DataFrame(data)
#
# One column:
# df["Name"]
#
# Multiple columns:
# df[["Name", "Marks"]]
#
# Row by label:
# df.loc[0]
#
# Row by position:
# df.iloc[0]
#
# Add column:
# df["Passed"] = df["Marks"] >= 40
#
# Rename:
# df.rename(columns={"Name": "Student_Name"})
#
# Drop column:
# df.drop(columns=["Passed"])
#
# Drop row:
# df.drop(index=0)
#
# Combine rows:
# pd.concat([df, new_row], ignore_index=True)
