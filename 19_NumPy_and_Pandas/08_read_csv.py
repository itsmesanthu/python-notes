
# ============================================================
# READING CSV FILES WITH PANDAS
# ============================================================

import pandas as pd


# ============================================================
# 1. WHAT IS A CSV FILE?
# ============================================================

# CSV stands for Comma-Separated Values.
# It stores tabular data in a text file.
#
# Example students.csv:
#
# Name,Age,Marks
# Ravi,22,85
# Priya,23,92
# Aman,21,78


# ============================================================
# 2. READING A CSV FILE
# ============================================================

# The CSV file must exist at the specified path.
# Place students.csv in the same folder as this Python file.

# df = pd.read_csv("students.csv")
# print(df)

# Output:
#     Name  Age  Marks
# 0   Ravi   22     85
# 1  Priya   23     92
# 2   Aman   21     78


# ============================================================
# 3. CREATING A SAMPLE CSV FILE FOR PRACTICE
# ============================================================

sample_data = {
    "Name": ["Ravi", "Priya", "Aman", "Sneha"],
    "Age": [22, 23, 21, 24],
    "Marks": [85, 92, 78, 88]
}

sample_df = pd.DataFrame(sample_data)

sample_df.to_csv("students.csv", index=False)

print("CSV file created successfully")

# Output:
# CSV file created successfully

# index=False prevents Pandas from saving row indexes
# as an extra column.


# ============================================================
# 4. READING THE CREATED CSV
# ============================================================

df = pd.read_csv("students.csv")

print(df)

# Output:
#     Name  Age  Marks
# 0   Ravi   22     85
# 1  Priya   23     92
# 2   Aman   21     78
# 3  Sneha   24     88


# ============================================================
# 5. READING SELECTED COLUMNS
# ============================================================

df = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)

print(df)

# Reads only the selected columns.


# ============================================================
# 6. READING A LIMITED NUMBER OF ROWS
# ============================================================

df = pd.read_csv("students.csv", nrows=2)

print(df)

# Reads only the first two data rows.


# ============================================================
# 7. READING CSV WITH A DIFFERENT DELIMITER
# ============================================================

# Example data separated by semicolons:
#
# Name;Age;Marks
# Ravi;22;85
# Priya;23;92

# df = pd.read_csv("students_semicolon.csv", sep=";")


# ============================================================
# 8. SKIPPING ROWS
# ============================================================

# Skips the first data row after the header.
# df = pd.read_csv("students.csv", skiprows=[1])


# ============================================================
# 9. BASIC CSV INSPECTION
# ============================================================

df = pd.read_csv("students.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())


# ============================================================
# PANDAS CSV QUICK REVISION
# ============================================================

# Read CSV:
# pd.read_csv("students.csv")
#
# Save CSV:
# df.to_csv("output.csv", index=False)
#
# Select columns:
# pd.read_csv("students.csv", usecols=["Name", "Marks"])
#
# Limit rows:
# pd.read_csv("students.csv", nrows=5)
#
# Different separator:
# pd.read_csv("data.csv", sep=";")
#
# Skip rows:
# pd.read_csv("data.csv", skiprows=[1])
#
# Common inspection:
# df.head()
# df.shape
# df.columns
# df.info()
