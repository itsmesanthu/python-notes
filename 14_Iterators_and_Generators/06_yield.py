# ============================================================
# yield
# ============================================================

# yield is used inside a generator function.
#
# Unlike return, yield does not terminate the function
# permanently.
#
# It pauses the function and remembers its state.
#
# When next() is called again, execution continues
# from where it stopped.
# ============================================================


# ============================================================
# 1. BASIC yield
# ============================================================

def numbers():

    yield 10
    yield 20
    yield 30


result = numbers()

print(next(result))
print(next(result))
print(next(result))


# Output:
# 10
# 20
# 30


# ============================================================
# 2. yield PAUSES THE FUNCTION
# ============================================================

def test():

    print("Start")

    yield 10

    print("Middle")

    yield 20

    print("End")


result = test()

print(next(result))
print(next(result))
print(next(result))


# Output:
# Start
# 10
# Middle
# 20
# End
# StopIteration


# ============================================================
# 3. yield VS return
# ============================================================

# return:
#     ↓
# Ends the function.
#
#
# yield:
#     ↓
# Pauses the function and resumes later.
# ============================================================


# ============================================================
# 4. GENERATOR WITH LOOP
# ============================================================

def even_numbers():

    for num in range(1, 11):

        if num % 2 == 0:
            yield num


for num in even_numbers():
    print(num)


# Output:
# 2
# 4
# 6
# 8
# 10


# ============================================================
# 5. INFINITE GENERATOR
# ============================================================

def count():

    number = 1

    while True:

        yield number

        number += 1


result = count()

print(next(result))
print(next(result))
print(next(result))
print(next(result))


# Output:
# 1
# 2
# 3
# 4


# ============================================================
# QUICK REVISION
# ============================================================

# yield
#     ↓
# Pauses a generator function.
#
#
# next()
#     ↓
# Resumes the generator.
#
#
# yield remembers:
#     ↓
# 1. Current position
# 2. Local variables
# 3. Function state
# ============================================================