# ============================================================
# BASE CASE
# ============================================================
# The base case is the condition that stops recursion.
#
# Without a proper base case, the function keeps calling
# itself until Python raises a RecursionError.
# ============================================================


def count(number):

    if number == 0:
        print("Done")
        return

    print(number)

    count(number - 1)


count(5)
