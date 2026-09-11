For `05-Strings/05_string_formatting.py`, I’d make it a **professional, runnable teaching file** that covers the major formatting approaches, format specifiers, alignment, numbers, dates, expressions, and common mistakes.

```
"""
05_string_formatting.py
=======================

Python String Formatting
------------------------

This file covers:

1. Why string formatting is needed
2. String concatenation
3. str.format()
4. Positional arguments
5. Named arguments
6. Index-based formatting
7. f-strings
8. Expressions inside f-strings
9. Number formatting
10. Decimal precision
11. Percentage formatting
12. Thousands separators
13. Alignment and width
14. Padding
15. Sign formatting
16. Binary, octal, hexadecimal
17. Scientific notation
18. Date/time formatting
19. Nested formatting
20. Raw strings + f-strings
21. Old-style % formatting
22. Common mistakes
23. Best practices

Run:
    python 05_string_formatting.py
"""

# ============================================================
# 1. WHY STRING FORMATTING?
# ============================================================

print("=" * 60)
print("1. WHY STRING FORMATTING")
print("=" * 60)

name = "Kishor"
age = 25

# String concatenation
message = "My name is " + name + " and I am " + str(age) + " years old."

print(message)

# Problem:
# Concatenation becomes difficult when many values are involved.
#
# Modern Python usually prefers f-strings for readable formatting.

# ============================================================
# 2. str.format()
# ============================================================

print("\n" + "=" * 60)
print("2. str.format()")
print("=" * 60)

name = "Kishor"
language = "Python"

message = "My name is {} and I am learning {}.".format(name, language)

print(message)

# ============================================================
# 3. POSITIONAL ARGUMENTS
# ============================================================

print("\n" + "=" * 60)
print("3. POSITIONAL ARGUMENTS")
print("=" * 60)

name = "Kishor"
language = "Python"

print("Name: {}, Language: {}".format(name, language))

# Explicit positions

print("{0} is learning {1}.".format(name, language))

# Reusing the same argument

print("{0} {0} {0}".format("Python"))

# ============================================================
# 4. NAMED ARGUMENTS
# ============================================================

print("\n" + "=" * 60)
print("4. NAMED ARGUMENTS")
print("=" * 60)

name = "Kishor"
age = 25
city = "Aurangabad"

message = (
    "Name: {name}, Age: {age}, City: {city}"
    .format(
        name=name,
        age=age,
        city=city
    )
)

print(message)

# ============================================================
# 5. F-STRINGS
# ============================================================

print("\n" + "=" * 60)
print("5. F-STRINGS")
print("=" * 60)

name = "Kishor"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)

# ============================================================
# 6. EXPRESSIONS INSIDE F-STRINGS
# ============================================================

print("\n" + "=" * 60)
print("6. EXPRESSIONS INSIDE F-STRINGS")
print("=" * 60)

a = 10
b = 20

print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"Maximum: {max(a, b)}")

# ============================================================
# 7. METHOD CALLS INSIDE F-STRINGS
# ============================================================

print("\n" + "=" * 60)
print("7. METHOD CALLS INSIDE F-STRINGS")
print("=" * 60)

name = "kishor"

print(f"Original: {name}")
print(f"Uppercase: {name.upper()}")
print(f"Title Case: {name.title()}")

# ============================================================
# 8. DECIMAL PRECISION
# ============================================================

print("\n" + "=" * 60)
print("8. DECIMAL PRECISION")
print("=" * 60)

price = 99.987654

print(f"Price: {price:.2f}")
print(f"Price: {price:.3f}")
print(f"Price: {price:.4f}")

# .2f means:
#
# .2 -> 2 digits after decimal
# f  -> fixed-point notation

# ============================================================
# 9. PERCENTAGE FORMATTING
# ============================================================

print("\n" + "=" * 60)
print("9. PERCENTAGE FORMATTING")
print("=" * 60)

score = 0.875

print(f"Score: {score:.2%}")

# Output:
# Score: 87.50%

# ============================================================
# 10. THOUSANDS SEPARATOR
# ============================================================

print("\n" + "=" * 60)
print("10. THOUSANDS SEPARATOR")
print("=" * 60)

population = 1_250_000

print(f"Population: {population:,}")

salary = 1250000.50

print(f"Salary: {salary:,.2f}")

# ============================================================
# 11. WIDTH
# ============================================================

print("\n" + "=" * 60)
print("11. WIDTH")
print("=" * 60)

name = "Python"

print(f"|{name:10}|")

# 10 = minimum field width

# ============================================================
# 12. LEFT ALIGNMENT
# ============================================================

print("\n" + "=" * 60)
print("12. LEFT ALIGNMENT")
print("=" * 60)

name = "Python"

print(f"|{name:<10}|")

# ============================================================
# 13. RIGHT ALIGNMENT
# ============================================================

print("\n" + "=" * 60)
print("13. RIGHT ALIGNMENT")
print("=" * 60)

print(f"|{name:>10}|")

# ============================================================
# 14. CENTER ALIGNMENT
# ============================================================

print("\n" + "=" * 60)
print("14. CENTER ALIGNMENT")
print("=" * 60)

print(f"|{name:^10}|")

# ============================================================
# 15. CUSTOM PADDING
# ============================================================

print("\n" + "=" * 60)
print("15. CUSTOM PADDING")
print("=" * 60)

print(f"|{name:-<10}|")
print(f"|{name:->10}|")
print(f"|{name:-^10}|")

# ============================================================
# 16. ZERO PADDING
# ============================================================

print("\n" + "=" * 60)
print("16. ZERO PADDING")
print("=" * 60)

number = 42

print(f"{number:05d}")

# Output:
# 00042

# ============================================================
# 17. SIGN FORMATTING
# ============================================================

print("\n" + "=" * 60)
print("17. SIGN FORMATTING")
print("=" * 60)

positive = 100
negative = -100

print(f"{positive:+d}")
print(f"{negative:+d}")

print(f"{positive:d}")
print(f"{negative:d}")

# ============================================================
# 18. BINARY
# ============================================================

print("\n" + "=" * 60)
print("18. BINARY")
print("=" * 60)

number = 42

print(f"Binary: {number:b}")

# ============================================================
# 19. OCTAL
# ============================================================

print("\n" + "=" * 60)
print("19. OCTAL")
print("=" * 60)

print(f"Octal: {number:o}")

# ============================================================
# 20. HEXADECIMAL
# ============================================================

print("\n" + "=" * 60)
print("20. HEXADECIMAL")
print("=" * 60)

print(f"Lowercase hex: {number:x}")
print(f"Uppercase hex: {number:X}")

# ============================================================
# 21. SCIENTIFIC NOTATION
# ============================================================

print("\n" + "=" * 60)
print("21. SCIENTIFIC NOTATION")
print("=" * 60)

number = 1234567.89

print(f"{number:e}")
print(f"{number:.2e}")

# ============================================================
# 22. GENERAL NUMBER FORMATTING
# ============================================================

print("\n" + "=" * 60)
print("22. GENERAL NUMBER FORMATTING")
print("=" * 60)

number = 1234567.89

print(f"{number:g}")

# ============================================================
# 23. format() WITH NUMBER SPECIFIERS
# ============================================================

print("\n" + "=" * 60)
print("23. format() WITH NUMBER SPECIFIERS")
print("=" * 60)

price = 1234.5678

print("Price: {:.2f}".format(price))
print("Price: {:,.2f}".format(price))

# ============================================================
# 24. f-STRING DEBUGGING
# ============================================================

print("\n" + "=" * 60)
print("24. F-STRING DEBUGGING")
print("=" * 60)

name = "Kishor"
age = 25

# The = syntax displays both the expression and value.

print(f"{name=}")
print(f"{age=}")

a = 10
b = 20

print(f"{a + b=}")

# ============================================================
# 25. MULTIPLE VALUES
# ============================================================

print("\n" + "=" * 60)
print("25. MULTIPLE VALUES")
print("=" * 60)

name = "Kishor"
age = 25
language = "Python"

print(
    f"Name: {name}, "
    f"Age: {age}, "
    f"Language: {language}"
)

# ============================================================
# 26. MULTILINE F-STRING
# ============================================================

print("\n" + "=" * 60)
print("26. MULTILINE F-STRING")
print("=" * 60)

name = "Kishor"
language = "Python"

message = f"""
Name     : {name}
Language : {language}
"""

print(message)

# ============================================================
# 27. NESTED FORMAT SPECIFICATION
# ============================================================

print("\n" + "=" * 60)
print("27. NESTED FORMAT SPECIFICATION")
print("=" * 60)

value = 123.456789
precision = 2

print(f"{value:.{precision}f}")

# ============================================================
# 28. DATE/TIME FORMATTING
# ============================================================

print("\n" + "=" * 60)
print("28. DATE/TIME FORMATTING")
print("=" * 60)

from datetime import datetime

now = datetime.now()

print(f"Date: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")
print(f"Date & Time: {now:%Y-%m-%d %H:%M:%S}")

# ============================================================
# 29. COMMON DATE FORMAT CODES
# ============================================================

print("\n" + "=" * 60)
print("29. COMMON DATE FORMAT CODES")
print("=" * 60)

print(f"Year       : {now:%Y}")
print(f"Month      : {now:%m}")
print(f"Day        : {now:%d}")
print(f"Hour       : {now:%H}")
print(f"Minute     : {now:%M}")
print(f"Second     : {now:%S}")
print(f"Weekday    : {now:%A}")
print(f"Month Name : {now:%B}")

# ============================================================
# 30. RAW STRINGS + F-STRINGS
# ============================================================

print("\n" + "=" * 60)
print("30. RAW STRINGS + F-STRINGS")
print("=" * 60)

username = "Kishor"

path = rf"C:\Users\{username}\Documents"

print(path)

# ============================================================
# 31. OLD-STYLE % FORMATTING
# ============================================================

print("\n" + "=" * 60)
print("31. OLD-STYLE % FORMATTING")
print("=" * 60)

name = "Kishor"
age = 25

print("Name: %s, Age: %d" % (name, age))

price = 99.9876

print("Price: %.2f" % price)

# ============================================================
# 32. COMMON % FORMAT SPECIFIERS
# ============================================================

print("\n" + "=" * 60)
print("32. COMMON % FORMAT SPECIFIERS")
print("=" * 60)

name = "Kishor"
age = 25
price = 99.99

print("String : %s" % name)
print("Integer: %d" % age)
print("Float  : %f" % price)
print("2 Dec  : %.2f" % price)

# ============================================================
# 33. COMPARING FORMATTING TECHNIQUES
# ============================================================

print("\n" + "=" * 60)
print("33. COMPARING FORMATTING TECHNIQUES")
print("=" * 60)

name = "Kishor"
age = 25

# 1. Concatenation
print("Name: " + name + ", Age: " + str(age))

# 2. format()
print("Name: {}, Age: {}".format(name, age))

# 3. f-string
print(f"Name: {name}, Age: {age}")

# 4. % formatting
print("Name: %s, Age: %d" % (name, age))

# ============================================================
# 34. PRACTICAL EXAMPLE — STUDENT REPORT
# ============================================================

print("\n" + "=" * 60)
print("34. PRACTICAL EXAMPLE — STUDENT REPORT")
print("=" * 60)

student_name = "Kishor"
math = 85
science = 92
python = 95

total = math + science + python
percentage = total / 300

print(f"Student   : {student_name}")
print(f"Math      : {math}")
print(f"Science   : {science}")
print(f"Python    : {python}")
print(f"Total     : {total}")
print(f"Percentage: {percentage:.2%}")

# ============================================================
# 35. PRACTICAL EXAMPLE — PRODUCT BILL
# ============================================================

print("\n" + "=" * 60)
print("35. PRACTICAL EXAMPLE — PRODUCT BILL")
print("=" * 60)

product = "Laptop"
price = 74999.99
quantity = 2

total = price * quantity

print(f"Product : {product}")
print(f"Price   : ₹{price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Total   : ₹{total:,.2f}")

# ============================================================
# 36. PRACTICAL EXAMPLE — TABLE
# ============================================================

print("\n" + "=" * 60)
print("36. PRACTICAL EXAMPLE — TABLE")
print("=" * 60)

print(f"{'Name':<15}{'Age':>5}{'Score':>10}")
print("-" * 30)

students = [
    ("Kishor", 25, 95),
    ("Rahul", 24, 88),
    ("Amit", 26, 91),
]

for name, age, score in students:
    print(f"{name:<15}{age:>5}{score:>10}")

# ============================================================
# 37. COMMON MISTAKES
# ============================================================

print("\n" + "=" * 60)
print("37. COMMON MISTAKES")
print("=" * 60)

# Mistake 1:
# Mixing string and integer using +

# age = 25
# print("Age: " + age)
#
# TypeError occurs because age is an integer.

# Correct:
age = 25
print("Age:", age)
print(f"Age: {age}")

# Mistake 2:
# Forgetting the f before an f-string.

name = "Kishor"

print(f"Hello {name}")   # Correct
print("Hello {name}")    # Literal text

# Mistake 3:
# Incorrect format specifier.

price = 99.99

print(f"{price:.2f}")    # Correct

# ============================================================
# 38. FORMAT SPECIFIER CHEAT SHEET
# ============================================================

print("\n" + "=" * 60)
print("38. FORMAT SPECIFIER CHEAT SHEET")
print("=" * 60)

number = 42
decimal = 1234.5678

print(f"Decimal integer : {number:d}")
print(f"Binary          : {number:b}")
print(f"Octal           : {number:o}")
print(f"Hex lowercase   : {number:x}")
print(f"Hex uppercase   : {number:X}")

print(f"Fixed point     : {decimal:.2f}")
print(f"Percentage       : {0.875:.2%}")
print(f"Thousands        : {decimal:,.2f}")
print(f"Scientific       : {decimal:.2e}")

print(f"Left aligned    : |{'Python':<10}|")
print(f"Right aligned   : |{'Python':>10}|")
print(f"Center aligned  : |{'Python':^10}|")
print(f"Zero padded     : {number:05d}")

# ============================================================
# 39. IMPORTANT FORMAT SYNTAX
# ============================================================

"""
General format syntax:

    {value:format_spec}

Examples:

    {price:.2f}
    {number:,}
    {number:05d}
    {name:<10}
    {name:>10}
    {name:^10}
    {number:b}
    {number:x}
    {score:.2%}

Common structure:

    [[fill]align][sign][#][0][width][grouping][.precision][type]

Alignment:

    <   Left
    >   Right
    ^   Center

Number types:

    d   Integer
    f   Fixed-point
    e   Scientific notation
    %   Percentage
    b   Binary
    o   Octal
    x   Hexadecimal lowercase
    X   Hexadecimal uppercase

Other useful formatting:

    ,   Thousands separator
    +   Always show sign
    0   Zero padding
"""

# ============================================================
# 40. BEST PRACTICES
# ============================================================

print("\n" + "=" * 60)
print("40. BEST PRACTICES")
print("=" * 60)

"""
1. Prefer f-strings for modern Python code.

    f"Hello {name}"

2. Use format() when it makes the code clearer or when
   working with formatting templates.

3. Avoid unnecessary string concatenation.

4. Use explicit precision for financial/display values.

    f"{price:.2f}"

5. Use thousands separators for large human-readable numbers.

    f"{population:,}"

6. Use alignment when creating CLI reports and tables.

7. Remember that formatting creates a string representation;
   it does not change the original value.

8. Keep business calculations separate from presentation
   formatting.

Good:

    total = price * quantity
    print(f"Total: ₹{total:,.2f}")

Avoid mixing complex calculations into large output strings.
"""

# ============================================================
# 41. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("41. FINAL SUMMARY")
print("=" * 60)

print(
    """
Python provides several ways to format strings:

1. Concatenation
       "Hello " + name

2. str.format()
       "Hello {}".format(name)

3. f-strings
       f"Hello {name}"

4. % formatting
       "Hello %s" % name

For modern Python development, f-strings are generally
the preferred choice for readable, expressive formatting.

Important concepts to remember:

    f"{value}"
    f"{value:.2f}"
    f"{value:,}"
    f"{value:.2%}"
    f"{value:05d}"
    f"{value:b}"
    f"{value:x}"
    f"{value:<10}"
    f"{value:>10}"
    f"{value:^10}"

Mastering string formatting is essential for:

    - CLI applications
    - Reports
    - Logging
    - Data presentation
    - Financial output
    - APIs
    - Web applications
    - Automation scripts
    - Debugging
    - Professional Python development
"""
)

print("\nString formatting chapter completed successfully!")
```
