 # 09 — Dictionaries in Python

 > A complete guide to Python Dictionaries — from fundamentals to practical usage, methods, dictionary operations, comprehensions, nested dictionaries, and real-world examples.

---

 ## 📌 Overview

 A **Dictionary** in Python is a built-in data structure used to store data in **key-value pairs**.

 Each value is accessed using its corresponding key.

 ### Basic Structure

```
dictionary = {
    "key": "value"
}
```

 Example:

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}
```

 Here:

 - `"name"` is a key.
- `"Alice"` is its value.
- `"age"` is a key.
- `21` is its value.
- `"course"` is a key.
- `"Python"` is its value.

---

 ## 🎯 Learning Objectives

 After completing this topic, you should understand:

 - What a Dictionary is
- How to create Dictionaries
- Keys and values
- Accessing dictionary values
- Adding and updating data
- Removing elements
- Dictionary methods
- Membership testing
- Iterating over Dictionaries
- Dictionary operations
- Dictionary comprehensions
- Nested Dictionaries
- Copying Dictionaries
- Practical use cases
- Common mistakes

---

 # 1\. What is a Dictionary?

 A Dictionary stores data as:

```
key → value
```

 Example:

```
student = {
    "name": "Alice",
    "age": 21,
    "city": "Pune",
}
```

 You can retrieve data using its key:

```
print(student["name"])
```

 Output:

```
Alice
```

---

 # 2\. Dictionary Characteristics

 Python Dictionaries have several important characteristics.

 | Property | Dictionary |
| --- | --- |
| Key-value structure | ✅ |
| Ordered | ✅ |
| Mutable | ✅ |
| Duplicate keys | ❌ |
| Duplicate values | ✅ |
| Indexing | ❌ |
| Key-based access | ✅ |
| Nested data | ✅ |

 Modern Python Dictionaries preserve **insertion order**.

---

 # 3\. Creating a Dictionary

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print(student)
```

---

 ## Empty Dictionary

```
student = {}

print(student)
```

 Or:

```
student = dict()

print(student)
```

---

 # 4\. Keys and Values

 Consider:

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}
```

 Keys:

```
name
age
course
```

 Values:

```
Alice
21
Python
```

 You can retrieve all keys:

```
print(student.keys())
```

 And all values:

```
print(student.values())
```

---

 # 5\. Dictionary Keys

 Dictionary keys must be **hashable**.

 Common valid keys include:

```
data = {
    "name": "Alice",
    101: "Employee",
    (1, 2): "Coordinates",
}
```

 Lists cannot be used as dictionary keys:

```
data = {
    [1, 2]: "Invalid"
}
```

 This raises:

```
TypeError: unhashable type: 'list'
```

---

 # 6\. Accessing Dictionary Values

 ## Using `[]`

```
student = {
    "name": "Alice",
    "age": 21,
}

print(student["name"])
print(student["age"])
```

 Output:

```
Alice
21
```

---

 ## Using `get()`

```
print(student.get("name"))
```

 `get()` is useful when a key may not exist.

```
print(student.get("email"))
```

 Output:

```
None
```

 You can provide a default value:

```
print(student.get("email", "Not available"))
```

 Output:

```
Not available
```

---

 # 7\. `[]` vs `get()`

 This is an important distinction.

 ### Using `[]`

```
student = {
    "name": "Alice"
}

print(student["email"])
```

 Raises:

```
KeyError
```

 ### Using `get()`

```
print(student.get("email"))
```

 Returns:

```
None
```

 ### Professional guideline

 Use:

```
dictionary[key]
```

 when the key **must exist**.

 Use:

```
dictionary.get(key)
```

 when the key **may be missing**.

---

 # 8\. Adding Dictionary Elements

 You can add a new key-value pair simply by assigning a value.

```
student = {
    "name": "Alice",
    "age": 21,
}

student["city"] = "Pune"

print(student)
```

 Result:

```
{
    "name": "Alice",
    "age": 21,
    "city": "Pune"
}
```

---

 # 9\. Updating Existing Values

 If the key already exists, assignment changes its value.

```
student = {
    "name": "Alice",
    "age": 21,
}

