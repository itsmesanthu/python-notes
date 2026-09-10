# ============================================================
# INSTANCE VARIABLES
# ============================================================
# Instance variables are variables that belong to a particular
# object.
#
# They are usually created using self inside the constructor.
#
# Every object can have different values.
# ============================================================


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Santhu", 22)
student2 = Student("Tanu", 21)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)