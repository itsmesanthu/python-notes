# ==========================================
# LIST METHODS
# ==========================================


# ------------------------------------------
# 1. append()
# ------------------------------------------

numbers = [10, 20, 30]

numbers.append(40)

print("append():", numbers)


# ------------------------------------------
# 2. extend()
# ------------------------------------------

numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print("extend():", numbers)


# ------------------------------------------
# 3. insert()
# ------------------------------------------

numbers = [10, 20, 30]

numbers.insert(1, 15)

print("insert():", numbers)


# ------------------------------------------
# 4. remove()
# ------------------------------------------

numbers = [10, 20, 30, 40]

numbers.remove(30)

print("remove():", numbers)


# ------------------------------------------
# 5. pop()
# ------------------------------------------

numbers = [10, 20, 30, 40]

removed = numbers.pop(2)

print("Removed:", removed)
print("pop():", numbers)


# pop() without index
numbers = [10, 20, 30]

removed = numbers.pop()

print("Removed last:", removed)
print("List:", numbers)


# ------------------------------------------
# 6. clear()
# ------------------------------------------

numbers = [10, 20, 30]

numbers.clear()

print("clear():", numbers)


# ------------------------------------------
# 7. index()
# ------------------------------------------

numbers = [10, 20, 30, 40]

position = numbers.index(30)

print("index():", position)


# ------------------------------------------
# 8. count()
# ------------------------------------------

numbers = [10, 20, 10, 30, 10]

count = numbers.count(10)

print("count():", count)


# ------------------------------------------
# 9. sort()
# ------------------------------------------

numbers = [50, 20, 40, 10, 30]

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# ------------------------------------------
# 10. reverse()
# ------------------------------------------

numbers = [10, 20, 30, 40]

numbers.reverse()

print("reverse():", numbers)


# ------------------------------------------
# 11. copy()
# ------------------------------------------

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print("Original:", numbers)
print("Copy:", new_numbers)


# ==========================================
# LIST METHOD SUMMARY
# ==========================================

print("\n========== LIST METHODS ==========")

print("append()  -> Add one element")
print("extend()  -> Add multiple elements")
print("insert()  -> Add at specific index")
print("remove()  -> Remove specific value")
print("pop()     -> Remove using index")
print("clear()   -> Remove all elements")
print("index()   -> Find index")
print("count()   -> Count occurrences")
print("sort()    -> Sort the list")
print("reverse() -> Reverse the list")
print("copy()    -> Copy the list")