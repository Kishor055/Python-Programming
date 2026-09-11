```
"""
02_string_indexing.py
=====================

Python String Indexing
----------------------

String indexing is used to access individual characters
from a string.

Important concepts:

    - Python uses zero-based indexing.
    - Positive indexing starts from the left.
    - Negative indexing starts from the right.
    - Each character has an index position.
    - Strings are immutable.
"""

# ============================================================
# 1. BASIC STRING
# ============================================================

text = "Python"

print(text)

# Index positions:
#
#     P   y   t   h   o   n
#     0   1   2   3   4   5

# ============================================================
# 2. POSITIVE INDEXING
# ============================================================

text = "Python"

# First character
print(text[0])
# P

# Second character
print(text[1])
# y

# Third character
print(text[2])
# t

# Fourth character
print(text[3])
# h

# Fifth character
print(text[4])
# o

# Sixth character
print(text[5])
# n

# ============================================================
# 3. INDEXING DIAGRAM
# ============================================================

"""
String:

    P   y   t   h   o   n
    ↑   ↑   ↑   ↑   ↑   ↑
    0   1   2   3   4   5

Python indexing starts at 0.

Therefore:

    text[0] -> P
    text[1] -> y
    text[2] -> t
    text[3] -> h
    text[4] -> o
    text[5] -> n
"""

# ============================================================
# 4. NEGATIVE INDEXING
# ============================================================

text = "Python"

# Negative indexes start from the right.
#
#     P   y   t   h   o   n
#    -6  -5  -4  -3  -2  -1

# Last character
print(text[-1])
# n

# Second-last character
print(text[-2])
# o

# Third-last character
print(text[-3])
# h

# First character using negative index
print(text[-6])
# P

# ============================================================
# 5. POSITIVE VS NEGATIVE INDEXING
# ============================================================

text = "Python"

# First character
print(text[0])
print(text[-6])

# Last character
print(text[5])
print(text[-1])

# Both pairs access the same characters.

# ============================================================
# 6. ACCESSING FIRST CHARACTER
# ============================================================

text = "Python"

first_character = text[0]

print(first_character)
# P

# ============================================================
# 7. ACCESSING LAST CHARACTER
# ============================================================

text = "Python"

last_character = text[-1]

print(last_character)
# n

# ============================================================
# 8. ACCESSING MIDDLE CHARACTER
# ============================================================

text = "Python"

# Length of "Python" is 6.
# Index positions are 0 to 5.

print(text[3])
# h

# ============================================================
# 9. USING len() WITH INDEXING
# ============================================================

text = "Python"

length = len(text)

print(length)
# 6

# Last index = length - 1
last_index = length - 1

print(last_index)
# 5

print(text[last_index])
# n

# ============================================================
# 10. INDEXING USING VARIABLES
# ============================================================

text = "Python"

index = 2

print(text[index])
# t

# ============================================================
# 11. LOOP THROUGH INDEX POSITIONS
# ============================================================

text = "Python"

for index in range(len(text)):
    print(index, text[index])

# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

# ============================================================
# 12. ENUMERATE WITH INDEXING
# ============================================================

text = "Python"

# enumerate() provides both index and character.
for index, character in enumerate(text):
    print(index, character)

# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

# ============================================================
# 13. NEGATIVE INDEXING WITH VARIABLES
# ============================================================

text = "Python"

index = -1

print(text[index])
# n

# ============================================================
# 14. INDEXING A STRING WITH SPECIAL CHARACTERS
# ============================================================

text = "Python@123"

print(text[0])
# P

print(text[6])
# @

print(text[-1])
# 3

# ============================================================
# 15. INDEXING SPACES
# ============================================================

text = "Hello World"

# Space is also a character and has an index.
#
# H e l l o   W o r l d
# 0 1 2 3 4 5 6 7 8 9 10

print(text[5])
# ' '

# ============================================================
# 16. INDEXING MULTILINE STRINGS
# ============================================================

text = "Hello\nWorld"

# \n is a newline character and occupies one position.
print(text[5])
# newline character

print(text[6])
# W

# ============================================================
# 17. INDEXING UNICODE CHARACTERS
# ============================================================

text = "Python 🐍"

print(text[0])
# P

print(text[-1])
# 🐍

# Python string indexing works with Unicode characters.

# ============================================================
# 18. INDEX OUT OF RANGE
# ============================================================

text = "Python"

"""
Valid positive indexes:

    0, 1, 2, 3, 4, 5

Valid negative indexes:

    -1, -2, -3, -4, -5, -6

An index outside these ranges raises IndexError.

Example:

    print(text[6])

Result:

    IndexError: string index out of range
"""

# ============================================================
# 19. SAFE INDEX CHECK
# ============================================================

text = "Python"

index = 3

if 0 <= index < len(text):
    print(text[index])
else:
    print("Index out of range")

# h

# ============================================================
# 20. NEGATIVE INDEX CHECK
# ============================================================

text = "Python"

index = -2

if -len(text) <= index < len(text):
    print(text[index])
else:
    print("Index out of range")

# o

# ============================================================
# 21. STRING INDEXING IS READ-ONLY
# ============================================================

text = "Python"

"""
You can READ a character:

    print(text[0])

But you cannot directly CHANGE a character:

    text[0] = "J"

This raises:

    TypeError:
    'str' object does not support item assignment

Reason:

    Strings are immutable.
"""

# ============================================================
# 22. MODIFYING A CHARACTER INDIRECTLY
# ============================================================

text = "Python"

# Strings cannot be changed directly.
# A new string must be created.

text = "J" + text[1:]

print(text)
# Jython

# ============================================================
# 23. INDEXING WITH EXPRESSIONS
# ============================================================

text = "Python"

print(text[1 + 1])
# t

print(text[2 * 2])
# o

print(text[len(text) - 1])
# n

# ============================================================
# 24. INDEXING USING CONDITIONAL LOGIC
# ============================================================

text = "Python"

index = 4

if index < len(text):
    print(f"Character at index {index}: {text[index]}")
else:
    print("Invalid index")

# ============================================================
# 25. FIRST AND LAST CHARACTER
# ============================================================

text = "Programming"

first = text[0]
last = text[-1]

print(first)
# P

print(last)
# g

# ============================================================
# 26. SECOND CHARACTER FROM EACH SIDE
# ============================================================

text = "Programming"

print(text[1])
# r

print(text[-2])
# n

# ============================================================
# 27. INDEXING IN A LOOP
# ============================================================

text = "Python"

for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

# ============================================================
# 28. REVERSE INDEX LOOP
# ============================================================

text = "Python"

for i in range(len(text) - 1, -1, -1):
    print(f"Index {i}: {text[i]}")

# Output:
# Index 5: n
# Index 4: o
# Index 3: h
# Index 2: t
# Index 1: y
# Index 0: P

# ============================================================
# 29. FIND CHARACTER POSITION
# ============================================================

text = "Python"

# index() returns the first occurrence of a character.
position = text.index("t")

print(position)
# 2

# ============================================================
# 30. FIND CHARACTER POSITION SAFELY
# ============================================================

text = "Python"

# find() returns -1 instead of raising ValueError
position = text.find("z")

print(position)
# -1

# ============================================================
# 31. CHARACTER FREQUENCY USING INDEXING
# ============================================================

text = "banana"

count = 0

for i in range(len(text)):
    if text[i] == "a":
        count += 1

print(count)
# 3

# ============================================================
# 32. ACCESS EVEN INDEX CHARACTERS
# ============================================================

text = "Python"

for i in range(0, len(text), 2):
    print(text[i])

# Output:
# P
# t
# o

# ============================================================
# 33. ACCESS ODD INDEX CHARACTERS
# ============================================================

text = "Python"

for i in range(1, len(text), 2):
    print(text[i])

# Output:
# y
# h
# n

# ============================================================
# 34. INDEXING EMPTY STRING
# ============================================================

text = ""

"""
An empty string has no valid indexes.

Therefore:

    text[0]

raises:

    IndexError: string index out of range

Always check the string before accessing an index
when the string may be empty.
"""

if text:
    print(text[0])
else:
    print("String is empty")

# ============================================================
# 35. INDEXING USER INPUT
# ============================================================

name = input("Enter your name: ")

if name:
    print("First character:", name[0])
    print("Last character:", name[-1])
else:
    print("No name entered")

# ============================================================
# 36. PRACTICAL EXAMPLE — FIRST LETTER
# ============================================================

name = "Kishor"

first_letter = name[0]

print(first_letter)
# K

# ============================================================
# 37. PRACTICAL EXAMPLE — LAST LETTER
# ============================================================

name = "Kishor"

last_letter = name[-1]

print(last_letter)
# r

# ============================================================
# 38. PRACTICAL EXAMPLE — FILE NAME
# ============================================================

filename = "program.py"

# Last character
print(filename[-1])
# y

# Character before extension
print(filename[-4])
# .

# ============================================================
# 39. PRACTICAL EXAMPLE — EMAIL
# ============================================================

email = "user@example.com"

# First character
print(email[0])
# u

# Last character
print(email[-1])
# m

# ============================================================
# 40. IMPORTANT INDEXING RULES
# ============================================================

"""
RULE 1:
    Indexing starts from 0.

RULE 2:
    The first character is at index 0.

RULE 3:
    The last character is at index len(string) - 1.

RULE 4:
    Negative indexing starts from -1.

RULE 5:
    -1 always represents the last character.

RULE 6:
    Spaces are characters and have indexes.

RULE 7:
    Special characters are also characters and have indexes.

RULE 8:
    Unicode characters can be accessed using indexing.

RULE 9:
    Invalid indexes raise IndexError.

RULE 10:
    Strings are immutable, so indexed characters cannot
    be assigned directly.
"""

# ============================================================
# 41. INDEXING CHEAT SHEET
# ============================================================

"""
Given:

    text = "Python"

Positive indexes:

    text[0] -> P
    text[1] -> y
    text[2] -> t
    text[3] -> h
    text[4] -> o
    text[5] -> n

Negative indexes:

    text[-1] -> n
    text[-2] -> o
    text[-3] -> h
    text[-4] -> t
    text[-5] -> y
    text[-6] -> P

Important:

    First character -> text[0]
    Last character  -> text[-1]

    First index     -> 0
    Last index      -> len(text) - 1
"""

# ============================================================
# 42. INDEXING VS SLICING
# ============================================================

"""
INDEXING:

    text[0]

Returns one character.

Example:

    text = "Python"

    text[0]
    -> "P"

SLICING:

    text[0:3]

Returns a portion of the string.

Example:

    text = "Python"

    text[0:3]
    -> "Pyt"

Key difference:

    Indexing -> individual character
    Slicing  -> substring
"""

# ============================================================
# 43. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

Use positive indexing when:

    - You know the position from the beginning.

Use negative indexing when:

    - You need characters near the end.
    - You want cleaner code such as text[-1].

Use enumerate() when:

    - You need both index and character while iterating.

Use len() when:

    - You need to determine valid index boundaries.

Remember:

    text[0]
        First character

    text[-1]
        Last character

    text[len(text) - 1]
        Last character

    text[index]
        Character at a specific position

Invalid:

    text[len(text)]

because the maximum valid positive index is:

    len(text) - 1
"""

# ============================================================
# END
# ============================================================

print("\nString indexing demonstration completed successfully!")
```
