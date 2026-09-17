# ============================================================
# MULTIPLE DECORATORS
# ============================================================
#
# Python allows multiple decorators to be applied
# to the same function.
#
#
# Example:
#
# @decorator1
# @decorator2
# def function():
#     pass
#
#
# Decorators are applied from bottom to top.
# ============================================================


# ============================================================
# 1. TWO DECORATORS
# ============================================================

def decorator1(func):

    def wrapper():

        print("Decorator 1 - Before")

        func()

        print("Decorator 1 - After")

    return wrapper


def decorator2(func):

    def wrapper():

        print("Decorator 2 - Before")

        func()

        print("Decorator 2 - After")

    return wrapper


@decorator1
@decorator2
def greet():

    print("Hello")


greet()


# Output:
# Decorator 1 - Before
# Decorator 2 - Before
# Hello
# Decorator 2 - After
# Decorator 1 - After


# ============================================================
# 2. UNDERSTANDING DECORATOR ORDER
# ============================================================

@decorator1
@decorator2
def greet():
    print("Hello")


# Python interprets this approximately as:
#
# greet = decorator1(decorator2(greet))
#
#
# decorator2 is applied first.
# decorator1 is applied second.


# ============================================================
# 3. THREE DECORATORS
# ============================================================

def first(func):

    def wrapper():

        print("First Before")

        func()

        print("First After")

    return wrapper


def second(func):

    def wrapper():

        print("Second Before")

        func()

        print("Second After")

    return wrapper


def third(func):

    def wrapper():

        print("Third Before")

        func()

        print("Third After")

    return wrapper


@first
@second
@third
def greet():

    print("Hello Python")


greet()


# Output:
# First Before
# Second Before
# Third Before
# Hello Python
# Third After
# Second After
# First After


# ============================================================
# 4. PRACTICAL EXAMPLE
# ============================================================

def authentication(func):

    def wrapper():

        print("Checking authentication")

        func()

    return wrapper


def logging(func):

    def wrapper():

        print("Logging request")

        func()

    return wrapper


@authentication
@logging
def dashboard():

    print("Dashboard opened")


dashboard()


# Output:
# Checking authentication
# Logging request
# Dashboard opened


# ============================================================
# 5. DECORATOR ORDER
# ============================================================

# When we write:
#
# @A
# @B
# def function():
#     pass
#
#
# Python applies:
#
# function = A(B(function))
#
#
# Therefore:
#
# B is applied first.
# A is applied second.
# ============================================================


# ============================================================
# DECORATORS QUICK REVISION
# ============================================================

# Decorator
#     ↓
# Function that modifies another function.
#
#
# Inner Function
#     ↓
# Function defined inside another function.
#
#
# @decorator
#     ↓
# Shortcut for:
#
# function = decorator(function)
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
#
#
# Multiple Decorators
#     ↓
# More than one decorator can be applied.
#
#
# Example:
#
# @A
# @B
# def function():
#     pass
#
#
# Equivalent:
#
# function = A(B(function))
# ============================================================
