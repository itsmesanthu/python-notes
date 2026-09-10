# ============================================================
# CONSTRUCTOR
# ============================================================
# A constructor is a special method that is automatically
# called when an object is created.
#
# In Python, the constructor is:
#
# __init__()
#
# It is mainly used to initialize object data.
# ============================================================


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating object
student1 = Student("santhu", 22)

print(student1.name)
print(student1.age)