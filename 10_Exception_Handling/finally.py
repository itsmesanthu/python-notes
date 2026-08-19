# ============================================================
# FINALLY
# ============================================================
# The finally block executes whether an exception occurs
# or not.
#
# It is commonly used for cleanup operations.
# ============================================================


try:
    file = open("example.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Execution completed.")