"""
03_list_slicing.py
==================

Python List Slicing

List slicing is used to extract a portion of a list.

Syntax:

    list[start:stop:step]

Important rules:

    - start is inclusive.
    - stop is exclusive.
    - step controls the direction and interval.
    - start is optional.
    - stop is optional.
    - step is optional.
    - Slicing returns a new list.
    - Original list is not modified by normal slicing.
"""


# ============================================================
# 1. BASIC LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers)


# ============================================================
# 2. BASIC SLICING
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Output:
# [20, 30, 40]

# Index 1 is included.
# Index 4 is excluded.


# ============================================================
# 3. SLICE FROM INDEX 0
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])


# ============================================================
# 4. SLICE FROM INDEX 1
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])


# ============================================================
# 5. SLICE INCLUDING LAST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:5])


# ============================================================
# 6. OMIT START
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

# Equivalent to:
# numbers[0:3]


# ============================================================
# 7. OMIT STOP
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[2:])

# Equivalent to:
# numbers[2:len(numbers)]


# ============================================================
# 8. OMIT START AND STOP
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:])

# Returns a shallow copy of the list.


# ============================================================
# 9. SLICE WITH STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:6:2])

# Takes every second element.


# ============================================================
# 10. STEP OF 3
# ============================================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[0:8:3])


# ============================================================
# 11. OMIT START WITH STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:6:2])


# ============================================================
# 12. OMIT STOP WITH STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1::2])


# ============================================================
# 13. OMIT START, STOP, AND USE STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])


# ============================================================
# 14. EVERY ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[::1])


# ============================================================
# 15. EVERY SECOND ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])


# ============================================================
# 16. EVERY THIRD ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::3])


# ============================================================
# 17. FIRST THREE ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])


# ============================================================
# 18. FIRST FOUR ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:4])


# ============================================================
# 19. LAST THREE ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-3:])


# ============================================================
# 20. LAST TWO ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-2:])


# ============================================================
# 21. ALL EXCEPT LAST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:-1])


# ============================================================
# 22. ALL EXCEPT LAST TWO ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:-2])


# ============================================================
# 23. ALL EXCEPT FIRST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:])


# ============================================================
# 24. ALL EXCEPT FIRST TWO ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[2:])


# ============================================================
# 25. MIDDLE PORTION
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[2:5])


# ============================================================
# 26. NEGATIVE START INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-4:-1])


# ============================================================
# 27. NEGATIVE STOP INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:-1])


# ============================================================
# 28. BOTH NEGATIVE INDEXES
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-4:-1])


# ============================================================
# 29. NEGATIVE INDEX WITH POSITIVE STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[-5:-1:2])


# ============================================================
# 30. REVERSE A LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])


# ============================================================
# 31. REVERSE WITH NEGATIVE STEP
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[4:0:-1])


# ============================================================
# 32. REVERSE FROM LAST INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-1::-1])


# ============================================================
# 33. REVERSE USING NEGATIVE START
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-1:-6:-1])


# ============================================================
# 34. EVERY SECOND ELEMENT IN REVERSE
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::-2])


# ============================================================
# 35. EVERY THIRD ELEMENT IN REVERSE
# ============================================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::-3])


# ============================================================
# 36. REVERSE A PORTION
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[5:1:-1])


# ============================================================
# 37. COPY A LIST USING SLICING
# ============================================================

numbers = [10, 20, 30, 40]

copy = numbers[:]

print(numbers)
print(copy)


# ============================================================
# 38. SLICING CREATES A NEW LIST
# ============================================================

numbers = [10, 20, 30]

result = numbers[:]

print(numbers is result)


# ============================================================
# 39. MODIFY SLICED COPY
# ============================================================

numbers = [10, 20, 30]

copy = numbers[:]

copy[0] = 100

print("Original:", numbers)
print("Copy:", copy)


# ============================================================
# 40. SLICE DOES NOT MODIFY ORIGINAL LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

result = numbers[1:4]

print("Original:", numbers)
print("Slice:", result)


# ============================================================
# 41. ASSIGNING A SLICE
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[1:3] = [200, 300]

print(numbers)


