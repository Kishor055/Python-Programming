"""
03_nested_loop.py
=================

Nested Loops in Python

A nested loop is a loop inside another loop.

Syntax:

    for outer_variable in outer_iterable:
        for inner_variable in inner_iterable:
            # code

The outer loop controls the larger iteration.
The inner loop runs completely for each iteration
of the outer loop.

Nested loops are commonly used for:
    - Patterns
    - Matrices
    - Tables
    - 2D lists
    - Grids
    - Combinations
    - Comparisons
"""


# ============================================================
# 1. BASIC NESTED FOR LOOP
# ============================================================

for row in range(3):
    for column in range(3):
        print(row, column)


# ============================================================
# 2. ROW AND COLUMN
# ============================================================

for row in range(1, 4):
    for column in range(1, 4):
        print(f"Row: {row}, Column: {column}")


# ============================================================
# 3. NESTED LOOP EXECUTION
# ============================================================

for outer in range(3):

    print("Outer:", outer)

    for inner in range(3):
        print("  Inner:", inner)


# ============================================================
# 4. SIMPLE STAR PATTERN
# ============================================================

for row in range(5):

    for column in range(5):
        print("*", end=" ")

    print()


# ============================================================
# 5. RIGHT-ANGLE TRIANGLE
# ============================================================

for row in range(1, 6):

    for column in range(row):
        print("*", end=" ")

    print()


# ============================================================
# 6. INVERTED RIGHT-ANGLE TRIANGLE
# ============================================================

for row in range(5, 0, -1):

    for column in range(row):
        print("*", end=" ")

    print()


# ============================================================
# 7. NUMBER TRIANGLE
# ============================================================

for row in range(1, 6):

    for column in range(row):
        print(row, end=" ")

    print()


# ============================================================
# 8. INCREMENTING NUMBER TRIANGLE
# ============================================================

number = 1

for row in range(1, 5):

    for column in range(row):
        print(number, end=" ")
        number += 1

    print()


# ============================================================
# 9. SAME NUMBER IN EACH ROW
# ============================================================

for row in range(1, 6):

    for column in range(row):
        print(row, end=" ")

    print()


# ============================================================
# 10. COLUMN NUMBERS
# ============================================================

for row in range(1, 6):

    for column in range(1, row + 1):
        print(column, end=" ")

    print()


# ============================================================
# 11. REPEATED ALPHABET PATTERN
# ============================================================

for row in range(5):

    for column in range(5):
        print("A", end=" ")

    print()


# ============================================================
# 12. ALPHABET TRIANGLE
# ============================================================

for row in range(1, 6):

    for column in range(row):
        print(chr(65 + column), end=" ")

    print()


# ============================================================
# 13. REPEATED ALPHABET BY ROW
# ============================================================

for row in range(5):

    for column in range(row + 1):
        print(chr(65 + row), end=" ")

    print()


# ============================================================
# 14. SQUARE NUMBER PATTERN
# ============================================================

for row in range(1, 6):

    for column in range(1, 6):
        print(column, end=" ")

    print()


# ============================================================
# 15. MULTIPLICATION TABLE
# ============================================================

for number in range(1, 6):

    for multiplier in range(1, 11):

        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )

    print()


# ============================================================
# 16. ALL MULTIPLICATION TABLES
# ============================================================

for number in range(1, 11):

    print(f"Table of {number}")

    for multiplier in range(1, 11):

        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )

    print()


# ============================================================
# 17. MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value)

    print()


# ============================================================
# 18. PRINT MATRIX IN GRID FORMAT
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()


# ============================================================
# 19. MATRIX USING INDEXES
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):
        print(
            matrix[row][column],
            end=" "
        )

    print()


# ============================================================
# 20. MATRIX WITH ROW AND COLUMN INDEX
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):

        print(
            f"matrix[{row}][{column}] = "
            f"{matrix[row][column]}"
        )


# ============================================================
# 21. SUM OF MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:

    for value in row:
        total += value

print("Matrix total:", total)


# ============================================================
# 22. ROW SUM
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    total = 0

    for value in row:
        total += value

    print("Row total:", total)


# ============================================================
# 23. COLUMN SUM
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for column in range(len(matrix[0])):

    total = 0

    for row in range(len(matrix)):
        total += matrix[row][column]

    print("Column total:", total)


