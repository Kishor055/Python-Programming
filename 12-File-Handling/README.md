# 📁 12 — File Handling

> **Learn how Python reads, writes, updates, and manages files and persistent data.**

File Handling is an essential Python skill for working with **real-world data**.

Programs often need to:

* Read configuration files
* Store user data
* Save application output
* Process logs
* Read CSV/JSON data
* Create reports
* Work with images and other binary files

Python provides built-in tools such as `open()`, file objects, `pathlib`, and `json` to handle these tasks efficiently.

---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

* What is File Handling?
* Opening files with `open()`
* File modes
* Reading files
* Writing files
* Appending data
* Using `with`
* Closing files
* `read()`
* `readline()`
* `readlines()`
* Iterating over files
* `write()`
* `writelines()`
* File cursor
* `seek()`
* `tell()`
* Text files
* Binary files
* Encoding
* `pathlib`
* JSON files
* Error handling with files
* Practical file-processing projects

---

# 🧠 1. What is File Handling?

**File Handling** means performing operations on files stored on a computer.

Common operations include:

```text
Create
   ↓
Open
   ↓
Read / Write / Append
   ↓
Update
   ↓
Close
```

Python provides the built-in `open()` function for working with files. ([Python documentation][1])

---

# 📂 2. Types of Files

Files can broadly be divided into two categories.

## 2.1 Text Files

Text files contain human-readable characters.

Examples:

```text
.txt
.csv
.json
.py
.html
.xml
```

Example:

```text
Hello Python
Welcome to File Handling
```

---

## 2.2 Binary Files

Binary files contain raw bytes.

Examples:

```text
.jpg
.png
.pdf
.mp3
.mp4
.exe
.zip
```

Binary files should be opened using binary mode such as `rb` or `wb`. ([Python documentation][1])

---

# 🔓 3. Opening a File

The basic syntax is:

```python
open(filename, mode)
```

Example:

```python
file = open("data.txt", "r")
```

A more explicit version:

```python
file = open("data.txt", "r", encoding="utf-8")
```

Using an explicit encoding such as UTF-8 is a good practice for text files. ([Python documentation][1])

---

# ⚙️ 4. File Modes

Python provides different modes for different operations.

| Mode | Meaning       |
| ---- | ------------- |
| `r`  | Read          |
| `w`  | Write         |
| `a`  | Append        |
| `x`  | Create        |
| `r+` | Read + Write  |
| `w+` | Write + Read  |
| `a+` | Append + Read |
| `rb` | Read binary   |
| `wb` | Write binary  |
| `ab` | Append binary |

### Quick Reference

```text
r   → Read
w   → Write / overwrite
a   → Append
x   → Create new file
b   → Binary mode
+   → Read and write
```

⚠️ Be careful with `w`: if the file already exists, its existing contents are replaced. ([Python documentation][1])

---

# 📖 5. Reading a File

Suppose `data.txt` contains:

```text
Python
Java
C++
JavaScript
```

You can read it using:

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

Output:

```text
Python
Java
C++
JavaScript
```

---

# ⭐ 6. Using `with`

The recommended approach is:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

The `with` statement automatically closes the file, even if an exception occurs. ([Python documentation][1])

### Best Practice

Prefer:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()
```

instead of manually managing:

```python
file = open("data.txt", "r")
data = file.read()
file.close()
```

---

# 📄 7. `read()`

`read()` reads file contents.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)
```

You can also specify the number of characters to read:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read(10)

print(data)
```

---

# 📃 8. `readline()`

`readline()` reads one line at a time.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)
```

This is useful when processing files line by line. ([Python documentation][2])

---

# 📚 9. `readlines()`

`readlines()` returns all lines as a list.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

Example output:

```python
[
    "Python\n",
    "Java\n",
    "C++\n"
]
```

---

# 🔄 10. Iterating Through a File

A memory-efficient way to process lines is:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

This is often preferable to loading a very large file completely into memory. ([Python documentation][2])

