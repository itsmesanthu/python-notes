# ============================================================
# strptime()
# ============================================================

# strptime() is used to convert a string into
# a datetime object.
#
#
# Syntax:
#
# datetime.strptime(string, format)
#
#
# Important difference:
#
# strftime()
#     ↓
# datetime → string
#
#
# strptime()
#     ↓
# string → datetime
# ============================================================

from datetime import datetime


# ============================================================
# 1. BASIC STRING TO DATETIME
# ============================================================

date_string = "23-09-2026"

date_object = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(date_object)


# Output:
# 2026-09-23 00:00:00


# ============================================================
# 2. STRING WITH TIME
# ============================================================

date_string = "23-09-2026 10:30:45"

date_object = datetime.strptime(
    date_string,
    "%d-%m-%Y %H:%M:%S"
)

print(date_object)


# Output:
# 2026-09-23 10:30:45


# ============================================================
# 3. EXTRACT DATE COMPONENTS
# ============================================================

date_string = "18/09/2004"

date_object = datetime.strptime(
    date_string,
    "%d/%m/%Y"
)

print(date_object.year)
print(date_object.month)
print(date_object.day)


# Output:
# 2004
# 9
# 18


# ============================================================
# 4. CONVERT USER INPUT
# ============================================================

date_string = input("Enter date (DD-MM-YYYY): ")

date_object = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print("Date:", date_object)


# ============================================================
# 5. strftime VS strptime
# ============================================================

# strftime:
#
# datetime → string
#
# Example:
#
# now.strftime("%d-%m-%Y")
#
#
# strptime:
#
# string → datetime
#
# Example:
#
# datetime.strptime(
#     "23-09-2026",
#     "%d-%m-%Y"
# )
# ============================================================


# ============================================================
# QUICK REVISION
# ============================================================

# strftime()
#     ↓
# Object → String
#
#
# strptime()
#     ↓
# String → Object
# ============================================================