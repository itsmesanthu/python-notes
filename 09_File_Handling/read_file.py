# ============================================================
# READING A FILE
# ============================================================

# Open the file in read mode.

file = open("example.txt", "r")

# Read the complete file.
content = file.read()
print(content)

# Close the file.

file.close()