# ============================================================
# FILE METHODS
# ============================================================


with open("example.txt", "r") as file:

    # --------------------------------------------------------
    # read()
    # --------------------------------------------------------
    # Reads the complete file.

    content = file.read()

    print(content)


with open("example.txt", "r") as file:

    # --------------------------------------------------------
    # readline()
    # --------------------------------------------------------
    # Reads one line.

    line = file.readline()

    print(line)


with open("example.txt", "r") as file:

    # --------------------------------------------------------
    # readlines()
    # --------------------------------------------------------
    # Reads all lines and returns them as a list.

    lines = file.readlines()

    print(lines)