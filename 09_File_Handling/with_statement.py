# ============================================================
# WITH STATEMENT
# ============================================================
# The with statement automatically closes the file
# after the block finishes.
#
# This is safer and cleaner than manually calling close().
# ============================================================


with open("example.txt", "r") as file:

    content = file.read()

    print(content)


# The file is automatically closed here.