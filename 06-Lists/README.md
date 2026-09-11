 # 06 — Lists

 ## 📚 Python Lists

 A **list** is one of Python's most important built-in data structures.

 Lists are used to store **multiple values in a single variable**.

```
numbers = [10, 20, 30, 40, 50]
```

 A Python list is:

 - Ordered
- Mutable
- Dynamic
- Indexable
- Sliceable
- Iterable
- Heterogeneous
- Able to contain duplicate values
- Able to contain other lists and complex objects

---

 ## 📂 Chapter Structure

```
06-Lists/
│
├── README.md
│
├── 01_list_basics.py
├── 02_list_indexing.py
├── 03_list_slicing.py
├── 04_list_methods.py
├── 05_list_operations.py
├── 06_list_comprehension.py
├── 07_nested_lists.py
└── 08_list_practice.py
```

---

 # 1\. What Is a List?

 A list is a collection of objects enclosed inside square brackets `[]`.

```
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

 Output:

```
[10, 20, 30, 40, 50]
```

 Each element is separated by a comma.

```
languages = ["Python", "Java", "C++", "JavaScript"]
```

---

 # 2\. Creating Lists

 ## Empty List

```
numbers = []

print(numbers)
```

 Output:

```
[]
```

 ## List With Values

```
numbers = [10, 20, 30, 40]
```

 ## List of Strings

```
languages = ["Python", "Java", "C++"]
```

 ## Mixed Data Types

 Python lists can contain different data types.

```
data = [
    "Kishor",
    25,
    95.5,
    True
]
```

 ## Nested List

 A list can contain another list.

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

---

 # 3\. List Characteristics

 ## Ordered

 Lists preserve the order in which elements are inserted.

```
items = ["A", "B", "C"]

print(items)
```

 The order remains:

```
A
B
C
```

 ## Mutable

 Lists can be changed after creation.

```
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

 Output:

```
[100, 20, 30]
```

 ## Allow Duplicates

```
numbers = [10, 20, 10, 30, 10]

print(numbers)
```

 ## Dynamic

 Lists can grow or shrink during program execution.

```
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

---

 # 4\. List Indexing

 Lists use **zero-based indexing**.

```
languages = ["Python", "Java", "C++", "JavaScript"]
```

 Indexes:

```
Python      Java       C++       JavaScript
   0          1         2             3
```

 Access an element:

```
print(languages[0])
```

 Output:

```
Python
```

---

 # 5\. Negative Indexing

 Negative indexing starts from the end.

```
Python      Java       C++       JavaScript
  -4         -3        -2            -1
```

```
languages = ["Python", "Java", "C++", "JavaScript"]

print(languages[-1])
```

 Output:

```
JavaScript
```

 The most common use:

```
languages[-1]
```

 means:

 > Get the last element.

---

 # 6\. Accessing List Elements

```
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
```

---

 # 7\. Changing List Elements

 Lists are mutable.

```
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
```

 Output:

```
[10, 200, 30]
```

 Unlike strings, list elements can be changed directly.

---

 # 8\. List Length

 Use `len()` to determine the number of elements.

```
numbers = [10, 20, 30, 40]

print(len(numbers))
```

 Output:

```
4
```

 The last valid positive index is:

```
len(numbers) - 1
```

---

 # 9\. List Slicing

 List slicing extracts a portion of a list.

 Syntax:

```
list[start:stop:step]
```

 Example:

```
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

 Output:

```
[20, 30, 40]
```

 The `stop` index is excluded.

---

 # 10\. Common Slicing Patterns

```
numbers = [10, 20, 30, 40, 50]
```

 First three:

```
numbers[:3]
```

 Last three:

```
numbers[-3:]
```

 From index 2:

```
numbers[2:]
```

 Everything except the last element:

```
numbers[:-1]
```

 Every second element:

```
numbers[::2]
```

 Reverse:

```
numbers[::-1]
```

---

 # 11\. Adding Elements

 Python provides several ways to add elements.

 ## append()

 Adds one element to the end.

```
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

 Output:

```
[10, 20, 30, 40]
```

---

 ## insert()

 Adds an element at a specific index.

```
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

 Output:

```
[10, 15, 20, 30]
```

 Syntax:

```
list.insert(index, value)
```

---

 ## extend()

 Adds multiple elements from another iterable.

