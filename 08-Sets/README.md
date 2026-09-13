 # 08 — Sets in Python

 > A complete guide to Python Sets — from fundamentals to practical usage, set operations, methods, comprehensions, `frozenset`, and real-world examples.

---

 ## 📌 Overview

 A **Set** in Python is a built-in collection data type used to store **unique elements**.

 Sets are especially useful when you need to:

 - Remove duplicate values
- Perform fast membership checks
- Compare collections
- Find common elements
- Find elements that exist in one collection but not another
- Perform mathematical set operations

 Python sets are **unordered**, **mutable**, and contain only **unique hashable elements**. Because sets do not maintain positional indexing, you cannot access their elements using indexes or slices.  Python documentation

---

 ## 🎯 Learning Objectives

 After completing this topic, you should understand:

 - What a Set is
- How to create Sets
- How to create an empty Set
- How Sets handle duplicate values
- How to add and remove elements
- Set membership testing
- Set operators
- Union
- Intersection
- Difference
- Symmetric Difference
- Subsets and Supersets
- Disjoint Sets
- Set comprehensions
- `frozenset`
- Common mistakes
- Practical use cases

---

 # 1\. What is a Set?

 A Set is a collection of **unique elements**.

 ### Example

```
numbers = {10, 20, 30, 40}

print(numbers)
```

 Possible output:

```
{40, 10, 20, 30}
```

 The order of elements should not be relied upon because Sets are unordered collections.

---

 # 2\. Sets Automatically Remove Duplicates

 One of the most useful properties of a Set is that duplicate elements are automatically removed.

```
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)
```

 Output:

```
{10, 20, 30}
```

 This makes Sets extremely useful for removing duplicates from data.

 ### Practical Example

```
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

unique_names = set(names)

print(unique_names)
```

 Output:

```
{'Alice', 'Bob', 'Charlie'}
```

---

 # 3\. Creating a Set

 ## Using Curly Braces

```
languages = {"Python", "Java", "C++"}

print(languages)
```

---

 ## Using `set()`

```
numbers = set([1, 2, 3, 4])

print(numbers)
```

 You can also create a Set from other iterables:

```
text = set("hello")

print(text)
```

 Possible output:

```
{'h', 'e', 'l', 'o'}
```

 Notice that the second `l` is removed.

---

 # 4\. Creating an Empty Set

 This is an important Python concept.

 ### ❌ Incorrect

```
numbers = {}
```

 `{}` creates an **empty dictionary**, not an empty Set.

 ### ✅ Correct

```
numbers = set()
```

 Check the type:

```
numbers = set()

print(type(numbers))
```

 Output:

```
<class 'set'>
```

---

 # 5\. Characteristics of Sets

 Python Sets have several important characteristics:

 | Property | Set |
| --- | --- |
| Ordered | ❌ No |
| Allows duplicates | ❌ No |
| Mutable | ✅ Yes |
| Indexing | ❌ No |
| Slicing | ❌ No |
| Supports membership testing | ✅ Yes |
| Elements must be hashable | ✅ Yes |

 Python's documentation specifies that Set elements must be hashable. Mutable objects such as lists and dictionaries cannot be Set elements.  Python documentation

---

 # 6\. Set Elements Must Be Hashable

 You can store immutable/hashable values such as:

```
numbers = {10, 20, 30}
```

```
data = {"Python", 100, 3.14, True}
```

 But you cannot directly store a list inside a Set:

```
numbers = {[1, 2, 3]}
```

 This raises:

```
TypeError: unhashable type: 'list'
```

 ### Why?

 Set membership relies on hashing. Therefore, elements need to be hashable.

---

 # 7\. Accessing Set Elements

 Sets do not support indexing.

 ### ❌ Invalid

```
numbers = {10, 20, 30}

print(numbers[0])
```

 This raises:

```
TypeError
```

 Instead, use iteration:

```
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

---

 # 8\. Membership Testing

 Sets are very useful for checking whether an element exists.

 Use:

```
in
```

 and

```
not in
```

 ### Example

```
languages = {"Python", "Java", "C++"}

