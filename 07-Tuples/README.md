 # 🐍 Python Tuples

 > **Module 07 — Tuples in Python**

 A complete guide to **Tuples in Python**, covering fundamentals, syntax, indexing, slicing, immutability, tuple operations, methods, packing and unpacking, nested tuples, iteration, conversion, and practical examples.

---

 ## 📚 Table of Contents

 - Introduction
- What is a Tuple?
- Why Use Tuples?
- Characteristics of Tuples
- Creating Tuples
- Empty Tuple
- Single-Element Tuple
- Tuple with Different Data Types
- Tuple Constructor
- Indexing
- Negative Indexing
- Slicing
- Tuple Immutability
- Tuple Packing
- Tuple Unpacking
- Extended Unpacking
- Tuple Concatenation
- Tuple Repetition
- Membership Operators
- Iteration
- Nested Tuples
- Tuple Methods
- Built-in Functions with Tuples
- Converting Between List and Tuple
- Tuple Comparison
- Tuple as Dictionary Keys
- Tuple vs List
- Mutable Objects Inside Tuples
- Common Mistakes
- Practical Examples
- Best Practices
- Key Takeaways

---

 # 📌 Introduction

 Python provides several built-in collection data types for storing multiple values.

 The major collection types are:

 | Data Type | Ordered | Mutable | Duplicates | Syntax |
| --- | --- | --- | --- | --- |
| List | ✅ | ✅ | ✅ | `[]` |
| Tuple | ✅ | ❌ | ✅ | `()` |
| Set | ❌ | ✅\* | ❌ | `{}` |
| Dictionary | ✅ | ✅ | Keys: ❌ | `{key: value}` |

 A **tuple** is an ordered collection of objects that cannot be modified after the tuple itself has been created.

 Tuples are particularly useful when data should remain fixed and should not be accidentally changed.

---

 # 📦 What is a Tuple?

 A tuple is a Python sequence containing zero or more elements.

 Tuples are normally written using parentheses:

```
numbers = (10, 20, 30, 40)

print(numbers)
```

 ### Output

```
(10, 20, 30, 40)
```

 However, the parentheses are not what fundamentally define a tuple. The **comma** is important.

 For example:

```
numbers = 10, 20, 30

print(type(numbers))
```

 ### Output

```
<class 'tuple'>
```

 Python treats the comma-separated values as a tuple.

---

 # 🎯 Why Use Tuples?

 Tuples are useful when you want to represent a group of values that should remain unchanged.

 Examples include:

 - Coordinates
- RGB colors
- Database records
- Configuration values
- Fixed collections
- Function return values
- Dictionary keys
- Constant-like data

 Example:

```
coordinates = (18.5204, 73.8567)

print(coordinates)
```

 The coordinate pair represents one logical piece of information and generally should not be modified.

---

 # ⭐ Characteristics of Tuples

 A Python tuple is:

 ### 1\. Ordered

 Elements maintain their position.

```
data = ("Python", "Java", "C++")

print(data[0])
```

 Output:

```
Python
```

 ### 2\. Immutable

 The tuple itself cannot be changed after creation.

```
numbers = (10, 20, 30)

# numbers[0] = 100
```

 This raises:

```
TypeError
```

 ### 3\. Allows Duplicate Values

```
numbers = (10, 20, 10, 30, 10)

print(numbers)
```

 Output:

```
(10, 20, 10, 30, 10)
```

 ### 4\. Can Store Different Data Types

```
data = (101, "Kishor", 95.5, True)

print(data)
```

 ### 5\. Supports Indexing

```
data = ("Python", "Java", "C++")

print(data[1])
```

 Output:

```
Java
```

 ### 6\. Supports Slicing

```
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

 Output:

```
(20, 30, 40)
```

---

 # 🏗️ Creating Tuples

 ## Basic Tuple

```
fruits = ("apple", "banana", "mango")

print(fruits)
```

 Output:

```
('apple', 'banana', 'mango')
```

---

 ## Empty Tuple

 An empty tuple can be created using:

```
empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))
```

 Output:

```
()
<class 'tuple'>
```

---

 # 1️⃣ Single-Element Tuple

 A common beginner mistake is forgetting the comma.

 ### Correct

```
number = (10,)

print(type(number))
```

 Output:

```
<class 'tuple'>
```

 ### Incorrect

```
number = (10)