# ============================================================
# 42. REPLACE A SLICE WITH DIFFERENT LENGTH
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[1:3] = [200, 300, 400, 500]

print(numbers)


# ============================================================
# 43. REPLACE A SLICE WITH FEWER ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[1:4] = [200]

print(numbers)


# ============================================================
# 44. DELETE USING SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[1:4] = []

print(numbers)


# ============================================================
# 45. DELETE USING DEL AND SLICE
# ============================================================

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)


# ============================================================
# 46. INSERT USING SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 50]

numbers[2:2] = [30, 40]

print(numbers)


# ============================================================
# 47. INSERT MULTIPLE ELEMENTS
# ============================================================

numbers = [1, 5]

numbers[1:1] = [2, 3, 4]

print(numbers)


# ============================================================
# 48. CLEAR LIST USING SLICE
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[:] = []

print(numbers)


# ============================================================
# 49. REPLACE ENTIRE LIST USING SLICE
# ============================================================

numbers = [10, 20, 30]

numbers[:] = [100, 200, 300]

print(numbers)


# ============================================================
# 50. SLICE ASSIGNMENT PRESERVES OBJECT ID
# ============================================================

numbers = [10, 20, 30]

original_id = id(numbers)

numbers[:] = [100, 200, 300]

new_id = id(numbers)

print(original_id == new_id)
print(numbers)


# ============================================================
# 51. REASSIGNMENT VS SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 30]

numbers = [100, 200, 300]

# A completely new list object is assigned.


numbers = [10, 20, 30]

numbers[:] = [100, 200, 300]

# The existing list object is modified.


# ============================================================
# 52. STEP IN SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

numbers[::2] = [100, 300, 500]

print(numbers)


# ============================================================
# 53. EXTENDED SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

numbers[1::2] = [200, 400, 600]

print(numbers)


# ============================================================
# 54. EXTENDED SLICE ASSIGNMENT LENGTH RULE
# ============================================================

"""
When a slice has a non-1 step, the replacement iterable
must have exactly the same number of elements.

Example:

    numbers[::2] = [100, 200, 300]

If the selected slice contains 3 elements,
the replacement must also contain 3 elements.
"""


# ============================================================
# 55. STRING LIST SLICING
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Go"
]

print(languages[0:3])
print(languages[2:])
print(languages[:2])
print(languages[-2:])


# ============================================================
# 56. STUDENT MARKS SLICING
# ============================================================

marks = [85, 90, 78, 92, 88, 95]

first_three = marks[:3]
last_three = marks[-3:]

print("First three:", first_three)
print("Last three:", last_three)


# ============================================================
# 57. SHOPPING CART SLICING
# ============================================================

cart = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Webcam"
]

print(cart[:2])
print(cart[2:])
print(cart[-2:])


# ============================================================
# 58. PAGINATION USING SLICING
# ============================================================

items = [
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
    "Item 5",
    "Item 6",
    "Item 7",
    "Item 8",
    "Item 9",
    "Item 10"
]

page_size = 3

page_1 = items[0:page_size]
page_2 = items[page_size:page_size * 2]
page_3 = items[page_size * 2:page_size * 3]

print(page_1)
print(page_2)
print(page_3)


# ============================================================
# 59. DYNAMIC PAGINATION
# ============================================================

items = list(range(1, 21))

page_size = 5
page_number = 2

start = (page_number - 1) * page_size
end = start + page_size

page = items[start:end]

print(page)


# ============================================================
# 60. CHUNKING A LIST
# ============================================================

numbers = list(range(1, 11))

chunk_size = 3

for start in range(0, len(numbers), chunk_size):
    chunk = numbers[start:start + chunk_size]
    print(chunk)


# ============================================================
# 61. SLICING WITH VARIABLES
# ============================================================

numbers = [10, 20, 30, 40, 50]

start = 1
stop = 4

result = numbers[start:stop]

print(result)


# ============================================================
# 62. DYNAMIC STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

step = 2

print(numbers[::step])


# ============================================================
# 63. CONDITIONAL SLICING
# ============================================================

numbers = [10, 20, 30, 40, 50]

start = 1
stop = 4

if 0 <= start <= len(numbers) and 0 <= stop <= len(numbers):
    print(numbers[start:stop])