print("Python" in languages)
print("Ruby" in languages)
```

 Output:

```
True
False
```

 ### Example with `not in`

```
languages = {"Python", "Java", "C++"}

print("Ruby" not in languages)
```

 Output:

```
True
```

---

 # 9\. Finding the Number of Elements

 Use `len()`:

```
languages = {"Python", "Java", "C++"}

print(len(languages))
```

 Output:

```
3
```

---

 # 10\. Adding Elements

 ## `add()`

 The `add()` method adds a single element.

```
languages = {"Python", "Java"}

languages.add("C++")

print(languages)
```

 Possible output:

```
{'Python', 'Java', 'C++'}
```

 If the element already exists, no duplicate is created.

```
languages = {"Python", "Java"}

languages.add("Python")

print(languages)
```

 The Set remains:

```
{'Python', 'Java'}
```

---

 # 11\. Adding Multiple Elements

 ## `update()`

 Use `update()` when you want to add multiple elements.

```
languages = {"Python", "Java"}

languages.update(["C", "C++", "Go"])

print(languages)
```

 Possible output:

```
{'Python', 'Java', 'C', 'C++', 'Go'}
```

 `update()` can accept another iterable.

```
numbers = {1, 2, 3}

numbers.update({4, 5})
numbers.update([6, 7])

print(numbers)
```

---

 # 12\. Removing Elements

 Python provides several methods for removing Set elements.

---

 ## `remove()`

```
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

 Output:

```
{10, 30}
```

 ### Important

 If the element does not exist, `remove()` raises a `KeyError`.

```
numbers = {10, 20, 30}

numbers.remove(50)
```

 This causes:

```
KeyError
```

---

 # 13\. `discard()`

 `discard()` also removes an element.

 The difference is that it **does not raise an error if the element does not exist**.

```
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
```

 If the element doesn't exist:

```
numbers.discard(50)
```

 No error occurs.

 ### `remove()` vs `discard()`

 | Method | Element exists | Element doesn't exist |
| --- | --- | --- |
| `remove()` | Removes it | Raises `KeyError` |
| `discard()` | Removes it | Does nothing |

---

 # 14\. `pop()`

 `pop()` removes and returns an arbitrary element from the Set.

```
numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)
```

 Because Sets are unordered, you should **not assume which element will be removed**. Python documents `pop()` as removing and returning an arbitrary element.  Python documentation

---

 # 15\. `clear()`

 `clear()` removes all elements.

```
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

 Output:

```
set()
```

---

 # 16\. Set Operations

 Set operations are one of the most important concepts in Python Sets.

 Consider:

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

 We can perform:

 - Union
- Intersection
- Difference
- Symmetric Difference

---

 # 17\. Union

 Union combines elements from both Sets.

 ### Operator

```
|
```

 ### Method

```
union()
```

 Example:

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A | B

print(result)
```

 Output:

```
{1, 2, 3, 4, 5, 6}
```

 Using the method:

```
result = A.union(B)

print(result)
```

 ### Mathematical Meaning

```
A ∪ B
```

 means all elements that exist in `A`, `B`, or both.

---

 # 18\. Intersection

 Intersection returns elements common to both Sets.

 ### Operator

```
&
```

 ### Method

```
intersection()
```

 Example:

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A & B

print(result)
```

 Output:

```
{3, 4}
```

 Using the method:

```
result = A.intersection(B)

print(result)
```

 ### Mathematical Meaning

```
A ∩ B
```

---

 # 19\. Difference

 Difference returns elements that exist in the first Set but not in the second.

 ### Operator

```
-
```

 Example:

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
```

 Output:

```
{1, 2}
```

 Reverse the operation:

```
print(B - A)
```

 Output:

```
{5, 6}
```

 ### Important

 Set difference is **directional**.

```
A - B != B - A
```

---

 # 20\. Symmetric Difference

 Symmetric difference returns elements that exist in either Set, but **not in both**.

 ### Operator

