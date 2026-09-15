# 🧩 19 — JSON in Python

> A complete beginner-to-advanced guide to JSON, Python's `json` module, serialization, deserialization, APIs, configuration files, data exchange, validation, and real-world applications.

---

## 📌 Overview

**JSON** stands for:

> **JavaScript Object Notation**

JSON is a lightweight, text-based data format commonly used for storing and exchanging structured data.

Although JSON originated from the JavaScript ecosystem, it is language-independent and is widely used with:

* Python
* JavaScript
* Java
* C++
* C#
* Go
* PHP
* Ruby
* APIs
* Databases
* Configuration systems
* Cloud services

Python provides a built-in `json` module for working with JSON data.

```python
import json
```

---

# 🎯 Learning Objectives

By the end of this chapter, you will understand:

* What JSON is
* Why JSON is important
* JSON syntax
* JSON data types
* JSON objects
* JSON arrays
* JSON strings
* JSON numbers
* JSON booleans
* JSON `null`
* Python-to-JSON conversion
* JSON-to-Python conversion
* Serialization
* Deserialization
* `json.dumps()`
* `json.loads()`
* `json.dump()`
* `json.load()`
* Pretty printing
* Sorting JSON keys
* JSON files
* Nested JSON
* JSON validation
* Custom serialization
* API responses
* Error handling
* Security considerations
* Real-world JSON projects

---

# 1. What is JSON?

JSON is a structured text format used to represent data.

Example:

```json
{
  "name": "Kishor",
  "age": 25,
  "language": "Python"
}
```

The data contains:

```text
name     → Kishor
age      → 25
language → Python
```

JSON is especially useful when different systems need to exchange data.

---

# 2. Why is JSON Important?

JSON is one of the most important data formats in modern software development.

It is commonly used for:

```text
Python Application
       ↓
      JSON
       ↓
REST API
       ↓
Web Application
```

For example, a backend server might return:

```json
{
  "id": 101,
  "username": "kishor",
  "active": true
}
```

A frontend application can then read and use this information.

---

# 3. Characteristics of JSON

JSON is:

* Lightweight
* Human-readable
* Machine-readable
* Structured
* Language-independent
* Easy to parse
* Widely supported
* Common in APIs
* Common in configuration files

---

# 4. Basic JSON Structure

A JSON document can contain an **object**:

```json
{
  "name": "Kishor",
  "age": 25
}
```

or an **array**:

```json
[
  "Python",
  "Java",
  "C++"
]
```

JSON can also contain nested structures.

```json
{
  "user": {
    "name": "Kishor",
    "skills": [
      "Python",
      "Machine Learning"
    ]
  }
}
```

---

# 5. JSON Data Types

JSON supports six primary data types:

| JSON Type | Example              |
| --------- | -------------------- |
| String    | `"Python"`           |
| Number    | `100`                |
| Object    | `{"name": "Kishor"}` |
| Array     | `["Python", "Java"]` |
| Boolean   | `true`               |
| Null      | `null`               |

---

# 6. JSON Object

A JSON object is surrounded by:

```text
{}
```

Example:

```json
{
  "name": "Kishor",
  "age": 25,
  "city": "Pune"
}
```

Objects contain:

```text
key : value
```

Each key must be a JSON string.

Correct:

```json
{
  "name": "Kishor"
}
```

---

# 7. JSON Array

A JSON array is surrounded by:

```text
[]
```

Example:

```json
[
  "Python",
  "Java",
  "C++"
]
```

Arrays can contain multiple values.

They can also contain objects:

```json
[
  {
    "id": 1,
    "name": "Kishor"
  },
  {
    "id": 2,
    "name": "Rahul"
  }
]
```

---

# 8. JSON Strings

Strings must use double quotes.

Correct:

```json
{
  "name": "Kishor"
}
```

Incorrect JSON:

```json
{
  "name": 'Kishor'
}
```

Unlike Python source code, JSON strings are conventionally represented using **double quotes**.

---

# 9. JSON Numbers

JSON supports numbers.

```json
{
  "age": 25,
  "price": 999.99,
  "quantity": 10
}
```

