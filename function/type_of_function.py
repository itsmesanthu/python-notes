# =========================================
# CLOSURE 
# =========================================

print("CLOSURE \n")

print("Definition:")
print("A closure is a function inside another function")
print("that remembers the outer function variable.\n")


def outer(x):

    def inner(y):
        return x + y

    return inner

result = outer(10)

print("Result is:", result(5))

print("\nProgram Finished Successfully!")
print("---------------------------------\n")

# =========================================
# DECORATOR 
# =========================================

print("DECORATOR \n")

print("Definition:")
print("A decorator is used to add extra functionality")
print("to another function.\n")


def decorator(func):

    def wrapper():
        print("Before Function Execution")

        func()

        print("After Function Execution")

    return wrapper


@decorator
def hello():
    print("Hello Python")


hello()

print("\nProgram Finished Successfully!")
print("---------------------------------\n")

# =========================================
# LAMBDA FUNCTION 
# =========================================

print("LAMBDA FUNCTION \n")

print("Definition:")
print("A lambda function is a small anonymous function.\n")

square = lambda x: x * x

print("Square is:", square(5))
print("\nProgram Finished Successfully!")
print("---------------------------------\n")

# =========================================
# RECURSIVE FUNCTION IN PYTHON
# =========================================

print("RECURSIVE FUNCTION IN PYTHON\n")

print("Definition:")
print("A recursive function calls itself again and again.\n")


def countdown(n):

    if n == 0:
        print("Completed")
        return
    print(n)
    countdown(n - 1)
countdown(5)

print("\nProgram Finished Successfully!")
print("---------------------------------\n")
# =========================================
# GENERATOR FUNCTION IN PYTHON
# =========================================

print("GENERATOR FUNCTION IN PYTHON\n")

print("Definition:")
print("A generator function uses yield keyword")
print("to generate values one by one.\n")


def numbers():

    yield 1
    yield 2
    yield 3


for i in numbers():
    print(i)

print("\nProgram Finished Successfully!")
print("---------------------------------\n")