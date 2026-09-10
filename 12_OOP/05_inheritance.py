# ============================================================
# INHERITANCE
# ============================================================
# Inheritance is an OOP concept where one class can acquire
# the properties and methods of another class.
#
# It is mainly used for:
# 1. Code reusability
# 2. Extending existing classes
# 3. Creating relationships between classes
#
#
# Parent Class / Base Class
# -------------------------
# The class whose properties and methods are inherited.
#
#
# Child Class / Derived Class
# ---------------------------
# The class that inherits from another class.
#
#
# Syntax:
#
# class ChildClass(ParentClass):
#     # child class code
# ============================================================


# ============================================================
# 1. BASIC INHERITANCE
# ============================================================
# A child class can access methods from its parent class.
# ============================================================


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()      # Parent method
dog.bark()     # Child method


# Output:
# Animal is eating
# Dog is barking


# ============================================================
# 2. PARENT CLASS
# ============================================================
# A parent class is the class whose properties and methods
# are inherited by another class.
# ============================================================


class Vehicle:

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


# ============================================================
# 3. CHILD CLASS
# ============================================================
# A child class inherits from a parent class.
#
# Car inherits from Vehicle.
# ============================================================


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


car = Car()

car.start()    # Inherited method
car.stop()     # Inherited method
car.drive()    # Child method


# ============================================================
# 4. CODE REUSABILITY
# ============================================================
# One of the main advantages of inheritance is code reuse.
#
# Instead of writing the same methods in every class,
# we define common functionality in a parent class.
# ============================================================


class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.sleep()
dog.bark()

cat.eat()
cat.sleep()
cat.meow()


# ============================================================
# 5. INHERITING CONSTRUCTOR
# ============================================================
# If the child class does not have its own __init__(),
# Python can use the constructor of the parent class.
# ============================================================


class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

student = Student("Tanu")
print(student.name)


# Output:
# Tanu


# ============================================================
# 6. CHILD CLASS CONSTRUCTOR
# ============================================================
# A child class can define its own constructor.
#
# When a child has its own __init__(), the parent constructor
# is not automatically called.
# ============================================================


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student = Student("Tanu", 85)

print(student.name)
print(student.marks)


# ============================================================
# 7. super()
# ============================================================
# super() is used to access the parent class.
#
# It is commonly used to:
#
# 1. Call the parent constructor
# 2. Call the parent method
# ============================================================


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):

        super().__init__(name)

        self.marks = marks


student = Student("Tanu", 85)

print(student.name)
print(student.marks)


# ============================================================
# 8. METHOD OVERRIDING
# ============================================================
# Method overriding happens when the child class defines
# a method with the same name as the parent class.
#
# The child version replaces the inherited version when
# called using the child object.
# ============================================================


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


dog = Dog()

dog.sound()


# Output:
# Dog says Woof


# ============================================================
# 9. CALLING PARENT METHOD USING super()
# ============================================================
# If the child overrides a method but still wants to execute
# the parent version, we can use super().
# ============================================================


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        super().sound()

        print("Dog says Woof")


dog = Dog()

dog.sound()


# Output:
# Animal makes a sound
# Dog says Woof


# ============================================================
# 10. SINGLE INHERITANCE
# ============================================================
# One parent class and one child class.
#
#
# Parent
#   ↓
# Child
# ============================================================


class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()


# ============================================================
# 11. MULTIPLE INHERITANCE
# ============================================================
# A child class inherits from more than one parent class.
#
#
# Parent 1       Parent 2
#      \           /
#       \         /
#          Child
# ============================================================


class Father:

    def father_property(self):
        print("Father's property")


class Mother:

    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):

    def child_property(self):
        print("Child's property")


child = Child()

child.father_property()
child.mother_property()
child.child_property()


# ============================================================
# 12. MULTILEVEL INHERITANCE
# ============================================================
# In multilevel inheritance, inheritance happens through
# multiple levels.
#
#
# Grandparent
#      ↓
#    Parent
#      ↓
#    Child
# ============================================================


class Grandfather:

    def grandfather_method(self):
        print("Grandfather method")


class Father(Grandfather):

    def father_method(self):
        print("Father method")


class Son(Father):

    def son_method(self):
        print("Son method")


son = Son()

son.grandfather_method()
son.father_method()
son.son_method()


# ============================================================
# 13. HIERARCHICAL INHERITANCE
# ============================================================
# Multiple child classes inherit from the same parent class.
#
#
#             Parent
#             /    \
#            /      \
#         Child1   Child2
# ============================================================