```
numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)
```

 Output:

```
[10, 20, 30, 40, 50, 60]
```

 ### `append()` vs `extend()`

```
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
```

 Output:

```
[1, 2, [3, 4]]
```

 But:

```
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
```

 Output:

```
[1, 2, 3, 4]
```

---

 # 12\. Removing Elements

 ## remove()

 Removes the first matching value.

```
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

 Output:

```
[10, 30, 20]
```

 If the value does not exist, `remove()` raises `ValueError`.

---

 ## pop()

 Removes and returns an element.

```
numbers = [10, 20, 30]

value = numbers.pop()

print(value)
print(numbers)
```

 Output:

```
30
[10, 20]
```

 Remove by index:

```
numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)
```

 Output:

```
20
[10, 30]
```

---

 ## del

 `del` can remove an element or a slice.

```
numbers = [10, 20, 30]

del numbers[1]

print(numbers)
```

 Output:

```
[10, 30]
```

 Delete a range:

```
numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)
```

---

 ## clear()

 Removes all elements.

```
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

 Output:

```
[]
```

---

 # 13\. Searching Lists

 ## in

 Check whether an element exists.

```
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

 Output:

```
True
```

 ## not in

```
print("Ruby" not in languages)
```

---

 ## index()

 Returns the index of the first matching value.

```
numbers = [10, 20, 30, 40]

print(numbers.index(30))
```

 Output:

```
2
```

---

 ## count()

 Counts occurrences of a value.

```
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

 Output:

```
3
```

---

 # 14\. Iterating Over Lists

 The most common approach is a `for` loop.

```
languages = ["Python", "Java", "C++"]

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

 # 15\. Iterating With Index

 Use `range()` and `len()`:

```
languages = ["Python", "Java", "C++"]

for index in range(len(languages)):
    print(index, languages[index])
```

---

 # 16\. enumerate()

 `enumerate()` provides both the index and value.

```
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)
```

 Output:

```
0 Python
1 Java
2 C++
```

 You can also specify the starting index:

```
for index, language in enumerate(languages, start=1):
    print(index, language)
```

---

 # 17\. List Concatenation

 Two lists can be combined using `+`.

```
first = [1, 2, 3]
second = [4, 5, 6]

result = first + second

print(result)
```

 Output:

```
[1, 2, 3, 4, 5, 6]
```

---

 # 18\. List Repetition

 Use `*` to repeat a list.

```
numbers = [1, 2, 3]

print(numbers * 2)
```

 Output:

```
[1, 2, 3, 1, 2, 3]
```

---

 # 19\. Comparing Lists

 Lists can be compared.

```
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

 Output:

```
True
```

 Order matters:

```
a = [1, 2, 3]
b = [3, 2, 1]

print(a == b)
```

 Output:

```
False
```

---

 # 20\. Sorting Lists

 ## sort()

 Sorts the list in place.

```
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
```

 Output:

```
[10, 20, 30, 40, 50]
```

 Descending order:

```
numbers.sort(reverse=True)
```

---

 ## sorted()

 `sorted()` returns a new sorted list.

```
numbers = [50, 10, 40, 20, 30]

result = sorted(numbers)

print(result)
print(numbers)
```

 The original list remains unchanged.

 ### `sort()` vs `sorted()`

```
sort()
    └── modifies the original list

sorted()
    └── returns a new sorted list
```

---

 # 21\. Reversing Lists

 ## reverse()

 Reverses the list in place.

```
numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
```

 Output:

```
[4, 3, 2, 1]
```

---

 ## Slicing Reverse

```
numbers = [1, 2, 3, 4]

result = numbers[::-1]

print(result)
```

 Unlike `reverse()`, this creates a new list.

---

 # 22\. List Copying

 Lists require special attention when copying.

```
original = [10, 20, 30]

copy = original.copy()

copy.append(40)

print(original)
print(copy)
```

 Output:

```
[10, 20, 30]
[10, 20, 30, 40]
```

---

 # 23\. Reference Assignment

 This does **not** create an independent list.

```
original = [10, 20, 30]

copy = original

copy.append(40)

print(original)
```

 Output:

```
[10, 20, 30, 40]
```

 Both variables refer to the same list.

---

 # 24\. Copy Methods

 Common shallow-copy techniques:

```
copy1 = original.copy()
```

