# ============================================================
# NESTED IF
# ============================================================
# A nested if means using one if statement inside another if
# statement.
# ============================================================


age = 25
has_license = True

if age >= 18:
    print("You are old enough to drive.")

    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are not old enough to drive.")
    