# ============================================================
# CONDITIONAL PRACTICE
# ============================================================

# 1. Check whether a number is positive, negative, or zero.

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
