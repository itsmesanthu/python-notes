# ============================================================
# BASIC DECORATOR
# ============================================================
#
# A decorator is a function that takes another function
# as an argument and adds extra behavior to it.
#
#
# Basic flow:
#
# Original Function
#       ↓
# Decorator
#       ↓
# Modified Function
# ============================================================


# ============================================================
# 1. BASIC DECORATOR
# ============================================================

def decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


def greet():
    print("Hello")


greet = decorator(greet)

greet()


# Output:
# Before function
# Hello
# After function


# ============================================================
# 2. UNDERSTANDING THE FLOW
# ============================================================

def decorator(func):

    def wrapper():

        print("Starting")

        func()

        print("Ending")

    return wrapper


def greet():
    print("Hello Santhu")


greet = decorator(greet)

greet()


# Output:
# Starting
# Hello Santhu
# Ending


# ============================================================
# 3. DECORATOR WITHOUT @ SYMBOL
# ============================================================

def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


def welcome():
    print("Welcome")


welcome = decorator(welcome)

welcome()


# ============================================================
# 4. DECORATOR WITH DIFFERENT FUNCTION
# ============================================================

def decorator(func):

    def wrapper():

        print("----- Start -----")

        func()

        print("----- End -----")

    return wrapper


def login():
    print("User Login")


login = decorator(login)

login()


# Output:
# ----- Start -----
# User Login
# ----- End -----


# ============================================================
# QUICK REVISION
# ============================================================
#
# Decorator:
#     ↓
# Takes a function as input.
#
#     ↓
#
# Adds extra behavior.
#
#     ↓
#
# Returns a new function.
#
#
# Basic structure:
#
# def decorator(func):
#
#     def wrapper():
#         # extra code
#         func()
#         # extra code
#
#     return wrapper
# ============================================================