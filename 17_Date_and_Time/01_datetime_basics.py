# ============================================================
# DATE AND TIME
# ============================================================

# Python provides the datetime module to work with:
#
# 1. Date
# 2. Time
# 3. Date and time together
# 4. Formatting dates
# 5. Converting strings to dates
# 6. Date and time calculations
#
#
# Main classes:
#
# datetime
# date
# time
# timedelta
# ============================================================


# ============================================================
# 1. IMPORT datetime MODULE
# ============================================================

import datetime


# ============================================================
# 2. CURRENT DATE AND TIME
# ============================================================

now = datetime.datetime.now()

print(now)


# Output will be similar to:
# 2026-09-23 17:30:15.123456


# ============================================================
# 3. CURRENT DATE
# ============================================================

today = datetime.date.today()

print(today)


# Output:
# 2026-09-23


# ============================================================
# 4. CREATE A DATE
# ============================================================

my_date = datetime.date(2026, 9, 23)

print(my_date)


# Output:
# 2026-09-23


# ============================================================
# 5. CREATE A TIME
# ============================================================

my_time = datetime.time(10, 30, 45)

print(my_time)


# Output:
# 10:30:45


# ============================================================
# 6. CREATE DATE AND TIME
# ============================================================

my_datetime = datetime.datetime(
    2026,
    9,
    23,
    10,
    30,
    45
)

print(my_datetime)


# Output:
# 2026-09-23 10:30:45


# ============================================================
# QUICK REVISION
# ============================================================

# datetime module
#     ↓
# Used for working with date and time.
#
#
# datetime.datetime
#     ↓
# Date + Time
#
#
# datetime.date
#     ↓
# Date only
#
#
# datetime.time
#     ↓
# Time only
#
#
# datetime.timedelta
#     ↓
# Difference / calculation between dates and times.
# ============================================================