# ============================================================
# 64. SLICE BOUNDARIES BEYOND LIST LENGTH
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[0:100])
print(numbers[-100:100])


# ============================================================
# 65. NEGATIVE BOUNDARIES
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-4:-1])
print(numbers[-5:-2])


# ============================================================
# 66. EMPTY SLICE
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[3:3])


# ============================================================
# 67. START GREATER THAN STOP
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[4:2])

# With a positive step, this produces an empty list.


# ============================================================
# 68. START GREATER THAN STOP WITH NEGATIVE STEP
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[4:2:-1])


# ============================================================
# 69. NEGATIVE STEP DIRECTION
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[4:1:-1])

# Start at index 4.
# Move backward.
# Stop before index 1.


# ============================================================
# 70. STEP CANNOT BE ZERO
# ============================================================

"""
This is invalid:

    numbers[::0]

It raises:

    ValueError: slice step cannot be zero
"""


# ============================================================
# 71. SLICE OBJECT
# ============================================================

numbers = [10, 20, 30, 40, 50]

slice_object = slice(1, 4)

result = numbers[slice_object]

print(result)


# ============================================================
# 72. SLICE OBJECT WITH STEP
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

slice_object = slice(0, 6, 2)

result = numbers[slice_object]

print(result)


# ============================================================
# 73. REUSABLE SLICE OBJECT
# ============================================================

numbers = [10, 20, 30, 40, 50]
letters = ["a", "b", "c", "d", "e"]

middle = slice(1, 4)

print(numbers[middle])
print(letters[middle])


# ============================================================
# 74. SLICE OBJECT WITH NEGATIVE STEP
# ============================================================

numbers = [10, 20, 30, 40, 50]

reverse = slice(None, None, -1)

print(numbers[reverse])


# ============================================================
# 75. SLICING A NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0:2])


# ============================================================
# 76. SLICING ROWS AND COLUMNS
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = matrix[0:2]

for row in rows:
    print(row[0:2])


# ============================================================
# 77. SLICING A LIST OF TUPLES
# ============================================================

coordinates = [
    (10, 20),
    (30, 40),
    (50, 60),
    (70, 80)
]

print(coordinates[1:3])


# ============================================================
# 78. SLICING A LIST OF DICTIONARIES
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 85},
    {"name": "Amit", "marks": 95},
    {"name": "Sneha", "marks": 88}
]

print(students[:2])
print(students[-2:])


# ============================================================
# 79. SLICING AND SHALLOW COPY
# ============================================================

students = [
    ["Kishor", 90],
    ["Rahul", 85]
]

copy = students[:]

copy[0][1] = 100

print(students)
print(copy)

# The outer list is copied.
# The nested lists are still shared.


# ============================================================
# 80. SLICING VS INDEXING
# ============================================================

numbers = [10, 20, 30, 40, 50]

# Indexing returns one element.
print(numbers[2])

# Slicing returns a list.
print(numbers[2:3])


# ============================================================
# 81. SLICING VS COPY
# ============================================================

numbers = [10, 20, 30]

copy_1 = numbers[:]
copy_2 = numbers.copy()

print(copy_1)
print(copy_2)

print(copy_1 is numbers)
print(copy_2 is numbers)


# ============================================================
# 82. SLICING AND SORTING
# ============================================================

numbers = [50, 10, 40, 20, 30]

result = sorted(numbers[:3])

print(result)


# ============================================================
# 83. SLICING AND REVERSE
# ============================================================

numbers = [10, 20, 30, 40, 50]

first_three_reversed = numbers[:3][::-1]

print(first_three_reversed)


# ============================================================
# 84. SLICING WITH LIST COMPREHENSION
# ============================================================

numbers = [10, 20, 30, 40, 50, 60]

result = [
    number * 2
    for number in numbers[1:5]
]

print(result)


# ============================================================
# 85. SLICING AFTER FILTERING
# ============================================================

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers[:2])


# ============================================================
# 86. SLICING AND UNPACKING
# ============================================================

numbers = [10, 20, 30, 40, 50]

first = numbers[:1]
middle = numbers[1:-1]
last = numbers[-1:]

print(first)
print(middle)
print(last)


