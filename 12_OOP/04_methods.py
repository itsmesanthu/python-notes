# ============================================================
# METHOD
# ============================================================
# A method is a function defined inside a class.
#
# Methods are used to define the behavior of an object.
#
# An instance method normally takes self as its first parameter.
# ============================================================


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)


student1 = Student("Santhu", 22)

student1.introduce()