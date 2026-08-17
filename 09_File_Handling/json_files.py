# ============================================================
# JSON FILES
# ============================================================

import json


student = {
    "name": "Santhosh",
    "age": 25,
    "skills": ["Python", "SQL"]
}


# ------------------------------------------------------------
# WRITE PYTHON DATA INTO JSON
# ------------------------------------------------------------

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)


# ------------------------------------------------------------
# READ JSON
# ------------------------------------------------------------

with open("student.json", "r") as file:

    data = json.load(file)

    print(data)
    print(data["name"])