# ============================================================
# 24. FIND MAXIMUM IN MATRIX
# ============================================================

matrix = [
    [10, 25, 30],
    [45, 5, 60],
    [70, 80, 15]
]

maximum = matrix[0][0]

for row in matrix:

    for value in row:

        if value > maximum:
            maximum = value

print("Maximum:", maximum)


# ============================================================
# 25. FIND MINIMUM IN MATRIX
# ============================================================

matrix = [
    [10, 25, 30],
    [45, 5, 60],
    [70, 80, 15]
]

minimum = matrix[0][0]

for row in matrix:

    for value in row:

        if value < minimum:
            minimum = value

print("Minimum:", minimum)


# ============================================================
# 26. COUNT EVEN NUMBERS IN MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

count = 0

for row in matrix:

    for value in row:

        if value % 2 == 0:
            count += 1

print("Even numbers:", count)


# ============================================================
# 27. COUNT ODD NUMBERS IN MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

count = 0

for row in matrix:

    for value in row:

        if value % 2 != 0:
            count += 1

print("Odd numbers:", count)


# ============================================================
# 28. SEARCH IN MATRIX
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50

found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

print("Found:", found)


# ============================================================
# 29. SEARCH MATRIX WITH POSITION
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 60

found = False

for row_index in range(len(matrix)):

    for column_index in range(
        len(matrix[row_index])
    ):

        if matrix[row_index][column_index] == target:

            print(
                "Found at:",
                row_index,
                column_index
            )

            found = True
            break

    if found:
        break


# ============================================================
# 30. MATRIX SEARCH WITH FOR-ELSE
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 100

for row in matrix:

    for value in row:

        if value == target:
            print("Found")
            break

    else:
        continue

    break

else:
    print("Not found")


# ============================================================
# 31. BREAK IN NESTED LOOP
# ============================================================
# break only terminates the nearest enclosing loop.


for row in range(3):

    for column in range(3):

        if column == 1:
            break

        print(row, column)


# ============================================================
# 32. CONTINUE IN NESTED LOOP
# ============================================================
# continue affects only the nearest enclosing loop.


for row in range(3):

    for column in range(3):

        if column == 1:
            continue

        print(row, column)


# ============================================================
# 33. BREAK FROM BOTH LOOPS
# ============================================================
# Use a flag when you need to exit both loops.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5

found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

print("Found:", found)


# ============================================================
# 34. NESTED WHILE LOOP
# ============================================================

row = 1

while row <= 3:

    column = 1

    while column <= 3:

        print(row, column)

        column += 1

    row += 1


# ============================================================
# 35. WHILE LOOP STAR PATTERN
# ============================================================

row = 1

while row <= 5:

    column = 1

    while column <= row:

        print("*", end=" ")

        column += 1

    print()

    row += 1


# ============================================================
# 36. INVERTED STAR PATTERN USING WHILE
# ============================================================

row = 5

while row >= 1:

    column = 1

    while column <= row:

        print("*", end=" ")

        column += 1

    print()

    row -= 1


# ============================================================
# 37. NUMBER TRIANGLE USING WHILE
# ============================================================

row = 1

while row <= 5:

    column = 1

    while column <= row:

        print(column, end=" ")

        column += 1

    print()

    row += 1


# ============================================================
# 38. PYRAMID PATTERN
# ============================================================