```
copy2 = list(original)
```

```
copy3 = original[:]
```

---

 # 25\. List Comprehension

 List comprehensions provide a concise way to create lists.

 Traditional approach:

```
numbers = []

for number in range(1, 6):
    numbers.append(number * 2)

print(numbers)
```

 List comprehension:

```
numbers = [number * 2 for number in range(1, 6)]

print(numbers)
```

 Output:

```
[2, 4, 6, 8, 10]
```

---

 # 26\. List Comprehension With Condition

```
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

 Output:

```
[2, 4, 6]
```

 General syntax:

```
[expression for item in iterable if condition]
```

---

 # 27\. Nested Lists

 A list can contain other lists.

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

 Access a row:

```
print(matrix[0])
```

 Output:

```
[1, 2, 3]
```

 Access an individual value:

```
print(matrix[1][2])
```

 Output:

```
6
```

---

 # 28\. List Unpacking

 Values can be assigned to multiple variables.

```
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)
```

 Output:

```
10
20
30
```

---

 # 29\. Extended Unpacking

 The `*` operator can capture multiple elements.

```
numbers = [10, 20, 30, 40, 50]

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

---

 # 30\. Built-in Functions With Lists

 Python provides many useful built-in functions.

```
numbers = [10, 20, 30, 40, 50]
```

 Length:

```
len(numbers)
```

 Minimum:

```
min(numbers)
```

 Maximum:

```
max(numbers)
```

 Sum:

```
sum(numbers)
```

 Sorted:

```
sorted(numbers)
```

---

 # 31\. `any()` and `all()`

 ## any()

 Returns `True` if at least one value is truthy.

```
values = [False, False, True]

print(any(values))
```

 Output:

```
True
```

 ## all()

 Returns `True` if every value is truthy.

```
values = [True, True, True]

print(all(values))
```

 Output:

```
True
```

---

 # 32\. Converting Other Iterables to Lists

 Use `list()`.

```
text = "Python"

characters = list(text)

print(characters)
```

 Output:

```
['P', 'y', 't', 'h', 'o', 'n']
```

 Tuple to list:

```
values = (10, 20, 30)

numbers = list(values)
```

 Range to list:

```
numbers = list(range(5))

print(numbers)
```

 Output:

```
[0, 1, 2, 3, 4]
```

---

 # 33\. Lists and Strings

 A string can be converted into a list of characters.

```
text = "Python"

characters = list(text)
```

 A list of strings can be joined into a string.

```
words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)
```

 Output:

```
Python is powerful
```

---

 # 34\. Mutable vs Immutable

 Lists are **mutable**.

```
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

 Strings are **immutable**.

```
text = "Python"

# text[0] = "J"  # TypeError
```

 This is one of the most important differences between lists and strings.

---

 # 35\. Shallow Copy

 A list's `copy()` method creates a **shallow copy**.

```
original = [1, 2, 3]

copy = original.copy()
```

 For a flat list, changes to the copy do not affect the original.

 However, nested mutable objects can still be shared.

```
original = [[1, 2], [3, 4]]

copy = original.copy()

copy[0].append(100)

print(original)
```

 The nested list is shared.

 For deeply nested independent structures, use `copy.deepcopy()` when appropriate.

---

 # 36\. Common List Methods

 | Method | Purpose |
| --- | --- |
| `append()` | Add one element at the end |
| `extend()` | Add multiple elements |
| `insert()` | Insert at an index |
| `remove()` | Remove first matching value |
| `pop()` | Remove and return an element |
| `clear()` | Remove all elements |
| `index()` | Find first matching index |
| `count()` | Count occurrences |
| `sort()` | Sort in place |
| `reverse()` | Reverse in place |
| `copy()` | Create a shallow copy |

---

 # 37\. List Method Return Values

 An important Python concept:

 Many list methods modify the list **in place** and return `None`.

```
numbers = [3, 1, 2]

result = numbers.sort()

print(result)
```

 Output:

```
None
```

 The correct usage is:

```
numbers.sort()

print(numbers)
```

 This applies to methods such as:

```
append()
extend()
insert()
remove()
sort()
reverse()
clear()
```

---

 # 38\. `append()` vs `extend()`

 This distinction is extremely important.

```
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
```

 Result:

```
[1, 2, [3, 4]]
```

 Using `extend()`:

```
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
```

 Result:

```
[1, 2, 3, 4]
```

 Remember:

```
append()
    one object