There is no separate JSON integer and float type in the same sense as Python's type system; JSON uses the general **number** type.

---

# 10. JSON Boolean

JSON uses:

```json
true
false
```

Example:

```json
{
  "active": true,
  "verified": false
}
```

### Important

JSON uses lowercase:

```text
true
false
```

Python uses:

```python
True
False
```

---

# 11. JSON Null

JSON uses:

```json
null
```

Example:

```json
{
  "middle_name": null
}
```

Python uses:

```python
None
```

---

# 12. JSON vs Python Data Types

Python and JSON have closely related data structures.

| Python  | JSON    |
| ------- | ------- |
| `dict`  | object  |
| `list`  | array   |
| `str`   | string  |
| `int`   | number  |
| `float` | number  |
| `True`  | `true`  |
| `False` | `false` |
| `None`  | `null`  |

Example:

```python
data = {
    "name": "Kishor",
    "age": 25,
    "active": True,
    "skills": ["Python", "AI"],
    "middle_name": None
}
```

Equivalent JSON:

```json
{
  "name": "Kishor",
  "age": 25,
  "active": true,
  "skills": [
    "Python",
    "AI"
  ],
  "middle_name": null
}
```

---

# 13. Python's `json` Module

Python includes the `json` module in its standard library.

```python
import json
```

No external installation is required.

---

# 14. Serialization and Deserialization

These are two fundamental JSON concepts.

## Serialization

Converting Python data into JSON representation.

```text
Python Object
      ↓
Serialization
      ↓
JSON
```

## Deserialization

Converting JSON data back into Python objects.

```text
JSON
 ↓
Deserialization
 ↓
Python Object
```

---

# 15. `json.dumps()`

`dumps()` means:

> JSON dump to a string

It converts a Python object into a JSON-formatted string.

```python
import json

data = {
    "name": "Kishor",
    "age": 25
}

json_string = json.dumps(data)

print(json_string)
```

Output:

```text
{"name": "Kishor", "age": 25}
```

---

# 16. Python Dictionary → JSON String

```python
import json

user = {
    "id": 101,
    "name": "Kishor",
    "active": True
}

result = json.dumps(user)

print(result)
print(type(result))
```

Output:

```text
{"id": 101, "name": "Kishor", "active": true}
<class 'str'>
```

Notice:

```text
Python True
     ↓
JSON true
```

---

# 17. Pretty Printing JSON

By default, JSON may be displayed on one line.

You can make it easier to read using `indent`.

```python
import json

data = {
    "name": "Kishor",
    "age": 25,
    "skills": [
        "Python",
        "AI",
        "Machine Learning"
    ]
}

print(
    json.dumps(
        data,
        indent=4
    )
)
```

Output:

```json
{
    "name": "Kishor",
    "age": 25,
    "skills": [
        "Python",
        "AI",
        "Machine Learning"
    ]
}
```

Pretty printing is especially useful for:

* Debugging
* Configuration files
* Logs
* Documentation
* Human-readable output

---

# 18. Sorting JSON Keys

You can sort dictionary keys alphabetically.

```python
import json

data = {
    "z": 10,
    "a": 20,
    "m": 30
}

print(
    json.dumps(
        data,
        indent=4,
        sort_keys=True
    )
)
```

Output:

```json
{
    "a": 20,
    "m": 30,
    "z": 10
}
```

---

# 19. `json.loads()`

`loads()` means:

> Load JSON from a string.

It converts a JSON string into a Python object.

```python
import json

json_string = '{"name": "Kishor", "age": 25}'

data = json.loads(json_string)

print(data)
print(type(data))
```

Output:

```text
{'name': 'Kishor', 'age': 25}
<class 'dict'>
```

---

# 20. JSON String → Python Dictionary

```python
import json

json_data = """
{
    "name": "Kishor",
    "age": 25,
    "active": true
}
"""

data = json.loads(json_data)

print(data["name"])
print(data["age"])
print(data["active"])
```

---

# 21. `dumps()` vs `loads()`

Remember:

| Function       | Direction            |
| -------------- | -------------------- |
| `json.dumps()` | Python → JSON string |
| `json.loads()` | JSON string → Python |