---

# ✍️ 11. Writing to a File

Use `w` mode:

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python!")
```

The file will contain:

```text
Hello Python!
```

---

# 📝 12. Writing Multiple Lines

```python
lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

---

# ➕ 13. Appending to a File

Use `a` mode when you want to add content without replacing existing data.

```python
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nJavaScript")
```

If the original file contains:

```text
Python
Java
```

After appending:

```text
Python
Java
JavaScript
```

---

# 🆕 14. Creating a New File

Use `x` mode:

```python
with open("new_file.txt", "x", encoding="utf-8") as file:
    file.write("New file created!")
```

If the file already exists, Python raises an exception.

---

# 🔒 15. Closing a File

If you open a file manually:

```python
file = open("data.txt", "r", encoding="utf-8")

data = file.read()

file.close()
```

Always close files when you are finished.

Better:

```python
with open("data.txt", encoding="utf-8") as file:
    data = file.read()
```

The `with` statement handles closing automatically. ([Python documentation][1])

---

# 🎯 16. File Cursor

When Python reads or writes a file, it maintains a current position called the **file cursor**.

Example:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read(5))
    print(file.read(5))
```

The second `read()` continues from the current cursor position.

---

# 📍 17. `tell()`

`tell()` returns the current file position.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.tell())

    file.read(5)

    print(file.tell())
```

---

# 🔙 18. `seek()`

`seek()` moves the file cursor to a specific position.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    file.seek(0)

    print(file.read())
```

Basic pattern:

```python
file.seek(position)
```

Python's file objects provide `tell()` and `seek()` for inspecting and changing the current file position. ([Python documentation][2])

---

# 🔤 19. Encoding

Text files contain characters that must be encoded.

Prefer:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()
```

UTF-8 is a common modern choice for text files and helps ensure consistent handling of Unicode text. ([Python documentation][1])

---

# 🖼️ 20. Binary File Handling

For binary files, use `b` mode.

Example:

```python
with open("image.jpg", "rb") as file:
    data = file.read()

print(type(data))
```

Output:

```text
<class 'bytes'>
```

To write binary data:

```python
with open("copy.jpg", "wb") as file:
    file.write(data)
```

---

# 📁 21. Working with File Paths

Python provides the `pathlib` module for modern path handling.

```python
from pathlib import Path

file_path = Path("data.txt")

print(file_path.exists())
print(file_path.name)
print(file_path.suffix)
```

Example:

```text
True
data.txt
.txt
```

---

# 🗂️ 22. Creating Directories with `pathlib`

```python
from pathlib import Path

folder = Path("data")

folder.mkdir(exist_ok=True)
```

Create nested directories:

```python
folder = Path("data/users/profiles")

folder.mkdir(parents=True, exist_ok=True)
```

---

# 🔍 23. Checking Whether a File Exists

```python
from pathlib import Path

file = Path("data.txt")

if file.exists():
    print("File exists")
else:
    print("File does not exist")
```

---

# 🗑️ 24. Deleting a File

```python
from pathlib import Path

file = Path("data.txt")

if file.exists():
    file.unlink()
```

⚠️ Be careful when deleting files programmatically.

---

# 🧾 25. File Properties

Using `pathlib`:

```python
from pathlib import Path

file = Path("data.txt")

print(file.name)
print(file.stem)
print(file.suffix)
print(file.parent)
print(file.exists())
```

Useful properties:

| Property    | Meaning                     |
| ----------- | --------------------------- |
| `.name`     | File name                   |
| `.stem`     | File name without extension |
| `.suffix`   | Extension                   |
| `.parent`   | Parent directory            |
| `.exists()` | Checks existence            |

---

# 🧮 26. Counting Lines in a File

```python
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))
```

A memory-efficient approach:

```python
count = 0

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print("Number of lines:", count)
```

---

# 🔎 27. Searching Inside a File

```python
keyword = "Python"

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        if keyword in line:
            print(line.strip())
```

---