student["age"] = 22

print(student)
```

 The value of `"age"` is updated.

---

 # 10\. Updating Multiple Values

 Use `update()`.

```
student = {
    "name": "Alice",
    "age": 21,
}

student.update({
    "age": 22,
    "city": "Pune",
})

print(student)
```

---

 # 11\. Removing Dictionary Elements

 Python provides several ways to remove dictionary data.

---

 ## `pop()`

 Removes a specified key and returns its value.

```
student = {
    "name": "Alice",
    "age": 21,
    "city": "Pune",
}

age = student.pop("age")

print("Removed:", age)
print(student)
```

---

 ## `popitem()`

 Removes and returns the last inserted key-value pair.

```
student = {
    "name": "Alice",
    "age": 21,
    "city": "Pune",
}

item = student.popitem()

print("Removed:", item)
print(student)
```

---

 ## `del`

```
student = {
    "name": "Alice",
    "age": 21,
}

del student["age"]

print(student)
```

---

 ## `clear()`

 Removes everything.

```
student = {
    "name": "Alice",
    "age": 21,
}

student.clear()

print(student)
```

 Output:

```
{}
```

---

 # 12\. Dictionary Methods

 Important methods include:

 | Method | Purpose |
| --- | --- |
| `get()` | Safely retrieve a value |
| `keys()` | Return dictionary keys |
| `values()` | Return dictionary values |
| `items()` | Return key-value pairs |
| `update()` | Add/update multiple pairs |
| `pop()` | Remove a specified key |
| `popitem()` | Remove the last inserted pair |
| `setdefault()` | Get a value and optionally create the key |
| `copy()` | Create a shallow copy |
| `clear()` | Remove all elements |
| `fromkeys()` | Create a dictionary from keys |

---

 # 13\. `keys()`

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print(student.keys())
```

 Iterating:

```
for key in student.keys():
    print(key)
```

---

 # 14\. `values()`

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

for value in student.values():
    print(value)
```

---

 # 15\. `items()`

 `items()` provides both keys and values.

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

for key, value in student.items():
    print(key, ":", value)
```

 This is one of the most commonly used patterns when working with Dictionaries.

---

 # 16\. Membership Testing

 Use `in` to check whether a key exists.

```
student = {
    "name": "Alice",
    "age": 21,
}

print("name" in student)
print("email" in student)
```

 Output:

```
True
False
```

 By default, membership testing checks **keys**, not values.

---

 # 17\. Iterating Over a Dictionary

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

for key in student:
    print(key)
```

 To access both:

```
for key, value in student.items():
    print(f"{key}: {value}")
```

---

 # 18\. Dictionary Length

 Use `len()`:

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print(len(student))
```

 Output:

```
3
```

---

 # 19\. Duplicate Keys

 A Dictionary cannot contain duplicate keys.

```
student = {
    "name": "Alice",
    "name": "Bob",
}

print(student)
```

 The later value replaces the earlier value.

 Result:

```
{'name': 'Bob'}
```

---

 # 20\. Duplicate Values

 Duplicate values are allowed.

```
students = {
    "Alice": 90,
    "Bob": 90,
    "Charlie": 85,
}

print(students)
```

 Multiple keys can point to the same value.

---

 # 21\. Dictionary Operations

 Dictionaries are primarily designed around **key-based access**, rather than mathematical set-style operations.

 Useful operations include:

```
student["name"]
```

```
"name" in student
```

```
len(student)
```

```
student.keys()
```

```
student.values()
```

```
student.items()
```

---

 # 22\. Dictionary Comprehension

 Dictionary comprehension provides a concise way to create Dictionaries.

 ### Syntax

```
{key: value for item in iterable}
```

 Example:

```
numbers = range(1, 6)

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)
```

 Output:

```
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

 # 23\. Dictionary Comprehension with Condition

```
numbers = range(1, 11)

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)
```

 Output:

```
{
    2: 4,
    4: 16,
    6: 36,
    8: 64,
    10: 100
}
```

---

 # 24\. Nested Dictionaries

 A Dictionary can contain another Dictionary.

```
students = {
    "student_1": {
        "name": "Alice",
        "age": 21,
    },
    "student_2": {
        "name": "Bob",
        "age": 22,
    },
}
```

 Access nested data:

```
print(students["student_1"]["name"])
```

 Output:

```
Alice
```

 Nested Dictionaries are useful for representing structured data.

---

 # 25\. Practical Example — Student

```
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
    "marks": 92,
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])
```

---

 # 26\. Practical Example — Product

```
product = {
    "id": 101,
    "name": "Laptop",
    "price": 75000,
    "stock": 15,
}

print("Product:", product["name"])
print("Price:", product["price"])
print("Stock:", product["stock"])
```

---

 # 27\. Practical Example — Employee

```
employee = {
    "id": 1001,
    "name": "Alice",
    "department": "Engineering",
    "skills": ["Python", "SQL", "Git"],
}

print(employee["name"])
print(employee["department"])
print(employee["skills"])
```

 Dictionaries can contain other Python data structures such as Lists, Sets, Tuples, and even other Dictionaries.

---

 # 28\. Practical Example — Word Frequency

 Dictionaries are commonly used to count occurrences.

```
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "python",
]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

 Output:

```
{
    'python': 3,
    'java': 2,
    'c++': 1
}
```

 This is a very important real-world Dictionary pattern.

---

 # 29\. Practical Example — Configuration

 Dictionaries are useful for application configuration.

```
config = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
}

print("Host:", config["host"])
print("Port:", config["port"])
print("Debug:", config["debug"])
```

---

 # 30\. Practical Example — API-Style Data

 Dictionaries are commonly used to represent structured records.

```
user = {
    "id": 101,
    "username": "alice",
    "email": "alice@example.com",
    "active": True,
}
```

 Access:

```
print(user["username"])
print(user["email"])
```

 This structure is also conceptually similar to JSON objects used extensively in APIs.

---

 # 31\. Copying a Dictionary

 Use `copy()` to create a shallow copy.

```
original = {
    "name": "Alice",
    "age": 21,
}

copied = original.copy()

copied["age"] = 22

print("Original:", original)
print("Copied:", copied)
```

 The original Dictionary remains unchanged.

---

 # 32\. `setdefault()`

 `setdefault()` retrieves a value if the key exists.

 If the key does not exist, it inserts the key with a default value.

```
student = {
    "name": "Alice",
}

age = student.setdefault("age", 21)

print(age)
print(student)
```

 Result:

```
21
{'name': 'Alice', 'age': 21}
```

---

 # 33\. `fromkeys()`

 `fromkeys()` creates a Dictionary using a sequence of keys.

```
keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)
```

 Result:

```
{
    "name": None,
    "age": None,
    "city": None
}
```

 You can provide a default value:

```
student = dict.fromkeys(keys, "Unknown")

print(student)
```

---

 # 34\. Dictionary vs List

 | Feature | List | Dictionary |
| --- | --- | --- |
| Structure | Values | Key-value pairs |
| Access | Index | Key |
| Duplicate values | ✅ | ✅ |
| Duplicate keys | N/A | ❌ |
| Mutable | ✅ | ✅ |
| Use case | Ordered collection | Named/structured data |

 ### Use a List when:

 - Position matters
- You have a sequence of values
- You need index-based access

 ### Use a Dictionary when:

 - Data has meaningful keys
- You need key-based lookup
- You are representing structured records

---

 # 35\. Dictionary vs Set

 | Feature | Set | Dictionary |
| --- | --- | --- |
| Stores | Values | Key-value pairs |
| Unique elements | ✅ | Keys only |
| Key-value relationship | ❌ | ✅ |
| Membership | Values | Keys |
| Mutable | ✅ | ✅ |
| Typical use | Unique data | Structured data |

---

 # 36\. Common Mistakes

 ## Mistake 1 — Accessing a Missing Key

```
student = {
    "name": "Alice"
}

print(student["age"])
```

 This raises:

```
KeyError
```

 Use:

```
print(student.get("age"))
```

 when the key may be missing.

---

 ## Mistake 2 — Assuming `in` Checks Values

