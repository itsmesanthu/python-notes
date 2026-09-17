# ============================================================
# DECORATORS
# ============================================================
#
# A decorator is a function that modifies or extends
# the behavior of another function without changing
# its original code.
#
# Before learning decorators, we need to understand:
#
# 1. Functions can be stored in variables
# 2. Functions can be passed as arguments
# 3. Functions can be returned from another function
# 4. Inner functions
# ============================================================


# ============================================================
# 1. FUNCTION STORED IN A VARIABLE
# ============================================================

def greet():
    print("Hello")


message = greet

message()


# Output:
# Hello


# ============================================================
# 2. FUNCTION PASSED AS AN ARGUMENT
# ============================================================

def greet():
    print("Hello")


def call_function(func):
    func()


call_function(greet)


# Output:
# Hello


# ============================================================
# 3. ANOTHER EXAMPLE
# ============================================================

def add():
    print(10 + 20)


def execute(func):
    print("Executing function")
    func()


execute(add)


# Output:
# Executing function
# 30


# ============================================================
# 4. PASSING DIFFERENT FUNCTIONS
# ============================================================

def morning():
    print("Good Morning")


def evening():
    print("Good Evening")


def execute(func):
    func()


execute(morning)
execute(evening)


# Output:
# Good Morning
# Good Evening


# ============================================================
# 5. FUNCTION RETURNING A VALUE
# ============================================================

def add():
    return 10 + 20


def execute(func):
    result = func()
    print(result)


execute(add)


# Output:
# 30


# ============================================================
# QUICK REVISION
# ============================================================
#
# Python functions are first-class objects.
#
# This means a function can be:
#
# 1. Stored in a variable
# 2. Passed as an argument
# 3. Returned from another function
# 4. Stored inside a data structure
#
#
# Function as argument:
#
# def execute(func):
#     func()
#
# execute(greet)
# ============================================================