Memory trick:

```text
s = string

dumps → dump to string
loads → load from string
```

---

# 22. JSON Files

JSON is commonly stored in `.json` files.

Example:

```text
users.json
```

Contents:

```json
{
    "name": "Kishor",
    "age": 25,
    "skills": [
        "Python",
        "AI"
    ]
}
```

---

# 23. Writing JSON to a File

Use `json.dump()`.

```python
import json

data = {
    "name": "Kishor",
    "age": 25,
    "skills": [
        "Python",
        "Machine Learning"
    ]
}

with open("user.json", "w") as file:
    json.dump(data, file, indent=4)
```

---

# 24. `json.dump()` vs `json.dumps()`

This distinction is very important.

### `json.dump()`

Writes JSON to a file-like object.

```python
json.dump(data, file)
```

### `json.dumps()`

Returns JSON as a string.

```python
json_string = json.dumps(data)
```

Remember:

```text
dump
 ↓
file

dumps
 ↓
string
```

---

# 25. Reading JSON from a File

Use `json.load()`.

```python
import json

with open("user.json", "r") as file:
    data = json.load(file)

print(data)
```

---

# 26. `json.load()` vs `json.loads()`

| Function       | Input            |
| -------------- | ---------------- |
| `json.load()`  | File-like object |
| `json.loads()` | String           |

Example:

```python
json.load(file)
```

versus:

```python
json.loads(json_string)
```

---

# 27. Complete JSON File Workflow

```text
Python Dictionary
       ↓
json.dump()
       ↓
JSON File
       ↓
json.load()
       ↓
Python Dictionary
```

Example:

```python
import json

data = {
    "name": "Kishor",
    "age": 25
}

# Write
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)
```

---

# 28. Nested JSON

JSON can contain objects inside objects.

```json
{
    "user": {
        "name": "Kishor",
        "contact": {
            "email": "kishor@example.com",
            "phone": "1234567890"
        }
    }
}
```

Access it in Python:

```python
print(data["user"]["name"])
print(data["user"]["contact"]["email"])
```

---

# 29. JSON Arrays of Objects

A very common API structure is:

```json
[
    {
        "id": 1,
        "name": "Kishor"
    },
    {
        "id": 2,
        "name": "Rahul"
    }
]
```

Python:

```python
users = json.loads(json_data)

for user in users:
    print(user["name"])
```

---

# 30. Complex JSON Structure

Example:

```json
{
    "company": {
        "name": "Tech Corp",
        "employees": [
            {
                "id": 1,
                "name": "Kishor",
                "skills": [
                    "Python",
                    "AI"
                ]
            },
            {
                "id": 2,
                "name": "Rahul",
                "skills": [
                    "Java",
                    "SQL"
                ]
            }
        ]
    }
}
```

Python can navigate this structure using dictionaries and lists.

```python
print(data["company"]["employees"][0]["name"])
```

---

# 31. Updating JSON Data

JSON loaded into Python becomes a normal Python object.

Therefore, you can modify it normally.

```python
import json

data = {
    "name": "Kishor",
    "age": 25
}

data["age"] = 26
data["city"] = "Pune"

print(json.dumps(data, indent=4))
```

---

# 32. Adding Data to a JSON File

```python
import json

with open("users.json", "r") as file:
    users = json.load(file)

users.append({
    "name": "New User",
    "age": 30
})

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)
```

Important:

JSON files are generally rewritten when you update their structured contents this way.

---

# 33. Removing Data

```python
import json

with open("users.json", "r") as file:
    users = json.load(file)

users.pop(0)

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)
```

---

# 34. JSON Error Handling

Invalid JSON can raise:

```python
json.JSONDecodeError
```

Example:

```python
import json

invalid_json = '{"name": "Kishor",}'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError:
    print("Invalid JSON")
```

---

# 35. Handling Missing JSON Files

```python
import json

try:
    with open("config.json", "r") as file:
        config = json.load(file)

except FileNotFoundError:
    print("Configuration file not found")

except json.JSONDecodeError:
    print("Invalid JSON configuration")
```

---

# 36. JSON and Unicode

JSON can represent Unicode text.

