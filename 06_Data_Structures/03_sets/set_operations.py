# ==========================================
# SET OPERATIONS
# ==========================================


A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}


print("Set A:", A)
print("Set B:", B)


# ==========================================
# 1. UNION
# ==========================================
# Union combines elements from both sets.
#
# Duplicate values are removed.
#
# A | B
#
# OR
#
# A.union(B)


union_result = A | B

print("\nUnion:", union_result)


union_result = A.union(B)

print("Union using method:", union_result)


# Result:
# {1, 2, 3, 4, 5, 6, 7, 8}


# ==========================================
# 2. INTERSECTION
# ==========================================
# Intersection gives common elements
# between two sets.
#
# A & B
#
# OR
#
# A.intersection(B)


intersection_result = A & B

print("\nIntersection:", intersection_result)


intersection_result = A.intersection(B)

print("Intersection using method:", intersection_result)


# Result:
# {4, 5}


# ==========================================
# 3. DIFFERENCE
# ==========================================
# Difference gives elements present in A
# but NOT present in B.
#
# A - B


difference_result = A - B

print("\nA - B:", difference_result)


difference_result = A.difference(B)

print("A.difference(B):", difference_result)


# Result:
# {1, 2, 3}


# ------------------------------------------
# B - A
# ------------------------------------------
# Elements present in B but NOT in A.

difference_result = B - A

print("B - A:", difference_result)


# Result:
# {6, 7, 8}


# ==========================================
# 4. SYMMETRIC DIFFERENCE
# ==========================================
# Gives elements that are in either A or B,
# but NOT in both.
#
# A ^ B


symmetric_result = A ^ B

print("\nSymmetric Difference:", symmetric_result)


symmetric_result = A.symmetric_difference(B)

print(
    "Symmetric Difference using method:",
    symmetric_result
)


# Result:
# {1, 2, 3, 6, 7, 8}


# ==========================================
# 5. ISSUBSET
# ==========================================
# Checks whether all elements of one set
# are present in another set.


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("\nA is subset of B:", A.issubset(B))


# Output:
# True


# Operator version:
print("Using <= :", A <= B)


# ==========================================
# 6. ISSUPERSET
# ==========================================
# Checks whether one set contains all
# elements of another set.

print("\nB is superset of A:", B.issuperset(A))


# Output:
# True


# Operator version:
print("Using >= :", B >= A)


# ==========================================
# 7. DISJOINT
# ==========================================
# Two sets are disjoint if they have
# NO common elements.

A = {1, 2, 3}
B = {4, 5, 6}

print("\nAre A and B disjoint?", A.isdisjoint(B))


# Output:
# True


# Sets with common elements

A = {1, 2, 3}
B = {3, 4, 5}

print("Are A and B disjoint?", A.isdisjoint(B))


# Output:
# False


# ==========================================
# 8. UNION WITH MULTIPLE SETS
# ==========================================

A = {1, 2}
B = {3, 4}
C = {5, 6}

result = A.union(B, C)

print("\nUnion of A, B and C:", result)


# Operator version

result = A | B | C

print("Using | :", result)


# ==========================================
# 9. INTERSECTION WITH MULTIPLE SETS
# ==========================================

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
C = {3, 4, 6}

result = A.intersection(B, C)

print("\nCommon elements:", result)


# Operator version

result = A & B & C

print("Using & :", result)


# ==========================================
# 10. PRACTICAL EXAMPLE
# ==========================================

# Students who know Python

python_students = {
    "Santhosh",
    "Rahul",
    "Kiran",
    "Arun"
}


# Students who know Java

java_students = {
    "Rahul",
    "Kiran",
    "Vijay",
    "Ravi"
}


# Students who know both

both = python_students & java_students

print("\nStudents who know both:")
print(both)


# Students who know Python

# but NOT Java

only_python = python_students - java_students

print("\nOnly Python:")
print(only_python)


# Students who know Java

# but NOT Python

only_java = java_students - python_students

print("\nOnly Java:")
print(only_java)


# Students who know either Python or Java

either = python_students | java_students

print("\nPython or Java:")
print(either)


# Students who know only one language

only_one = python_students ^ java_students

print("\nOnly one language:")
print(only_one)
