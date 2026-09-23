# ============================================================
# DATE AND TIME FORMATTING
# ============================================================

# strftime() is used to convert a date/time object
# into a formatted string.
#
#
# Syntax:
#
# datetime_object.strftime(format)
# ============================================================

from datetime import datetime


# ============================================================
# 1. BASIC FORMATTING
# ============================================================

now = datetime.now()

result = now.strftime("%Y-%m-%d")

print(result)


# Example:
# 2026-09-23


# ============================================================
# 2. DAY-MONTH-YEAR
# ============================================================

now = datetime.now()

result = now.strftime("%d-%m-%Y")

print(result)


# Example:
# 23-09-2026


# ============================================================
# 3. DAY / MONTH / YEAR
# ============================================================

result = now.strftime("%d/%m/%Y")

print(result)


# Example:
# 23/09/2026


# ============================================================
# 4. TIME FORMAT
# ============================================================

result = now.strftime("%H:%M:%S")

print(result)


# Example:
# 17:30:15


# ============================================================
# 5. 12-HOUR FORMAT
# ============================================================

result = now.strftime("%I:%M:%S %p")

print(result)


# Example:
# 05:30:15 PM


# ============================================================
# 6. FULL DATE
# ============================================================

result = now.strftime("%A, %d %B %Y")

print(result)


# Example:
# Wednesday, 23 September 2026


# ============================================================
# 7. COMMON FORMAT CODES
# ============================================================

# %Y
#     ↓
# Four-digit year
#
# %y
#     ↓
# Two-digit year
#
# %m
#     ↓
# Month number
#
# %d
#     ↓
# Day of month
#
# %H
#     ↓
# Hour (24-hour)
#
# %I
#     ↓
# Hour (12-hour)
#
# %M
#     ↓
# Minute
#
# %S
#     ↓
# Second
#
# %p
#     ↓
# AM / PM
#
# %A
#     ↓
# Full weekday name
#
# %a
#     ↓
# Short weekday name
#
# %B
#     ↓
# Full month name
#
# %b
#     ↓
# Short month name
# ============================================================


# ============================================================
# QUICK REVISION
# ============================================================

# strftime()
#     ↓
# Date/time object → String
#
#
# Example:
#
# now.strftime("%d-%m-%Y")
#
# Output:
#
# 23-09-2026
# ============================================================