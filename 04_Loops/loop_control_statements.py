# =========================================
# LOOP CONTROL STATEMENTS IN PYTHON
# =========================================

print("LOOP CONTROL STATEMENTS\n")

# BREAK
print("Break Example")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n----------------------\n")

# CONTINUE
print("Continue Example")
for i in range(1, 6):
    if i == 4:
        continue
    print(i)

print("\n----------------------\n")

# PASS
print("Pass Example")
for i in range(1, 6):
    if i == 4:
        pass
    print(i)

print("\nProgram Finished Successfully!")