```python
import json

data = {
    "name": "किशोर",
    "language": "Python"
}

print(
    json.dumps(
        data,
        ensure_ascii=False,
        indent=4
    )
)
```

`ensure_ascii=False` allows Unicode characters to remain readable instead of being escaped unnecessarily.

---

# 37. JSON and `ensure_ascii`

Default behavior:

```python
json.dumps(data)
```

For non-ASCII characters, Python may represent them using escaped Unicode sequences.

For human-readable Unicode output:

```python
json.dumps(
    data,
    ensure_ascii=False
)
```

This is useful for multilingual applications.

---

# 38. JSON and Custom Objects

Consider:

```python
from datetime import datetime

data = {
    "created_at": datetime.now()
}
```

Trying to serialize this directly:

```python
import json

json.dumps(data)
```

can raise:

```text
TypeError
```

because standard JSON does not directly represent Python's `datetime` object.

---

# 39. Custom Serialization

One simple solution is to convert the datetime to a string.

```python
from datetime import datetime
import json

data = {
    "created_at": datetime.now().isoformat()
}

print(json.dumps(data))
```

Result:

```json
{
    "created_at": "2026-09-15T14:30:00"
}
```

---

# 40. `default=` in `json.dumps()`

You can provide a custom conversion function.

```python
from datetime import datetime
import json

data = {
    "created_at": datetime.now()
}

def convert(value):
    if isinstance(value, datetime):
        return value.isoformat()

    raise TypeError(
        f"Type {type(value)} is not JSON serializable"
    )

result = json.dumps(
    data,
    default=convert
)

print(result)
```

---

# 41. JSON and Dataclasses

Python dataclasses are not automatically JSON objects.

Example:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

You can convert the dataclass to a dictionary first.

```python
from dataclasses import asdict
import json

user = User("Kishor", 25)

data = asdict(user)

json_data = json.dumps(data)

print(json_data)
```

---

# 42. JSON and APIs

JSON is extremely common in REST APIs.

Example response:

```json
{
    "status": "success",
    "user": {
        "id": 101,
        "name": "Kishor"
    }
}
```

A Python program can parse this response:

```python
import json

response = """
{
    "status": "success",
    "user": {
        "id": 101,
        "name": "Kishor"
    }
}
"""

data = json.loads(response)

print(data["status"])
print(data["user"]["name"])
```

---

# 43. JSON Request Data

A client may send:

```json
{
    "username": "kishor",
    "email": "user@example.com",
    "active": true
}
```

The server can deserialize it into a Python dictionary and process it.

Typical flow:

```text
Client
  ↓
JSON Request
  ↓
API Server
  ↓
Python Dictionary
  ↓
Business Logic
  ↓
Python Dictionary
  ↓
JSON Response
  ↓
Client
```

---

# 44. JSON Configuration Files

JSON is often used for configuration.

Example:

```json
{
    "application": {
        "name": "MyApp",
        "version": "1.0"
    },
    "database": {
        "host": "localhost",
        "port": 5432
    }
}
```

Python:

```python
import json

with open("config.json") as file:
    config = json.load(file)

print(config["application"]["name"])
print(config["database"]["host"])
```

---

# 45. Configuration Best Practices

Avoid storing secrets directly in JSON files committed to Git.

Do not commit:

```json
{
    "password": "my-secret-password"
}
```

or:

```json
{
    "api_key": "secret-api-key"
}
```

Instead, use appropriate secret-management or environment-variable mechanisms.

---

# 46. JSON Validation

Valid JSON syntax does not necessarily mean valid application data.

For example:

```json
{
    "age": "twenty"
}
```

This is valid JSON.

But an application may require:

```text
age → integer
```

Therefore, applications often need two levels of validation:

```text
JSON Syntax Validation
          ↓
Application Data Validation
```

---

# 47. JSON Schema Concept

For larger applications, a JSON Schema can describe expected structure.

Conceptually:

```json
{
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "age": {
            "type": "integer"
        }
    }
}
```

JSON Schema can be used to define:

* Required fields
* Data types
* Allowed values
* String constraints
* Number constraints
* Object structure
* Array structure

---

