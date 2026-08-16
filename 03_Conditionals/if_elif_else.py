# ============================================================
# IF-ELIF-ELSE STATEMENT
# ============================================================
# Used when we need to check multiple conditions.
#
# if      -> checks the first condition
# elif    -> checks another condition
# else    -> executes when none of the conditions are True
# ============================================================


marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")