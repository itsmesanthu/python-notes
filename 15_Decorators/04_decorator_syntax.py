# ============================================================
# DECORATOR SYNTAX
# ============================================================
#
# Python provides the @ symbol to apply a decorator.
#
#
# Instead of:
#
# greet = decorator(greet)
#
# We can write:
#
# @decorator
# def greet():
#     ...
# ============================================================


# ============================================================
# 1. BASIC @ DECORATOR
# ============================================================

def decorator(func):

    def wrapper():

        print("Before function")

        func()

        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()


# Output:
# Before function
# Hello
# After function


# ============================================================
# 2. DECORATOR WITH ANOTHER FUNCTION
# ============================================================

def decorator(func):

    def wrapper():

        print("Starting program")

        func()

        print("Program completed")

    return wrapper


@decorator
def welcome():
    print("Welcome to Python")


welcome()


# Output:
# Starting program
# Welcome to Python
# Program completed


# ============================================================
# 3. MULTIPLE FUNCTIONS
# ============================================================

def decorator(func):

    def wrapper():

        print("-----")

        func()

        print("-----")

    return wrapper


@decorator
def login():
    print("Login")


@decorator
def logout():
    print("Logout")


login()
logout()


# Output:
# -----
# Login
# -----
# -----
# Logout
# -----


# ============================================================
# 4. DECORATOR WITH FUNCTION RETURN VALUE
# ============================================================

def decorator(func):

    def wrapper():

        print("Calculating...")

        result = func()

        return result

    return wrapper


@decorator
def add():
    return 10 + 20


result = add()

print(result)


# Output:
# Calculating...
# 30


# ============================================================
# 5. @decorator VS NORMAL SYNTAX
# ============================================================

# Using @:

@decorator
def greet():
    print("Hello")


# Equivalent to:
#
# def greet():
#     print("Hello")
#
# greet = decorator(greet)


# ============================================================
# QUICK REVISION
# ============================================================
#
# @decorator
#     ↓
# Python automatically passes the function
# to the decorator.
#
#
# @decorator
# def greet():
#     pass
#
#
# Is equivalent to:
#
# def greet():
#     pass
#
# greet = decorator(greet)
# ============================================================