print(type(number))
```

 Output:

```
<class 'int'>
```

 The comma creates the tuple:

```
number = 10,
```

 This is also valid:

```
number = (10,)
```

 ### Important Rule

 > **For a one-element tuple, the comma is required.**

---

 # 🔢 Tuple with Different Data Types

 A tuple can contain different types of values.

```
student = (
    101,
    "Kishor",
    21,
    85.5,
    True
)

print(student)
```

 A tuple can even contain other collections:

```
data = (
    10,
    "Python",
    [1, 2, 3],
    {"name": "Kishor"}
)

print(data)
```

---

 # 🔧 Tuple Constructor

 Python provides the `tuple()` constructor.

```
numbers = tuple([10, 20, 30, 40])

print(numbers)
```

 Output:

```
(10, 20, 30, 40)
```

 You can convert other iterables into tuples:

```
text = tuple("Python")

print(text)
```

 Output:

```
('P', 'y', 't', 'h', 'o', 'n')
```

 You can also convert a range:

```
numbers = tuple(range(1, 6))

print(numbers)
```

 Output:

```
(1, 2, 3, 4, 5)
```

---

 # 🔍 Indexing

 Tuple indexing starts from `0`.

```
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[0])
print(languages[1])
print(languages[2])
print(languages[3])
```

 Output:

```
Python
Java
C++
JavaScript
```

 ### Index Structure

```
Tuple:    Python   Java   C++   JavaScript
Index:       0       1     2        3
```

---

 # 🔙 Negative Indexing

 Python also supports negative indexes.

```
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[-1])
print(languages[-2])
print(languages[-3])
print(languages[-4])
```

 Output:

```
JavaScript
C++
Java
Python
```

 ### Negative Index Structure

```
Tuple:       Python    Java    C++    JavaScript
Index:         -4       -3      -2       -1
```

---

 # ✂️ Slicing

 Slicing allows us to extract a portion of a tuple.

 ### Syntax

```
tuple[start:stop:step]
```

 Example:

```
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

 Output:

```
(20, 30, 40)
```

 The `stop` index is excluded.

---

 ## Slice from Beginning

```
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
```

 Output:

```
(10, 20, 30)
```

---

 ## Slice to the End

```
print(numbers[2:])
```

 Output:

```
(30, 40, 50)
```

---

 ## Copy the Entire Tuple

```
print(numbers[:])
```

 Output:

```
(10, 20, 30, 40, 50)
```

---

 ## Slicing with Step

```
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])
```

 Output:

```
(10, 30, 50)
```

---

 ## Reverse a Tuple

```
numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])
```

 Output:

```
(50, 40, 30, 20, 10)
```

---

 # 🔒 Tuple Immutability

 One of the most important characteristics of tuples is **immutability**.

 Immutable means:

 > Once a tuple is created, its own elements cannot be added, removed, or replaced.

 Example:

```
numbers = (10, 20, 30)

numbers[0] = 100
```

 This produces:

```
TypeError: 'tuple' object does not support item assignment
```

---

 ## ❌ Cannot Modify an Element

```
data = ("Python", "Java", "C++")

# data[1] = "JavaScript"
```

 Not allowed.

---

 ## ❌ Cannot Append

```
data = (10, 20, 30)

# data.append(40)
```

 Tuples do not have an `append()` method.

---

 ## ❌ Cannot Remove

```
data = (10, 20, 30)

# data.remove(20)
```

 Tuples do not have a `remove()` method.

---

 ## ❌ Cannot Delete an Individual Element

```
data = (10, 20, 30)

# del data[0]
```

 This is not allowed.

---

 ## ✅ Can Delete the Entire Tuple

 Although individual elements cannot be deleted, the variable can be deleted:

```
data = (10, 20, 30)

del data
```

 After this, `data` no longer exists.

---

 # 🎒 Tuple Packing

 When multiple values are assigned to a single variable, Python automatically packs them into a tuple.

```
student = "Kishor", 21, "Python"

print(student)
print(type(student))
```

 Output:

```
('Kishor', 21, 'Python')
<class 'tuple'>
```

 This is called **tuple packing**.

---

 # 📤 Tuple Unpacking

 Tuple unpacking means assigning tuple elements to separate variables.

```
student = ("Kishor", 21, "Python")

name, age, language = student

print(name)
print(age)
print(language)
```

 Output:

```
Kishor
21
Python
```

 The number of variables should normally match the number of tuple elements.

---

 # ⭐ Extended Unpacking

 Python allows one variable to collect multiple values using `*`.

```
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

 Output:

```
10
[20, 30, 40]
50
```

 Notice that `middle` becomes a **list**, even though the original object is a tuple.

---

 ## Ignoring Values

 You can use `_` when a value is not needed.

```
student = ("Kishor", 21, "Python")