for row in range(1, 6):

    for space in range(5 - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()


# ============================================================
# 39. INVERTED PYRAMID
# ============================================================

for row in range(5, 0, -1):

    for space in range(5 - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()


# ============================================================
# 40. DIAMOND PATTERN
# ============================================================

size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()

for row in range(size - 1, 0, -1):

    for space in range(size - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()


# ============================================================
# 41. HOLLOW SQUARE
# ============================================================

size = 5

for row in range(size):

    for column in range(size):

        if (
            row == 0
            or row == size - 1
            or column == 0
            or column == size - 1
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# ============================================================
# 42. HOLLOW TRIANGLE
# ============================================================

size = 5

for row in range(1, size + 1):

    for column in range(1, row + 1):

        if (
            column == 1
            or column == row
            or row == size
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# ============================================================
# 43. FLOYD'S TRIANGLE
# ============================================================

number = 1

for row in range(1, 6):

    for column in range(row):

        print(number, end=" ")

        number += 1

    print()


# ============================================================
# 44. PASCAL-LIKE NUMBER PATTERN
# ============================================================

for row in range(1, 6):

    value = 1

    for column in range(1, row + 1):

        print(value, end=" ")

        value = value * (row - column) // column

    print()


# ============================================================
# 45. CHESSBOARD PATTERN
# ============================================================

size = 8

for row in range(size):

    for column in range(size):

        if (row + column) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")

    print()


# ============================================================
# 46. 0-1 PATTERN
# ============================================================

for row in range(1, 6):

    for column in range(row):

        if (row + column) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")

    print()


# ============================================================
# 47. CHARACTER GRID
# ============================================================

for row in range(5):

    for column in range(5):
        print(chr(65 + column), end=" ")

    print()


# ============================================================
# 48. CHARACTER TRIANGLE
# ============================================================

for row in range(1, 6):

    for column in range(row):

        print(
            chr(65 + column),
            end=" "
        )

    print()


# ============================================================
# 49. REVERSE CHARACTER TRIANGLE
# ============================================================

for row in range(5, 0, -1):

    for column in range(row):

        print(
            chr(65 + column),
            end=" "
        )

    print()


# ============================================================
# 50. NESTED LOOP OVER LIST OF LISTS
# ============================================================

data = [
    ["Python", "Java"],
    ["C++", "Go"],
    ["Rust", "JavaScript"]
]

for group in data:

    for language in group:
        print(language)


# ============================================================
# 51. NESTED LOOP WITH DICTIONARIES
# ============================================================

students = [
    {
        "name": "Kishor",
        "marks": [90, 85, 95]
    },
    {
        "name": "Rahul",
        "marks": [80, 75, 88]
    }
]

for student in students:

    print(student["name"])

    for mark in student["marks"]:
        print(mark)


# ============================================================
# 52. STUDENT TOTALS
# ============================================================

students = [
    {
        "name": "Kishor",
        "marks": [90, 85, 95]
    },
    {
        "name": "Rahul",
        "marks": [80, 75, 88]
    }
]

for student in students:

    total = 0

    for mark in student["marks"]:
        total += mark

    print(
        student["name"],
        "Total:",
        total
    )


# ============================================================
# 53. STUDENT AVERAGES
# ============================================================

students = [
    {
        "name": "Kishor",
        "marks": [90, 85, 95]
    },
    {
        "name": "Rahul",
        "marks": [80, 75, 88]
    }
]

for student in students:

    total = 0

    for mark in student["marks"]:
        total += mark

    average = total / len(
        student["marks"]
    )

    print(
        student["name"],
        "Average:",
        average
    )


# ============================================================
# 54. COMPARE EVERY ELEMENT
# ============================================================

numbers = [10, 20, 30]

for first in numbers:

    for second in numbers:

        print(
            first,
            second
        )


# ============================================================
# 55. ALL PAIRS
# ============================================================

numbers = [1, 2, 3, 4]

for first in numbers:

    for second in numbers:

        if first != second:
            print(
                first,
                second
            )


# ============================================================
# 56. UNIQUE PAIRS
# ============================================================
# Avoid duplicate pairs such as (1, 2) and (2, 1).


numbers = [1, 2, 3, 4]

for first_index in range(len(numbers)):

    for second_index in range(
        first_index + 1,
        len(numbers)
    ):

        print(
            numbers[first_index],
            numbers[second_index]
        )


# ============================================================
# 57. ALL COMBINATIONS
# ============================================================

colors = ["Red", "Green", "Blue"]

for first in colors:

    for second in colors:

        print(
            first,
            second
        )


# ============================================================
# 58. COMBINATIONS WITHOUT REPETITION
# ============================================================

colors = ["Red", "Green", "Blue"]

for first_index in range(len(colors)):

    for second_index in range(
        first_index + 1,
        len(colors)
    ):

        print(
            colors[first_index],
            colors[second_index]
        )


# ============================================================
# 59. FIND DUPLICATES
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

duplicates = []

for first_index in range(len(numbers)):

    for second_index in range(
        first_index + 1,
        len(numbers)
    ):

        if (
            numbers[first_index]
            == numbers[second_index]
        ):

            if numbers[first_index] not in duplicates:
                duplicates.append(
                    numbers[first_index]
                )

print("Duplicates:", duplicates)


# ============================================================
# 60. REMOVE DUPLICATES MANUALLY
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique = []

for number in numbers:

    exists = False

    for value in unique:

        if number == value:
            exists = True
            break

    if not exists:
        unique.append(number)

print("Unique:", unique)


# ============================================================
# 61. COMMON ELEMENTS
# ============================================================

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

common = []

for first in list_a:

    for second in list_b:

        if first == second:

            if first not in common:
                common.append(first)

print("Common:", common)


# ============================================================
# 62. MANUAL SEARCH WITHOUT `in`
# ============================================================

numbers = [10, 20, 30, 40]

target = 30

found = False

for number in numbers:

    if number == target:
        found = True
        break

print("Found:", found)


# ============================================================
# 63. BUBBLE SORT
# ============================================================

numbers = [50, 20, 40, 10, 30]

for outer in range(len(numbers)):

    for inner in range(
        0,
        len(numbers) - outer - 1
    ):

        if numbers[inner] > numbers[inner + 1]:

            numbers[inner], numbers[inner + 1] = (
                numbers[inner + 1],
                numbers[inner]
            )

print("Sorted:", numbers)


# ============================================================
# 64. BUBBLE SORT DESCENDING
# ============================================================

numbers = [50, 20, 40, 10, 30]

for outer in range(len(numbers)):

    for inner in range(
        0,
        len(numbers) - outer - 1
    ):

        if numbers[inner] < numbers[inner + 1]:

            numbers[inner], numbers[inner + 1] = (
                numbers[inner + 1],
                numbers[inner]
            )

print("Sorted:", numbers)


# ============================================================
# 65. BUBBLE SORT WITH EARLY EXIT
# ============================================================

numbers = [10, 20, 30, 40, 50]

for outer in range(len(numbers)):

    swapped = False

    for inner in range(
        0,
        len(numbers) - outer - 1
    ):

        if numbers[inner] > numbers[inner + 1]:

            numbers[inner], numbers[inner + 1] = (
                numbers[inner + 1],
                numbers[inner]
            )

            swapped = True

    if not swapped:
        break

print("Sorted:", numbers)


# ============================================================
# 66. MATRIX TRANSFORMATION
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):

        matrix[row][column] *= 2

print(matrix)


# ============================================================
# 67. TRANSPOSE MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for column in range(len(matrix[0])):

    new_row = []

    for row in range(len(matrix)):

        new_row.append(
            matrix[row][column]
        )

    transpose.append(new_row)

print(transpose)


# ============================================================
# 68. MATRIX ADDITION
# ============================================================

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

result = []

for row in range(len(matrix_a)):

    new_row = []

    for column in range(
        len(matrix_a[row])
    ):

        new_row.append(
            matrix_a[row][column]
            + matrix_b[row][column]
        )

    result.append(new_row)

print(result)


# ============================================================
# 69. MATRIX MULTIPLICATION
# ============================================================

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

for row in range(len(matrix_a)):

    for column in range(len(matrix_b[0])):

        for index in range(len(matrix_b)):

            result[row][column] += (
                matrix_a[row][index]
                * matrix_b[index][column]
            )

print(result)


# ============================================================
# 70. DIAGONAL ELEMENTS
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):

        if row == column:
            print(
                "Main diagonal:",
                matrix[row][column]
            )


# ============================================================
# 71. SECONDARY DIAGONAL
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

size = len(matrix)

for row in range(size):

    for column in range(size):

        if row + column == size - 1:

            print(
                "Secondary diagonal:",
                matrix[row][column]
            )


# ============================================================
# 72. UPPER TRIANGLE
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):

        if column >= row:
            print(
                matrix[row][column],
                end=" "
            )

        else:
            print(" ", end=" ")

    print()


# ============================================================
# 73. LOWER TRIANGLE
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):

        if column <= row:
            print(
                matrix[row][column],
                end=" "
            )

        else:
            print(" ", end=" ")

    print()


# ============================================================
# 74. MULTIPLE CONDITIONS IN NESTED LOOP
# ============================================================

for row in range(1, 6):

    for column in range(1, 6):

        if (
            row % 2 == 0
            and column % 2 == 0
        ):
            print(
                row,
                column
            )


# ============================================================
# 75. NESTED LOOP WITH FUNCTION
# ============================================================

def multiply(a, b):
    return a * b


for row in range(1, 4):

    for column in range(1, 4):

        print(
            multiply(row, column),
            end=" "
        )

    print()


# ============================================================
# 76. NESTED LOOP WITH ENUMERATE
# ============================================================

languages = [
    ["Python", "Java"],
    ["C++", "Go"],
    ["Rust", "JavaScript"]
]

for row_index, row in enumerate(languages):

    for column_index, language in enumerate(row):

        print(
            row_index,
            column_index,
            language
        )


# ============================================================
# 77. NESTED LOOP WITH ZIP
# ============================================================

names = [
    ["Kishor", "Rahul"],
    ["Amit", "Rohit"]
]

marks = [
    [90, 85],
    [95, 88]
]

for name_row, mark_row in zip(names, marks):

    for name, mark in zip(
        name_row,
        mark_row
    ):

        print(name, mark)


# ============================================================
# 78. THREE LEVEL NESTED LOOP
# ============================================================

for x in range(2):

    for y in range(2):

        for z in range(2):

            print(x, y, z)


# ============================================================
# 79. THREE-DIMENSIONAL DATA
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

for block in data:

    for row in block:

        for value in row:

            print(value)


# ============================================================
# 80. THREE-DIMENSIONAL SUM
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

total = 0

for block in data:

    for row in block:

        for value in row:
            total += value

print("Total:", total)


# ============================================================
# 81. NESTED LOOP FOR COMPARISON
# ============================================================

numbers = [10, 20, 30, 40]

for first in numbers:

    for second in numbers:

        if first < second:

            print(
                first,
                "<",
                second
            )


# ============================================================
# 82. FIND PAIR WITH TARGET SUM
# ============================================================

numbers = [2, 4, 6, 8, 10]

target = 12

for first_index in range(len(numbers)):

    for second_index in range(
        first_index + 1,
        len(numbers)
    ):

        if (
            numbers[first_index]
            + numbers[second_index]
            == target
        ):

            print(
                "Pair:",
                numbers[first_index],
                numbers[second_index]
            )


# ============================================================
# 83. FIND ALL PAIRS WITH TARGET SUM
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

target = 7

for first_index in range(len(numbers)):

    for second_index in range(
        first_index + 1,
        len(numbers)
    ):

        if (
            numbers[first_index]
            + numbers[second_index]
            == target
        ):

            print(
                numbers[first_index],
                numbers[second_index]
            )


# ============================================================
# 84. CHARACTER COMBINATIONS
# ============================================================

characters = ["A", "B", "C"]

for first in characters:

    for second in characters:

        if first != second:

            print(
                first + second
            )


# ============================================================
# 85. PASSWORD COMBINATIONS
# ============================================================
# Demonstration only.


digits = ["0", "1", "2"]

for first in digits:

    for second in digits:

        for third in digits:

            print(
                first + second + third
            )


# ============================================================
# 86. GRID COORDINATES
# ============================================================

for x in range(3):

    for y in range(3):

        print(
            f"({x}, {y})"
        )


# ============================================================
# 87. GAME BOARD
# ============================================================

rows = 5
columns = 5

for row in range(rows):

    for column in range(columns):

        print(".", end=" ")

    print()


# ============================================================
# 88. CHECKERBOARD
# ============================================================

rows = 8
columns = 8

for row in range(rows):

    for column in range(columns):

        if (row + column) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")

    print()


# ============================================================
# 89. NESTED LOOP WITH WHILE AND FOR
# ============================================================

row = 1

while row <= 3:

    for column in range(1, 4):

        print(
            row,
            column
        )

    row += 1


# ============================================================
# 90. NESTED FOR AND WHILE
# ============================================================

for row in range(1, 4):

    column = 1

    while column <= 3:

        print(
            row,
            column
        )

        column += 1


# ============================================================
# 91. NESTED WHILE LOOPS WITH MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 0

while row < len(matrix):

    column = 0

    while column < len(matrix[row]):

        print(
            matrix[row][column],
            end=" "
        )

        column += 1

    print()

    row += 1


# ============================================================
# 92. SEARCH WITH NESTED WHILE
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 80

row = 0
found = False

while row < len(matrix):

    column = 0

    while column < len(matrix[row]):

        if matrix[row][column] == target:
            found = True
            break

        column += 1

    if found:
        break

    row += 1

print("Found:", found)


# ============================================================
# 93. NESTED LOOP FOR DATA VALIDATION
# ============================================================

records = [
    [10, 20, 30],
    [40, -5, 60],
    [70, 80, 90]
]

valid = True

for row in records:

    for value in row:

        if value < 0:
            valid = False
            break

    if not valid:
        break

print("Valid data:", valid)


# ============================================================
# 94. FIND DUPLICATE ROWS
# ============================================================

rows = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

for first_index in range(len(rows)):

    for second_index in range(
        first_index + 1,
        len(rows)
    ):

        if rows[first_index] == rows[second_index]:

            print(
                "Duplicate rows:",
                first_index,
                second_index
            )


# ============================================================
# 95. ROW-WISE MAXIMUM
# ============================================================

matrix = [
    [10, 20, 30],
    [5, 50, 15],
    [70, 25, 40]
]

for row in matrix:

    maximum = row[0]

    for value in row:

        if value > maximum:
            maximum = value

    print("Row maximum:", maximum)


# ============================================================
# 96. ROW-WISE MINIMUM
# ============================================================

matrix = [
    [10, 20, 30],
    [5, 50, 15],
    [70, 25, 40]
]

for row in matrix:

    minimum = row[0]

    for value in row:

        if value < minimum:
            minimum = value

    print("Row minimum:", minimum)


# ============================================================
# 97. COUNT FREQUENCY IN MATRIX
# ============================================================

matrix = [
    [1, 2, 1],
    [3, 1, 4],
    [1, 5, 2]
]

target = 1

count = 0

for row in matrix:

    for value in row:

        if value == target:
            count += 1

print(
    f"{target} occurs {count} times"
)


# ============================================================
# 98. NESTED LOOP COMPLEXITY
# ============================================================

"""
If the outer loop runs N times and the inner loop
also runs N times:

    for i in range(N):
        for j in range(N):
            ...

The total number of iterations is approximately:

    N * N = N²

Therefore, the time complexity is:

    O(N²)

Three nested loops may result in:

    O(N³)

Always consider the size of the input before using
deeply nested loops.
"""


# ============================================================
# 99. PROFESSIONAL GUIDELINES
# ============================================================

"""
PROFESSIONAL GUIDELINES
-----------------------

1. Use nested loops when the problem naturally contains
   multiple levels of iteration.

2. Common examples:
       - Matrix processing
       - Grid traversal
       - Pattern generation
       - Pair comparisons
       - Combinations
       - Table generation

3. Keep nesting depth as low as practical.

4. Deep nesting can make code difficult to read and maintain.

5. Extract complex nested logic into functions.

6. Use enumerate() when indexes are required.

7. Use direct iteration when indexes are unnecessary.

8. Use break carefully because it exits only the nearest loop.

9. Use a flag when an event in an inner loop must terminate
   an outer loop.

10. Consider algorithmic complexity:
        - Two nested loops: often O(n²)
        - Three nested loops: often O(n³)

11. Look for better algorithms when nested loops process
    large datasets.

12. Python built-ins such as sorted(), any(), all(), zip(),
    and comprehensions can sometimes replace nested loops
    with clearer or faster code.

13. Avoid modifying a collection unexpectedly while
    iterating over it.

14. For matrix operations, maintain consistent row lengths
    when working with rectangular matrices.
"""


# ============================================================
# 100. KEY CONCEPT
# ============================================================

"""
KEY CONCEPT
-----------

For every single iteration of the OUTER loop,
the INNER loop completes all of its iterations.

Example:

    for i in range(3):
        for j in range(3):
            print(i, j)

Execution:

    i = 0 -> j = 0, 1, 2
    i = 1 -> j = 0, 1, 2
    i = 2 -> j = 0, 1, 2

Total inner-loop executions:

    3 × 3 = 9
"""


# ============================================================
# END OF NESTED LOOP
# ============================================================

print("\nNested loop demonstration completed successfully!")
