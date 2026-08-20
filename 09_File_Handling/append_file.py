# ============================================================
# APPENDING TO A FILE
# ============================================================
# "a" mode adds content to the end of the existing file.
# Existing content is not removed.
# ============================================================


file = open("example.txt", "a")

file.write("\nThis line was added later.")

file.close()