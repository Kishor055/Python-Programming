```
"""
03_string_slicing.py
====================

Python String Slicing
---------------------

String slicing is used to extract a portion of a string.

Syntax:

    string[start:stop:step]

Rules:

    start -> Starting index (included)
    stop  -> Ending index (excluded)
    step  -> Direction / number of positions to move

Important:

    - Python uses zero-based indexing.
    - The stop index is always excluded.
    - Slicing does not modify the original string.
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
#
# Negative indexes:
#
#    -6  -5  -4  -3  -2  -1
#     P   y   t   h   o   n

# ============================================================
# 2. BASIC SLICING
# ============================================================

# Syntax:
#
# string[start:stop]

text = "Python"

print(text[0:2])
# Py

print(text[1:4])
# yth

print(text[2:5])
# tho

# ============================================================
# 3. START INDEX IS INCLUDED
# ============================================================

text = "Python"

# Index 1 is included
print(text[1:4])
# yth

# ============================================================
# 4. STOP INDEX IS EXCLUDED
# ============================================================

text = "Python"

# Index 4 is NOT included
print(text[1:4])
# yth

# ============================================================
# 5. SLICE FROM START
# ============================================================

text = "Python"

# Omitting start means start from index 0
print(text[:3])
# Pyt

# Equivalent:
print(text[0:3])
# Pyt

# ============================================================
# 6. SLICE TO END
# ============================================================

text = "Python"

# Omitting stop means continue to the end
print(text[3:])
# hon

# Equivalent:
print(text[3:len(text)])
# hon

# ============================================================
# 7. COPY THE ENTIRE STRING
# ============================================================

text = "Python"

# Both start and stop are omitted
print(text[:])
# Python

# ============================================================
# 8. NEGATIVE INDEX SLICING
# ============================================================

text = "Python"

# Negative indexes:
#
#    P   y   t   h   o   n
#   -6  -5  -4  -3  -2  -1

print(text[-3:])
# hon

print(text[:-2])
# Pyth

print(text[-5:-2])
# yth

# ============================================================
# 9. SLICING WITH STEP
# ============================================================

text = "Python"

# Syntax:
#
# string[start:stop:step]

print(text[0:6:1])
# Python

print(text[0:6:2])
# Pto

print(text[1:6:2])
# yhn

# ============================================================
# 10. STEP OF 2
# ============================================================

text = "Python Programming"

# Take every second character
print(text[::2])

# ============================================================
# 11. STEP OF 3
# ============================================================

text = "Python Programming"

# Take every third character
print(text[::3])

# ============================================================
# 12. SKIP CHARACTERS
# ============================================================

text = "ABCDEFGHIJ"

print(text[::2])
# ACEGI

print(text[::3])
# ADGJ

# ============================================================
# 13. NEGATIVE STEP
# ============================================================

text = "Python"

# Negative step moves from right to left
print(text[::-1])
# nohtyP

# ============================================================
# 14. REVERSE A STRING
# ============================================================

text = "Python"

# [::-1] is the common Python technique for reversing a string
reverse = text[::-1]

print(reverse)
# nohtyP

# ============================================================
# 15. REVERSE WITH A STEP
# ============================================================

text = "ABCDEFGHIJ"

# Reverse and take every second character
print(text[::-2])
# JHFDB

# ============================================================
# 16. REVERSE PART OF A STRING
# ============================================================

text = "Python"

# Reverse characters from index 4 down to index 1
print(text[4:0:-1])
# ohty

# ============================================================
# 17. OMIT START WITH NEGATIVE STEP
# ============================================================

text = "Python"

# When start is omitted with a negative step,
# Python starts from the last valid index.
print(text[: : -1])
# nohtyP

# Equivalent:
print(text[len(text) - 1::-1])
# nohtyP

# ============================================================
# 18. OMIT STOP WITH NEGATIVE STEP
# ============================================================

text = "Python"

# Start from index 5 and move backwards
print(text[5::-1])
# nohtyP

# ============================================================
# 19. PARTIAL REVERSE
# ============================================================

text = "ABCDEFGHIJ"

# Start at index 7 and move backwards until index 2
# Index 2 is excluded
print(text[7:2:-1])
# HGFED

# ============================================================
# 20. SLICE USING VARIABLES
# ============================================================

text = "Python Programming"

start = 0
stop = 6

print(text[start:stop])
# Python

# ============================================================
# 21. DYNAMIC STEP
# ============================================================

text = "ABCDEFGHIJ"

step = 2

print(text[::step])
# ACEGI

# ============================================================
# 22. FIRST THREE CHARACTERS
# ============================================================

text = "Python"

first_three = text[:3]

print(first_three)
# Pyt

# ============================================================
# 23. LAST THREE CHARACTERS
# ============================================================

text = "Python"

last_three = text[-3:]

print(last_three)
# hon

# ============================================================
# 24. FIRST CHARACTER
# ============================================================

text = "Python"

# Slicing returns a string
first_character = text[:1]

print(first_character)
# P

# ============================================================
# 25. LAST CHARACTER
# ============================================================

text = "Python"

last_character = text[-1:]

print(last_character)
# n

# ============================================================
# 26. REMOVE FIRST CHARACTER
# ============================================================

text = "Python"

result = text[1:]

print(result)
# ython

# ============================================================
# 27. REMOVE LAST CHARACTER
# ============================================================

text = "Python"

result = text[:-1]

print(result)
# Pytho

# ============================================================
# 28. REMOVE FIRST AND LAST CHARACTER
# ============================================================

text = "Python"

result = text[1:-1]

print(result)
# ytho

# ============================================================
# 29. EXTRACT MIDDLE
# ============================================================

text = "Python"

result = text[1:5]

print(result)
# ytho

# ============================================================
# 30. EVERY OTHER CHARACTER
# ============================================================

text = "Python"

result = text[::2]

print(result)
# Pto

# ============================================================
# 31. ODD INDEX CHARACTERS
# ============================================================

text = "Python"

# Start from index 1 and take every second character
result = text[1::2]

print(result)
# yhn

# ============================================================
# 32. EVEN INDEX CHARACTERS
# ============================================================

text = "Python"

# Start from index 0 and take every second character
result = text[::2]

print(result)
# Pto

# ============================================================
# 33. STRING SLICING WITH LEN()
# ============================================================

text = "Python"

length = len(text)

print(text[0:length])
# Python

# ============================================================
# 34. OUT-OF-RANGE STOP INDEX
# ============================================================

text = "Python"

# Slicing is safe even when stop is larger than the string
print(text[0:100])
# Python

# ============================================================
# 35. OUT-OF-RANGE START INDEX
# ============================================================

text = "Python"

# Start beyond the end returns an empty string
print(text[100:200])
# ''

# ============================================================
# 36. NEGATIVE OUT-OF-RANGE INDEX
# ============================================================

text = "Python"

# Negative slicing indexes outside the string are handled safely
print(text[-100:3])
# Pyt

# ============================================================
# 37. EMPTY SLICE
# ============================================================

text = "Python"

print(text[3:3])
# ''

print(text[5:2])
# ''

# ============================================================
# 38. STEP CANNOT BE ZERO
# ============================================================

"""
A slice step cannot be zero.

This is invalid:

    text[::0]

It raises:

    ValueError: slice step cannot be zero
"""

# ============================================================
# 39. STRING SLICING IS NON-DESTRUCTIVE
# ============================================================

text = "Python"

result = text[:3]

print(result)
# Pyt

# Original string remains unchanged
print(text)
# Python

# ============================================================
# 40. STRINGS ARE IMMUTABLE
# ============================================================

text = "Python"

# Slicing creates a new string.
# It does not modify the original string.

result = text[1:]

print(text)
# Python

print(result)
# ython

# ============================================================
# 41. REPLACE PART OF A STRING USING SLICING
# ============================================================

text = "Python"

# Replace first character with "J"
result = "J" + text[1:]

print(result)
# Jython

# The original string is unchanged
print(text)
# Python

# ============================================================
# 42. REMOVE PART OF A STRING USING SLICING
# ============================================================

text = "Python Programming"

# Remove "Python "
result = text[7:]

print(result)
# Programming

# ============================================================
# 43. COMBINE MULTIPLE SLICES
# ============================================================

text = "Python Programming"

# Extract "Python" and "Programming"
first = text[:6]
second = text[7:]

print(first)
# Python

print(second)
# Programming

# ============================================================
# 44. PALINDROME CHECK
# ============================================================

text = "madam"

# A palindrome reads the same forwards and backwards.
is_palindrome = text == text[::-1]

print(is_palindrome)
# True

# ============================================================
# 45. CASE-INSENSITIVE PALINDROME
# ============================================================

text = "Madam"

normalized = text.lower()

print(normalized == normalized[::-1])
# True

# ============================================================
# 46. REVERSE WORDS USING SLICING
# ============================================================

text = "Python"

characters = text[::-1]

print(characters)
# nohtyP

# ============================================================
# 47. EXTRACT FILE EXTENSION
# ============================================================

filename = "program.py"

extension = filename[filename.rfind(".") + 1:]

print(extension)
# py

# ============================================================
# 48. EXTRACT LAST N CHARACTERS
# ============================================================

filename = "program.py"

# Last 3 characters
print(filename[-3:])
# py

# ============================================================
# 49. EXTRACT DOMAIN FROM EMAIL
# ============================================================

email = "user@example.com"

at_position = email.find("@")

domain = email[at_position + 1:]

print(domain)
# example.com

# ============================================================
# 50. SLICE SYNTAX CHEAT SHEET
# ============================================================

"""
Given:

    text = "Python"

Index:

     P   y   t   h   o   n
     0   1   2   3   4   5
    -6  -5  -4  -3  -2  -1

Basic:

    text[0:3]       -> "Pyt"
    text[:3]        -> "Pyt"
    text[3:]        -> "hon"
    text[:]         -> "Python"

Negative:

    text[-3:]       -> "hon"
    text[:-2]       -> "Pyth"
    text[-5:-2]     -> "yth"

Step:

    text[::2]       -> "Pto"
    text[1::2]      -> "yhn"
    text[::3]       -> "Ph"

Reverse:

    text[::-1]      -> "nohtyP"
    text[::-2]      -> "nhy"

General syntax:

    text[start:stop:step]

Important rules:

    start -> included
    stop  -> excluded
    step  -> controls direction and interval

    Positive step -> left to right
    Negative step -> right to left
    step = 0      -> ValueError
"""

# ============================================================
# 51. COMMON SLICING PATTERNS
# ============================================================

"""
Common patterns:

    text[:n]
        First n characters

    text[-n:]
        Last n characters

    text[n:]
        Everything after index n

    text[:-n]
        Everything except last n characters

    text[::2]
        Every second character

    text[1::2]
        Characters at odd indexes

    text[::3]
        Every third character

    text[::-1]
        Reverse string

    text[1:-1]
        Remove first and last character

    text[:]
        Full shallow slice/copy of the string value
"""

# ============================================================
# 52. INTERVIEW-STYLE EXAMPLES
# ============================================================

text = "ABCDEFGHIJ"

# First 5 characters
print(text[:5])
# ABCDE

# Last 5 characters
print(text[-5:])
# FGHIJ

# Remove first 2 characters
print(text[2:])
# CDEFGHIJ

# Remove last 2 characters
print(text[:-2])
# ABCDEFGH

# Reverse
print(text[::-1])
# JIHGFEDCBA

# Every second character
print(text[::2])
# ACEGI

# Every second character from index 1
print(text[1::2])
# BDFHJ

# Reverse every second character
print(text[::-2])
# JHFDB

# ============================================================
# 53. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

1. Slicing uses:

       start:stop:step

2. The stop index is exclusive.

3. Positive step moves from left to right.

4. Negative step moves from right to left.

5. Strings are immutable.

6. Slicing returns a new string.

7. Slicing generally does not raise IndexError for
   out-of-range boundaries.

8. A slice step of zero is invalid.

9. [::-1] is the standard Python idiom for reversing
   a sequence.

10. Use slicing when the operation is simple and readable.

11. For complex text processing, prefer appropriate
    string methods such as split(), replace(), find(),
    startswith(), endswith(), etc.
"""

# ============================================================
# END
# ============================================================

print("\nString slicing demonstration completed successfully!")
```
