# ==========================================
# SET METHODS
# ==========================================


# ------------------------------------------
# 1. add()
# ------------------------------------------
# Adds ONE element to the set.

numbers = {10, 20, 30}

numbers.add(40)

print("add():", numbers)


# ------------------------------------------
# 2. update()
# ------------------------------------------
# Adds MULTIPLE elements to the set.

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print("update():", numbers)


# We can also update using another set.

numbers.update({70, 80})

print("After second update:", numbers)


# ------------------------------------------
# 3. remove()
# ------------------------------------------
# Removes a specific element.
#
# If the element does not exist,
# remove() gives KeyError.

numbers = {10, 20, 30, 40}

numbers.remove(30)

print("remove():", numbers)


# ------------------------------------------
# 4. discard()
# ------------------------------------------
# Removes a specific element.
#
# If the element does not exist,
# discard() does NOT give an error.

numbers = {10, 20, 30, 40}

numbers.discard(30)

print("discard():", numbers)

numbers.discard(100)

print("After discarding missing value:", numbers)


# ------------------------------------------
# remove() vs discard()
# ------------------------------------------

numbers = {10, 20, 30}

# numbers.remove(100)
# ❌ KeyError

numbers.discard(100)
# ✅ No error


# ------------------------------------------
# 5. pop()
# ------------------------------------------
# Removes and returns an arbitrary element.
#
# Sets are unordered, so we cannot choose
# which element will be removed by index.

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed:", removed)
print("After pop():", numbers)


# ------------------------------------------
# 6. clear()
# ------------------------------------------
# Removes all elements.

numbers = {10, 20, 30}

numbers.clear()

print("clear():", numbers)


# ------------------------------------------
# 7. copy()
# ------------------------------------------
# Creates a copy of the set.

numbers = {10, 20, 30}

new_numbers = numbers.copy()

print("Original:", numbers)
print("Copy:", new_numbers)


# ------------------------------------------
# 8. len()
# ------------------------------------------
# len() is a built-in function.

numbers = {10, 20, 30, 40}

print("Length:", len(numbers))


# ------------------------------------------
# 9. Membership
# ------------------------------------------

numbers = {10, 20, 30}

print(20 in numbers)
print(100 in numbers)


# ==========================================
# SET METHOD SUMMARY
# ==========================================

print("\n========== SET METHODS ==========")

print("add()      -> Add one element")
print("update()   -> Add multiple elements")
print("remove()   -> Remove element, error if missing")
print("discard()  -> Remove element, no error if missing")
print("pop()      -> Remove arbitrary element")
print("clear()    -> Remove all elements")
print("copy()     -> Create a copy")
print("len()      -> Find number of elements")