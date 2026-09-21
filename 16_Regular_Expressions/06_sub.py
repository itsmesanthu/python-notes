# ============================================================
# re.sub()
# ============================================================

# re.sub() is used to replace matching text
# with another value.
#
#
# Syntax:
#
# re.sub(pattern, replacement, string)
# ============================================================

import re


# ============================================================
# 1. BASIC REPLACEMENT
# ============================================================

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)


# Output:
# I like Python


# ============================================================
# 2. REPLACE NUMBERS
# ============================================================

text = "My phone number is 9876543210"

result = re.sub(r"\d", "*", text)

print(result)


# Output:
# My phone number is **********


# ============================================================
# 3. REMOVE NUMBERS
# ============================================================

text = "Python123"

result = re.sub(r"\d", "", text)

print(result)


# Output:
# Python


# ============================================================
# 4. REMOVE EXTRA SPACES
# ============================================================

text = "Python     is     easy"

result = re.sub(r"\s+", " ", text)

print(result)


# Output:
# Python is easy


# ============================================================
# 5. REPLACE MULTIPLE CHARACTERS
# ============================================================

text = "Python-Java-C"

result = re.sub(r"[-]", ",", text)

print(result)


# Output:
# Python,Java,C


# ============================================================
# 6. REMOVE SPECIAL CHARACTERS
# ============================================================

text = "Python@123!"

result = re.sub(r"[^a-zA-Z0-9]", "", text)

print(result)


# Output:
# Python123


# ============================================================
# QUICK REVISION
# ============================================================
#
# re.sub()
#     ↓
# Replaces matching patterns.
#
#
# Example:
#
# re.sub("old", "new", text)
#
#
# It can also be used to:
#
# 1. Remove numbers
# 2. Remove special characters
# 3. Replace spaces
# 4. Clean text
# ============================================================