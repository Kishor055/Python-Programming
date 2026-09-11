"""
04_list_methods.py
==================

Python List Methods

This file demonstrates the built-in methods available on Python lists.

Methods covered:

    append()
    extend()
    insert()
    remove()
    pop()
    clear()
    index()
    count()
    sort()
    reverse()
    copy()
"""


# ============================================================
# 1. append()
# ============================================================
# Adds one element to the end of the list.
# Syntax:
#     list.append(element)

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# append() can add any object, including another list.

numbers = [10, 20, 30]

numbers.append([40, 50])

print(numbers)


# append() adds the entire object as one element.

items = []

items.append("Python")
items.append(100)
items.append(True)

print(items)


# append() returns None.

numbers = [10, 20, 30]

result = numbers.append(40)

print(numbers)
print(result)


# ============================================================
# 2. extend()
# ============================================================
# Adds each element from an iterable to the end of the list.
# Syntax:
#     list.extend(iterable)

numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)


# extend() with a tuple.

numbers = [10, 20]

numbers.extend((30, 40))

print(numbers)


# extend() with a set.

numbers = [10, 20]

numbers.extend({30, 40})

print(numbers)


# extend() with a string.
# Each character is added separately.

letters = ["A", "B"]

letters.extend("CDE")

print(letters)


# extend() with a range.

numbers = [1, 2]

numbers.extend(range(3, 6))

print(numbers)


# extend() returns None.

numbers = [10, 20]

result = numbers.extend([30, 40])

print(numbers)
print(result)


# ============================================================
# 3. insert()
# ============================================================
# Inserts an element at a specified index.
# Syntax:
#     list.insert(index, element)

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)


# Insert at the beginning.

numbers = [20, 30, 40]

numbers.insert(0, 10)

print(numbers)


# Insert at the end.

numbers = [10, 20, 30]

numbers.insert(len(numbers), 40)

print(numbers)


# Insert beyond the end.
# The element is added at the end.

numbers = [10, 20, 30]

numbers.insert(100, 40)

print(numbers)


# Insert using a negative index.

numbers = [10, 20, 30, 40]

numbers.insert(-1, 35)

print(numbers)


# insert() returns None.

numbers = [10, 20, 30]

result = numbers.insert(1, 15)

print(numbers)
print(result)


# ============================================================
# 4. remove()
# ============================================================
# Removes the first matching element by value.
# Syntax:
#     list.remove(value)

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)


# Only the first occurrence is removed.

numbers = [10, 20, 20, 20, 30]

numbers.remove(20)

print(numbers)


# remove() is value-based, not index-based.

numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)


# Check before removing to avoid ValueError.

numbers = [10, 20, 30]

if 20 in numbers:
    numbers.remove(20)

print(numbers)


# remove() returns None.

numbers = [10, 20, 30]

result = numbers.remove(20)

print(numbers)
print(result)


# ============================================================
# 5. pop()
# ============================================================
# Removes and returns an element.
# Syntax:
#     list.pop()
#     list.pop(index)


# Remove the last element.

numbers = [10, 20, 30]

removed = numbers.pop()

print("Removed:", removed)
print("List:", numbers)


# Remove by index.

numbers = [10, 20, 30]

removed = numbers.pop(1)

print("Removed:", removed)
print("List:", numbers)


# Remove the first element.

numbers = [10, 20, 30]

removed = numbers.pop(0)

print("Removed:", removed)
print("List:", numbers)


# Remove the last element using negative index.

numbers = [10, 20, 30]

removed = numbers.pop(-1)

print("Removed:", removed)
print("List:", numbers)


# pop() can be useful when processing a stack.

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# ============================================================
# 6. clear()
# ============================================================
# Removes all elements from the list.
# Syntax:
#     list.clear()

numbers = [10, 20, 30, 40]

numbers.clear()

print(numbers)


# clear() keeps the same list object.

numbers = [10, 20, 30]

original_id = id(numbers)

numbers.clear()

new_id = id(numbers)

print(original_id == new_id)
print(numbers)


# clear() returns None.

numbers = [10, 20, 30]

result = numbers.clear()

print(numbers)
print(result)


# ============================================================
# 7. index()
# ============================================================
# Returns the index of the first matching value.
# Syntax:
#     list.index(value)
#     list.index(value, start)
#     list.index(value, start, stop)


numbers = [10, 20, 30, 40]

print(numbers.index(30))


