# ============================================================
# CSV FILES
# ============================================================

import csv


# ------------------------------------------------------------
# WRITING CSV
# ------------------------------------------------------------

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])

    writer.writerow(["Santhosh", 25, "Python"])
    writer.writerow(["Alex", 24, "Java"])


# ------------------------------------------------------------
# READING CSV
# ------------------------------------------------------------

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)