extend()
    elements from an iterable
```

---

 # 39\. `remove()` vs `pop()` vs `del`

 ### `remove()`

 Remove by value:

```
numbers.remove(20)
```

 ### `pop()`

 Remove by index and return the value:

```
value = numbers.pop(1)
```

 ### `del`

 Delete by index or slice:

```
del numbers[1]
```

 Quick comparison:

 | Operation | Removes By | Returns Value |
| --- | --- | --- |
| `remove()` | Value | No |
| `pop()` | Index | Yes |
| `del` | Index/Slice | No |

---

 # 40\. Nested List Iteration

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value)
```

---

 # 41\. Practical Example — Student Marks

```
marks = [85, 92, 78, 90, 88]

total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)
```

---

 # 42\. Practical Example — Shopping Cart

```
cart = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

cart.append("Monitor")

print(cart)
```

---

 # 43\. Practical Example — Remove Completed Task

```
tasks = [
    "Learn Python",
    "Practice Lists",
    "Build Project"
]

tasks.remove("Practice Lists")

print(tasks)
```

---

 # 44\. Practical Example — Filter Even Numbers

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

 Output:

```
[2, 4, 6, 8]
```

---

 # 45\. Common Mistakes

 ## Mistake 1 — Invalid Index

```
numbers = [10, 20, 30]

# numbers[3]
```

 The highest valid index is:

```
2
```

---

 ## Mistake 2 — Confusing `append()` and `extend()`

```
numbers.append([4, 5])
```

 creates a nested list.

```
numbers.extend([4, 5])
```

 adds the elements individually.

---

 ## Mistake 3 — Assuming `sort()` Returns a List

 Incorrect:

```
numbers = [3, 1, 2]

numbers = numbers.sort()
```

 Now `numbers` becomes:

```
None
```

 Correct:

```
numbers.sort()
```

---

 ## Mistake 4 — Accidental Shared Reference

```
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

 Output:

```
[1, 2, 3, 4]
```

 Use:

```
b = a.copy()
```

 when an independent shallow copy is required.

---

 # 46\. List vs Tuple

 | Feature | List | Tuple |
| --- | --- | --- |
| Syntax | `[]` | `()` |
| Mutable | Yes | No |
| Ordered | Yes | Yes |
| Duplicates | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Dynamic modification | Yes | No |
| Typical use | Changeable collection | Fixed collection |

 Example:

```
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
```

---

 # 47\. List vs Set

 | Feature | List | Set |
| --- | --- | --- |
| Ordered | Yes | No guaranteed positional indexing |
| Mutable | Yes | Yes |
| Duplicates | Allowed | Not allowed |
| Indexing | Yes | No |
| Slicing | Yes | No |
| Membership | Yes | Yes |
| Syntax | `[]` | `{}` |

 Use a list when order and positional access matter.

 Use a set when uniqueness and fast membership testing are the main goals.

---

 # 48\. List vs Dictionary

 | Feature | List | Dictionary |
| --- | --- | --- |
| Stores | Values | Key-value pairs |
| Access | Index | Key |
| Syntax | `[]` | `{key: value}` |
| Ordered | Yes | Yes, insertion order |
| Duplicate values | Allowed | Allowed |
| Duplicate keys | N/A | Not allowed |

 Example:

```
numbers = [10, 20, 30]
```

 Dictionary:

```
student = {
    "name": "Kishor",
    "age": 25
}
```

---

 # 49\. When Should You Use a List?

 Use a list when:

 - You need an ordered collection.
- Duplicate values are acceptable.
- You need indexing.
- You need slicing.
- The collection needs to change.
- You need to iterate over values.
- You need to store multiple related items.

 Examples:

```
students = ["Amit", "Rahul", "Kishor"]
```

```
marks = [85, 90, 78, 92]
```

```
shopping_cart = ["Laptop", "Mouse", "Keyboard"]
```

---

 # 50\. Professional Best Practices

 ### Prefer meaningful variable names

 Good:

```
student_marks = [85, 90, 92]
```

 Avoid:

```
x = [85, 90, 92]
```

 when the purpose of `x` is not obvious.

 ### Use list comprehensions when they improve readability

 Good:

```
squares = [number ** 2 for number in numbers]
```

 Avoid overly complicated comprehensions.

 ### Avoid unnecessary copies

 Only create a copy when you actually need independent list state.

 ### Use `enumerate()`

 Instead of:

```
for i in range(len(items)):
    print(i, items[i])