# index() returns the first matching occurrence.

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))


# Search starting from a specific index.

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20, 2))


# Search within a start and stop range.

numbers = [10, 20, 30, 20, 40, 20]

print(numbers.index(20, 2, 5))


# Check before calling index().

numbers = [10, 20, 30]

if 20 in numbers:
    print(numbers.index(20))


# ============================================================
# 8. count()
# ============================================================
# Returns the number of occurrences of a value.
# Syntax:
#     list.count(value)


numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))


# Count a value that does not exist.

numbers = [10, 20, 30]

print(numbers.count(100))


# Count strings.

languages = ["Python", "Java", "Python", "C++", "Python"]

print(languages.count("Python"))


# Count booleans.

values = [True, False, True, True]

print(values.count(True))


# ============================================================
# 9. sort()
# ============================================================
# Sorts the list in place.
# Syntax:
#     list.sort()
#     list.sort(reverse=True)
#     list.sort(key=function)


numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)


# Sort in descending order.

numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)


# sort() modifies the original list.

numbers = [3, 1, 2]

numbers.sort()

print(numbers)


# sort() returns None.

numbers = [3, 1, 2]

result = numbers.sort()

print(numbers)
print(result)


# Sort strings alphabetically.

languages = ["Python", "Java", "C++", "JavaScript"]

languages.sort()

print(languages)


# Sort strings in reverse order.

languages = ["Python", "Java", "C++", "JavaScript"]

languages.sort(reverse=True)

print(languages)


# ============================================================
# 10. sort() WITH key
# ============================================================
# key specifies a function used to determine the sorting value.


words = ["Python", "Java", "C"]

words.sort(key=len)

print(words)


# Sort by string length in descending order.

words = ["Python", "Java", "C"]

words.sort(key=len, reverse=True)

print(words)


# Sort case-insensitively.

words = ["python", "Java", "C++", "javascript"]

words.sort(key=str.lower)

print(words)


# Sort tuples by the second element.

students = [
    ("Kishor", 90),
    ("Rahul", 85),
    ("Amit", 95)
]

students.sort(key=lambda student: student[1])

print(students)


# Sort dictionaries by a value.

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 85},
    {"name": "Amit", "marks": 95}
]

students.sort(key=lambda student: student["marks"])

print(students)


# ============================================================
# 11. reverse()
# ============================================================
# Reverses the list in place.
# Syntax:
#     list.reverse()


numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)


# reverse() modifies the original list.

numbers = [1, 2, 3]

numbers.reverse()

print(numbers)


# reverse() returns None.

numbers = [1, 2, 3]

result = numbers.reverse()

print(numbers)
print(result)


# Reverse strings in a list.

languages = ["Python", "Java", "C++"]

languages.reverse()

print(languages)


# ============================================================
# 12. copy()
# ============================================================
# Creates a shallow copy of the list.
# Syntax:
#     list.copy()


numbers = [10, 20, 30]

copy_numbers = numbers.copy()

print(numbers)
print(copy_numbers)


# copy() creates a different list object.

numbers = [10, 20, 30]

copy_numbers = numbers.copy()

print(numbers is copy_numbers)


# Modifying the copy does not modify a flat original list.

numbers = [10, 20, 30]

copy_numbers = numbers.copy()

copy_numbers.append(40)

print("Original:", numbers)
print("Copy:", copy_numbers)


# ============================================================
# 13. SHALLOW COPY WITH NESTED LISTS
# ============================================================
# copy() copies only the outer list.
# Nested mutable objects are still shared.

numbers = [
    [1, 2],
    [3, 4]
]

copy_numbers = numbers.copy()

copy_numbers[0].append(100)

print("Original:", numbers)
print("Copy:", copy_numbers)


# ============================================================
# 14. APPEND VS EXTEND
# ============================================================

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)


numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)


# append() adds one object.
# extend() adds elements from an iterable.


# ============================================================
# 15. INSERT VS APPEND
# ============================================================

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)


# append() adds at the end.
# insert() adds at a specified position.


# ============================================================
# 16. REMOVE VS POP
# ============================================================

numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)


numbers = [10, 20, 30, 40]

removed = numbers.pop(2)

print("Removed:", removed)
print("List:", numbers)


# remove() uses a value.
# pop() uses an index and returns the removed value.


# ============================================================
# 17. POP VS DEL
# ============================================================

numbers = [10, 20, 30]

