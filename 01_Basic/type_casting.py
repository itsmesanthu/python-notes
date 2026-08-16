# =========================================
# TYPE CASTING (TYPE CONVERSION) IN PYTHON
# =========================================

print("TYPE CASTING IN PYTHON\n")

# -----------------------------------------
# DEFINITION
# -----------------------------------------
print("Definition:")
print("Type casting is converting one data type into another data type.\n")

# -----------------------------------------
# WHY TYPE CASTING IS NEEDED
# -----------------------------------------
print("Why Type Casting is Needed:")
print("input() function always takes data as string.")
print("To perform calculations, we convert data types.\n")

print("Example Concept:")
print('"10" + 5  -> Error (string + integer not allowed)\n')

# =========================================
# TYPES OF TYPE CASTING
# =========================================

print("TYPES OF TYPE CASTING\n")

# Implicit Type Casting
print("1. Implicit Type Casting (Automatic Conversion)")

a = 10      # int
b = 2.5     # float
c = a + b   # Python converts int to float automatically

print("Result:", c)
print("Data Type:", type(c), "\n")

# Explicit Type Casting
print("2. Explicit Type Casting (Manual Conversion)")

d = "25"
e = int(d)

print("Converted Value:", e)
print("Data Type:", type(e), "\n")

# =========================================
# TYPE CASTING FUNCTIONS
# =========================================

print("TYPE CASTING FUNCTIONS\n")

# int() Function
print("1. int() → Convert to Integer")

x = int("100")
print("Value:", x)
print("Data Type:", type(x), "\n")

# float() Function
print("2. float() → Convert to Float")

y = float("10.5")
print("Value:", y)
print("Data Type:", type(y), "\n")

# str() Function
print("3. str() → Convert to String")

z = str(50)
print("Value:", z)
print("Data Type:", type(z), "\n")

# bool() Function
print("4. bool() → Convert to Boolean")

print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool(5):", bool(5))
print("bool('Python'):", bool("Python"))

print("\nRule:")
print("0  -> False")
print("Any non-zero or non-empty value -> True\n")

# =========================================
# REAL WORLD EXAMPLE
# =========================================

print("REAL WORLD EXAMPLE\n")

marks = int(input("Enter your marks: "))
bonus = 5

total = marks + bonus

print("Total Marks after bonus:", total)
