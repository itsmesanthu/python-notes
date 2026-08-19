# ============================================================
# EXCEPTION HANDLING
# ============================================================
# Exception handling allows us to handle runtime errors
# without crashing the entire program.
#
# Main keywords:
#
# try     -> Code that might cause an error
# except  -> Handles the error
# else    -> Runs when there is no error
# finally -> Runs whether there is an error or not
# ============================================================


try:
    number = int(input("Enter a number: "))

    result = 10 / number

    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")