```
student = {
    "name": "Alice"
}

print("Alice" in student)
```

 This is:

```
False
```

 because Dictionary membership checks keys.

 To check values:

```
print("Alice" in student.values())
```

---

 ## Mistake 3 — Using a Mutable Key

 This is invalid:

```
data = {
    [1, 2]: "value"
}
```

 Dictionary keys must be hashable.

---

 ## Mistake 4 — Accidentally Overwriting a Key

```
data = {
    "name": "Alice"
}

data["name"] = "Bob"
```

 The previous value is replaced.

---

 # 37\. Performance Note

 Dictionary lookup is typically **O(1) average-case** because Dictionaries are implemented using hash tables.

 This makes Dictionaries highly useful when you need frequent key-based lookups.

 For example:

```
users = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
}

print(users[102])
```

 Instead of searching through every item manually, Python can use the key's hash to locate the corresponding entry efficiently.

---

 # 38\. Dictionary Methods Cheat Sheet

```
data.get(key)
```

 Safely retrieve a value.

```
data.keys()
```

 Get keys.

```
data.values()
```

 Get values.

```
data.items()
```

 Get key-value pairs.

```
data.update(other)
```

 Add/update multiple entries.

```
data.pop(key)
```

 Remove a specific key.

```
data.popitem()
```

 Remove the last inserted pair.

```
data.setdefault(key, default)
```

 Get or create a key.

```
data.copy()
```

 Create a shallow copy.

```
data.clear()
```

 Remove everything.

---

 # 39\. Key Takeaways

 > **Python Dictionary = Key → Value**

 Remember these concepts:

 - Dictionaries store data as **key-value pairs**.
- Keys must be **hashable**.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.
- Dictionaries preserve insertion order.
- Use `dictionary[key]` when the key is expected to exist.
- Use `dictionary.get(key)` when the key may be missing.
- Use `keys()` for keys.
- Use `values()` for values.
- Use `items()` for key-value pairs.
- Use `update()` to add or modify multiple entries.
- Use `pop()` to remove a specific key.
- Use `popitem()` to remove the last inserted pair.
- Dictionary comprehensions provide concise Dictionary creation.
- Nested Dictionaries are useful for structured data.
- Dictionaries are excellent for fast key-based lookup.

---

 # 40\. Interview Questions

 ### Basic

 1. What is a Dictionary in Python?
2. What is the difference between a key and a value?
3. Can Dictionary keys be duplicated?
4. Can Dictionary values be duplicated?
5. How do you create an empty Dictionary?
6. How do you access a Dictionary value?
7. What happens when you access a missing key?

 ### Intermediate

 8. What is the difference between `[]` and `get()`?
9. What does `keys()` return?
10. What does `values()` return?
11. What does `items()` return?
12. What is the difference between `pop()` and `popitem()`?
13. What does `setdefault()` do?
14. What is Dictionary comprehension?
15. What is a nested Dictionary?

 ### Advanced

 16. Why must Dictionary keys be hashable?
17. Why are Dictionary lookups typically O(1) average-case?
18. What happens when the same key is specified multiple times?
19. What is the difference between a shallow copy and a deep copy?
20. When should you use a Dictionary instead of a List or Set?

---

 ## 📂 Recommended Files

```
09-Dictionaries/
│
├── README.md
├── 01_dictionary_basics.py
├── 02_dictionary_methods.py
├── 03_dictionary_operations.py
├── 04_dictionary_comprehension.py
├── 05_nested_dictionaries.py
└── 06_practical_examples.py
```

---

 ## 🚀 Learning Path

 Follow the files in this order:

```
01_dictionary_basics.py
          ↓
02_dictionary_methods.py
          ↓
03_dictionary_operations.py
          ↓
04_dictionary_comprehension.py
          ↓
05_nested_dictionaries.py
          ↓
06_practical_examples.py
```

 By the end of this chapter, you should be comfortable using Dictionaries to model and manipulate structured real-world data.

 > **Dictionary = Fast Key-Based Access + Structured Data + Flexible Values**

 I can continue with **`09-Dictionaries/01_dictionary_basics.py`** in the same detailed pro-coder style.