removed = numbers.pop(1)

print("Removed:", removed)
print(numbers)


numbers = [10, 20, 30]

del numbers[1]

print(numbers)


# pop() returns the removed element.
# del does not return the removed element.


# ============================================================
# 18. CLEAR VS DEL
# ============================================================

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


numbers = [10, 20, 30]

del numbers[:]

print(numbers)


# Both can remove all elements from the existing list.


# ============================================================
# 19. METHOD CHAINING
# ============================================================
# Most mutating list methods return None,
# so chaining them is generally not appropriate.


numbers = [3, 1, 2]

numbers.sort()

print(numbers)


# Avoid:
#
# numbers.sort().reverse()
#
# because sort() returns None.


# ============================================================
# 20. COMBINING LIST METHODS
# ============================================================

numbers = [30, 10, 20]

numbers.append(40)
numbers.extend([50, 60])
numbers.insert(0, 5)

print(numbers)


# ============================================================
# 21. PRACTICAL EXAMPLE — SHOPPING CART
# ============================================================

cart = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

cart.append("Monitor")
cart.remove("Mouse")

print(cart)


# ============================================================
# 22. PRACTICAL EXAMPLE — TASK MANAGEMENT
# ============================================================

tasks = [
    "Learn Python",
    "Practice Lists",
    "Build Project"
]

tasks.append("Review Code")

completed = tasks.pop(1)

print("Completed:", completed)
print("Remaining:", tasks)


# ============================================================
# 23. PRACTICAL EXAMPLE — STUDENT MARKS
# ============================================================

marks = [85, 92, 78, 90, 88]

marks.sort(reverse=True)

print("Sorted marks:", marks)
print("Highest:", marks[0])
print("Lowest:", marks[-1])


# ============================================================
# 24. PRACTICAL EXAMPLE — DUPLICATE COUNTS
# ============================================================

numbers = [10, 20, 10, 30, 10, 20]

print("10 occurs:", numbers.count(10))
print("20 occurs:", numbers.count(20))
print("30 occurs:", numbers.count(30))


# ============================================================
# 25. PRACTICAL EXAMPLE — FINDING AN ELEMENT
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

language = "Python"

if language in languages:
    position = languages.index(language)
    print("Found at index:", position)


# ============================================================
# 26. PRACTICAL EXAMPLE — SAFE REMOVE
# ============================================================

languages = [
    "Python",
    "Java",
    "C++"
]

language = "Java"

if language in languages:
    languages.remove(language)

print(languages)


# ============================================================
# 27. PRACTICAL EXAMPLE — STACK
# ============================================================
# append() + pop() can implement stack behavior.


stack = []

stack.append("First")
stack.append("Second")
stack.append("Third")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# ============================================================
# 28. PRACTICAL EXAMPLE — QUEUE-LIKE BEHAVIOR
# ============================================================
# append() + pop(0) can provide queue-like behavior,
# but collections.deque is generally more efficient
# for frequent operations at the beginning.


queue = []

queue.append("Person 1")
queue.append("Person 2")
queue.append("Person 3")

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))


# ============================================================
# 29. METHOD RETURN VALUE SUMMARY
# ============================================================

"""
Methods that modify the list generally return None:

    append()
    extend()
    insert()
    remove()
    sort()
    reverse()
    clear()

Methods that return useful information:

    pop()    -> removed element
    index()  -> index of element
    count()  -> number of occurrences
    copy()   -> new shallow copy
"""


# ============================================================
# 30. LIST METHODS QUICK REFERENCE
# ============================================================

"""
append(value)
    Add one element to the end.

extend(iterable)
    Add elements from an iterable.

insert(index, value)
    Insert a value at an index.

remove(value)
    Remove the first matching value.

pop()
    Remove and return the last element.

pop(index)
    Remove and return the element at index.

clear()
    Remove all elements.

index(value)
    Return the first matching index.

index(value, start)
    Search from a starting index.

index(value, start, stop)
    Search within a range.

count(value)
    Count occurrences.

sort()
    Sort in ascending order.

sort(reverse=True)
    Sort in descending order.

sort(key=function)
    Sort using a custom key.

reverse()
    Reverse the list in place.

copy()
    Create a shallow copy.
"""


# ============================================================
# 31. IMPORTANT BEHAVIOR
# ============================================================

