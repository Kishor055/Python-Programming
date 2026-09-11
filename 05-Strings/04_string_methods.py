```
"""
04_string_methods.py
====================

Python String Methods
---------------------

This file demonstrates commonly used Python string methods.

String methods do not modify the original string because strings
are immutable. Most methods return a new string or another value.
"""

# ============================================================
# 1. CASE CONVERSION METHODS
# ============================================================

text = "python programming language"

# upper() -> Converts all characters to uppercase
print(text.upper())
# PYTHON PROGRAMMING LANGUAGE

# lower() -> Converts all characters to lowercase
text = "PYTHON PROGRAMMING LANGUAGE"
print(text.lower())
# python programming language

# capitalize() -> Converts first character to uppercase
# and the remaining characters to lowercase
text = "python PROGRAMMING"
print(text.capitalize())
# Python programming

# title() -> Converts the first character of each word to uppercase
text = "python programming language"
print(text.title())
# Python Programming Language

# swapcase() -> Swaps uppercase characters to lowercase
# and lowercase characters to uppercase
text = "Python Programming"
print(text.swapcase())
# pYTHON pROGRAMMING

# casefold() -> Converts text to a normalized lowercase form
# Useful for case-insensitive comparisons
a = "Python"
b = "PYTHON"

print(a.casefold() == b.casefold())
# True

# ============================================================
# 2. SEARCHING METHODS
# ============================================================

text = "Python Programming"

# find() -> Returns the first index of the substring
# Returns -1 if the substring is not found
print(text.find("Program"))
# 7

print(text.find("Java"))
# -1

# rfind() -> Returns the last index of the substring
text = "Python Python Python"
print(text.rfind("Python"))
# 14

# index() -> Returns the first index of the substring
# Raises ValueError if the substring is not found
text = "Python Programming"
print(text.index("Program"))
# 7

# rindex() -> Returns the last index of the substring
text = "Python Python Python"
print(text.rindex("Python"))
# 14

# count() -> Counts the number of non-overlapping occurrences
text = "banana"
print(text.count("a"))
# 3

print(text.count("an"))
# 1

# ============================================================
# 3. PREFIX AND SUFFIX METHODS
# ============================================================

text = "Python Programming"

# startswith() -> Checks whether the string starts with a value
print(text.startswith("Python"))
# True

print(text.startswith("Java"))
# False

# endswith() -> Checks whether the string ends with a value
print(text.endswith("Programming"))
# True

print(text.endswith("Java"))
# False

# ============================================================
# 4. WHITESPACE METHODS
# ============================================================

text = "   Python Programming   "

# strip() -> Removes leading and trailing whitespace
print(text.strip())
# Python Programming

# lstrip() -> Removes leading whitespace
print(text.lstrip())
# Python Programming

# rstrip() -> Removes trailing whitespace
print(text.rstrip())
#    Python Programming

# ============================================================
# 5. REMOVING SPECIFIC CHARACTERS
# ============================================================

text = "...Python..."

# strip(chars) -> Removes specified characters from both ends
print(text.strip("."))
# Python

# lstrip(chars) -> Removes specified characters from the left
print(text.lstrip("."))
# Python...

# rstrip(chars) -> Removes specified characters from the right
print(text.rstrip("."))
# ...Python

# ============================================================
# 6. REPLACEMENT METHODS
# ============================================================

text = "I love Java"

# replace() -> Replaces occurrences of one substring with another
print(text.replace("Java", "Python"))
# I love Python

# replace(old, new, count) -> Limits the number of replacements
text = "apple apple apple"

print(text.replace("apple", "orange", 2))
# orange orange apple

# ============================================================
# 7. SPLITTING METHODS
# ============================================================

text = "Python Java C++"

# split() -> Splits the string into a list
# Default separator is whitespace
print(text.split())
# ['Python', 'Java', 'C++']

# split(separator) -> Splits using a specified separator
text = "Python,Java,C++"

print(text.split(","))
# ['Python', 'Java', 'C++']

# split(separator, maxsplit) -> Limits the number of splits
text = "one-two-three-four"

print(text.split("-", 2))
# ['one', 'two', 'three-four']

# rsplit() -> Splits from the right side
text = "one-two-three-four"

print(text.rsplit("-", 2))
# ['one-two', 'three', 'four']

# splitlines() -> Splits a multiline string into a list of lines
text = "Python\nJava\nC++"

print(text.splitlines())
# ['Python', 'Java', 'C++']

# ============================================================
# 8. JOIN METHOD
# ============================================================

words = ["Python", "is", "powerful"]

# join() -> Joins iterable elements using the calling string
result = " ".join(words)

print(result)
# Python is powerful

# Join using a comma
result = ", ".join(words)

print(result)
# Python, is, powerful

# Join using a hyphen
result = "-".join(words)

print(result)
# Python-is-powerful

# ============================================================
# 9. PARTITION METHODS
# ============================================================

text = "Python-Programming"

# partition() -> Splits the string into three parts:
# before separator, separator, after separator
print(text.partition("-"))
# ('Python', '-', 'Programming')

# rpartition() -> Performs partitioning from the right
text = "Python-Programming-Language"

print(text.rpartition("-"))
# ('Python-Programming', '-', 'Language')

# ============================================================
# 10. CHARACTER VALIDATION METHODS
# ============================================================

# isalpha() -> True if all characters are alphabetic
print("Python".isalpha())
# True

print("Python123".isalpha())
# False

# isdigit() -> True if all characters are digits
print("12345".isdigit())
# True

print("123abc".isdigit())
# False

# isalnum() -> True if all characters are alphabetic or numeric
print("Python123".isalnum())
# True

print("Python 123".isalnum())
# False

# isdecimal() -> True if all characters are decimal characters
print("12345".isdecimal())
# True

# isnumeric() -> True if all characters are numeric
print("12345".isnumeric())
# True

# isascii() -> True if all characters are ASCII
print("Python".isascii())
# True

print("नमस्ते".isascii())
# False

# ============================================================
# 11. CASE VALIDATION METHODS
# ============================================================

# islower() -> True if all cased characters are lowercase
print("python".islower())
# True

print("Python".islower())
# False

# isupper() -> True if all cased characters are uppercase
print("PYTHON".isupper())
# True

print("Python".isupper())
# False

# istitle() -> True if the string follows title-case rules
print("Python Programming".istitle())
# True

print("python programming".istitle())
# False

# ============================================================
# 12. WHITESPACE VALIDATION
# ============================================================

# isspace() -> True if the string contains only whitespace
print("   ".isspace())
# True

print("Python".isspace())
# False

# ============================================================
# 13. IDENTIFIER VALIDATION
# ============================================================

# isidentifier() -> Checks whether the string is a valid
# Python identifier
print("variable".isidentifier())
# True

print("my_variable".isidentifier())
# True

print("123variable".isidentifier())
# False

print("my-variable".isidentifier())
# False

# ============================================================
# 14. PRINTABLE CHARACTER VALIDATION
# ============================================================

# isprintable() -> True if all characters are printable
print("Hello World!".isprintable())
# True

print("Hello\nWorld".isprintable())
# False

# ============================================================
# 15. PREFIX/SUFFIX REMOVAL
# ============================================================

text = "PythonProgramming"

# removeprefix() -> Removes the specified prefix if present
print(text.removeprefix("Python"))
# Programming

# removesuffix() -> Removes the specified suffix if present
print(text.removesuffix("Programming"))
# Python

# ============================================================
# 16. STRING TRANSLATION
# ============================================================

# maketrans() -> Creates a translation table
# translate() -> Applies the translation table

translation_table = str.maketrans(
    "abc",
    "123"
)

text = "abc cab"

print(text.translate(translation_table))
# 123 312

# ============================================================
# 17. TRANSLATE WITH DELETION
# ============================================================

# Characters can be removed by passing None
translation_table = str.maketrans(
    "",
    "",
    "aeiou"
)

text = "Python Programming"

print(text.translate(translation_table))
# Pythn Prgrmmng

# ============================================================
# 18. CENTER / ALIGNMENT METHODS
# ============================================================

text = "Python"

# center(width) -> Centers the string inside the given width
print(text.center(20))
#        Python

# center(width, fillchar) -> Uses a custom fill character
print(text.center(20, "-"))
# -------Python-------

# ljust(width) -> Left-aligns the string
print(text.ljust(15, "-"))
# Python---------

# rjust(width) -> Right-aligns the string
print(text.rjust(15, "-"))
# ---------Python

# ============================================================
# 19. ZERO-FILL
# ============================================================

number = "42"

# zfill(width) -> Pads the string with zeros on the left
print(number.zfill(5))
# 00042

number = "-42"

print(number.zfill(5))
# -0042

# ============================================================
# 20. EXPAND TABS
# ============================================================

text = "Name:\tKishor"

# expandtabs() -> Replaces tab characters with spaces
print(text.expandtabs(4))
# Name:   Kishor

# ============================================================
# 21. ENCODING
# ============================================================

text = "Python"

# encode() -> Converts a string into bytes
data = text.encode("utf-8")

print(data)
# b'Python'

print(type(data))
# <class 'bytes>'

# ============================================================
# 22. STRING FORMATTING METHODS
# ============================================================

name = "Kishor"
age = 25

# format() -> Inserts values into placeholders
print("Name: {}, Age: {}".format(name, age))
# Name: Kishor, Age: 25

# Positional formatting
print("{0} is {1} years old.".format(name, age))
# Kishor is 25 years old.

# Named formatting
print(
    "Name: {name}, Age: {age}".format(
        name=name,
        age=age
    )
)
# Name: Kishor, Age: 25

# ============================================================
# 23. CASE-INSENSITIVE COMPARISON
# ============================================================

username_1 = "KISHOR"
username_2 = "kishor"

# casefold() is useful for Unicode-aware case-insensitive comparison
print(username_1.casefold() == username_2.casefold())
# True

# ============================================================
# 24. PRACTICAL EXAMPLE — CLEAN USER INPUT
# ============================================================

user_input = "   Kishor   "

# strip() removes unwanted surrounding whitespace
# title() converts the text to title case
clean_name = user_input.strip().title()

print(clean_name)
# Kishor

# ============================================================
# 25. PRACTICAL EXAMPLE — EMAIL VALIDATION
# ============================================================

email = "user@example.com"

# lower() can normalize case for basic email comparisons
email = email.strip().lower()

print(email)
# user@example.com

# startswith() and endswith() can perform simple checks
print(email.startswith("user"))
# True

print(email.endswith(".com"))
# True

# ============================================================
# 26. PRACTICAL EXAMPLE — CSV DATA
# ============================================================

data = "Kishor,25,Python"

# split() converts delimited text into a list
name, age, language = data.split(",")

print(name)
# Kishor

print(age)
# 25

print(language)
# Python

# ============================================================
# 27. PRACTICAL EXAMPLE — WORD CLEANING
# ============================================================

text = "   Python   Programming   "

# strip() -> Removes outer whitespace
# split() -> Separates words
# join() -> Rebuilds the string with a single space

clean_text = " ".join(text.strip().split())

print(clean_text)
# Python Programming

# ============================================================
# 28. QUICK STRING METHODS REFERENCE
# ============================================================

"""
CASE:
    upper()
    lower()
    capitalize()
    title()
    swapcase()
    casefold()

SEARCH:
    find()
    rfind()
    index()
    rindex()
    count()

PREFIX / SUFFIX:
    startswith()
    endswith()
    removeprefix()
    removesuffix()

WHITESPACE:
    strip()
    lstrip()
    rstrip()
    expandtabs()

REPLACE:
    replace()

SPLIT / JOIN:
    split()
    rsplit()
    splitlines()
    join()

PARTITION:
    partition()
    rpartition()

VALIDATION:
    isalpha()
    isalnum()
    isascii()
    isdecimal()
    isdigit()
    isnumeric()
    isidentifier()
    islower()
    isupper()
    istitle()
    isspace()
    isprintable()

ALIGNMENT:
    center()
    ljust()
    rjust()
    zfill()

TRANSLATION:
    maketrans()
    translate()

ENCODING:
    encode()

FORMATTING:
    format()
"""

# ============================================================
# 29. IMPORTANT RULE
# ============================================================

"""
IMPORTANT:

Python strings are immutable.

String methods do NOT modify the original string.

Example:

    text = "python"

    text.upper()

The result is created but not stored.

To keep the result:

    text = text.upper()

Example:
"""

text = "python"

text = text.upper()

print(text)
# PYTHON

# ============================================================
# END
# ============================================================

print("\nString methods demonstration completed successfully!")
```
