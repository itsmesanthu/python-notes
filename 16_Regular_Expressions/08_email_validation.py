# ============================================================
# EMAIL VALIDATION USING REGEX
# ============================================================

# Regular expressions can be used to check
# whether an email follows a basic expected pattern.
#
#
# Basic email pattern:
#
# username@domain.extension
# ============================================================

import re


# ============================================================
# 1. BASIC EMAIL VALIDATION
# ============================================================

email = "santhu@gmail.com"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

result = re.match(pattern, email)

if result:
    print("Valid email")
else:
    print("Invalid email")


# Output:
# Valid email

 
# ============================================================
# 2. INVALID EMAIL
# ============================================================

email = "santhu@gmail"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

result = re.match(pattern, email)

if result:
    print("Valid email")
else:
    print("Invalid email")


# Output:
# Invalid email


# ============================================================
# 3. CREATE A FUNCTION
# ============================================================

def validate_email(email):

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True

    return False


print(validate_email("santhu@gmail.com"))
print(validate_email("santhu@gmail"))


# Output:
# True
# False


# ============================================================
# 4. TEST MULTIPLE EMAILS
# ============================================================

emails = [
    "santhu@gmail.com",
    "test123@yahoo.com",
    "hello@company.in",
    "invalid@",
    "invalid.com",
    "user@gmail"
]

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

for email in emails:

    if re.match(pattern, email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")


# ============================================================
# 5. UNDERSTANDING THE PATTERN
# ============================================================

# ^
#     ↓
# Start of string
#
#
# [a-zA-Z0-9._%+-]+
#     ↓
# Username part
#
#
# @
#     ↓
# Required @ symbol
#
#
# [a-zA-Z0-9.-]+
#     ↓
# Domain name
#
#
# \.
#     ↓
# Literal dot
#
#
# [a-zA-Z]{2,}
#     ↓
# Extension with at least 2 letters
#
#
# $
#     ↓
# End of string
# ============================================================


# ============================================================
# QUICK REVISION
# ============================================================
#
# Email validation commonly checks:
#
# username
#     ↓
# @
#     ↓
# domain
#     ↓
# .
#     ↓
# extension
#
#
# Example:
#
# santhu@gmail.com
# ============================================================