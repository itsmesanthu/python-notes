# =========================================
# LOOPS IN PYTHON
# =========================================
print("LOOPS IN PYTHON\n")
# -----------------------------------------
# DEFINITION
# -----------------------------------------
print("Definition:")
print("A loop is used to execute a block of code repeatedly until a condition is satisfied.\n")
print("Types of Loops in Python:")
print("1. for loop")
print("2. while loop\n")
# -----------------------------------------
# FOR LOOP DEFINITION
# -----------------------------------------
print("FOR LOOP:")
print("A for loop is used to iterate over a sequence like string, list, or range.\n")
# =========================================
# PROGRAM 1 : MULTIPLICATION TABLE
# =========================================
num = int(input("Enter a number to print multiplication table: "))
print("\nMultiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("\n--------------------------------------\n")
# -----------------------------------------
# STRING LOOP
# -----------------------------------------
print("Example: Loop with String\n")
word = input("Enter a word: ")
print("\nCharacters in the word:\n")
for letter in word:
    print(letter)
print("\n--------------------------------------\n")
# -----------------------------------------
# COUNT CHARACTERS USING LOOP
# -----------------------------------------
print("Counting characters using loop\n")
count = 0
for letter in word:
    count = count + 1
print("Total characters:", count)
print("\nProgram Completed Successfully!")