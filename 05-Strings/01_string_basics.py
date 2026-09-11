```
"""
01_string_basics.py
===================

Python String Basics
--------------------

A string is a sequence of characters enclosed inside quotes.

Python supports:

    - Single quotes: 'Hello'
    - Double quotes: "Hello"
    - Triple single quotes: '''Hello'''
    - Triple double quotes: """Hello"""

Strings are:

    - Ordered
    - Indexed
    - Iterable
    - Immutable
    - Unicode-aware
"""

# ============================================================
# 1. CREATING STRINGS
# ============================================================

single_quote = 'Hello Python'
double_quote = "Hello Python"

print(single_quote)
print(double_quote)

# ============================================================
# 2. SINGLE QUOTES
# ============================================================

name = 'Kishor'

print(name)

# ============================================================
# 3. DOUBLE QUOTES
# ============================================================

message = "Welcome to Python"

print(message)

# ============================================================
# 4. USING QUOTES INSIDE A STRING
# ============================================================

# Double quotes can contain single quotes
message = "Python's syntax is simple"

print(message)

# Single quotes can contain double quotes
message = 'Python is called "easy to learn"'

print(message)

# ============================================================
# 5. ESCAPE CHARACTERS
# ============================================================

# Backslash is used to create escape sequences.

# \' -> Single quote
print('Python\'s programming')

# \" -> Double quote
print("He said \"Hello\"")

# \\ -> Backslash
print("C:\\Users\\Kishor")

# \n -> New line
print("Hello\nPython")

# \t -> Tab
print("Python\tProgramming")

# ============================================================
# 6. COMMON ESCAPE SEQUENCES
# ============================================================

"""
Common escape sequences:

    \\n   New line
    \\t   Tab
    \\\\   Backslash
    \\'   Single quote
    \\"   Double quote
    \\r   Carriage return
    \\b   Backspace
"""

# ============================================================
# 7. MULTILINE STRINGS
# ============================================================

message = """
Python is a programming language.
It is easy to learn.
It is widely used.
"""

print(message)

# ============================================================
# 8. TRIPLE SINGLE QUOTES
# ============================================================

message = '''
This is a
multiline string.
'''

print(message)

# ============================================================
# 9. TRIPLE DOUBLE QUOTES
# ============================================================

message = """
This is another
multiline string.
"""

print(message)

# ============================================================
# 10. STRING WITH NEWLINES
# ============================================================

message = "Python\nJava\nC++"

print(message)

# ============================================================
# 11. STRING LENGTH
# ============================================================

text = "Python"

# len() returns the number of characters.
length = len(text)

print(length)
# 6

# ============================================================
# 12. STRINGS ARE SEQUENCES
# ============================================================

text = "Python"

# A string contains characters in a specific order.
print(text[0])
print(text[1])
print(text[2])

# ============================================================
# 13. STRING TYPE
# ============================================================

text = "Python"

# type() returns the data type.
print(type(text))
# <class 'str'>

# ============================================================
# 14. EMPTY STRING
# ============================================================

empty_string = ""

print(empty_string)
print(len(empty_string))
# 0

# ============================================================
# 15. STRING WITH NUMBERS
# ============================================================

text = "12345"

# Numbers inside quotes are characters, not integers.
print(text)
print(type(text))

# ============================================================
# 16. INTEGER VS STRING
# ============================================================

number = 100
text = "100"

print(number)
print(type(number))

print(text)
print(type(text))

# ============================================================
# 17. CONVERT NUMBER TO STRING
# ============================================================

number = 100

text = str(number)

print(text)
print(type(text))

# ============================================================
# 18. CONVERT STRING TO INTEGER
# ============================================================

text = "100"

number = int(text)

print(number)
print(type(number))

# ============================================================
# 19. STRING CONCATENATION
# ============================================================

first_name = "Kishor"
last_name = "Patil"

full_name = first_name + " " + last_name

print(full_name)

# ============================================================
# 20. STRING REPETITION
# ============================================================

text = "Python "

# * repeats a string.
print(text * 3)

# Output:
# Python Python Python

# ============================================================
# 21. STRING MEMBERSHIP
# ============================================================

text = "Python Programming"

# in -> checks whether a substring exists
print("Python" in text)
# True

print("Java" in text)
# False

# not in -> checks whether a substring does not exist
print("Java" not in text)
# True

# ============================================================
# 22. MULTILINE STRING AS A DOCUMENT
# ============================================================

description = """
Python is a high-level programming language.
It supports multiple programming paradigms.
"""

print(description)

# ============================================================
# 23. RAW STRINGS
# ============================================================

# Raw strings treat backslashes mostly as literal characters.

path = r"C:\Users\Kishor\Documents"

print(path)

# ============================================================
# 24. UNICODE STRINGS
# ============================================================

# Python 3 strings support Unicode characters.

text = "Hello 🌍"

print(text)

text = "नमस्ते"

print(text)

text = "Python 🐍"

print(text)

# ============================================================
# 25. STRING COMPARISON
# ============================================================

first = "Python"
second = "Python"

print(first == second)
# True

print(first != second)
# False

# ============================================================
# 26. CASE-SENSITIVE COMPARISON
# ============================================================

first = "Python"
second = "python"

print(first == second)
# False

# Strings are case-sensitive by default.

# ============================================================
# 27. LEXICOGRAPHICAL COMPARISON
# ============================================================

print("apple" < "banana")
# True

print("cat" > "apple")
# True

# String comparison is based on character ordering.

# ============================================================
# 28. ITERATING THROUGH A STRING
# ============================================================

text = "Python"

for character in text:
    print(character)

# ============================================================
# 29. STRING VARIABLES
# ============================================================

language = "Python"
version = "3"

print(language)
print(version)

# ============================================================
# 30. MULTIPLE STRING VARIABLES
# ============================================================

first_name = "Kishor"
city = "Aurangabad"
language = "Python"

print(first_name)
print(city)
print(language)

# ============================================================
# 31. STRING WITH LEADING/TRAILING SPACES
# ============================================================

text = "   Python   "

print(text)

# strip() is used to remove surrounding whitespace.
print(text.strip())

# ============================================================
# 32. BASIC STRING METHODS
# ============================================================

text = "python programming"

# upper() -> Converts to uppercase
print(text.upper())

# lower() -> Converts to lowercase
print(text.lower())

# title() -> Capitalizes each word
print(text.title())

# capitalize() -> Capitalizes the first character
print(text.capitalize())

# ============================================================
# 33. STRING IMMUTABILITY
# ============================================================

text = "Python"

"""
Strings are immutable.

This is invalid:

    text[0] = "J"

A string cannot be modified character-by-character.

Instead, create a new string.
"""

new_text = "J" + text[1:]

print(text)
# Python

print(new_text)
# Jython

# ============================================================
# 34. CHECK WHETHER A VALUE IS A STRING
# ============================================================

value = "Python"

print(isinstance(value, str))
# True

value = 100

print(isinstance(value, str))
# False

# ============================================================
# 35. STRING WITH SPECIAL CHARACTERS
# ============================================================

text = "Python@123!"

print(text)

# ============================================================
# 36. STRING WITH SPACES
# ============================================================

text = "Python Programming Language"

print(text)

# ============================================================
# 37. STRING LITERALS
# ============================================================

"""
A string literal is a sequence of characters written directly
inside quotes.

Examples:

    "Python"
    'Python'
    """Python"""
    '''Python'''
"""

# ============================================================
# 38. DOCSTRINGS
# ============================================================

def greet():
    """Return a simple greeting message."""
    return "Hello Python"

print(greet())

# ============================================================
# 39. BASIC STRING FORMATTING
# ============================================================

name = "Kishor"
age = 25

# f-string
message = f"My name is {name} and I am {age} years old."

print(message)

# ============================================================
# 40. STRING CONCATENATION WITH DIFFERENT TYPES
# ============================================================

name = "Kishor"
age = 25

# Convert non-string values before concatenation.
message = "Name: " + name + ", Age: " + str(age)

print(message)

# ============================================================
# 41. USING print() WITH MULTIPLE VALUES
# ============================================================

name = "Kishor"
age = 25

# print() automatically separates values with a space.
print("Name:", name, "Age:", age)

# ============================================================
# 42. STRING TRUTHINESS
# ============================================================

# Empty strings are False in a Boolean context.
text = ""

print(bool(text))
# False

# Non-empty strings are True.
text = "Python"

print(bool(text))
# True

# ============================================================
# 43. STRING WITH WHITESPACE IS NOT EMPTY
# ============================================================

text = " "

print(bool(text))
# True

# A space is still a character.

# ============================================================
# 44. CHECK EMPTY STRING
# ============================================================

text = ""

if text:
    print("String is not empty")
else:
    print("String is empty")

# ============================================================
# 45. STRING LENGTH WITH SPACES
# ============================================================

text = "Hello World"

# Space is also counted as a character.
print(len(text))
# 11

# ============================================================
# 46. BASIC STRING OPERATIONS
# ============================================================

first = "Python"
second = "Programming"

# Concatenation
print(first + " " + second)

# Repetition
print(first * 2)

# Membership
print("Python" in first)

# Length
print(len(first))

# ============================================================
# 47. PRACTICAL EXAMPLE — USER PROFILE
# ============================================================

name = "Kishor"
profession = "Python Developer"
city = "Aurangabad"

profile = (
    f"Name       : {name}\n"
    f"Profession : {profession}\n"
    f"City       : {city}"
)

print(profile)

# ============================================================
# 48. PRACTICAL EXAMPLE — GREETING
# ============================================================

name = "Kishor"

greeting = "Hello, " + name + "!"

print(greeting)

# ============================================================
# 49. PRACTICAL EXAMPLE — WEBSITE URL
# ============================================================

domain = "example.com"

url = "https://" + domain

print(url)

# ============================================================
# 50. PRACTICAL EXAMPLE — USER INPUT
# ============================================================

name = input("Enter your name: ")

print("Hello,", name)

# ============================================================
# 51. INPUT ALWAYS RETURNS A STRING
# ============================================================

"""
input() always returns a string.

Example:

    age = input("Enter age: ")

Even if the user enters:

    25

the value is:

    "25"

To convert it into an integer:

    age = int(input("Enter age: "))
"""

# ============================================================
# 52. STRING TYPE CHECKING
# ============================================================

text = "Python"

if isinstance(text, str):
    print("The value is a string")

# ============================================================
# 53. STRING BASICS CHEAT SHEET
# ============================================================

"""
CREATION:

    "Python"
    'Python'
    '''Python'''
    \"\"\"Python\"\"\"

LENGTH:

    len(text)

CONCATENATION:

    text1 + text2

REPETITION:

    text * 3

MEMBERSHIP:

    "Python" in text
    "Java" not in text

TYPE:

    type(text)
    isinstance(text, str)

CONVERSION:

    str(value)

ITERATION:

    for character in text:
        print(character)

COMMON METHODS:

    upper()
    lower()
    title()
    capitalize()
    strip()

INDEXING:

    text[0]
    text[-1]

SLICING:

    text[0:3]
    text[:3]
    text[3:]
    text[::-1]

FORMATTING:

    f"Hello {name}"
"""

# ============================================================
# 54. IMPORTANT STRING RULES
# ============================================================

"""
IMPORTANT RULES
---------------

1. Strings are sequences of characters.

2. Strings can be created using single, double, or triple quotes.

3. Python strings are Unicode-aware.

4. Strings are immutable.

5. Indexing starts from zero.

6. Negative indexes start from -1.

7. len() returns the number of characters.

8. Spaces are characters.

9. input() returns a string.

10. Use str() to convert a value into a string.

11. Use int(), float(), etc. to convert strings into numbers
    when the content is valid.

12. Use f-strings for clean and readable string formatting.
"""

# ============================================================
# END
# ============================================================

print("\nString basics demonstration completed successfully!")
```