"""
Remember:

    numbers.append(10)
        -> modifies the list

    numbers.extend([10, 20])
        -> modifies the list

    numbers.insert(0, 10)
        -> modifies the list

    numbers.remove(10)
        -> modifies the list

    numbers.pop()
        -> modifies the list AND returns an element

    numbers.clear()
        -> modifies the list

    numbers.sort()
        -> modifies the list

    numbers.reverse()
        -> modifies the list

    numbers.copy()
        -> creates a new list
"""


# ============================================================
# 32. COMMON MISTAKE — ASSIGNING sort() RESULT
# ============================================================

numbers = [3, 1, 2]

# Wrong:
#
# numbers = numbers.sort()
#
# sort() returns None.


numbers = [3, 1, 2]

numbers.sort()

print(numbers)


# ============================================================
# 33. COMMON MISTAKE — ASSIGNING reverse() RESULT
# ============================================================

numbers = [1, 2, 3]

# Wrong:
#
# numbers = numbers.reverse()
#
# reverse() returns None.


numbers = [1, 2, 3]

numbers.reverse()

print(numbers)


# ============================================================
# 34. COMMON MISTAKE — append() VS extend()
# ============================================================

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)


# ============================================================
# 35. COMMON MISTAKE — remove() USES VALUE
# ============================================================

numbers = [10, 20, 30]

# Remove the value 20.
numbers.remove(20)

print(numbers)


# To remove by index, use pop() or del.

numbers = [10, 20, 30]

numbers.pop(1)

print(numbers)


# ============================================================
# 36. COMMON MISTAKE — remove() WITH MISSING VALUE
# ============================================================

numbers = [10, 20, 30]

if 40 in numbers:
    numbers.remove(40)

print(numbers)


# ============================================================
# 37. COMMON MISTAKE — index() WITH MISSING VALUE
# ============================================================

numbers = [10, 20, 30]

if 20 in numbers:
    print(numbers.index(20))


# ============================================================
# 38. PRACTICAL EXAMPLE — CLEANING DATA
# ============================================================

data = [
    "Python",
    "",
    "Java",
    "",
    "C++"
]

while "" in data:
    data.remove("")

print(data)


# ============================================================
# 39. PRACTICAL EXAMPLE — REMOVE DUPLICATE VALUE
# ============================================================

numbers = [10, 20, 10, 30, 10]

while numbers.count(10) > 0:
    numbers.remove(10)

print(numbers)


# ============================================================
# 40. PRACTICAL EXAMPLE — SORT STUDENTS BY NAME
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Amit", "marks": 95},
    {"name": "Rahul", "marks": 85}
]

students.sort(key=lambda student: student["name"])

print(students)


# ============================================================
# 41. PRACTICAL EXAMPLE — SORT STUDENTS BY MARKS
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Amit", "marks": 95},
    {"name": "Rahul", "marks": 85}
]

students.sort(
    key=lambda student: student["marks"],
    reverse=True
)

print(students)


# ============================================================
# 42. PRACTICAL EXAMPLE — COPY BEFORE MODIFYING
# ============================================================

original = [10, 20, 30, 40]

working_copy = original.copy()

working_copy.append(50)
working_copy.remove(20)

print("Original:", original)
print("Working copy:", working_copy)


# ============================================================
# 43. PRACTICAL EXAMPLE — PROCESSING A STACK
# ============================================================

stack = [
    "Task 1",
    "Task 2",
    "Task 3"
]

while stack:
    task = stack.pop()
    print("Processing:", task)


# ============================================================
# 44. PRACTICAL EXAMPLE — BUILDING A LIST
# ============================================================

numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)


# ============================================================
# 45. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

1. List methods that mutate the list usually return None.

2. append() adds exactly one object.

3. extend() adds elements from an iterable.

4. insert() is useful for positional insertion.

5. remove() removes by value.

6. pop() removes by index and returns the removed element.

7. clear() removes all elements from the existing list.

8. index() returns the first matching position.

9. count() returns the number of occurrences.

10. sort() modifies the original list.

11. reverse() modifies the original list.

12. copy() creates a shallow copy.

13. Use `in` before remove() or index() when the value
    may not exist.

14. For large collections, choose the appropriate data
    structure based on access and modification patterns.

15. For frequent insertion/removal from the beginning,
    collections.deque is generally preferable to a list.
"""


# ============================================================
# END OF LIST METHODS
# ============================================================

print("\nList methods demonstration completed successfully!")

