# ============================================================
# DATE OBJECTS
# ============================================================

from datetime import date


# ============================================================
# 1. CREATE DATE OBJECT
# ============================================================

birthday = date(2004, 9, 18)

print(birthday)


# Output:
# 2004-09-18


# ============================================================
# 2. ACCESS DATE COMPONENTS
# ============================================================

birthday = date(2004, 9, 18)

print("Year:", birthday.year)
print("Month:", birthday.month)
print("Day:", birthday.day)


# ============================================================
# 3. WEEKDAY
# ============================================================

my_date = date(2026, 9, 23)

print(my_date.weekday())


# weekday():
#
# Monday    -> 0
# Tuesday   -> 1
# Wednesday -> 2
# Thursday  -> 3
# Friday    -> 4
# Saturday  -> 5
# Sunday    -> 6


# ============================================================
# 4. isoweekday()
# ============================================================

my_date = date(2026, 9, 23)

print(my_date.isoweekday())


# isoweekday():
#
# Monday    -> 1
# Tuesday   -> 2
# Wednesday -> 3
# ...
# Sunday    -> 7


# ============================================================
# 5. DATE COMPARISON
# ============================================================

date1 = date(2026, 1, 1)
date2 = date(2026, 12, 31)

print(date1 < date2)
print(date1 == date2)
print(date1 > date2)


# Output:
# True
# False
# False


# ============================================================
# 6. DATE FROM TODAY
# ============================================================

today = date.today()

print("Today:", today)


# ============================================================
# QUICK REVISION
# ============================================================

# date(year, month, day)
#     ↓
# Creates a date object.
#
#
# date.year
# date.month
# date.day
#     ↓
# Access individual components.
#
#
# weekday()
#     ↓
# Monday = 0 ... Sunday = 6
#
#
# isoweekday()
#     ↓
# Monday = 1 ... Sunday = 7
# ============================================================