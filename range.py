# =========================================
# RANGE FUNCTION IN PYTHON
# =========================================
print("RANGE FUNCTION IN PYTHON\n")
print("Definition:")
print("range() is used to generate a sequence of numbers.")
print("It is commonly used with loops.\n")
# -----------------------------------------
# Example 1 : range(stop)
# -----------------------------------------
print("Example 1 : range(stop)")
print("This generates numbers from 0 to stop-1\n")
for i in range(5):
    print(i)
print("\n----------------------------\n")
# -----------------------------------------
# Example 2 : range(start, stop)
# -----------------------------------------
print("Example 2 : range(start, stop)")
print("This generates numbers from start to stop-1\n")
for i in range(2, 7):
    print(i)
print("\n----------------------------\n")
# -----------------------------------------
# Example 3 : range(start, stop, step)
# -----------------------------------------
print("Example 3 : range(start, stop, step)")
print("This generates numbers with a step increment\n")
for i in range(1, 10, 2):
    print(i)
print("\nProgram Finished Successfully!")