```
^
```

 Example:

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A ^ B)
```

 Output:

```
{1, 2, 5, 6}
```

 Using the method:

```
print(A.symmetric_difference(B))
```

 ### Mathematical Meaning

```
A △ B
```

---

 # 21\. Set Operations Cheat Sheet

 | Operation | Operator | Method | Meaning |
| --- | --- | --- | --- |
| Union | `A \| B` | `A.union(B)` | All unique elements |
| Intersection | `A & B` | `A.intersection(B)` | Common elements |
| Difference | `A - B` | `A.difference(B)` | Elements in A but not B |
| Symmetric Difference | `A ^ B` | `A.symmetric_difference(B)` | Elements in either, but not both |

 These operations are part of Python's built-in Set API.  Python documentation

---

 # 22\. Subset

 A Set `A` is a subset of `B` if every element of `A` exists in `B`.

 ### Method

```
issubset()
```

 ### Operator

```
<=
```

 Example:

```
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
```

 Output:

```
True
```

 Using the operator:

```
print(A <= B)
```

 Output:

```
True
```

---

 # 23\. Proper Subset

 Use `<` when the first Set must be a subset but cannot be equal to the second Set.

```
A = {1, 2}
B = {1, 2, 3}

print(A < B)
```

 Output:

```
True
```

---

 # 24\. Superset

 A Set is a superset if it contains all elements of another Set.

 ### Method

```
issuperset()
```

 ### Operator

```
>=
```

 Example:

```
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
```

 Output:

```
True
```

 Using the operator:

```
print(A >= B)
```

---

 # 25\. Proper Superset

 Use `>` when the first Set is a superset but the Sets are not equal.

```
A = {1, 2, 3}
B = {1, 2}

print(A > B)
```

 Output:

```
True
```

---

 # 26\. Disjoint Sets

 Two Sets are **disjoint** when they have no elements in common.

 Use:

```
isdisjoint()
```

 Example:

```
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))
```

 Output:

```
True
```

 If they share an element:

```
A = {1, 2, 3}
B = {3, 4, 5}

print(A.isdisjoint(B))
```

 Output:

```
False
```

---

 # 27\. Set Comprehension

 Set comprehensions provide a concise way to create Sets.

 ### Syntax

```
{expression for item in iterable}
```

 Example:

```
numbers = {1, 2, 3, 4, 5}

squares = {number ** 2 for number in numbers}

print(squares)
```

 Output:

```
{1, 4, 9, 16, 25}
```

---

 ## Set Comprehension with Condition

```
numbers = range(1, 11)

even_numbers = {number for number in numbers if number % 2 == 0}

print(even_numbers)
```

 Output:

```
{2, 4, 6, 8, 10}
```

---

 # 28\. Practical Example — Remove Duplicates

 Suppose we receive duplicate user IDs:

```
user_ids = [101, 102, 101, 103, 104, 102, 105]

unique_user_ids = set(user_ids)

print(unique_user_ids)
```

 This is one of the most common practical uses of Sets.

 If order must also be preserved, remember that converting directly to a Set does not preserve the original sequence order.

---

 # 29\. Practical Example — Common Skills

 Suppose two developers have different skills.

```
developer_a = {"Python", "Git", "SQL", "Docker"}
developer_b = {"Python", "Java", "Git", "AWS"}
```

 Find their common skills:

```
common_skills = developer_a & developer_b

print(common_skills)
```

 Output:

```
{'Python', 'Git'}
```

 Find skills unique to Developer A:

```
unique_to_a = developer_a - developer_b

print(unique_to_a)
```

 Output:

```
{'SQL', 'Docker'}
```

 Find all skills:

```
all_skills = developer_a | developer_b

print(all_skills)
```

---

 # 30\. Practical Example — Find Missing Items

```
required = {"Python", "SQL", "Git", "Docker"}

completed = {"Python", "Git"}

missing = required - completed

print(missing)
```

 Output:

```
{'SQL', 'Docker'}
```

 This pattern is useful for:

 - Required skills
- Course completion
- Permissions
- Feature support
- Configuration validation
- Checklist systems

---

 # 31\. Practical Example — Permission Checking

```
required_permissions = {"read", "write"}

user_permissions = {"read", "write", "delete"}

