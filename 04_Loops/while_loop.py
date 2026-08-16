# =========================================
# WHILE LOOP IN PYTHON
# =========================================
print("WHILE LOOP IN PYTHON\n")
print("Definition:")
print("A while loop repeatedly executes a block of code as long as the condition is True.\n")
# Example 1
print("Example 1 : Printing numbers from 1 to 5\n")
i = 1
while i <= 5:
    print(i)
    i += 1
print("\n----------------------------\n")
# Example 2
print("Example 2 : Multiplication Table\n")
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
print("\nProgram Finished Successfully!")