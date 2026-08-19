# ============================================================
# ELSE
# ============================================================
# The else block executes only when the try block
# completes successfully.
# ============================================================


try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)