```

 prefer:

```
for i, item in enumerate(items):
    print(i, item)
```

 ### Use `sorted()` when the original list should remain unchanged

```
sorted_numbers = sorted(numbers)
```

 Use `sort()` when modifying the existing list is intentional:

```
numbers.sort()
```

---

 # 51\. Performance Notes

 Python lists are implemented as dynamic arrays.

 Common practical complexities:

 | Operation | Typical Complexity |
| --- | --- |
| `list[index]` | O(1) |
| `list[-1]` | O(1) |
| `append()` | O(1) amortized |
| `pop()` from end | O(1) |
| `insert(0, value)` | O(n) |
| `pop(0)` | O(n) |
| Search with `in` | O(n) |
| `remove()` | O(n) |
| `index()` | O(n) |
| `count()` | O(n) |
| `sort()` | O(n log n) |

For frequent insertion/removal at both ends, `collections.deque` may be more appropriate than a list.

---

 # 52\. Important Concepts to Master

 Before completing this chapter, understand:

```
List creation
      ↓
Indexing
      ↓
Negative indexing
      ↓
Slicing
      ↓
Mutation
      ↓
Adding elements
      ↓
Removing elements
      ↓
Searching
      ↓
Iteration
      ↓
Sorting
      ↓
Copying
      ↓
List comprehension
      ↓
Nested lists
      ↓
Unpacking
      ↓
Performance
```

---

 # 53\. Quick Reference

```
# Create
numbers = [10, 20, 30]

# Access
numbers[0]

# Last element
numbers[-1]

# Length
len(numbers)

# Slice
numbers[1:3]

# Add
numbers.append(40)

# Add multiple
numbers.extend([50, 60])

# Insert
numbers.insert(1, 15)

# Remove by value
numbers.remove(20)

# Remove by index
numbers.pop(1)

# Delete
del numbers[0]

# Clear
numbers.clear()

# Search
20 in numbers

# Count
numbers.count(20)

# Find index
numbers.index(30)

# Sort
numbers.sort()

# Reverse
numbers.reverse()

# Copy
new_numbers = numbers.copy()

# Comprehension
squares = [x ** 2 for x in numbers]
```

---

 # 54\. Learning Checklist

 - [ ] Understand what a list is
- [ ] Create empty and populated lists
- [ ] Understand zero-based indexing
- [ ] Use positive indexing
- [ ] Use negative indexing
- [ ] Modify list elements
- [ ] Use list slicing
- [ ] Add elements with `append()`
- [ ] Add elements with `extend()`
- [ ] Insert elements with `insert()`
- [ ] Remove elements with `remove()`
- [ ] Remove elements with `pop()`
- [ ] Use `del`
- [ ] Clear lists with `clear()`
- [ ] Search with `in`
- [ ] Use `index()` and `count()`
- [ ] Iterate with `for`
- [ ] Use `enumerate()`
- [ ] Concatenate lists
- [ ] Repeat lists
- [ ] Sort lists
- [ ] Reverse lists
- [ ] Understand `sort()` vs `sorted()`
- [ ] Understand list copying
- [ ] Understand references
- [ ] Create list comprehensions
- [ ] Work with nested lists
- [ ] Understand list unpacking
- [ ] Use `any()` and `all()`
- [ ] Understand list performance

---

 # 55\. Summary

 A Python list is a flexible, mutable, ordered collection.

 The most important operations are:

```
numbers = [10, 20, 30]
```

```
numbers[0]
```

```
numbers[-1]
```

```
numbers[1:3]
```

```
numbers.append(40)
```

```
numbers.extend([50, 60])
```

```
numbers.remove(20)
```

```
numbers.pop()
```

```
numbers.sort()
```

```
numbers.reverse()
```

```
numbers.copy()
```

```
[x * 2 for x in numbers]
```

 Lists are fundamental to Python programming and are heavily used in:

 - Data processing
- Automation
- Web development
- APIs
- Algorithms
- Data science
- Machine learning
- File processing
- Application development

 Mastering lists provides the foundation for understanding more advanced Python data structures and algorithms.
