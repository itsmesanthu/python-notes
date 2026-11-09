
# ============================================================
# PANDAS FILTERING AND SORTING
# ============================================================

import pandas as pd


# ============================================================
# 1. SAMPLE DATAFRAME
# ============================================================

data = {
    "Name": ["Ravi", "Priya", "Aman", "Sneha", "Kiran"],
    "Age": [22, 23, 21, 24, 22],
    "Marks": [85, 92, 35, 88, 65],
    "City": ["Bangalore", "Mysore", "Bangalore", "Mysore", "Delhi"]
}

df = pd.DataFrame(data)

print(df)


# ============================================================
# 2. FILTERING WITH ONE CONDITION
# ============================================================

result = df[df["Marks"] > 80]

print(result)

# Returns students with marks greater than 80.


# ============================================================
# 3. FILTERING WITH EQUAL TO
# ============================================================

result = df[df["City"] == "Bangalore"]

print(result)

# Returns rows where City is Bangalore.


# ============================================================
# 4. FILTERING WITH AND
# ============================================================

result = df[
    (df["Marks"] >= 60) &
    (df["Age"] >= 22)
]

print(result)

# Both conditions must be true.
# Use & for AND and wrap each condition in parentheses.


# ============================================================
# 5. FILTERING WITH OR
# ============================================================

result = df[
    (df["City"] == "Delhi") |
    (df["Marks"] > 90)
]

print(result)

# At least one condition must be true.
# Use | for OR.


# ============================================================
# 6. FILTERING WITH NOT EQUAL
# ============================================================

result = df[df["City"] != "Bangalore"]

print(result)


# ============================================================
# 7. FILTERING USING ISIN
# ============================================================

result = df[df["City"].isin(["Bangalore", "Delhi"])]

print(result)

# Selects rows where City matches either listed value.


# ============================================================
# 8. FILTERING USING BETWEEN
# ============================================================

result = df[df["Marks"].between(60, 90)]

print(result)

# By default, both endpoints are included.


# ============================================================
# 9. SORTING IN ASCENDING ORDER
# ============================================================

result = df.sort_values("Marks")

print(result)

# Lowest marks appear first.


# ============================================================
# 10. SORTING IN DESCENDING ORDER
# ============================================================

result = df.sort_values("Marks", ascending=False)

print(result)

# Highest marks appear first.


# ============================================================
# 11. SORTING BY MULTIPLE COLUMNS
# ============================================================

result = df.sort_values(
    ["City", "Marks"],
    ascending=[True, False]
)

print(result)

# Sorts City alphabetically.
# Within each city, sorts Marks from highest to lowest.


# ============================================================
# 12. TOP RECORDS
# ============================================================

print(df.nlargest(3, "Marks"))

# Returns the three rows with the highest Marks.


# ============================================================
# 13. BOTTOM RECORDS
# ============================================================

print(df.nsmallest(2, "Marks"))

# Returns the two rows with the lowest Marks.


# ============================================================
# 14. FILTERING USING QUERY
# ============================================================

result = df.query("Marks >= 80 and Age >= 22")

print(result)

# query() lets you write conditions as a string.


# ============================================================
# FILTERING AND SORTING QUICK REVISION
# ============================================================

# Greater than:
# df[df["Marks"] > 80]
#
# Equal to:
# df[df["City"] == "Bangalore"]
#
# AND:
# df[(df["Marks"] > 60) & (df["Age"] > 20)]
#
# OR:
# df[(df["City"] == "Delhi") | (df["Marks"] > 90)]
#
# Multiple values:
# df[df["City"].isin(["Delhi", "Mysore"])]
#
# Range:
# df[df["Marks"].between(60, 90)]
#
# Ascending:
# df.sort_values("Marks")
#
# Descending:
# df.sort_values("Marks", ascending=False)
#
# Top records:
# df.nlargest(3, "Marks")
#
# Bottom records:
# df.nsmallest(3, "Marks")
#
# Query:
# df.query("Marks > 80")