if required_permissions.issubset(user_permissions):
    print("Access granted")
else:
    print("Access denied")
```

 Output:

```
Access granted
```

 This is a practical example of using Sets for authorization and permission checks.

---

 # 32\. Set Methods Reference

 | Method | Purpose |
| --- | --- |
| `add()` | Add one element |
| `update()` | Add multiple elements |
| `remove()` | Remove an element; raises `KeyError` if absent |
| `discard()` | Remove an element without error if absent |
| `pop()` | Remove and return an arbitrary element |
| `clear()` | Remove all elements |
| `copy()` | Create a shallow copy |
| `union()` | Combine Sets |
| `intersection()` | Find common elements |
| `difference()` | Find elements only in the first Set |
| `symmetric_difference()` | Find elements in either Set, but not both |
| `issubset()` | Check subset relationship |
| `issuperset()` | Check superset relationship |
| `isdisjoint()` | Check whether Sets have no common elements |

 Python's official documentation provides the complete API for these operations and methods.  Python documentation

---

 # 33\. Updating Sets with Operations

 Python also provides in-place versions of several operations.

 ### Union Update

```
A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print(A)
```

 Output:

```
{1, 2, 3, 4, 5}
```

 Equivalent operator:

```
A |= B
```

---

 ### Intersection Update

```
A = {1, 2, 3, 4}
B = {3, 4, 5}

A.intersection_update(B)

print(A)
```

 Output:

```
{3, 4}
```

 Equivalent:

```
A &= B
```

---

 ### Difference Update

```
A = {1, 2, 3, 4}
B = {3, 4}

A.difference_update(B)

print(A)
```

 Output:

```
{1, 2}
```

 Equivalent:

```
A -= B
```

---

 ### Symmetric Difference Update

```
A = {1, 2, 3}
B = {3, 4, 5}

A.symmetric_difference_update(B)

print(A)
```

 Output:

```
{1, 2, 4, 5}
```

 Equivalent:

```
A ^= B
```

---

 # 34\. Copying a Set

 Use `copy()` to create a shallow copy.

```
original = {1, 2, 3}

copied = original.copy()

print(copied)
```

 You can verify that they are separate Set objects:

```
original = {1, 2, 3}
copied = original.copy()

copied.add(4)

print(original)
print(copied)
```

 Output:

```
{1, 2, 3}
{1, 2, 3, 4}
```

---

 # 35\. `frozenset`

 Python also provides an immutable version of a Set called `frozenset`.

```
numbers = frozenset([1, 2, 3, 4])

print(numbers)
```

 Unlike a normal Set, a `frozenset` cannot be modified after creation.

 Therefore, methods such as:

```
add()
remove()
discard()
clear()
```

 are not available for modifying it.

 A `frozenset` is hashable, so it can be used as a dictionary key or as an element inside another Set.  Python documentation

 ### Example

```
permissions = frozenset({"read", "write"})

roles = {
    permissions
}

print(roles)
```

---

 # 36\. Set vs List

 Understanding when to use a Set instead of a List is important.

 | Feature | List | Set |
| --- | --- | --- |
| Ordered | ✅ | ❌ |
| Duplicates | ✅ | ❌ |
| Indexing | ✅ | ❌ |
| Slicing | ✅ | ❌ |
| Membership testing | Good | Typically very efficient |
| Mathematical operations | ❌ | ✅ |
| Unique values | Manual handling | Automatic |

 ### Use a List when:

 - Order matters
- Duplicate values matter
- You need indexing
- You need slicing

 ### Use a Set when:

 - You need unique values
- Order doesn't matter
- You frequently check membership
- You need union/intersection/difference operations

---

 # 37\. Common Mistakes

 ## Mistake 1 — Using `{}` for an Empty Set

```
data = {}
```

 This creates a dictionary.

 Use:

```
data = set()
```

---

 ## Mistake 2 — Trying to Index a Set

```
numbers = {10, 20, 30}

print(numbers[0])
```

 Sets do not support indexing.

 Instead:

```
for number in numbers:
    print(number)
