# ============================================================
# RECURSION
# ============================================================
# Recursion is a technique where a function calls itself
# to solve a smaller version of the same problem.
#
# Every recursive function needs:
#
# 1. Base Case
#    -> Stops the recursion.
#
# 2. Recursive Case
#    -> Calls the function again with a smaller/simpler input.
# ============================================================


def countdown(number):

    # Base case
    if number == 0:
        return

    print(number)

    # Recursive case
    countdown(number - 1)


countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1