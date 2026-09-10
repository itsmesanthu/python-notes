# ============================================================
# CLASS
# ============================================================
# A class is a blueprint or template used to create objects.
#
# A class can contain:
# 1. Variables (data/attributes)
# 2. Methods (functions/behavior)
#
# Syntax:
#
# class ClassName:
#     # variables
#     # methods
# ============================================================


class Student:

    name = "Santhu"
    age = 22


# ============================================================
# OBJECT
# ============================================================
# An object is an instance of a class.
#
# We create an object using:
#
# object_name = ClassName()
# ============================================================


student1 = Student()

print(student1.name)
print(student1.age)