# 48. JSON Security

JSON itself is just a data format, but applications processing JSON still need security controls.

Important practices:

### Validate input

Never assume incoming JSON is trustworthy.

### Limit input size

Very large JSON payloads can consume significant memory and processing time.

### Validate structure

Check required fields and expected data types.

### Avoid unsafe deserialization

Do not replace JSON parsing with unsafe mechanisms such as arbitrary object deserialization.

For normal JSON data:

```python
json.loads(data)
```

is the appropriate standard-library approach.

---

# 49. JSON vs Pickle

Python also provides `pickle`, but JSON and pickle serve different purposes.

| Feature                  | JSON                         | Pickle                           |
| ------------------------ | ---------------------------- | -------------------------------- |
| Human-readable           | ✅                            | ❌                                |
| Language-independent     | ✅                            | ❌                                |
| Python-specific          | ❌                            | ✅                                |
| API-friendly             | ✅                            | ❌                                |
| Arbitrary Python objects | Limited                      | More capable                     |
| Safe for untrusted data  | Better suited as data format | ❌ Do not unpickle untrusted data |

### Important

Never unpickle untrusted data.

For cross-language data exchange, JSON is generally much more appropriate.

---

# 50. JSON vs CSV

| Feature            | JSON      | CSV         |
| ------------------ | --------- | ----------- |
| Nested data        | ✅         | ❌           |
| Structured objects | ✅         | Limited     |
| Human-readable     | ✅         | ✅           |
| Tabular data       | Good      | Excellent   |
| API usage          | Excellent | Less common |
| Complex hierarchy  | Excellent | Poor        |

Use JSON when data is hierarchical or object-based.

Use CSV when data is primarily tabular.

---

# 51. JSON vs XML

| Feature           | JSON        | XML        |
| ----------------- | ----------- | ---------- |
| Syntax complexity | Lower       | Higher     |
| Readability       | High        | Moderate   |
| APIs              | Very common | Still used |
| Nested data       | ✅           | ✅          |
| Attributes        | ❌           | ✅          |
| Verbosity         | Lower       | Higher     |

Both formats remain relevant, depending on the system and requirements.

---

# 52. JSON File Encoding

When working with JSON files containing Unicode text, explicitly using UTF-8 is a good practice.

```python
import json

with open(
    "data.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        data,
        file,
        ensure_ascii=False,
        indent=4
    )
```

Reading:

```python
with open(
    "data.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)
```

---

# 53. JSON Lines

Another useful format is **JSON Lines**, often represented as:

```text
.jsonl
```

Instead of one large JSON array, each line contains a JSON value.

Example:

```json
{"id": 1, "name": "Kishor"}
{"id": 2, "name": "Rahul"}
{"id": 3, "name": "Amit"}
```

This format is useful for:

* Logs
* Data processing
* Machine learning datasets
* Streaming
* Large datasets

---

# 54. Processing JSON Lines

```python
import json

with open("users.jsonl", encoding="utf-8") as file:
    for line in file:
        user = json.loads(line)
        print(user["name"])
```

This approach can process records one line at a time instead of loading an entire collection into memory.

---

# 55. JSON Key Ordering

JSON objects are conceptually unordered collections of name/value pairs.

In Python, dictionaries preserve insertion order.

```python
data = {
    "name": "Kishor",
    "age": 25
}
```

Python will preserve insertion order when iterating over the dictionary.

However, applications should not generally depend on JSON object member ordering unless a specific protocol explicitly requires it.

---

# 56. Handling Optional Fields

Suppose JSON contains:

```json
{
    "name": "Kishor"
}
```

but your application expects an optional:

```text
city
```

You can safely access it with:

```python
city = data.get("city")
```

or:

```python
city = data.get("city", "Unknown")
```

This avoids an unnecessary `KeyError`.

---

# 57. Safe Nested Access

Given:

```json
{
    "user": {
        "profile": {
            "name": "Kishor"
        }
    }
}
```

You could access:

```python
name = data["user"]["profile"]["name"]
```

But if any intermediate key is missing, a `KeyError` occurs.

For complex external data, validate the structure before accessing deeply nested fields.

---