name, _, language = student

print(name)
print(language)
```

 Output:

```
Kishor
Python
```

---

 # ➕ Tuple Concatenation

 Two tuples can be joined using `+`.

```
a = (1, 2, 3)
b = (4, 5, 6)

result = a + b

print(result)
```

 Output:

```
(1, 2, 3, 4, 5, 6)
```

 ### Important

 The original tuples are not modified.

 A **new tuple** is created.

---

 # 🔁 Tuple Repetition

 The `*` operator repeats a tuple.

```
numbers = (1, 2)

result = numbers * 3

print(result)
```

 Output:

```
(1, 2, 1, 2, 1, 2)
```

---

 # 🔎 Membership Operators

 You can use `in` and `not in` with tuples.

```
languages = ("Python", "Java", "C++")

print("Python" in languages)
print("PHP" in languages)
```

 Output:

```
True
False
```

 Using `not in`:

```
print("PHP" not in languages)
```

 Output:

```
True
```

---

 # 🔄 Iterating Through a Tuple

 A tuple can be iterated using a `for` loop.

```
languages = ("Python", "Java", "C++")

for language in languages:
    print(language)
```

 Output:

```
Python
Java
C++
```

---

 ## Tuple with Index Using `enumerate()`

```
languages = ("Python", "Java", "C++")

for index, language in enumerate(languages):
    print(index, language)
```

 Output:

```
0 Python
1 Java
2 C++
```

---

 # 🪆 Nested Tuples

 A tuple can contain another tuple.

```
students = (
    ("Kishor", 85),
    ("Rahul", 90),
    ("Amit", 78)
)

print(students)
```

 You can access nested elements:

```
print(students[0])
print(students[0][0])
print(students[0][1])
```

 Output:

```
('Kishor', 85)
Kishor
85
```

---

 # 🛠️ Tuple Methods

 Tuples provide only two major methods:

 1. `count()`
2. `index()`

 This is because tuples are immutable and therefore do not need methods such as `append()`, `remove()`, or `sort()`.

---

 # 1\. `count()`

 `count()` returns the number of times a value occurs in a tuple.

 ### Syntax

```
tuple.count(value)
```

 Example:

```
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

 Output:

```
3
```

---

 # 2\. `index()`

 `index()` returns the position of the first occurrence of a value.

 ### Syntax

```
tuple.index(value)
```

 Example:

```
languages = ("Python", "Java", "C++", "Python")

print(languages.index("Python"))
```

 Output:

```
0
```

 Although `"Python"` occurs twice, `index()` returns the position of the **first occurrence**.

---

 # 🔢 Built-in Functions with Tuples

 Python provides several useful built-in functions.

---

 ## `len()`

 Returns the number of elements.

```
numbers = (10, 20, 30, 40)

print(len(numbers))
```

 Output:

```
4
```

---

 ## `max()`

 Returns the largest value.

```
numbers = (10, 50, 20, 40)

print(max(numbers))
```

 Output:

```
50
```

---

 ## `min()`

 Returns the smallest value.

```
numbers = (10, 50, 20, 40)

print(min(numbers))
```

 Output:

```
10
```

---

 ## `sum()`

 Returns the total of numeric elements.

```
numbers = (10, 20, 30, 40)

print(sum(numbers))
```

 Output:

```
100
```

---

 ## `sorted()`

 `sorted()` returns a **list**, not a tuple.

```
numbers = (40, 10, 30, 20)

result = sorted(numbers)

print(result)
print(type(result))
```

 Output:

```
[10, 20, 30, 40]
<class 'list'>
```

 If you want the result as a tuple:

```
result = tuple(sorted(numbers))

print(result)
```

 Output:

```
(10, 20, 30, 40)
```

---

 # 🔄 Converting Between List and Tuple

 ## List → Tuple

```
numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
```

 Output:

```
(10, 20, 30)
```

---

 ## Tuple → List

```
numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print(numbers_list)
```

 Output:

```
[10, 20, 30]
```

 This technique can be useful when you need to modify tuple data.

 ### Example

```
numbers = (10, 20, 30)

temp = list(numbers)

temp.append(40)

numbers = tuple(temp)

print(numbers)
```

 Output:

```
(10, 20, 30, 40)
```

 The original tuple was not modified. A new tuple was created.

---

 # ⚖️ Tuple Comparison

 Python can compare tuples.

 Comparison occurs element by element.