```

---

 ## Mistake 3 — Assuming Set Order

 Avoid writing code that depends on the printed or iteration order of a Set.

```
numbers = {10, 20, 30}

print(numbers)
```

 The displayed order should not be treated as a meaningful sequence.

---

 ## Mistake 4 — Using a Mutable Object as an Element

 This is invalid:

```
data = {[1, 2, 3]}
```

 Use an immutable alternative where appropriate:

```
data = {frozenset([1, 2, 3])}
```

---

 ## Mistake 5 — Confusing `remove()` and `discard()`

```
numbers.remove(100)
```

 can raise `KeyError`.

 Whereas:

```
numbers.discard(100)
```

 does not raise an error if `100` is absent.

---

 # 38\. Professional Coding Example

 Consider two teams working on different technologies:

```
team_backend = {
    "Python",
    "Django",
    "PostgreSQL",
    "Docker",
    "Git"
}

team_data = {
    "Python",
    "SQL",
    "PostgreSQL",
    "Pandas",
    "Git"
}

common_technologies = team_backend & team_data
backend_only = team_backend - team_data
data_only = team_data - team_backend
all_technologies = team_backend | team_data

print("Common:", common_technologies)
print("Backend only:", backend_only)
print("Data only:", data_only)
print("All technologies:", all_technologies)
```

 This demonstrates how Set operations can simplify real-world data comparison.

---

 # 39\. Interview Questions

 ### Basic

 1. What is a Set in Python?
2. Why does a Set not allow duplicate values?
3. How do you create an empty Set?
4. What is the difference between `{}` and `set()`?
5. Can Sets contain duplicate values?
6. Can Sets be indexed?
7. What types of objects can be stored in a Set?

 ### Intermediate

 8. What is the difference between `remove()` and `discard()`?
9. What is the difference between `set` and `frozenset`?
10. What is the difference between union and intersection?
11. What is symmetric difference?
12. What is a subset?
13. What is a superset?
14. What does `isdisjoint()` do?
15. How can you remove duplicates from a list?

 ### Advanced

 16. Why must Set elements be hashable?
17. Why can't a list be an element of a Set?
18. When should you use a Set instead of a List?
19. How can Sets be used for efficient membership testing?
20. What are the time-complexity characteristics of common Set operations?

---

 # 40\. Quick Revision

```
# Create
numbers = {1, 2, 3}

# Empty set
empty = set()

# Add
numbers.add(4)

# Add multiple
numbers.update([5, 6])

# Remove
numbers.remove(6)

# Safe remove
numbers.discard(10)

# Membership
print(3 in numbers)

# Length
print(len(numbers))

# Union
A | B

# Intersection
A & B

# Difference
A - B

# Symmetric Difference
A ^ B

# Subset
A <= B

# Superset
A >= B

# Disjoint
A.isdisjoint(B)

# Clear
numbers.clear()
```

---

 # 41\. Key Takeaways

 > **Think of a Set as a collection designed for uniqueness and membership.**

 The most important concepts to remember are:

 - Sets store **unique elements**.
- Sets are **unordered**.
- Sets do not support indexing or slicing.
- Set elements must be **hashable**.
- Use `set()` to create an empty Set.
- Use `add()` for one element.
- Use `update()` for multiple elements.
- Use `remove()` when absence should raise an error.
- Use `discard()` when absence should be ignored.
- Use `|` for union.
- Use `&` for intersection.
- Use `-` for difference.
- Use `^` for symmetric difference.
- Use `<=` / `issubset()` for subset checks.
- Use `>=` / `issuperset()` for superset checks.
- Use `isdisjoint()` to check whether Sets have no common elements.
- Use `frozenset` when you need an immutable, hashable Set.

---

 ## 📚 Official Documentation

 - Python Set Documentation
- Python Data Structures — Sets
- PEP 218 — Adding a Built-In Set Object Type

---

 ## 🚀 Next Step

 After mastering Sets, continue with the next Python collection/data-structure topic and focus on understanding **when to choose each data structure**, not just memorizing its syntax.

 > **Python Set = Unique Data + Fast Membership Testing + Mathematical Set Operations**