# 58. JSON Type Checking

After loading JSON:

```python
data = json.loads(json_string)
```

you can inspect the resulting Python type:

```python
print(type(data))
```

Examples:

```python
dict
list
str
int
float
bool
NoneType
```

The structure of the JSON determines the resulting Python object.

---

# 59. Common JSON Errors

### Invalid JSON

```json
{
    "name": "Kishor",
}
```

Trailing comma is invalid in standard JSON.

### Wrong boolean

```json
{
    "active": True
}
```

Incorrect.

Use:

```json
{
    "active": true
}
```

### Wrong null

```json
{
    "value": None
}
```

Incorrect.

Use:

```json
{
    "value": null
}
```

### Single quotes

```json
{
    'name': 'Kishor'
}
```

Not standard JSON.

Use double quotes.

---

# 60. Common Python Mistakes

## ❌ Mistake 1

```python
json.loads(data)
```

when `data` is already a Python dictionary.

`loads()` expects a JSON string.

---

## ❌ Mistake 2

```python
json.load(json_string)
```

`load()` expects a file-like object.

---

## ❌ Mistake 3

Confusing:

```python
dump()
```

with:

```python
dumps()
```

Remember:

```text
dump  → file
dumps → string

load  → file
loads → string
```

---

# 61. Professional JSON Workflow

A production application commonly follows:

```text
External Data
     ↓
Receive JSON
     ↓
Parse
     ↓
Validate
     ↓
Normalize
     ↓
Business Logic
     ↓
Transform
     ↓
Serialize
     ↓
JSON Response
```

For APIs:

```text
HTTP Request
     ↓
JSON Payload
     ↓
json.loads()
     ↓
Validation
     ↓
Application Logic
     ↓
json.dumps()
     ↓
HTTP Response
```

---

# 62. JSON Design Best Practices

### ✅ Use meaningful keys

Good:

```json
{
    "first_name": "Kishor"
}
```

Less descriptive:

```json
{
    "x": "Kishor"
}
```

### ✅ Keep structures consistent

Avoid returning different types for the same field.

Bad:

```json
{"age": 25}
```

and sometimes:

```json
{"age": "twenty-five"}
```

### ✅ Validate external data

Never blindly trust incoming JSON.

### ✅ Keep JSON reasonably small

Avoid unnecessary duplication.

### ✅ Use UTF-8

Especially for multilingual data.

### ✅ Use ISO 8601 for timestamps

Example:

```text
2026-09-15T14:30:00Z
```

### ✅ Do not store secrets casually

Use appropriate secret management.

---

# 63. Mini Project — User Management System

Create:

```text
users.json
```

Example:

```json
[
    {
        "id": 1,
        "name": "Kishor",
        "email": "kishor@example.com"
    }
]
```

Python:

```python
import json

FILE = "users.json"


def load_users():
    try:
        with open(FILE, encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_users(users):
    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            users,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_user(name, email):
    users = load_users()

    user = {
        "id": len(users) + 1,
        "name": name,
        "email": email
    }

    users.append(user)

    save_users(users)


add_user(
    "Kishor",
    "kishor@example.com"
)
```

This project demonstrates:

* File handling
* JSON serialization
* JSON deserialization
* Functions
* Lists
* Dictionaries
* Error handling
* Persistent storage

---

# 64. Practice Exercises

## 🟢 Beginner

### Exercise 1

Create a Python dictionary representing a student and convert it to JSON.

### Exercise 2

Convert this JSON into a Python dictionary:

```json
{
    "name": "Kishor",
    "age": 25
}
```

### Exercise 3

Write a dictionary to `student.json`.

### Exercise 4

Read `student.json`.

### Exercise 5

Pretty-print a JSON object.

---

## 🟡 Intermediate

### Exercise 6

Create a JSON file containing 5 students.

### Exercise 7

Read the students and print their names.

### Exercise 8

Add a new student.

### Exercise 9

Delete a student.

### Exercise 10

Search for a student by ID.

### Exercise 11

Handle a missing JSON file.

### Exercise 12

Handle invalid JSON.

---

## 🔴 Advanced

### Exercise 13

Build a JSON-based task manager.

