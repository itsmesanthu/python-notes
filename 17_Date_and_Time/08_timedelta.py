# ============================================================
# TIMEDELTA
# ============================================================

# timedelta represents a duration or difference
# between dates or times.
#
# It can be used to:
#
# 1. Add days to a date
# 2. Subtract days from a date
# 3. Find difference between dates
# 4. Work with hours, minutes, seconds
# ============================================================

from datetime import date, datetime, timedelta


# ============================================================
# 1. ADD DAYS
# ============================================================

today = date.today()

future_date = today + timedelta(days=7)

print("Today:", today)
print("After 7 days:", future_date)


# ============================================================
# 2. SUBTRACT DAYS
# ============================================================

today = date.today()

previous_date = today - timedelta(days=7)

print("Today:", today)
print("7 days ago:", previous_date)


# ============================================================
# 3. FIND DIFFERENCE BETWEEN DATES
# ============================================================

date1 = date(2026, 9, 23)
date2 = date(2026, 12, 25)

difference = date2 - date1

print(difference)


# Output:
# Number of days between the dates


# ============================================================
# 4. GET NUMBER OF DAYS
# ============================================================

print(difference.days)


# ============================================================
# 5. ADD HOURS
# ============================================================

now = datetime.now()

future = now + timedelta(hours=5)

print("Now:", now)
print("After 5 hours:", future)


# ============================================================
# 6. SUBTRACT HOURS
# ============================================================

now = datetime.now()

previous = now - timedelta(hours=5)

print("Now:", now)
print("5 hours ago:", previous)


# ============================================================
# 7. MULTIPLE TIME UNITS
# ============================================================

duration = timedelta(
    days=2,
    hours=5,
    minutes=30,
    seconds=15
)

print(duration)


# ============================================================
# 8. FIND AGE DIFFERENCE
# ============================================================

birth_date = date(2004, 9, 18)
today = date.today()

difference = today - birth_date

print("Days since birth:", difference.days)


# ============================================================
# 9. DEADLINE CALCULATION
# ============================================================

today = date.today()

deadline = today + timedelta(days=30)

print("Today:", today)
print("Deadline:", deadline)


# ============================================================
# QUICK REVISION
# ============================================================

# timedelta
#     ↓
# Represents a duration / difference.
#
#
# Add:
#
# date + timedelta
#
#
# Subtract:
#
# date - timedelta
#
#
# Difference:
#
# date2 - date1
#
#
# Common arguments:
#
# days
# seconds
# microseconds
# milliseconds
# minutes
# hours
# weeks
# ============================================================