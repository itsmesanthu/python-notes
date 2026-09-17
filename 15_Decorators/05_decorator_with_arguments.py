# ============================================================
# DECORATOR WITH ARGUMENTS
# ============================================================
#
# If the decorated function accepts arguments,
# the wrapper should also accept arguments.
#
#
# We commonly use:
#
# *args
# **kwargs
#
# to handle different numbers of arguments.
# ============================================================


# ============================================================
# 1. DECORATOR WITH ONE ARGUMENT
# ============================================================

def decorator(func):

    def wrapper(name):

        print("Before function")

        func(name)

        print("After function")

    return wrapper


@decorator
def greet(name):

    print("Hello", name)


greet("Santhu")


# Output:
# Before function
# Hello Santhu
# After function


# ============================================================
# 2. DECORATOR WITH TWO ARGUMENTS
# ============================================================

def decorator(func):

    def wrapper(a, b):

        print("Adding numbers")

        result = func(a, b)

        print("Result:", result)

    return wrapper


@decorator
def add(a, b):

    return a + b


add(10, 20)


# Output:
# Adding numbers
# Result: 30


# ============================================================
# 3. USING *args
# ============================================================

def decorator(func):

    def wrapper(*args):

        print("Function started")

        result = func(*args)

        print("Function ended")

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


result = add(10, 20)

print(result)


# Output:
# Function started
# Function ended
# 30


# ============================================================
# 4. USING **kwargs
# ============================================================

def decorator(func):

    def wrapper(**kwargs):

        print("Function called")

        result = func(**kwargs)

        return result

    return wrapper


@decorator
def student(name, age):

    print("Name:", name)
    print("Age:", age)


student(name="Santhu", age=21)


# Output:
# Function called
# Name: Santhu
# Age: 21


# ============================================================
# 5. USING *args AND **kwargs
# ============================================================

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


result = add(10, 20)

print(result)


# Output:
# Before
# After
# 30


# ============================================================
# 6. PRACTICAL EXAMPLE
# ============================================================

def login_required(func):

    def wrapper(username):

        if username == "Santhu":

            func(username)

        else:

            print("Access denied")

    return wrapper


@login_required
def dashboard(username):

    print("Welcome to dashboard,", username)


dashboard("Santhu")
dashboard("Raj")


# Output:
# Welcome to dashboard, Santhu
# Access denied


# ============================================================
# QUICK REVISION
# ============================================================
#
# Decorator with arguments:
#
# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#
#         result = func(*args, **kwargs)
#
#         return result
#
#     return wrapper
#
#
# *args
#     ↓
# Handles positional arguments.
#
#
# **kwargs
#     ↓
# Handles keyword arguments.
# ============================================================