Features:

```text
Add task
Update task
Delete task
Mark completed
Search tasks
Save to JSON
Load from JSON
```

### Exercise 14

Build an API response parser.

### Exercise 15

Build a JSON configuration manager.

### Exercise 16

Build a JSON log analyzer.

### Exercise 17

Build a JSON-to-CSV converter.

### Exercise 18

Build a JSON Lines processor for large datasets.

---

# 65. Interview Questions

## Beginner

1. What is JSON?
2. Why is JSON widely used?
3. What are JSON's basic data types?
4. What is a JSON object?
5. What is a JSON array?
6. How is JSON different from a Python dictionary?
7. Why does JSON use `true` instead of `True`?

## Intermediate

8. What does `json.dumps()` do?
9. What does `json.loads()` do?
10. What does `json.dump()` do?
11. What does `json.load()` do?
12. What is serialization?
13. What is deserialization?
14. How do you pretty-print JSON?
15. How do you sort JSON keys?
16. How do you handle invalid JSON?

## Advanced

17. How do you serialize a custom Python object?
18. What is the purpose of `default=` in `json.dumps()`?
19. How would you serialize a `datetime` object?
20. What is JSON Schema?
21. What is JSON Lines?
22. What is the difference between JSON and pickle?
23. Why should untrusted pickle data never be loaded?
24. How should API JSON payloads be validated?
25. How would you process very large JSON datasets?
26. How would you design a reliable JSON-based configuration system?

---

# 66. Quick Revision Cheat Sheet

### Import

```python
import json
```

### Python → JSON string

```python
json.dumps(data)
```

### JSON string → Python

```python
json.loads(data)
```

### Python → JSON file

```python
json.dump(data, file)
```

### JSON file → Python

```python
json.load(file)
```

### Pretty JSON

```python
json.dumps(
    data,
    indent=4
)
```

### Sorted keys

```python
json.dumps(
    data,
    sort_keys=True
)
```

### Unicode

```python
json.dumps(
    data,
    ensure_ascii=False
)
```

### JSON error

```python
json.JSONDecodeError
```

---

# 67. JSON Mental Model

```text
                    JSON
                     │
          ┌──────────┴──────────┐
          │                     │
        Object                Array
          │                     │
        dict                  list
          │                     │
          └──────────┬──────────┘
                     │
                json module
                     │
        ┌────────────┴────────────┐
        │                         │
   Serialization            Deserialization
        │                         │
    dumps / dump             loads / load
        │                         │
        └──────────┬──────────────┘
                   │
             Python Objects
```

---

# 68. Final Takeaways

The most important concepts from this chapter are:

```text
JSON
 ↓
Structured data format

json.dumps()
 ↓
Python → JSON string

json.loads()
 ↓
JSON string → Python

json.dump()
 ↓
Python → JSON file

json.load()
 ↓
JSON file → Python

Serialization
 ↓
Object → JSON representation

Deserialization
 ↓
JSON representation → Object
```

A professional Python developer should be comfortable working with JSON for:

* APIs
* Configuration
* Data exchange
* Persistent storage
* Logs
* Automation
* Web applications
* Cloud services
* Data pipelines

The most important distinction to memorize is:

```text
dump   → file
dumps  → string

load   → file
loads  → string
```

---

# 📚 References

* [Python `json` documentation](https://docs.python.org/3/library/json.html?utm_source=chatgpt.com)
* [Python Standard Library](https://docs.python.org/3/library/?utm_source=chatgpt.com)
* [JSON official website](https://www.json.org/?utm_source=chatgpt.com)
* [JSON Schema documentation](https://json-schema.org/?utm_source=chatgpt.com)
* [Python documentation](https://docs.python.org/3/?utm_source=chatgpt.com)

---

# 🧭 Python Learning Roadmap

```text
17-Regular-Expressions
          ↓
18-Date-and-Time
          ↓
19-JSON
          ↓
20-Next Topic
```

---

## 🚀 What's Next?

Continue your Python journey with the next topic in the repository:

**➡️ `20-APIs-and-Web-Requests`**

Keep learning. Keep building. Keep writing clean Python. 🐍