# 🔄 28. Replacing Text in a File

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

content = content.replace("Python", "Python Programming")

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(content)
```

---

# 🧹 29. Removing Empty Lines

```python
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

clean_lines = [line for line in lines if line.strip()]

with open("clean_data.txt", "w", encoding="utf-8") as file:
    file.writelines(clean_lines)
```

---

# 🧾 30. JSON File Handling

JSON is commonly used for structured data.

Example:

```json
{
    "name": "Kishor",
    "age": 25,
    "skills": ["Python", "Machine Learning"]
}
```

Python provides the built-in `json` module for serialization and deserialization. ([Python documentation][3])

---

## Write JSON

```python
import json

data = {
    "name": "Kishor",
    "age": 25,
    "skills": ["Python", "Machine Learning"]
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
```

---

## Read JSON

```python
import json

with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
```

Output:

```python
{
    'name': 'Kishor',
    'age': 25,
    'skills': ['Python', 'Machine Learning']
}
```

---

# 🔄 31. Serialization vs Deserialization

```text
Python Object
     ↓
Serialization
     ↓
JSON
     ↓
File / Network
     ↓
Deserialization
     ↓
Python Object
```

### Serialization

```python
json.dump()
json.dumps()
```

### Deserialization

```python
json.load()
json.loads()
```

---

# ⚠️ 32. Handling File Errors

Files may not exist or may not be accessible.

Example:

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found.")
```

Multiple errors:

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("Permission denied.")
```

This becomes especially important in real-world applications.

---

# 🏗️ 33. Real-World Example — Log File

Imagine an application generating logs:

```text
logs/
└── application.log
```

Python:

```python
from datetime import datetime

message = f"{datetime.now()} - Application started\n"

with open("application.log", "a", encoding="utf-8") as file:
    file.write(message)
```

Every execution adds a new log entry.

---

# 💼 34. Real-World Example — Student Records

```python
students = [
    "Rahul,85\n",
    "Amit,92\n",
    "Priya,88\n"
]

with open("students.csv", "w", encoding="utf-8") as file:
    file.writelines(students)
```

Result:

```text
students.csv

Rahul,85
Amit,92
Priya,88
```

---

# 🔥 35. Practical Mini Project — Notes Manager

### Project Structure

```text
notes_manager/
│
├── main.py
└── notes.txt
```

### `main.py`

```python
def add_note(note):
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")


def show_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("No notes found.")


while True:
    print("\n1. Add Note")
    print("2. Show Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter note: ")
        add_note(note)

    elif choice == "2":
        show_notes()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
```

This project combines:

```text
Functions
   +
File Handling
   +
Exception Handling
   +
User Input
```

---

# 🧠 36. Common Mistakes

### ❌ Forgetting to close files

```python
file = open("data.txt")
data = file.read()
```

Prefer:

```python
with open("data.txt", encoding="utf-8") as file:
    data = file.read()
```

---

### ❌ Accidentally overwriting data

```python
open("data.txt", "w")
```

`w` replaces existing content.

Use:

```python
open("data.txt", "a")
```

when you want to append.

---

### ❌ Using text mode for binary files

Avoid:

```python
open("image.jpg", "r")
```

Use:

```python
open("image.jpg", "rb")
```

---

### ❌ Ignoring encoding

Prefer:

```python
open("data.txt", "r", encoding="utf-8")
```

instead of relying on the platform default.

---

# 🧪 37. Practice Exercises

## 🟢 Beginner

1. Create a text file using Python.
2. Write your name and age into a file.
3. Read the contents of a file.
4. Count the number of lines.
5. Count the number of words.
6. Append new text to an existing file.
7. Check whether a file exists.
8. Create a directory using `pathlib`.

---

## 🟡 Intermediate

9. Search for a word inside a file.
10. Replace a word throughout a file.
11. Remove empty lines.
12. Copy one text file into another.
13. Count character frequency.
14. Create a simple log system.
15. Read and write JSON data.

---

## 🔴 Advanced

16. Build a Notes Manager.
17. Build a Contact Manager using JSON.
18. Build a Student Record System.
19. Build a File Organizer.
20. Build a Log Analyzer.
21. Build a Text File Word Counter.
22. Build a JSON-based To-Do application.

---

# 💬 38. Interview Questions

### Basic

**Q1. What is File Handling?**

Working with files to read, write, append, create, or process persistent data.

**Q2. What does `open()` do?**

It opens a file and returns a file object.

**Q3. What is the difference between `r`, `w`, and `a`?**

```text
r → Read
w → Write / overwrite
a → Append
```

**Q4. Why use `with open()`?**

It automatically manages the file resource and closes the file after the block. ([Python documentation][1])

**Q5. What does `read()` do?**

Reads file content.

---

### Intermediate

**Q6. Difference between `read()`, `readline()`, and `readlines()`?**

```text
read()      → Entire content / specified amount
readline()  → One line
readlines() → List of lines
```

**Q7. What is `seek()`?**

Moves the file cursor to a specified position.

**Q8. What is `tell()`?**

Returns the current file position.

**Q9. What is binary mode?**

A mode for reading/writing raw bytes, specified using `b`.

**Q10. What is JSON?**

A text-based structured data format commonly used for data exchange and storage.

---

# 📌 39. Quick Revision

```text
FILE HANDLING
│
├── open()
│
├── Modes
│   ├── r
│   ├── w
│   ├── a
│   ├── x
│   ├── r+
│   └── b
│
├── Reading
│   ├── read()
│   ├── readline()
│   └── readlines()
│
├── Writing
│   ├── write()
│   └── writelines()
│
├── Cursor
│   ├── tell()
│   └── seek()
│
├── Resource Management
│   └── with
│
├── Paths
│   └── pathlib
│
├── Structured Data
│   └── json
│
└── Error Handling
    ├── FileNotFoundError
    └── PermissionError
```

---

# 🏆 40. Best Practices

Follow these practices when working with files:

### ✅ Use `with`

```python
with open("data.txt", encoding="utf-8") as file:
    data = file.read()
```

### ✅ Specify encoding

```python
encoding="utf-8"
```

### ✅ Use the correct mode

```text
Read      → r
Overwrite → w
Append    → a
Binary    → rb / wb
```

### ✅ Use `pathlib`

```python
from pathlib import Path
```

### ✅ Handle expected exceptions

```python
try:
    ...
except FileNotFoundError:
    ...
```

### ✅ Avoid loading huge files unnecessarily

Process large files line by line:

```python
with open("large.log", encoding="utf-8") as file:
    for line in file:
        process(line)
```

---

# 📚 Official References

* [Python Documentation — Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
* [Python Documentation — `open()`](https://docs.python.org/3/library/functions.html#open)
* [Python Documentation — `pathlib`](https://docs.python.org/3/library/pathlib.html)
* [Python Documentation — `json`](https://docs.python.org/3/library/json.html)

The official Python tutorial covers file modes, file-object methods, `with`, binary files, and JSON serialization/deserialization. ([Python documentation][1])

---

# 🎯 Key Takeaway

> **File Handling allows Python programs to move beyond temporary in-memory data and work with persistent information stored on disk.**

Master these concepts:

```text
open()
  ↓
Modes
  ↓
read()
  ↓
write()
  ↓
append()
  ↓
with
  ↓
pathlib
  ↓
JSON
  ↓
Real-World Projects
```

Once you understand File Handling, you are ready to build applications that **store, process, and manage real-world data**.

---

## ⏭️ Next Topic

➡️ **[13 — Exception Handling](../13-Exception-Handling/)**

Continue your Python journey:

```text
11. Modules & Packages
          ↓
12. File Handling
          ↓
13. Exception Handling
          ↓
14. Object-Oriented Programming
          ↓
15. Advanced Python
```

---

⭐ **Keep coding. Keep building. Keep learning Python.**
