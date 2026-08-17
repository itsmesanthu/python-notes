# ============================================================
# FACTORIAL USING RECURSION
# ============================================================
# Factorial:
#
# 5! = 5 × 4 × 3 × 2 × 1
#    = 120
#
# Recursive formula:
#
# n! = n × (n - 1)!
#
# Base case:
#
# 0! = 1
# ============================================================


def factorial(number):

    # Base case
    if number == 0:
        return 1

    # Recursive case
    return number * factorial(number - 1)


print(factorial(5))
# 120


# factorial(5)
#     ↓
# 5 × factorial(4)
#         ↓
#         4 × factorial(3)
#                 ↓
#                 3 × factorial(2)
#                         ↓
#                         2 × factorial(1)
#                                 ↓
#                                 1 × factorial(0)
#                                         ↓
#                                         1