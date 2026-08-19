# ============================================================
# RAISE
# ============================================================
# The raise keyword allows us to manually generate
# an exception.
# ============================================================


age = 15

if age < 18:
    raise ValueError("Age must be 18 or above.")

print("You are eligible.")