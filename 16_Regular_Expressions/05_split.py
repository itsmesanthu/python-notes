# ============================================================
# re.split()
# ============================================================

# re.split() splits a string whenever the pattern
# is found.
#
#
# Syntax:
#
# re.split(pattern, string)
# ============================================================

import re


# ============================================================
# 1. SPLIT BY SPACE
# ============================================================

text = "Python is easy"

result = re.split(r"\s+", text)

print(result)


# Output:
# ['Python', 'is', 'easy']


# ============================================================
# 2. SPLIT BY COMMA
# ============================================================

text = "Python,Java,C,C++"

result = re.split(",", text)

print(result)


# Output:
# ['Python', 'Java', 'C', 'C++']


# ============================================================
# 3. SPLIT BY COMMA OR SPACE
# ============================================================

text = "Python, Java, C, C++"

result = re.split(r"[, ]+", text)

print(result)


# Output:
# ['Python', 'Java', 'C', 'C++']


# ============================================================
# 4. SPLIT USING MULTIPLE DELIMITERS
# ============================================================

text = "Python-Java,C;C++"

result = re.split(r"[-,;]", text)

print(result)


# Output:
# ['Python', 'Java', 'C', 'C++']


# ============================================================
# 5. LIMIT SPLITS
# ============================================================

text = "Python-Java-C-C++"

result = re.split("-", text, maxsplit=2)

print(result)


# Output:
# ['Python', 'Java', 'C-C++']


# ============================================================
# QUICK REVISION
# ============================================================
#
# re.split()
#     ↓
# Splits a string based on a pattern.
#
#
# Example:
#
# re.split(r"[,;]", text)
#
# Splits using:
# comma
# semicolon
# ============================================================