class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()


# ============================================================
# 14. HYBRID INHERITANCE
# ============================================================
# Hybrid inheritance is a combination of two or more
# types of inheritance.
#
#
#             Animal
#             /    \
#            /      \
#          Dog      Cat
#            \      /
#             \    /
#              Pet
# ============================================================


class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")


class Pet(Dog, Cat):

    def play(self):
        print("Playing")


pet = Pet()

pet.eat()
pet.bark()
pet.meow()
pet.play()


# ============================================================
# 15. METHOD RESOLUTION ORDER (MRO)
# ============================================================
# MRO stands for Method Resolution Order.
#
# It defines the order in which Python searches for a method
# when multiple inheritance is used.
#
# We can see the MRO using:
#
# ClassName.mro()
#
# or:
#
# ClassName.__mro__
# ============================================================


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


d = D()

d.show()

print(D.mro())


# Python searches approximately:
#
# D
# ↓
# B
# ↓
# C
# ↓
# A
# ↓
# object


# ============================================================
# 16. DIAMOND PROBLEM
# ============================================================
# The diamond problem can occur in multiple inheritance.
#
#
#             A
#            / \
#           B   C
#            \ /
#             D
#
# Python uses MRO to decide which method should be executed.
# ============================================================


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


d = D()

d.show()

print(D.mro())


# Output:
# B
#
# Because Python finds B before C according to the MRO.


# ============================================================
# 17. isinstance()
# ============================================================
# isinstance() checks whether an object is an instance of
# a particular class.
#
# Syntax:
#
# isinstance(object, ClassName)
# ============================================================


class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


# Output:
# True
# True
#
# Dog inherits from Animal.
# Therefore, a Dog object is also considered an Animal.


# ============================================================
# 18. issubclass()
# ============================================================
# issubclass() checks whether one class is a subclass of
# another class.
#
# Syntax:
#
# issubclass(ChildClass, ParentClass)
# ============================================================


class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))


# Output:
# True
# False


# ============================================================
# 19. object CLASS
# ============================================================
# Every Python class ultimately inherits from object.
#
# Example:
#
# class Animal:
#     pass
#
# is conceptually similar to:
#
# class Animal(object):
#     pass
# ============================================================


class Animal:
    pass


print(Animal.mro())


# Output will be similar to:
#
# [<class '__main__.Animal'>, <class 'object'>]


# ============================================================
# 20. INHERITANCE + POLYMORPHISM
# ============================================================
# Inheritance and polymorphism are commonly used together.
#
# The parent defines a common method and child classes
# provide different implementations.
# ============================================================


class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Woof")


class Cat(Animal):

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# Output:
# Woof
# Meow


# ============================================================
# 21. COMPLETE INHERITANCE EXAMPLE
# ============================================================
# This example combines:
#
# 1. Parent class
# 2. Child class
# 3. Constructor
# 4. Instance variables
# 5. Inheritance
# 6. super()
# 7. Method overriding
# ============================================================


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def __init__(self, name, breed):

        super().__init__(name)

        self.breed = breed

    def sound(self):

        print(self.name, "says Woof")

    def bark(self):

        print(self.name, "is barking")


dog = Dog("Bruno", "Labrador")

print("Name:", dog.name)
print("Breed:", dog.breed)

dog.eat()
dog.sound()
dog.bark()


# ============================================================
# INHERITANCE QUICK REVISION
# ============================================================
#
# Inheritance
#     ↓
# Reuse properties and methods from another class.
#
#
# Parent / Base Class
#     ↓
# Class being inherited from.
#
#
# Child / Derived Class
#     ↓
# Class that inherits.
#
#
# Single Inheritance
#     ↓
# A → B
#
#
# Multiple Inheritance
#     ↓
# A + B → C
#
#
# Multilevel Inheritance
#     ↓
# A → B → C
#
#
# Hierarchical Inheritance
#     ↓
#     A
#    / \
#   B   C
#
#
# Hybrid Inheritance
#     ↓
# Combination of inheritance types.
#
#
# Method Overriding
#     ↓
# Child provides its own implementation of a parent method.
#
#
# super()
#     ↓
# Access parent constructor or method.
#
#
# MRO
#     ↓
# Method Resolution Order.
#
#
# isinstance()
#     ↓
# Checks whether an object belongs to a class.
#
#
# issubclass()
#     ↓
# Checks whether a class inherits from another class.
#
#
# object
#     ↓
# Ultimate base class of Python.
# ============================================================