```
a = (1, 2, 3)
b = (1, 2, 4)

print(a < b)
```

 Output:

```
True
```

 Python first compares `1` with `1`.

 They are equal, so it compares `2` with `2`.

 They are equal again, so it compares `3` with `4`.

 Since:

```
3 < 4
```

 the result is `True`.

---

 # 🔑 Tuple as Dictionary Keys

 Because tuples are immutable, a tuple containing hashable values can be used as a dictionary key.

 Example:

```
locations = {
    (18.5204, 73.8567): "Pune",
    (19.0760, 72.8777): "Mumbai"
}

print(locations[(18.5204, 73.8567)])
```

 Output:

```
Pune
```

 This is a useful real-world application of tuples.

---

 # 🆚 Tuple vs List

 | Feature | Tuple | List |
| --- | --- | --- |
| Syntax | `()` | `[]` |
| Mutable | ❌ | ✅ |
| Ordered | ✅ | ✅ |
| Indexed | ✅ | ✅ |
| Allows duplicates | ✅ | ✅ |
| Can contain different data types | ✅ | ✅ |
| `append()` | ❌ | ✅ |
| `remove()` | ❌ | ✅ |
| `sort()` method | ❌ | ✅ |
| `count()` | ✅ | ✅ |
| `index()` | ✅ | ✅ |
| Can be dictionary key\* | ✅ | ❌ |
| Best for | Fixed data | Changeable data |

 \* A tuple can be a dictionary key only when its elements are hashable.

---

 # 🧠 Mutable Objects Inside Tuples

 An important concept is that tuple immutability applies to the **tuple structure**, not necessarily to objects stored inside it.

 Example:

```
data = ([10, 20, 30], "Python")

data[0].append(40)

print(data)
```

 Output:

```
([10, 20, 30, 40], 'Python')
```

 Why did this work?

 The tuple still contains the same list object at index `0`.

 We did **not replace** the tuple element.

 We modified the list object contained inside the tuple.

 However, this is not allowed:

```
# data[0] = [100, 200]
```

 The tuple's element reference itself cannot be replaced.

 ### Important Concept

 > A tuple is immutable, but an object stored inside the tuple may itself be mutable.

---

 # ⚠️ Common Mistakes

 ## Mistake 1: Forgetting the comma

```
number = (10)

print(type(number))
```

 This is an integer.

 Correct:

```
number = (10,)
```

---

 ## Mistake 2: Trying to use `append()`

```
numbers = (10, 20, 30)

# numbers.append(40)
```

 Tuples do not have `append()`.

---

 ## Mistake 3: Trying to change an element

```
numbers = (10, 20, 30)

# numbers[0] = 100
```

 This produces a `TypeError`.

---

 ## Mistake 4: Wrong number of variables during unpacking

```
numbers = (10, 20, 30)

# a, b = numbers
```

 This raises:

```
ValueError
```

 There are three values but only two variables.

 Correct:

```
a, b, c = numbers
```

---

 # 💻 Practical Examples

 ## Example 1: Student Record

```
student = (
    101,
    "Kishor",
    "Python",
    85
)

roll_no, name, course, marks = student

print("Roll No:", roll_no)
print("Name:", name)
print("Course:", course)
print("Marks:", marks)
```

 Output:

```
Roll No: 101
Name: Kishor
Course: Python
Marks: 85
```

---

 ## Example 2: Find Total Marks

```
marks = (85, 90, 78, 92, 88)

total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)
```

 Output:

```
Total: 433
Average: 86.6
```

---

 ## Example 3: Find Highest and Lowest Marks

```
marks = (85, 90, 78, 92, 88)

print("Highest:", max(marks))
print("Lowest:", min(marks))
```

 Output:

```
Highest: 92
Lowest: 78
```

---

 ## Example 4: Count Occurrences

```
numbers = (1, 2, 3, 2, 4, 2, 5)

count = numbers.count(2)

print("2 occurs", count, "times")
```

 Output:

```
2 occurs 3 times
```

---

 ## Example 5: Coordinates

```
point = (10, 20)

x, y = point

print("X:", x)
print("Y:", y)
```

 Output:

```
X: 10
Y: 20
```

---

 ## Example 6: RGB Color

```
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

print("Red:", red)
print("Green:", green)
print("Blue:", blue)
```

 Tuples are a natural representation for fixed RGB values.

---

 ## Example 7: Swapping Variables

 Tuple unpacking makes variable swapping simple:

```
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

 Output:

```
20
10
```

 Conceptually, Python packs the right-hand side and then unpacks it into the variables.

---

 ## Example 8: Iterate Through Nested Tuples

```
students = (
    ("Kishor", 85),
    ("Rahul", 90),
    ("Amit", 78)
)

for name, marks in students:
    print(name, "->", marks)
```

 Output:

```
Kishor -> 85
Rahul -> 90
Amit -> 78
```

---

 # 🚀 Real-World Applications

 Tuples are commonly useful when representing data that naturally behaves like a fixed record.

 ### Coordinates

```
location = (18.5204, 73.8567)
```

 ### RGB Colors

```
color = (255, 128, 0)
```

 ### Database-like Records

```
employee = (101, "Kishor", "Developer", 75000)
```

 ### Function Return Values

```
def get_user():
    return "Kishor", 21

name, age = get_user()

print(name)
print(age)
```

 ### Dictionary Keys

```
routes = {
    ("Pune", "Mumbai"): 150,
    ("Pune", "Nashik"): 210
}
```

---

 # 🏆 Best Practices

 ### 1\. Use tuples for fixed data

 Good:

```
days = ("Monday", "Tuesday", "Wednesday")
```

 Use a list when the collection needs frequent modification.

---

 ### 2\. Use meaningful unpacking

 Instead of:

```
data = ("Kishor", 21, "Python")

a, b, c = data
```

 Prefer:

```
name, age, language = data
```

 This improves readability.

---

 ### 3\. Use `_` for intentionally ignored values

```
name, _, language = ("Kishor", 21, "Python")
```

 This clearly communicates that the middle value is not required.

---

 ### 4\. Remember the single-element comma

 Always use:

```
item = ("Python",)
```

 not:

```
item = ("Python")
```

---

 ### 5\. Don't convert tuples to lists unnecessarily

 If data is logically fixed, keeping it as a tuple communicates your intent and prevents accidental structural modification.

---

 # 🧩 Quick Reference

```
# Create
t = (10, 20, 30)

# Empty tuple
t = ()

# Single-element tuple
t = (10,)

# Without parentheses
t = 10, 20, 30

# Indexing
t[0]

# Negative indexing
t[-1]

# Slicing
t[1:3]

# Reverse
t[::-1]

# Length
len(t)

# Count
t.count(10)

# First index
t.index(20)

# Membership
10 in t

# Concatenation
t1 + t2

# Repetition
t * 3

# Unpacking
a, b, c = t

# Extended unpacking
a, *b = t

# Tuple conversion
tuple([1, 2, 3])

# List conversion
list(t)

# Delete entire tuple
del t
```

---

 # 📌 Key Takeaways

 - A **tuple** is an ordered collection of values.
- Tuples are **immutable**.
- Tuples can contain duplicate values.
- Tuples can contain different data types.
- Tuple indexing starts from `0`.
- Negative indexing starts from `-1`.
- Tuples support slicing.
- A single-element tuple requires a **comma**.
- Tuples support concatenation using `+`.
- Tuples support repetition using `*`.
- Tuples support membership operators such as `in` and `not in`.
- Tuples can be unpacked into individual variables.
- Python provides `count()` and `index()` tuple methods.
- Built-in functions such as `len()`, `min()`, `max()`, and `sum()` can work with tuples.
- Tuples can be converted to lists and vice versa.
- Tuples containing hashable elements can be used as dictionary keys.
- Tuples are ideal for representing **fixed or read-only collections**.

---

 # 🎓 Learning Outcome

 After completing this module, you should be able to:

 - Understand what tuples are and why they are used.
- Create tuples using different techniques.
- Work with tuple indexes and slices.
- Explain tuple immutability.
- Perform tuple concatenation and repetition.
- Use tuple methods effectively.
- Pack and unpack tuple values.
- Work with nested tuples.
- Convert between tuples and lists.
- Use tuples in practical Python programs.
- Understand when to choose a tuple instead of a list.

---

 ## 🔗 Repository

 This module is part of the **Python Programming** learning repository.

 📂 **Module:** `07-Tuples`

 🔗 **GitHub:**\
  Kishor055/Python-Programming — 07-Tuples

---

 ## 🐍 Continue Learning

 Recommended learning sequence:

```
01 → Python Basics
02 → Variables & Data Types
03 → Operators
04 → Conditional Statements
05 → Loops
06 → Lists
07 → Tuples
08 → Dictionaries
09 → Sets
...
```

---

 ### ⭐ Support

 If this repository helps you learn Python, consider giving it a ⭐ on GitHub and sharing it with other Python learners.

 **Happy Coding! 🐍💻**
