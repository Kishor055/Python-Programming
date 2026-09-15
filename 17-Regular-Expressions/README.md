# 🔎 17 — Regular Expressions in Python

> **Python Programming — Beginner → Advanced**

Regular Expressions, commonly called **Regex** or **RegEx**, are patterns used to **search, match, extract, validate, replace, and manipulate text**.

Python provides regular expression support through the built-in:

```python
import re
```

Regular expressions are extremely useful when working with:

* Email addresses
* Phone numbers
* URLs
* Password validation
* User input
* Log files
* File names
* Dates and times
* Text extraction
* Data cleaning
* Web scraping
* Search functionality
* Natural Language Processing
* Data preprocessing

---

## 📚 Table of Contents

* [Learning Objectives](#-learning-objectives)
* [What is a Regular Expression?](#-what-is-a-regular-expression)
* [Why Learn Regex?](#-why-learn-regex)
* [The `re` Module](#-the-re-module)
* [Regex Mental Model](#-regex-mental-model)
* [Raw Strings](#-raw-strings)
* [Basic Matching](#-basic-matching)
* [`re.search()`](#-research)
* [`re.match()`](#-rematch)
* [`re.fullmatch()`](#-refullmatch)
* [`re.findall()`](#-refindall)
* [`re.finditer()`](#-refinditer)
* [`re.split()`](#-resplit)
* [`re.sub()`](#-resub)
* [`re.subn()`](#-resubn)
* [Regex Character Literals](#-regex-character-literals)
* [Character Classes](#-character-classes)
* [Predefined Character Classes](#-predefined-character-classes)
* [Quantifiers](#-quantifiers)
* [Greedy vs Non-Greedy Matching](#-greedy-vs-non-greedy-matching)
* [Anchors](#-anchors)
* [Alternation](#-alternation)
* [Grouping](#-grouping)
* [Capturing Groups](#-capturing-groups)
* [Named Groups](#-named-groups)
* [Non-Capturing Groups](#-non-capturing-groups)
* [Backreferences](#-backreferences)
* [Lookahead](#-lookahead)
* [Lookbehind](#-lookbehind)
* [Flags](#-flags)
* [Compiled Patterns](#-compiled-patterns)
* [Match Objects](#-match-objects)
* [Regex Validation](#-regex-validation)
* [Email Validation](#-email-validation)
* [Phone Validation](#-phone-validation)
* [Password Validation](#-password-validation)
* [Date Validation](#-date-validation)
* [URL Extraction](#-url-extraction)
* [Text Extraction](#-text-extraction)
* [Regex for Data Cleaning](#-regex-for-data-cleaning)
* [Regex with File Handling](#-regex-with-file-handling)
* [Regex with Log Files](#-regex-with-log-files)
* [Advanced Regex](#-advanced-regex)
* [Common Mistakes](#-common-mistakes)
* [Regex Performance](#-regex-performance)
* [When to Use Regex](#-when-to-use-regex)
* [When Not to Use Regex](#-when-not-to-use-regex)
* [Practice Exercises](#-practice-exercises)
* [Mini Projects](#-mini-projects)
* [Interview Questions](#-interview-questions)
* [Quick Revision](#-quick-revision)
* [Best Practices](#-best-practices)
* [References](#-references)
* [Next Topic](#-next-topic)

---

# 🎯 Learning Objectives

After completing this chapter, you should be able to:

* Understand what Regular Expressions are
* Understand regex patterns
* Use Python's `re` module
* Search for patterns
* Match text
* Extract information
* Replace text
* Split text
* Use character classes
* Use quantifiers
* Use anchors
* Use groups
* Use capturing groups
* Use named groups
* Understand lookarounds
* Use regex flags
* Compile regex patterns
* Work with Match objects
* Validate user input
* Extract structured information from text
* Process logs and files
* Build practical regex-based applications

---

# 🧠 What is a Regular Expression?

A **Regular Expression** is a sequence of characters that defines a search pattern.

For example:

```text
hello
```

matches the exact text:

```text
hello
```

A more flexible pattern:

```text
\d+
```

means:

> Match one or more digits.

So it can match:

```text
123
42
98765
```

---

# 💡 Why Learn Regex?

Suppose you have:

```text
My phone number is 9876543210.
```

You could manually search the text.

But with regex:

```python
r"\d{10}"
```

Python can identify a 10-digit number automatically.

This becomes extremely useful when processing thousands or millions of lines.

---

# 🐍 The `re` Module

Python's built-in regex functionality is provided by the `re` module.

```python
import re
```

No external package is required.

Basic example:

```python
import re

text = "Python is powerful"

result = re.search(r"Python", text)

print(result)
```

If a match exists, `result` contains a Match object.

---

# 🧠 Regex Mental Model

Think of regex as a **mini-language for describing text patterns**.

For example:

```text
\d{3}-\d{3}-\d{4}
```

can describe:

```text
123-456-7890
```

Break it down:

```text
\d      → digit
{3}     → exactly 3 times
-       → literal hyphen
\d{3}   → 3 digits
-       → literal hyphen
\d{4}   → 4 digits
```

Regex becomes easier when you learn to read patterns **piece by piece**.

---

# 🧵 Raw Strings

In Python, regex patterns are commonly written using raw strings:

```python
r"\d+"
```

instead of:

```python
"\\d+"
```

The `r` tells Python to treat backslashes more literally.

### Recommended

```python
pattern = r"\d+"
```

This makes regex code easier to read.

---

# 🔍 Basic Matching

Suppose:

```python
text = "Python Programming"
```

Search for:

```python
r"Python"
```

Example:

```python
import re

text = "Python Programming"

result = re.search(r"Python", text)

if result:
    print("Found")
```

Output:

```text
Found
```

---

# 🔎 `re.search()`

`re.search()` searches the **entire string** for the first location where the pattern matches.

```python
import re

text = "I love Python"

result = re.search(r"Python", text)

if result:
    print(result.group())
```

Output:

```text
Python
```

### Important

`search()` returns the **first matching occurrence**.

---

# 🎯 `re.match()`

`re.match()` checks for a match **at the beginning of the string**.

```python
import re

text = "Python is powerful"

result = re.match(r"Python", text)

print(result.group())
```

Output:

```text
Python
```

But:

```python
text = "I love Python"

result = re.match(r"Python", text)

print(result)
```

returns:

```text
None
```

because `Python` is not at the beginning.

---

# 🎯 `re.fullmatch()`

`fullmatch()` requires the **entire string** to match the pattern.

```python
import re

result = re.fullmatch(r"\d{4}", "2025")

print(result)
```

This matches.

But:

```python
re.fullmatch(r"\d{4}", "Year: 2025")
```

does not match.

### Useful for

* Validation
* IDs
* Codes
* Strict input formats

---

# 📋 `re.findall()`

`findall()` returns all non-overlapping matches.

```python
import re

text = "Python 3 is faster than Python 2"

numbers = re.findall(r"\d+", text)

print(numbers)
```

Output:

```text
['3', '2']
```

Example:

```python
words = re.findall(r"\bPython\b", text)

print(words)
```

Output:

```text
['Python', 'Python']
```

---

# 🔄 `re.finditer()`

`finditer()` returns an iterator containing Match objects.

```python
import re

text = "Python Python Python"

matches = re.finditer(r"Python", text)

for match in matches:
    print(match.group(), match.start(), match.end())
```

This is useful when you need:

* Match position
* Match text
* Groups
* Detailed Match object information

---

# ✂️ `re.split()`

`re.split()` splits text using a regex pattern.

```python
import re

text = "apple,banana;orange"

result = re.split(r"[,;]", text)

print(result)
```

Output:

```text
['apple', 'banana', 'orange']
```

---

# 🔁 `re.sub()`

`re.sub()` replaces matching text.

```python
import re

text = "Python is difficult"

result = re.sub(r"difficult", "powerful", text)

print(result)
```

Output:

```text
Python is powerful
```

---

# 🔢 `re.subn()`

`subn()` performs replacement and also returns the number of replacements.

```python
import re

text = "cat cat cat"

result = re.subn(r"cat", "dog", text)

print(result)
```

Output:

```text
('dog dog dog', 3)
```

---

# 🔤 Regex Character Literals

The simplest regex matches literal characters.

```text
python
```

matches:

```text
python
```

Case-sensitive matching means:

```text
python
```

does not automatically match:

```text
Python
```

unless appropriate flags are used.

---

# 🧩 Character Classes

A character class matches one character from a set.

## `[abc]`

Matches:

```text
a
b
c
```

Example:

```python
re.findall(r"[aeiou]", "python programming")
```

---

## `[a-z]`

Matches lowercase letters.

```python
re.findall(r"[a-z]", "Hello")
```

---

## `[A-Z]`

Matches uppercase letters.

---

## `[0-9]`

Matches digits.

```python
re.findall(r"[0-9]", "Python 123")
```

---

# 🚫 Negated Character Classes

The `^` inside a character class means:

> Not these characters.

Example:

```text
[^0-9]
```

means:

> Match anything that is not a digit.

```python
re.findall(r"[^0-9]", "abc123")
```

---

# 🔣 Predefined Character Classes

Python provides shortcuts for common patterns.

| Pattern | Meaning                                 |
| ------- | --------------------------------------- |
| `\d`    | Digit                                   |
| `\D`    | Non-digit                               |
| `\w`    | Word character                          |
| `\W`    | Non-word character                      |
| `\s`    | Whitespace                              |
| `\S`    | Non-whitespace                          |
| `.`     | Any character except newline by default |

---

## `\d`

Matches digits.

```python
re.findall(r"\d+", "Age: 25")
```

Output:

```text
['25']
```

---

## `\w`

Matches word characters.

Typically includes letters, digits, and underscore.

```python
re.findall(r"\w+", "hello_world 123")
```

---

## `\s`

Matches whitespace.

```python
re.findall(r"\s+", "Hello   World")
```

---

# 🔢 Quantifiers

Quantifiers specify **how many times** a pattern should occur.

| Quantifier | Meaning         |
| ---------- | --------------- |
| `*`        | Zero or more    |
| `+`        | One or more     |
| `?`        | Zero or one     |
| `{n}`      | Exactly n       |
| `{n,}`     | At least n      |
| `{n,m}`    | Between n and m |

---

# ⭐ `*`

Zero or more occurrences.

```text
a*
```

Can match:

```text
""
"a"
"aa"
"aaa"
```

---

# ➕ `+`

One or more occurrences.

```text
\d+
```

Matches:

```text
1
25
12345
```

But not an empty string.

---

# ❓ `?`

Zero or one occurrence.

```text
colou?r
```

Can match:

```text
color
colour
```

---

# 🔢 `{n}`

Exactly `n` occurrences.

```text
\d{4}
```

Matches:

```text
2025
1234
9876
```

---

# 🔢 `{n,}`

At least `n` occurrences.

```text
\d{3,}
```

Matches:

```text
123
1234
12345
```

---

# 🔢 `{n,m}`

Between `n` and `m`.

```text
\d{2,4}
```

Matches:

```text
12
123
1234
```

---

# 🐘 Greedy vs Non-Greedy Matching

Regex quantifiers are generally **greedy** by default.

Consider:

```python
text = "<b>Hello</b><b>World</b>"
```

Pattern:

```python
r"<b>.*</b>"
```

may consume more text than expected.

A non-greedy version:

```python
r"<b>.*?</b>"
```

tries to match as little as possible while still satisfying the pattern.

### Comparison

```text
.*    → Greedy
.*?   → Non-greedy
```

Understanding greediness is important when extracting structured text.

---

# ⚓ Anchors

Anchors specify positions rather than characters.

## `^`

Beginning of string.

```python
r"^Python"
```

Matches:

```text
Python is great
```

but not:

```text
I love Python
```

---

## `$`

End of string.

```python
r"Python$"
```

Matches:

```text
I love Python
```

but not:

```text
Python is great
```

---

# 🧱 Word Boundary

`\b` represents a word boundary.

Example:

```python
r"\bcat\b"
```

matches:

```text
cat
```

but avoids matching `cat` inside:

```text
catalog
```

This is extremely useful for matching complete words.

---

# 🔀 Alternation

The `|` operator means **OR**.

Example:

```python
r"cat|dog"
```

matches either:

```text
cat
```

or:

```text
dog
```

Example:

```python
text = "I have a cat and a dog"

result = re.findall(r"cat|dog", text)

print(result)
```

---

# 🧩 Grouping

Parentheses create groups:

```text
(...)
```

Example:

```python
r"(cat|dog)"
```

This treats the alternatives as one logical unit.

---

# 📦 Capturing Groups

Groups can capture specific parts of a match.

Example:

```python
import re

text = "Name: Kishor, Age: 25"

pattern = r"Name:\s*(\w+),\s*Age:\s*(\d+)"

match = re.search(pattern, text)

print(match.group(1))
print(match.group(2))
```

Output:

```text
Kishor
25
```

---

# 🏷️ Named Groups

Named groups make complex regex easier to understand.

Syntax:

```text
(?P<name>pattern)
```

Example:

```python
import re

text = "Name: Kishor, Age: 25"

pattern = (
    r"Name:\s*(?P<name>\w+),"
    r"\s*Age:\s*(?P<age>\d+)"
)

match = re.search(pattern, text)

print(match.group("name"))
print(match.group("age"))
```

Output:

```text
Kishor
25
```

Named groups are recommended for complex patterns.

---

# 🚫 Non-Capturing Groups

Sometimes you need grouping but do not need the captured value.

Use:

```text
(?:...)
```

Example:

```python
r"(?:Mr|Mrs|Ms)\.?\s+\w+"
```

This groups alternatives without creating a numbered capture group.

---

# 🔁 Backreferences

A backreference allows you to refer to previously captured text.

Example:

```python
r"(\w+)\s+\1"
```

This can detect repeated words:

```text
hello hello
```

but not:

```text
hello world
```

Backreferences are useful for patterns where later text must match earlier captured text.

---

# 👀 Lookahead

A lookahead checks what comes next without consuming it.

Positive lookahead:

```text
(?=pattern)
```

Example:

```python
r"\d+(?= USD)"
```

This finds numbers followed by `" USD"`.

---

# 👀 Negative Lookahead

Negative lookahead:

```text
(?!pattern)
```

means:

> The specified pattern must not occur next.

Lookaheads are useful for complex validation and filtering.

---

# 🔙 Lookbehind

Lookbehind checks what appears before the current position.

Positive lookbehind:

```text
(?<=pattern)
```

Example:

```python
r"(?<=\$)\d+"
```

can find numbers immediately preceded by `$`.

---

# 🚫 Negative Lookbehind

Syntax:

```text
(?<!pattern)
```

This means:

> The specified pattern must not occur immediately before the current position.

---

# 🚩 Regex Flags

Flags modify regex behavior.

Common flags include:

| Flag            | Meaning                          |
| --------------- | -------------------------------- |
| `re.IGNORECASE` | Ignore case                      |
| `re.MULTILINE`  | `^` and `$` work per line        |
| `re.DOTALL`     | `.` matches newline              |
| `re.VERBOSE`    | Allows readable multi-line regex |
| `re.ASCII`      | ASCII-only character behavior    |

---

# 🔤 `re.IGNORECASE`

```python
import re

text = "Python PYTHON python"

matches = re.findall(
    r"python",
    text,
    re.IGNORECASE
)

print(matches)
```

Output:

```text
['Python', 'PYTHON', 'python']
```

---

# 📄 `re.MULTILINE`

Useful when processing multiple lines.

```python
pattern = r"^ERROR"
```

With:

```python
re.MULTILINE
```

the `^` anchor can match the beginning of each line.

---

# 📝 `re.DOTALL`

Normally:

```text
.
```

does not match newline characters.

With:

```python
re.DOTALL
```

it can.

---

# 📖 `re.VERBOSE`

Complex regex can become difficult to read.

`re.VERBOSE` allows formatting and comments.

Example:

```python
pattern = re.compile(
    r"""
    \d{3}      # Area code
    -
    \d{3}      # Prefix
    -
    \d{4}      # Number
    """,
    re.VERBOSE
)
```

This is highly useful for production-quality complex patterns.

---

# ⚡ Compiled Patterns

If the same pattern is used repeatedly, compile it.

```python
import re

pattern = re.compile(r"\d+")

print(pattern.findall("Age 25"))
print(pattern.findall("Year 2025"))
```

A compiled pattern provides methods such as:

```python
pattern.search()
pattern.match()
pattern.fullmatch()
pattern.findall()
pattern.finditer()
pattern.sub()
pattern.split()
```

Compilation is also useful because it makes a reusable regex object.

---

# 📦 Match Objects

Methods such as `search()` and `match()` can return a Match object.

Example:

```python
import re

text = "Python 123"

match = re.search(r"\d+", text)

if match:
    print(match.group())
    print(match.start())
    print(match.end())
```

Possible output:

```text
123
7
10
```

---

# 🔍 Important Match Methods

## `group()`

Returns the matched text.

```python
match.group()
```

## `start()`

Returns the starting index.

```python
match.start()
```

## `end()`

Returns the ending index.

```python
match.end()
```

## `span()`

Returns:

```python
(start, end)
```

Example:

```python
match.span()
```

---

# 📧 Email Validation

A simple educational pattern:

```python
import re

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

email = "user@example.com"

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

### Important

Email syntax is more complicated than many simple regex patterns suggest.

For production systems, avoid assuming that a short regex completely implements the full email specification.

---

# 📱 Phone Number Validation

Example for a simple 10-digit number:

```python
import re

phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid phone number")
```

For a specific application, define the exact accepted format first.

---

# 🔐 Password Validation

Suppose the requirements are:

* At least 8 characters
* One uppercase letter
* One lowercase letter
* One digit

Example:

```python
import re

pattern = (
    r"^(?=.*[A-Z])"
    r"(?=.*[a-z])"
    r"(?=.*\d)"
    r".{8,}$"
)

password = "Python123"

if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")
```

### Note

Regex can validate password format, but it does not determine whether a password is actually secure.

---

# 📅 Date Validation

Example format:

```text
25-12-2025
```

Regex:

```python
pattern = r"\d{2}-\d{2}-\d{4}"
```

Usage:

```python
date = "25-12-2025"

if re.fullmatch(pattern, date):
    print("Format looks valid")
```

### Important

Regex validates the **shape**, not necessarily the real calendar date.

For example:

```text
99-99-9999
```

matches the simple pattern but is not a valid date.

For actual date validation, combine regex with Python's date-handling tools.

---

# 🌐 URL Extraction

A basic educational example:

```python
import re

text = """
Visit https://example.com
or https://python.org
"""

urls = re.findall(
    r"https?://[^\s]+",
    text
)

print(urls)
```

Output:

```text
['https://example.com', 'https://python.org']
```

For production-grade URL parsing and validation, dedicated URL parsing libraries/tools are often preferable to an enormous regex.

---

# 📝 Text Extraction

Regex is excellent for extracting structured information.

Example:

```python
text = """
Order ID: 12345
Order ID: 67890
"""

ids = re.findall(
    r"Order ID:\s*(\d+)",
    text
)

print(ids)
```

Output:

```text
['12345', '67890']
```

---

# 🧹 Regex for Data Cleaning

Suppose:

```python
text = "Hello!!!   Python...."
```

Remove punctuation:

```python
cleaned = re.sub(
    r"[^\w\s]",
    "",
    text
)

print(cleaned)
```

Normalize multiple spaces:

```python
cleaned = re.sub(
    r"\s+",
    " ",
    cleaned
)
```

Regex is commonly used as one stage of data-cleaning pipelines.

---

# 📄 Regex with File Handling

Regex can process files line by line.

```python
import re

pattern = re.compile(r"ERROR")

with open("application.log", encoding="utf-8") as file:

    for line in file:

        if pattern.search(line):
            print(line.strip())
```

This is useful for large files because the file can be processed incrementally.

---

# 📊 Regex with Log Files

Example log:

```text
INFO User logged in
ERROR Database connection failed
INFO Request completed
ERROR Timeout occurred
```

Extract error lines:

```python
import re

pattern = re.compile(r"^ERROR.*$", re.MULTILINE)

matches = pattern.findall(log_data)

for error in matches:
    print(error)
```

---

# 🧠 Advanced Regex

At an advanced level, you should understand:

```text
Character Classes
Quantifiers
Anchors
Groups
Named Groups
Backreferences
Lookahead
Lookbehind
Flags
Compiled Patterns
Match Objects
Greedy Matching
Non-Greedy Matching
```

---

# 🧩 Combining Regex Components

Real patterns often combine several concepts.

Example:

```text
^\d{3}-\d{3}-\d{4}$
```

Breakdown:

```text
^          → Beginning
\d{3}      → Three digits
-          → Hyphen
\d{3}      → Three digits
-          → Hyphen
\d{4}      → Four digits
$          → End
```

This illustrates an important skill:

> **Read regex from left to right and understand every component.**

---

# 🧠 Regex Is a Language

Do not try to memorize hundreds of patterns.

Instead learn the building blocks:

```text
Literal
   ↓
Character Class
   ↓
Quantifier
   ↓
Anchor
   ↓
Group
   ↓
Lookaround
```

Then combine them.

For example:

```text
\d{3}-\d{3}-\d{4}
```

is simply:

```text
digit + repetition + literal + digit + repetition + literal + digit + repetition
```

---

# ⚠️ Common Mistakes

## 1. Forgetting Raw Strings

Prefer:

```python
r"\d+"
```

over complicated escaped strings.

---

## 2. Using `match()` When You Need `search()`

Remember:

```text
match()  → beginning
search() → anywhere
```

---

## 3. Using Regex for Everything

Regex is not always the best solution.

Sometimes normal Python string operations are clearer:

```python
str.startswith()
str.endswith()
str.split()
str.replace()
str.find()
```

---

## 4. Writing One Giant Regex

Avoid extremely complicated patterns when a combination of:

* Regex
* Normal Python
* Parsing libraries
* Validation logic

would be clearer.

---

## 5. Forgetting `fullmatch()` for Strict Validation

For validation, consider:

```python
re.fullmatch()
```

rather than accidentally accepting a substring.

---

## 6. Ignoring Greedy Matching

Patterns such as:

```text
.*
```

can consume more text than expected.

Understand:

```text
.*
```

versus:

```text
.*?
```

---

# ⚡ Regex Performance

Most regex tasks are fast enough for ordinary applications.

However, poorly designed patterns can cause severe performance problems, particularly when patterns contain nested or ambiguous repetition.

Be careful with patterns involving structures like:

```text
(a+)+
```

or multiple overlapping wildcards.

### Production Principles

* Keep patterns simple.
* Avoid unnecessary nested quantifiers.
* Compile frequently reused patterns.
* Test patterns against realistic input.
* Test worst-case input.
* Avoid catastrophic backtracking patterns.
* Do not use regex where a parser is more appropriate.

---

# 🚦 When to Use Regex

Regex is a good choice when you need:

```text
✓ Pattern searching
✓ Text extraction
✓ Format detection
✓ Simple validation
✓ Replacement
✓ Token filtering
✓ Log processing
✓ Data cleaning
```

---

# 🚫 When Not to Use Regex

Avoid regex when:

```text
✗ Parsing complex programming languages
✗ Parsing complicated nested structures
✗ Processing JSON
✗ Processing XML/HTML structurally
✗ Validating complex business rules
✗ A normal string operation is clearer
```

For structured formats, use the appropriate parser.

For example, JSON should normally be processed using Python's `json` module rather than trying to parse arbitrary JSON with regex.

---

# 🧪 Practice Exercises

## 🟢 Beginner

1. Find all digits in a string.
2. Find all words in a sentence.
3. Find all uppercase letters.
4. Find all lowercase letters.
5. Find all whitespace characters.
6. Replace multiple spaces with one space.
7. Find all occurrences of `"Python"`.
8. Split text using commas and semicolons.

---

## 🟡 Intermediate

9. Extract phone numbers.
10. Extract email addresses.
11. Extract URLs.
12. Validate a 10-digit number.
13. Validate a simple username.
14. Validate a password format.
15. Extract dates.
16. Extract numbers from a sentence.
17. Find repeated words.
18. Remove punctuation from text.

---

## 🔴 Advanced

19. Create a regex using named groups.
20. Practice positive lookahead.
21. Practice negative lookahead.
22. Practice positive lookbehind.
23. Practice negative lookbehind.
24. Build a log parser.
25. Build a text-cleaning pipeline.
26. Create a reusable compiled regex library.
27. Benchmark different regex patterns.
28. Identify and optimize a potentially catastrophic regex.

---

# 🚀 Mini Project 1 — Text Analyzer

Build a program that analyzes a text file.

Extract:

```text
Emails
Phone Numbers
URLs
Dates
Numbers
Words
```

Example:

```python
import re

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)

numbers = re.findall(
    r"\d+",
    text
)
```

Display a summary:

```text
Emails Found   : 5
Phone Numbers  : 3
URLs Found     : 7
Dates Found    : 4
Numbers Found  : 21
```

---

# 🚀 Mini Project 2 — Log Analyzer

Create a program that reads:

```text
application.log
```

and identifies:

```text
INFO
WARNING
ERROR
CRITICAL
```

Produce:

```text
INFO     : 120
WARNING  : 18
ERROR    : 7
CRITICAL : 2
```

Use:

* `re`
* `re.compile()`
* File handling
* `finditer()`
* Groups

---

# 🚀 Mini Project 3 — Data Cleaner

Create a text-cleaning system that:

1. Removes unnecessary punctuation.
2. Removes extra whitespace.
3. Extracts numbers.
4. Extracts emails.
5. Normalizes text.
6. Produces a clean output file.

Pipeline:

```text
Raw Data
   ↓
Regex Cleaning
   ↓
Extraction
   ↓
Normalization
   ↓
Clean Data
```

---

# 🚀 Mini Project 4 — Input Validator

Build a reusable validation module:

```text
validators.py
```

Implement:

```python
validate_email()
validate_phone()
validate_username()
validate_password()
validate_date()
```

Example:

```python
if validate_email(email):
    print("Valid")
else:
    print("Invalid")
```

Keep the validation rules separate and test them thoroughly.

---

# 💼 Interview Questions

## Beginner

### 1. What is Regex?

Regex is a pattern language used for searching, matching, extracting, replacing, and validating text.

### 2. Which Python module provides regex support?

```python
re
```

### 3. What does `\d` mean?

A digit.

### 4. What does `\w` mean?

A word character.

### 5. What does `\s` mean?

Whitespace.

### 6. What does `+` mean?

One or more occurrences.

### 7. What does `*` mean?

Zero or more occurrences.

### 8. What does `?` mean?

Zero or one occurrence in its quantifier role.

---

## Intermediate

### 9. Difference between `match()` and `search()`?

```text
match()  → checks from the beginning
search() → searches anywhere
```

### 10. What does `findall()` return?

A list containing the matches.

### 11. What does `finditer()` return?

An iterator that produces Match objects.

### 12. What is a capturing group?

A parenthesized portion of a regex whose matched text can be retrieved.

### 13. What is a named group?

A capturing group assigned a name:

```text
(?P<name>...)
```

### 14. What is a non-capturing group?

```text
(?:...)
```

It groups a pattern without capturing it.

### 15. What is a raw string?

A Python string commonly used for regex patterns so backslashes are easier to work with:

```python
r"\d+"
```

---

## Advanced

### 16. What is a lookahead?

A zero-width assertion that checks what follows without consuming it.

### 17. What is a lookbehind?

A zero-width assertion that checks what precedes the current position.

### 18. What is a greedy quantifier?

A quantifier that generally attempts to consume as much matching text as possible.

### 19. What is a non-greedy quantifier?

A quantifier that attempts to consume as little matching text as possible while still satisfying the pattern.

### 20. Why use `re.compile()`?

To create a reusable compiled pattern, which is especially useful when the same pattern is used repeatedly.

### 21. What is catastrophic backtracking?

A situation where a poorly designed regex causes extremely large amounts of backtracking, potentially making matching very slow.

### 22. Should regex be used to parse JSON?

Generally no. Use a JSON parser.

---

# 🧠 Regex Cheat Sheet

| Pattern  | Meaning                                 |    |
| -------- | --------------------------------------- | -- |
| `.`      | Any character except newline by default |    |
| `^`      | Start                                   |    |
| `$`      | End                                     |    |
| `\d`     | Digit                                   |    |
| `\D`     | Non-digit                               |    |
| `\w`     | Word character                          |    |
| `\W`     | Non-word character                      |    |
| `\s`     | Whitespace                              |    |
| `\S`     | Non-whitespace                          |    |
| `\b`     | Word boundary                           |    |
| `*`      | 0 or more                               |    |
| `+`      | 1 or more                               |    |
| `?`      | 0 or 1                                  |    |
| `{n}`    | Exactly n                               |    |
| `{n,}`   | At least n                              |    |
| `{n,m}`  | n to m                                  |    |
| `[]`     | Character class                         |    |
| `[^]`    | Negated character class                 |    |
| `()`     | Capturing group                         |    |
| `(?:)`   | Non-capturing group                     |    |
| `        | `                                       | OR |
| `(?=)`   | Positive lookahead                      |    |
| `(?! )`  | Negative lookahead                      |    |
| `(?<=)`  | Positive lookbehind                     |    |
| `(?<! )` | Negative lookbehind                     |    |

---

# 🧠 Regex Method Cheat Sheet

| Method           | Purpose                       |
| ---------------- | ----------------------------- |
| `re.search()`    | Find first match anywhere     |
| `re.match()`     | Match from beginning          |
| `re.fullmatch()` | Match entire string           |
| `re.findall()`   | Return all matches            |
| `re.finditer()`  | Iterate through Match objects |
| `re.split()`     | Split using regex             |
| `re.sub()`       | Replace matches               |
| `re.subn()`      | Replace and count             |
| `re.compile()`   | Create reusable pattern       |

---

# ⚡ Quick Revision

### Import

```python
import re
```

### Search

```python
re.search(pattern, text)
```

### Match

```python
re.match(pattern, text)
```

### Full Validation

```python
re.fullmatch(pattern, text)
```

### Extract

```python
re.findall(pattern, text)
```

### Iterate

```python
re.finditer(pattern, text)
```

### Replace

```python
re.sub(pattern, replacement, text)
```

### Split

```python
re.split(pattern, text)
```

### Compile

```python
pattern = re.compile(r"\d+")
```

---

# 🏆 Regex Learning Roadmap

```text
Level 1 — Fundamentals
│
├── re module
├── search()
├── match()
├── fullmatch()
└── findall()
        │
        ▼
Level 2 — Pattern Building
│
├── Character Classes
├── \d
├── \w
├── \s
├── Quantifiers
└── Anchors
        │
        ▼
Level 3 — Text Extraction
│
├── Groups
├── Capturing Groups
├── Named Groups
├── finditer()
└── Match Objects
        │
        ▼
Level 4 — Advanced Regex
│
├── Lookahead
├── Lookbehind
├── Backreferences
├── Flags
├── Greedy / Non-Greedy
└── Compiled Patterns
        │
        ▼
Level 5 — Production
│
├── Log Analysis
├── Data Cleaning
├── Validation
├── Performance
├── Testing
└── Maintainable Patterns
```

---

# ✅ Best Practices

* Use raw strings for regex patterns.
* Give complex patterns descriptive variable names.
* Use `re.compile()` for frequently reused patterns.
* Prefer named groups for complicated extraction.
* Use `re.fullmatch()` when validating an entire input.
* Test regex against both valid and invalid inputs.
* Keep patterns readable.
* Use `re.VERBOSE` for complex expressions.
* Avoid unnecessarily complicated regex.
* Be careful with greedy quantifiers.
* Test performance on large and worst-case inputs.
* Prefer standard parsers for structured formats such as JSON.
* Document complex production regex patterns.
* Write automated tests for important validation patterns.

---

# 📌 Key Takeaways

> **Regex is a pattern language for working with text.**

> **Python provides regex support through the built-in `re` module.**

> **`search()` finds a match anywhere, while `match()` starts at the beginning.**

> **`fullmatch()` is useful when the entire input must satisfy a pattern.**

> **Character classes, quantifiers, anchors, and groups are the foundation of regex.**

> **Named groups make complex extraction easier to understand.**

> **Lookarounds allow advanced contextual matching without consuming text.**

> **Regex is powerful, but it should not replace proper parsers or simple string operations when those are clearer.**

> **Production-quality regex requires attention to readability, correctness, testing, and performance.**

---

# 📖 References

* [Python Documentation — `re` Regular Expression Operations](https://docs.python.org/3/library/re.html?utm_source=chatgpt.com)
* [Python Documentation — Regular Expression Syntax](https://docs.python.org/3/library/re.html?utm_source=chatgpt.com#regular-expression-syntax)
* [Python Documentation — `re` HOWTO](https://docs.python.org/3/howto/regex.html?utm_source=chatgpt.com)

---

# ⏭️ Next Topic

Continue your Python journey with:

## **18 — Multithreading and Multiprocessing**

You will learn:

* Processes vs threads
* Concurrency vs parallelism
* `threading`
* `multiprocessing`
* Thread lifecycle
* Process lifecycle
* Thread synchronization
* Locks
* Race conditions
* Queues
* Thread pools
* Process pools
* `concurrent.futures`
* CPU-bound vs I/O-bound tasks
* GIL
* Practical concurrent programming

---

<div align="center">

# 🐍 Keep Building. Keep Learning. Keep Coding.

### Python Programming — Beginner → Advanced

**Understand the pattern. Build the solution. Master Python.**

</div>
