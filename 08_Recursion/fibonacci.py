# ============================================================
# FIBONACCI USING RECURSION
# ============================================================
# Fibonacci sequence:
#
# 0, 1, 1, 2, 3, 5, 8, 13...
#
# Each number is the sum of the previous two numbers.
#
# F(n) = F(n - 1) + F(n - 2)
# ============================================================


def fibonacci(number):

    # Base cases
    if number == 0:
        return 0

    if number == 1:
        return 1

    # Recursive case
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(6))
# 8
