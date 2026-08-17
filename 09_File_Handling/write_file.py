# ============================================================
# WRITING TO A FILE
# ============================================================
# "w" mode creates a file if it doesn't exist.
#
# IMPORTANT:
# If the file already exists, "w" mode OVERWRITES its content.
# ============================================================


file = open("example.txt", "w")

file.write("Hello, Python!")

file.close()