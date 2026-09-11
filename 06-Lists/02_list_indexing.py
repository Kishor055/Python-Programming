```
"""
02_list_indexing.py
===================

Python List Indexing
--------------------

List indexing is used to access individual elements from a list.

Important concepts:

    - Python uses zero-based indexing.
    - Positive indexing starts from the left.
    - Negative indexing starts from the right.
    - Lists are mutable.
    - Invalid indexes raise IndexError.
"""

# ============================================================
# 1. BASIC LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers)

# ============================================================
# 2. POSITIVE INDEXING
# ============================================================

numbers = [10, 20, 30, 40, 50]

# Index positions:
#
#     10   20   30   40   50
#      0    1    2    3    4

print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[2])  # 30
print(numbers[3])  # 40
print(numbers[4])  # 50

# ============================================================
# 3. INDEXING DIAGRAM
# ============================================================

"""
List:

    10    20    30    40    50
    ↑     ↑     ↑     ↑     ↑
    0     1     2     3     4

Python indexing starts from 0.
"""

# ============================================================
# 4. NEGATIVE INDEXING
# ============================================================

numbers = [10, 20, 30, 40, 50]

# Negative indexes:
#
#     10    20    30    40    50
#    -5    -4    -3    -2    -1

print(numbers[-1])  # 50
print(numbers[-2])  # 40
print(numbers[-3])  # 30
print(numbers[-4])  # 20
print(numbers[-5])  # 10

# ============================================================
# 5. FIRST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

first = numbers[0]

print(first)

# ============================================================
# 6. LAST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

last = numbers[-1]

print(last)

# ============================================================
# 7. SECOND ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1])
print(numbers[-4])

# ============================================================
# 8. MIDDLE ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[2])
print(numbers[-3])

# ============================================================
# 9. INDEXING USING VARIABLES
# ============================================================

numbers = [10, 20, 30, 40, 50]

index = 2

print(numbers[index])

# ============================================================
# 10. INDEXING USING EXPRESSIONS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1 + 1])  # 30
print(numbers[2 * 2])  # 50
print(numbers[len(numbers) - 1])  # 50

# ============================================================
# 11. LIST LENGTH AND LAST INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

length = len(numbers)
last_index = length - 1

print("Length:", length)
print("Last index:", last_index)
print("Last element:", numbers[last_index])

# ============================================================
# 12. INDEXING STRINGS INSIDE A LIST
# ============================================================

languages = ["Python", "Java", "C++", "JavaScript"]

print(languages[0])
print(languages[1])
print(languages[-1])

# ============================================================
# 13. INDEXING MIXED DATA
# ============================================================

data = ["Kishor", 25, 95.5, True]

print(data[0])  # Kishor
print(data[1])  # 25
print(data[2])  # 95.5
print(data[3])  # True

# ============================================================
# 14. ACCESSING NESTED LISTS
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1])
print(matrix[2])

# ============================================================
# 15. INDEXING ELEMENTS IN A NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1
print(matrix[0][1])  # 2
print(matrix[1][1])  # 5
print(matrix[2][2])  # 9

# ============================================================
# 16. NEGATIVE INDEXING IN NESTED LISTS
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[-1])       # [7, 8, 9]
print(matrix[-1][-1])   # 9
print(matrix[-2][-1])   # 6
print(matrix[-3][-1])   # 3

# ============================================================
# 17. MODIFYING AN ELEMENT USING INDEX
# ============================================================

numbers = [10, 20, 30, 40]

numbers[0] = 100

print(numbers)

# ============================================================
# 18. MODIFYING THE LAST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40]

numbers[-1] = 400

print(numbers)

# ============================================================
# 19. MODIFYING MULTIPLE ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[0] = 100
numbers[2] = 300
numbers[-1] = 500

print(numbers)

# ============================================================
# 20. MODIFYING NESTED LIST ELEMENT
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[0][1] = 200

print(matrix)

# ============================================================
# 21. INDEXING WITH FOR LOOP
# ============================================================

numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers)):
    print(index, numbers[index])

# ============================================================
# 22. INDEXING WITH ENUMERATE
# ============================================================

numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):
    print(index, value)

# ============================================================
# 23. ENUMERATE WITH STARTING INDEX
# ============================================================

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages, start=1):
    print(index, language)

# ============================================================
# 24. REVERSE INDEXING LOOP
# ============================================================

numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers) - 1, -1, -1):
    print(index, numbers[index])

# ============================================================
# 25. ACCESS EVEN INDEX POSITIONS
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

for index in range(0, len(numbers), 2):
    print(index, numbers[index])

# ============================================================
# 26. ACCESS ODD INDEX POSITIONS
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

for index in range(1, len(numbers), 2):
    print(index, numbers[index])

# ============================================================
# 27. CHECK VALID INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

index = 3

if 0 <= index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range")

# ============================================================
# 28. CHECK NEGATIVE INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

index = -2

if -len(numbers) <= index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range")

# ============================================================
# 29. INVALID POSITIVE INDEX
# ============================================================

numbers = [10, 20, 30]

"""
Valid indexes:

    0
    1
    2

Invalid:

    numbers[3]

This raises:

    IndexError: list index out of range
"""

# ============================================================
# 30. INVALID NEGATIVE INDEX
# ============================================================

numbers = [10, 20, 30]

"""
Valid negative indexes:

    -1
    -2
    -3

Invalid:

    numbers[-4]

This raises:

    IndexError: list index out of range
"""

# ============================================================
# 31. SAFE INDEXING
# ============================================================

numbers = [10, 20, 30]

index = 5

if 0 <= index < len(numbers):
    print(numbers[index])
else:
    print("Invalid index")

# ============================================================
# 32. SAFE NEGATIVE INDEXING
# ============================================================

numbers = [10, 20, 30]

index = -5

if -len(numbers) <= index < len(numbers):
    print(numbers[index])
else:
    print("Invalid index")

# ============================================================
# 33. INDEXING AN EMPTY LIST
# ============================================================

numbers = []

"""
An empty list has no valid index.

numbers[0]

would raise:

    IndexError: list index out of range
"""

if numbers:
    print(numbers[0])
else:
    print("List is empty")

# ============================================================
# 34. FIRST AND LAST ELEMENT OF USER DATA
# ============================================================

names = ["Amit", "Rahul", "Kishor", "Sneha"]

print("First:", names[0])
print("Last:", names[-1])

# ============================================================
# 35. PRACTICAL EXAMPLE — STUDENT MARKS
# ============================================================

marks = [85, 90, 78, 92, 88]

print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("Third mark:", marks[2])

# ============================================================
# 36. PRACTICAL EXAMPLE — SHOPPING CART
# ============================================================

cart = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

print("First item:", cart[0])
print("Last item:", cart[-1])

# ============================================================
# 37. PRACTICAL EXAMPLE — MONTHS
# ============================================================

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
]

print(months[0])
print(months[2])
print(months[-1])

# ============================================================
# 38. PRACTICAL EXAMPLE — RGB COLOR
# ============================================================

rgb = [255, 128, 64]

red = rgb[0]
green = rgb[1]
blue = rgb[2]

print("Red:", red)
print("Green:", green)
print("Blue:", blue)

# ============================================================
# 39. PRACTICAL EXAMPLE — COORDINATES
# ============================================================

point = [10, 20]

x = point[0]
y = point[1]

print("X:", x)
print("Y:", y)

# ============================================================
# 40. PRACTICAL EXAMPLE — PRODUCT
# ============================================================

product = [
    "Laptop",
    75000,
    "Electronics",
    True
]

name = product[0]
price = product[1]
category = product[2]
available = product[3]

print("Name:", name)
print("Price:", price)
print("Category:", category)
print("Available:", available)

# ============================================================
# 41. LIST INDEX USING index()
# ============================================================

languages = ["Python", "Java", "C++", "Python"]

position = languages.index("Python")

print(position)

# ============================================================
# 42. FINDING INDEX OF A VALUE
# ============================================================

numbers = [10, 20, 30, 40, 50]

if 30 in numbers:
    print(numbers.index(30))

# ============================================================
# 43. FIND ALL INDEXES OF A VALUE
# ============================================================

numbers = [10, 20, 10, 30, 10, 40]

for index, value in enumerate(numbers):
    if value == 10:
        print(index)

# ============================================================
# 44. INDEXING AFTER APPEND
# ============================================================

numbers = [10, 20, 30]

numbers.append(40)

print(numbers[-1])

# ============================================================
# 45. INDEXING AFTER INSERT
# ============================================================

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
print(numbers[1])

# ============================================================
# 46. INDEXING AFTER REMOVE
# ============================================================

numbers = [10, 20, 30, 40]

numbers.remove(20)

print(numbers)
print(numbers[1])

# ============================================================
# 47. INDEXING AFTER POP
# ============================================================

numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print("Removed:", removed)
print("List:", numbers)

# ============================================================
# 48. INDEXING WITH CONDITIONAL LOGIC
# ============================================================

numbers = [10, 20, 30, 40, 50]

index = 2

if index < len(numbers):
    print(f"Element at index {index}: {numbers[index]}")

# ============================================================
# 49. INDEXING WITH A FUNCTION
# ============================================================

def get_element(items, index):
    if -len(items) <= index < len(items):
        return items[index]

    return None

numbers = [10, 20, 30, 40, 50]

print(get_element(numbers, 2))
print(get_element(numbers, -1))
print(get_element(numbers, 10))

# ============================================================
# 50. INDEXING NESTED DATA
# ============================================================

students = [
    ["Kishor", 90],
    ["Rahul", 85],
    ["Amit", 95]
]

print(students[0][0])
print(students[0][1])

print(students[1][0])
print(students[1][1])

# ============================================================
# 51. MODIFY NESTED DATA USING INDEX
# ============================================================

students = [
    ["Kishor", 90],
    ["Rahul", 85],
    ["Amit", 95]
]

students[1][1] = 95

print(students)

# ============================================================
# 52. THREE-DIMENSIONAL INDEXING
# ============================================================

data = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(data[0][0][0])
print(data[0][1][1])
print(data[1][0][1])
print(data[1][1][1])

# ============================================================
# 53. NEGATIVE INDEXING WITH MULTIPLE LEVELS
# ============================================================

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(data[-1][-1])
print(data[-2][-2])
print(data[-3][-3])

# ============================================================
# 54. INDEXING AND MUTABILITY
# ============================================================

numbers = [10, 20, 30]

print(numbers)

numbers[1] = 200

print(numbers)

# Lists can be modified using indexes.

# ============================================================
# 55. LIST INDEXING VS STRING INDEXING
# ============================================================

numbers = [10, 20, 30]
text = "Python"

print(numbers[0])
print(text[0])

# Both lists and strings support indexing.
#
# Difference:
#
#     List   -> mutable
#     String -> immutable

# ============================================================
# 56. INDEXING CHEAT SHEET
# ============================================================

"""
Given:

    numbers = [10, 20, 30, 40, 50]

Positive indexing:

    numbers[0] -> 10
    numbers[1] -> 20
    numbers[2] -> 30
    numbers[3] -> 40
    numbers[4] -> 50

Negative indexing:

    numbers[-1] -> 50
    numbers[-2] -> 40
    numbers[-3] -> 30
    numbers[-4] -> 20
    numbers[-5] -> 10

Important:

    First element -> numbers[0]
    Last element  -> numbers[-1]

    First index   -> 0
    Last index    -> len(numbers) - 1
"""

# ============================================================
# 57. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

1. Python list indexes start at 0.

2. The first element is:
       list[0]

3. The last element is:
       list[-1]

4. The last positive index is:
       len(list) - 1

5. Negative indexing starts at:
       -1

6. Invalid indexes raise:
       IndexError

7. Lists are mutable, so indexed elements can be changed.

8. enumerate() is useful when both index and value are needed.

9. Always validate dynamic indexes when they may come from
   user input or external data.

10. Nested lists can be accessed using multiple indexes:

       matrix[row][column]

11. Indexing returns a single element.

12. Slicing returns a portion of a list.
"""

# ============================================================
# END
# ============================================================

print("\nList indexing demonstration completed successfully!")
```