# ============================================================
# 87. REMOVE FIRST ELEMENT USING SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 30, 40]

numbers[:] = numbers[1:]

print(numbers)


# ============================================================
# 88. REMOVE LAST ELEMENT USING SLICE ASSIGNMENT
# ============================================================

numbers = [10, 20, 30, 40]

numbers[:] = numbers[:-1]

print(numbers)


# ============================================================
# 89. REMOVE FIRST AND LAST ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers[:] = numbers[1:-1]

print(numbers)


# ============================================================
# 90. ROTATE LIST LEFT
# ============================================================

numbers = [1, 2, 3, 4, 5]

position = 2

rotated = numbers[position:] + numbers[:position]

print(rotated)


# ============================================================
# 91. ROTATE LIST RIGHT
# ============================================================

numbers = [1, 2, 3, 4, 5]

position = 2

rotated = numbers[-position:] + numbers[:-position]

print(rotated)


# ============================================================
# 92. GET BATCH FROM LIST
# ============================================================

users = [
    "User 1",
    "User 2",
    "User 3",
    "User 4",
    "User 5",
    "User 6"
]

batch_size = 2

for start in range(0, len(users), batch_size):
    batch = users[start:start + batch_size]
    print(batch)


# ============================================================
# 93. PRACTICAL EXAMPLE — RECENT RECORDS
# ============================================================

records = [
    "Record 1",
    "Record 2",
    "Record 3",
    "Record 4",
    "Record 5"
]

recent_records = records[-3:]

print(recent_records)


# ============================================================
# 94. PRACTICAL EXAMPLE — TOP RESULTS
# ============================================================

scores = [98, 95, 92, 90, 88, 85]

top_three = scores[:3]

print(top_three)


# ============================================================
# 95. PRACTICAL EXAMPLE — SKIP ELEMENTS
# ============================================================

numbers = list(range(1, 11))

every_second = numbers[::2]

print(every_second)


# ============================================================
# 96. PRACTICAL EXAMPLE — REVERSE ORDER
# ============================================================

tasks = [
    "Task 1",
    "Task 2",
    "Task 3",
    "Task 4"
]

print(tasks[::-1])


# ============================================================
# 97. PRACTICAL EXAMPLE — PAGINATION FUNCTION
# ============================================================

def get_page(items, page_number, page_size):
    start = (page_number - 1) * page_size
    end = start + page_size

    return items[start:end]


items = list(range(1, 21))

print(get_page(items, 1, 5))
print(get_page(items, 2, 5))
print(get_page(items, 3, 5))


# ============================================================
# 98. PRACTICAL EXAMPLE — CHUNK FUNCTION
# ============================================================

def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]


numbers = list(range(1, 11))

for chunk in chunks(numbers, 3):
    print(chunk)


# ============================================================
# 99. SLICE SYNTAX CHEAT SHEET
# ============================================================

"""
Given:

    numbers = [10, 20, 30, 40, 50]

Basic:

    numbers[start:stop]

With step:

    numbers[start:stop:step]

First 3:

    numbers[:3]

Last 3:

    numbers[-3:]

From index 2:

    numbers[2:]

Everything except last:

    numbers[:-1]

Everything except first:

    numbers[1:]

Every second:

    numbers[::2]

Every third:

    numbers[::3]

Reverse:

    numbers[::-1]

Reverse every second:

    numbers[::-2]

Copy:

    numbers[:]

Middle:

    numbers[1:-1]
"""


# ============================================================
# 100. IMPORTANT SLICING RULES
# ============================================================

"""
RULE 1:
    start is inclusive.

RULE 2:
    stop is exclusive.

RULE 3:
    Default start is 0 when step is positive.

RULE 4:
    Default stop is len(list) when step is positive.

RULE 5:
    With a negative step, slicing moves from right to left.

RULE 6:
    step cannot be zero.

RULE 7:
    Normal slicing returns a new list.

RULE 8:
    Slicing normally does not modify the original list.

RULE 9:
    Slice assignment can modify the original list.

RULE 10:
    Extended slice assignment with a non-1 step requires
    matching lengths.
"""


# ============================================================
# END OF LIST SLICING
# ============================================================

print("\nList slicing demonstration completed successfully!")
