# 🔍 DSA with Python — Searching

> **Learn how to efficiently find elements in data structures — from simple Linear Search to optimized Binary Search and advanced searching techniques.**

Searching is one of the most fundamental operations in **Data Structures and Algorithms (DSA)**.

Whenever a program needs to answer questions such as:

* Does this element exist?
* Where is this element located?
* How many times does it occur?
* What is the first or last occurrence?
* What is the smallest value greater than a target?
* What is the largest value smaller than a target?

we are performing a **searching operation**.

This chapter explains searching from **beginner to advanced level**, with Python implementations, theory, examples, complexity analysis, problem-solving patterns, and interview-focused problems.

---

# 📚 Table of Contents

* [🎯 Learning Objectives](#-learning-objectives)
* [🧠 What Is Searching?](#-what-is-searching)
* [🔎 Why Searching Matters](#-why-searching-matters)
* [📦 Types of Searching](#-types-of-searching)
* [1️⃣ Linear Search](#1️⃣-linear-search)
* [2️⃣ Linear Search with Index](#2️⃣-linear-search-with-index)
* [3️⃣ Searching Multiple Occurrences](#3️⃣-searching-multiple-occurrences)
* [4️⃣ Sentinel Linear Search](#4️⃣-sentinel-linear-search)
* [5️⃣ Binary Search](#5️⃣-binary-search)
* [6️⃣ Binary Search Using Recursion](#6️⃣-binary-search-using-recursion)
* [7️⃣ First Occurrence](#7️⃣-first-occurrence)
* [8️⃣ Last Occurrence](#8️⃣-last-occurrence)
* [9️⃣ Count Occurrences](#9️⃣-count-occurrences)
* [🔟 Lower Bound](#-lower-bound)
* [🔟 Upper Bound](#-upper-bound)
* [📌 Floor and Ceiling](#-floor-and-ceiling)
* [🔄 Search in Reverse Sorted Array](#-search-in-reverse-sorted-array)
* [🔍 Search in Rotated Sorted Array](#-search-in-rotated-sorted-array)
* [🧩 Binary Search on Answer](#-binary-search-on-answer)
* [📐 Searching in 2D Arrays](#-searching-in-2d-arrays)
* [⚡ Jump Search](#-jump-search)
* [🚀 Interpolation Search](#-interpolation-search)
* [🌳 Exponential Search](#-exponential-search)
* [🧠 Hash-Based Searching](#-hash-based-searching)
* [🐍 Python Built-in Searching](#-python-built-in-searching)
* [⏱️ Complexity Analysis](#️-complexity-analysis)
* [🧪 Practice Problems](#-practice-problems)
* [🟢 Beginner Problems](#-beginner-problems)
* [🟡 Intermediate Problems](#-intermediate-problems)
* [🔴 Advanced Problems](#-advanced-problems)
* [💼 Interview Questions](#-interview-questions)
* [⚡ Quick Revision](#-quick-revision)
* [📋 Complexity Cheat Sheet](#-complexity-cheat-sheet)
* [🧭 Problem-Solving Strategy](#-problem-solving-strategy)
* [🏗️ Recommended Folder Structure](#️-recommended-folder-structure)
* [📖 References](#-references)
* [➡️ Next Topic](#️-next-topic)

---

# 🎯 Learning Objectives

After completing this chapter, you should be able to:

* Explain what searching means.
* Implement Linear Search.
* Implement Binary Search.
* Understand the difference between iterative and recursive search.
* Find the first occurrence of an element.
* Find the last occurrence.
* Count occurrences efficiently.
* Understand lower bound and upper bound.
* Find floor and ceiling values.
* Search sorted and reverse-sorted arrays.
* Search in rotated sorted arrays.
* Apply Binary Search on Answer.
* Search in two-dimensional arrays.
* Understand Jump Search.
* Understand Interpolation Search.
* Understand Exponential Search.
* Use hashing for fast lookup.
* Analyze search algorithms using Big-O notation.
* Select an appropriate searching algorithm for a problem.

---

# 🧠 What Is Searching?

**Searching** is the process of finding a particular element, value, position, or condition inside a collection of data.

Suppose:

```python
arr = [10, 20, 30, 40, 50]
```

We want to find:

```text
30
```

A searching algorithm determines whether `30` exists and, depending on the problem, returns its location.

Conceptually:

```text
Input Data
    ↓
Searching Algorithm
    ↓
Target
    ↓
Found / Not Found
```

---

# 🔎 Why Searching Matters

Searching appears everywhere in software development.

Examples include:

### Databases

Finding a user:

```text
user_id = 105
```

### File Systems

Finding a file:

```text
report.pdf
```

### Web Applications

Searching:

```text
"Python tutorial"
```

### E-Commerce

Finding products:

```text
Laptop
```

### Algorithms

Searching is often a subproblem inside:

* Sorting
* Graph algorithms
* Dynamic programming
* Optimization
* Scheduling
* Data processing

Efficient searching can dramatically improve application performance.

---

# 📦 Types of Searching

Common searching techniques include:

```text
Searching
│
├── Linear Search
│
├── Binary Search
│
├── Jump Search
│
├── Interpolation Search
│
├── Exponential Search
│
├── Hash-Based Search
│
├── Search in Rotated Array
│
└── Binary Search on Answer
```

The most important algorithms for DSA interviews are:

```text
Linear Search
Binary Search
Binary Search Variations
Binary Search on Answer
Hash-Based Lookup
```

---

# 1️⃣ Linear Search

## 📖 Theory

**Linear Search** checks each element sequentially until:

* The target is found, or
* The entire collection has been checked.

Example:

```text
Target = 40

[10, 20, 30, 40, 50]
 ↑
 ↓
Compare 10
 ↓
Compare 20
 ↓
Compare 30
 ↓
Compare 40 → FOUND
```

Linear search does not require the array to be sorted.

---

## 💻 Implementation

```python
def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1
```

Example:

```python
arr = [10, 20, 30, 40, 50]

result = linear_search(arr, 40)

print(result)
```

Output:

```text
3
```

---

## ⏱️ Complexity

Best case:

```text
O(1)
```

Worst case:

```text
O(n)
```

Average case:

```text
O(n)
```

Space:

```text
O(1)
```

---

# 2️⃣ Linear Search with Index

Python's `enumerate()` provides both index and value.

```python
def linear_search(arr, target):

    for index, value in enumerate(arr):

        if value == target:
            return index

    return -1
```

Example:

```python
arr = [5, 8, 12, 20]

print(linear_search(arr, 12))
```

Output:

```text
2
```

---

# 3️⃣ Searching Multiple Occurrences

Sometimes we need every position where the target occurs.

Example:

```text
arr = [10, 20, 10, 30, 10]
target = 10
```

Expected:

```text
[0, 2, 4]
```

Implementation:

```python
def find_all(arr, target):

    result = []

    for i, value in enumerate(arr):

        if value == target:
            result.append(i)

    return result
```

Example:

```python
print(find_all([10, 20, 10, 30, 10], 10))
```

Output:

```text
[0, 2, 4]
```

Complexity:

```text
Time:  O(n)
Space: O(k)
```

where `k` is the number of matches returned.

---

# 4️⃣ Sentinel Linear Search

Sentinel search is a variation of linear search that places the target at the end temporarily to simplify boundary checking.

Conceptually:

```text
Normal:

[10, 20, 30, 40, 50]
                     ↑
                  boundary


Sentinel:

[10, 20, 30, 40, target]
```

The main idea is to reduce repeated boundary checks inside the loop.

In modern Python code, ordinary linear search is usually preferable for clarity unless implementing the algorithm specifically for learning.

---

# 5️⃣ Binary Search

## 📖 Theory

**Binary Search** is one of the most important searching algorithms.

It works on a **sorted** search space.

Instead of checking every element, Binary Search repeatedly divides the search range into two halves.

Example:

```text
Array:

[10, 20, 30, 40, 50, 60, 70]

Target = 60
```

Start:

```text
[10, 20, 30, 40, 50, 60, 70]
               ↑
             middle
```

Compare target with middle.

Since:

```text
60 > 40
```

ignore the left half.

Search:

```text
[50, 60, 70]
```

Then continue dividing.

---

# 🔬 Why Binary Search Is Fast

Suppose we have:

```text
n = 1,000,000
```

Linear Search may inspect close to:

```text
1,000,000
```

elements.

Binary Search repeatedly divides:

```text
1,000,000
500,000
250,000
125,000
...
```

The number of steps grows logarithmically.

Therefore:

```text
Binary Search → O(log n)
```

---

# 💻 Iterative Binary Search

```python
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

Example:

```python
arr = [10, 20, 30, 40, 50, 60]

print(binary_search(arr, 50))
```

Output:

```text
4
```

---

# 🧠 Binary Search Invariant

At every step:

```text
target, if present, must exist within:

[left, right]
```

The algorithm continuously reduces this search space.

```text
Search Space
┌─────────────────────────────┐
│                             │
└─────────────────────────────┘
              ↓
       Divide in half
              ↓
     ┌────────┐   ┌────────┐
     │ Ignore │   │ Search │
     └────────┘   └────────┘
```

Understanding this invariant is more important than memorizing the code.

---

# ⏱️ Binary Search Complexity

| Case    |     Complexity |
| ------- | -------------: |
| Best    |           O(1) |
| Average |       O(log n) |
| Worst   |       O(log n) |
| Space   | O(1) iterative |

---

# 6️⃣ Binary Search Using Recursion

Binary Search can also be implemented recursively.

```python
def binary_search_recursive(arr, left, right, target):

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search_recursive(
            arr,
            mid + 1,
            right,
            target
        )

    return binary_search_recursive(
        arr,
        left,
        mid - 1,
        target
    )
```

Usage:

```python
arr = [10, 20, 30, 40, 50]

result = binary_search_recursive(
    arr,
    0,
    len(arr) - 1,
    40
)

print(result)
```

Output:

```text
3
```

### Complexity

```text
Time:  O(log n)
Space: O(log n)
```

The additional space comes from recursive call stack frames.

---

# 7️⃣ First Occurrence

Suppose:

```text
arr = [1, 2, 2, 2, 3, 4]
```

Target:

```text
2
```

We want:

```text
Index = 1
```

not index `2` or `3`.

Implementation:

```python
def first_occurrence(arr, target):

    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            answer = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer
```

The key idea is:

> When the target is found, continue searching toward the left.

---

# 8️⃣ Last Occurrence

For:

```text
[1, 2, 2, 2, 3, 4]
```

target:

```text
2
```

we want:

```text
Index = 3
```

Implementation:

```python
def last_occurrence(arr, target):

    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            answer = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer
```

The key idea is:

> When the target is found, continue searching toward the right.

---

# 9️⃣ Count Occurrences

For a sorted array:

```text
[1, 2, 2, 2, 3, 4]
```

we can calculate:

```text
count = last_index - first_index + 1
```

Example:

```python
def count_occurrences(arr, target):

    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)

    return last - first + 1
```

Complexity:

```text
O(log n)
```

---

# 🔟 Lower Bound

The **lower bound** is the first position where:

```text
arr[index] >= target
```

Example:

```text
arr = [1, 2, 4, 4, 5, 7]
target = 4
```

Lower bound:

```text
Index = 2
```

Implementation:

```python
def lower_bound(arr, target):

    left = 0
    right = len(arr)

    while left < right:

        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# 🔟 Upper Bound

The **upper bound** is the first position where:

```text
arr[index] > target
```

Example:

```text
arr = [1, 2, 4, 4, 5, 7]
target = 4
```

Upper bound:

```text
Index = 4
```

Implementation:

```python
def upper_bound(arr, target):

    left = 0
    right = len(arr)

    while left < right:

        mid = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# 📌 Floor and Ceiling

For a sorted array:

```text
[1, 3, 5, 7, 9]
```

For target:

```text
6
```

### Floor

Largest value:

```text
<= 6
```

Answer:

```text
5
```

### Ceiling

Smallest value:

```text
>= 6
```

Answer:

```text
7
```

These problems can often be solved using modified Binary Search.

---

# 🔄 Search in Reverse Sorted Array

Binary Search does not require ascending order specifically.

It can also work with:

```text
[90, 80, 70, 60, 50, 40]
```

The comparison logic must be reversed.

```python
def binary_search_descending(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

---

# 🔍 Search in Rotated Sorted Array

Consider:

```text
[4, 5, 6, 7, 0, 1, 2]
```

This was originally sorted but rotated.

Standard Binary Search cannot be applied directly without modification.

At each step, determine which half is sorted.

```text
[4, 5, 6, 7, 0, 1, 2]
 ↑        ↑        ↑
left     mid      right
```

One side of the array is guaranteed to be sorted.

Then determine whether the target lies inside that sorted region.

Typical complexity:

```text
Time:  O(log n)
Space: O(1)
```

---

# 🧩 Binary Search on Answer

One of the most important advanced patterns is **Binary Search on Answer**.

Instead of searching for an element, we search for the optimal answer.

The problem often looks like:

```text
Find the minimum possible value
```

or:

```text
Find the maximum possible value
```

provided we can define a monotonic condition.

Conceptually:

```text
Possible answers:

1  2  3  4  5  6  7  8
N  N  N  N  Y  Y  Y  Y
            ↑
          answer
```

Once the condition changes from `False` to `True`, it stays `True`.

Binary Search can locate that boundary.

---

## Example — Minimum Capacity

Suppose packages must be shipped within a fixed number of days.

We can ask:

```text
Can capacity X ship everything within D days?
```

If:

```text
capacity = 10 → No
capacity = 20 → No
capacity = 30 → Yes
capacity = 40 → Yes
```

then the feasibility function is monotonic.

Therefore, Binary Search can find the minimum feasible capacity.

---

# 📐 Searching in 2D Arrays

Consider:

```text
matrix = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]
```

A simple search:

```python
def search_matrix(matrix, target):

    for row in matrix:

        for value in row:

            if value == target:
                return True

    return False
```

Complexity:

```text
O(rows × columns)
```

For specially sorted matrices, more efficient approaches are possible.

---

# ⚡ Jump Search

Jump Search works on a sorted array.

Instead of checking every element, it jumps ahead by a block size.

Typically:

```text
√n
```

Example:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
 ↑        ↑        ↑
 jump     jump     jump
```

Once the correct block is found, perform Linear Search inside it.

Typical complexity:

```text
Time: O(√n)
Space: O(1)
```

It is mainly useful for understanding searching strategies; Binary Search is usually more important in practice for random-access sorted arrays.

---

# 🚀 Interpolation Search

Interpolation Search estimates where the target might be instead of always choosing the middle.

It works particularly well when values are **uniformly distributed**.

Conceptually:

```text
Binary Search:
Always choose middle.

Interpolation Search:
Estimate likely position.
```

Typical best-case behavior can be very fast on suitable distributions, while the worst case can degrade to:

```text
O(n)
```

Therefore, it should not be used blindly.

---

# 🌳 Exponential Search

Exponential Search is useful when the search range is unknown or potentially very large.

It first expands the range exponentially:

```text
1
2
4
8
16
32
...
```

Once a range containing the target is identified, Binary Search is applied.

Typical complexity:

```text
O(log n)
```

for appropriate sorted, random-access search spaces.

---

# 🧠 Hash-Based Searching

Hash-based lookup can provide average-case constant-time membership checks.

Python's:

```python
set
dict
```

are commonly used for this purpose.

Example:

```python
numbers = {10, 20, 30, 40}

print(30 in numbers)
```

Output:

```text
True
```

A dictionary:

```python
users = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

print(users.get(102))
```

Output:

```text
Bob
```

### Important

Hash-based searching is fundamentally different from Binary Search.

| Technique     | Requirement   | Typical Lookup |
| ------------- | ------------- | -------------: |
| Linear Search | None          |           O(n) |
| Binary Search | Sorted data   |       O(log n) |
| Hashing       | Hashable keys |   O(1) average |

---

# 🐍 Python Built-in Searching

Python provides convenient built-in operations.

## Membership

```python
arr = [10, 20, 30]

print(20 in arr)
```

For lists, membership is generally:

```text
O(n)
```

---

## `index()`

```python
arr = [10, 20, 30]

print(arr.index(20))
```

Output:

```text
1
```

If the value does not exist, `ValueError` is raised.

---

## `count()`

```python
arr = [1, 2, 2, 3]

print(arr.count(2))
```

Output:

```text
2
```

This is generally O(n).

---

## Binary Search with `bisect`

Python's `bisect` module provides tools for working with sorted lists.

```python
import bisect

arr = [10, 20, 30, 40, 50]

position = bisect.bisect_left(arr, 30)

print(position)
```

Output:

```text
2
```

`bisect_left()` is closely related to the lower-bound concept.

---

# ⏱️ Complexity Analysis

Understanding complexity allows us to compare algorithms.

Suppose:

```text
n = 1,000,000
```

Linear Search:

```text
O(n)
```

Binary Search:

```text
O(log n)
```

The difference becomes significant as `n` grows.

---

# 📊 Searching Algorithm Comparison

| Algorithm               | Sorted Required |      Best |                 Average |           Worst |    Space |
| ----------------------- | --------------- | --------: | ----------------------: | --------------: | -------: |
| Linear Search           | ❌               |      O(1) |                    O(n) |            O(n) |     O(1) |
| Binary Search           | ✅               |      O(1) |                O(log n) |        O(log n) |     O(1) |
| Recursive Binary Search | ✅               |      O(1) |                O(log n) |        O(log n) | O(log n) |
| Jump Search             | ✅               |      O(1) |                   O(√n) |           O(√n) |     O(1) |
| Interpolation Search    | ✅               |      O(1) | Depends on distribution |            O(n) |     O(1) |
| Exponential Search      | ✅               |      O(1) |                O(log n) |        O(log n) |     O(1) |
| Hash Lookup             | ❌               | O(1) avg. |               O(1) avg. | O(n) worst-case |     O(n) |

Complexities are asymptotic and depend on the data structure and assumptions.

---

# 🧪 Practice Problems

## 🟢 Beginner Problems

### 1. Linear Search

Find the index of a target.

```text
Input:
[5, 8, 2, 9, 1]
Target: 9

Output:
3
```

---

### 2. Search for Maximum

Find the largest value.

---

### 3. Search for Minimum

Find the smallest value.

---

### 4. Count Target

Count how many times a value occurs.

---

### 5. Find All Occurrences

Return all indexes containing the target.

---

### 6. Search in String

Find the first occurrence of a character.

---

### 7. Check Existence

Determine whether a target exists.

---

# 🟡 Intermediate Problems

### 1. Binary Search

Implement iterative Binary Search.

---

### 2. Recursive Binary Search

Implement Binary Search recursively.

---

### 3. First Occurrence

Find the first position of a target in a sorted array.

---

### 4. Last Occurrence

Find the last position of a target.

---

### 5. Count Occurrences

Use first and last occurrence.

---

### 6. Search Insert Position

Find where a target should be inserted.

---

### 7. Floor of a Number

Find the greatest value less than or equal to target.

---

### 8. Ceiling of a Number

Find the smallest value greater than or equal to target.

---

### 9. Square Root

Find the integer square root using Binary Search.

---

### 10. Peak Element

Find a peak element efficiently.

---

# 🔴 Advanced Problems

### 1. Search in Rotated Sorted Array

```text
[4, 5, 6, 7, 0, 1, 2]
```

Find a target efficiently.

---

### 2. Search in Rotated Array with Duplicates

Handle repeated values.

---

### 3. Find Minimum in Rotated Sorted Array

Return the minimum element efficiently.

---

### 4. Find Rotation Count

Determine how many times a sorted array was rotated.

---

### 5. Single Element in Sorted Array

Find the unique element when all other elements occur twice.

---

### 6. Median of Two Sorted Arrays

Find the median of two sorted arrays efficiently.

---

### 7. Kth Missing Positive Number

Find the kth missing positive number.

---

### 8. Aggressive Cows

Maximize the minimum distance between placed objects.

---

### 9. Allocate Books

Minimize the maximum pages assigned to a student.

---

### 10. Split Array Largest Sum

Minimize the largest subarray sum.

---

# 💼 Interview Questions

## Fundamentals

1. What is searching?
2. What is Linear Search?
3. What is the time complexity of Linear Search?
4. Does Linear Search require sorted data?
5. What is Binary Search?
6. Why does Binary Search require sorted data?
7. What is the time complexity of Binary Search?
8. What is the difference between iterative and recursive Binary Search?
9. What is the difference between searching a list and a set in Python?
10. What is a hash-based lookup?

## Intermediate

11. How does Binary Search work?
12. What is the Binary Search invariant?
13. How do you find the first occurrence?
14. How do you find the last occurrence?
15. How do you count duplicate values in a sorted array?
16. What is lower bound?
17. What is upper bound?
18. What is the difference between lower bound and upper bound?
19. How do you find floor and ceiling?
20. How do you search a descending sorted array?

## Advanced

21. How do you search a rotated sorted array?
22. Why does Binary Search still work on a rotated sorted array?
23. What is Binary Search on Answer?
24. What is a monotonic predicate?
25. How can Binary Search solve optimization problems?
26. What is Jump Search?
27. What is Interpolation Search?
28. When is Interpolation Search useful?
29. What is Exponential Search?
30. How does hashing compare with Binary Search?
31. How would you find a peak element?
32. How would you find the minimum element in a rotated array?
33. How would you find the kth missing positive number?
34. How can Binary Search be applied to a mathematical answer rather than an array index?
35. How do you avoid infinite loops in Binary Search?

---

# ⚡ Quick Revision

```text
SEARCHING
│
├── Linear Search
│   ├── Works on unsorted data
│   └── O(n)
│
├── Binary Search
│   ├── Sorted data
│   └── O(log n)
│
├── Binary Search Variations
│   ├── First occurrence
│   ├── Last occurrence
│   ├── Lower bound
│   ├── Upper bound
│   ├── Floor
│   └── Ceiling
│
├── Advanced Binary Search
│   ├── Rotated array
│   ├── Peak element
│   └── Binary Search on Answer
│
├── Jump Search
│   └── O(√n)
│
├── Interpolation Search
│   └── Distribution-dependent
│
├── Exponential Search
│   └── O(log n)
│
└── Hash Lookup
    └── O(1) average
```

---

# 📋 Complexity Cheat Sheet

| Technique             |                   Time | Main Requirement              |
| --------------------- | ---------------------: | ----------------------------- |
| Linear Search         |                   O(n) | No sorting required           |
| Binary Search         |               O(log n) | Sorted search space           |
| First Occurrence      |               O(log n) | Sorted array                  |
| Last Occurrence       |               O(log n) | Sorted array                  |
| Lower Bound           |               O(log n) | Sorted array                  |
| Upper Bound           |               O(log n) | Sorted array                  |
| Rotated Binary Search |       O(log n) typical | Rotated sorted array          |
| Jump Search           |                  O(√n) | Sorted array                  |
| Interpolation Search  | Distribution dependent | Sorted, suitable distribution |
| Exponential Search    |               O(log n) | Sorted search space           |
| Set Lookup            |           O(1) average | Hashable values               |
| Dictionary Lookup     |           O(1) average | Hashable keys                 |

---

# 🧭 Problem-Solving Strategy

When you see a searching problem, ask these questions.

## Step 1 — Is the data sorted?

If **No**:

```text
Linear Search
Hashing
```

may be appropriate.

If **Yes**:

```text
Binary Search
Two Pointers
```

may be possible.

---

## Step 2 — Is the answer an index?

If yes, think about:

```text
Binary Search
Lower Bound
Upper Bound
```

---

## Step 3 — Are duplicates present?

Think:

```text
First Occurrence
Last Occurrence
Lower Bound
Upper Bound
```

---

## Step 4 — Is the array rotated?

Think:

```text
Modified Binary Search
```

---

## Step 5 — Is the problem asking for minimum/maximum?

For example:

```text
minimum capacity
minimum speed
maximum distance
minimum time
```

Ask:

> **Can I check whether a candidate answer is feasible?**

If yes, investigate:

```text
Binary Search on Answer
```

---

## Step 6 — Can I use hashing?

If the problem requires repeated membership or frequency checks:

```text
set
dict
Counter
```

may reduce repeated searching.

---

# 🧠 The Most Important Binary Search Pattern

A powerful general template is:

```python
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

Memorize the **idea**, not just the code:

```text
1. Define search space
2. Find middle
3. Check condition
4. Eliminate half
5. Repeat
```

---

# ⚠️ Common Binary Search Mistakes

## Mistake 1 — Using Binary Search on unsorted data

Incorrect:

```text
Unsorted array
     ↓
Binary Search
```

Binary Search relies on an ordering property.

---

## Mistake 2 — Incorrect boundary updates

Incorrect logic can cause:

```text
Infinite Loop
```

Be consistent about whether your interval is:

```text
[left, right]
```

or:

```text
[left, right)
```

---

## Mistake 3 — Forgetting duplicate handling

Finding any occurrence is different from finding:

```text
first occurrence
last occurrence
```

---

## Mistake 4 — Returning too early

For first/last occurrence problems, finding the target is not necessarily the end.

You may need to continue searching.

---

## Mistake 5 — Ignoring the search space

Binary Search is not limited to array indexes.

It can search:

```text
numbers
positions
speeds
capacities
times
distances
answers
```

---

# 🏗️ Recommended Folder Structure

```text
22-DSA-with-Python/
│
├── 01-Arrays/
│   └── README.md
│
├── 02-Searching/
│   ├── README.md
│   │
│   ├── 01-linear-search.py
│   ├── 02-linear-search-all.py
│   ├── 03-sentinel-search.py
│   ├── 04-binary-search.py
│   ├── 05-recursive-binary-search.py
│   ├── 06-first-occurrence.py
│   ├── 07-last-occurrence.py
│   ├── 08-count-occurrences.py
│   ├── 09-lower-bound.py
│   ├── 10-upper-bound.py
│   ├── 11-floor-ceiling.py
│   ├── 12-descending-binary-search.py
│   ├── 13-rotated-array-search.py
│   ├── 14-peak-element.py
│   ├── 15-binary-search-answer.py
│   ├── 16-jump-search.py
│   ├── 17-interpolation-search.py
│   └── 18-exponential-search.py
│
├── 03-Strings/
├── 04-Linked-Lists/
├── 05-Stacks/
├── 06-Queues/
└── ...
```

---

# 🏆 Mastery Checklist

Before moving to the next DSA topic, make sure you can:

* [ ] Explain searching.
* [ ] Implement Linear Search.
* [ ] Find all occurrences.
* [ ] Explain Binary Search.
* [ ] Implement iterative Binary Search.
* [ ] Implement recursive Binary Search.
* [ ] Explain Binary Search invariants.
* [ ] Find first occurrence.
* [ ] Find last occurrence.
* [ ] Count occurrences.
* [ ] Implement lower bound.
* [ ] Implement upper bound.
* [ ] Find floor and ceiling.
* [ ] Search descending arrays.
* [ ] Search rotated sorted arrays.
* [ ] Find peak elements.
* [ ] Understand Binary Search on Answer.
* [ ] Explain monotonic predicates.
* [ ] Understand Jump Search.
* [ ] Understand Interpolation Search.
* [ ] Understand Exponential Search.
* [ ] Use `set` and `dict` for fast average-case lookup.
* [ ] Analyze time and space complexity.
* [ ] Recognize Binary Search patterns in interview problems.

---

# 📖 References

* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)
* [Python Built-in Types — Lists](https://docs.python.org/3/library/stdtypes.html?utm_source=chatgpt.com#lists)
* [Python `bisect` Module](https://docs.python.org/3/library/bisect.html?utm_source=chatgpt.com)
* [Python `collections` Module](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com)

---

# 🎯 Final Takeaways

Searching is more than simply finding an element.

The real DSA skill is recognizing the **structure of the search problem**.

```text
Unsorted Data
     ↓
Linear Search / Hashing

Sorted Data
     ↓
Binary Search

Duplicates
     ↓
First / Last / Bounds

Rotated Sorted Data
     ↓
Modified Binary Search

Minimum / Maximum Answer
     ↓
Binary Search on Answer
```

The most important progression is:

```text
Linear Search
      ↓
Binary Search
      ↓
First / Last Occurrence
      ↓
Lower / Upper Bound
      ↓
Rotated Array
      ↓
Binary Search on Answer
```

> **The key to Binary Search is not “find the middle.” The key is “eliminate half of the search space while maintaining a correct invariant.”**

---

# ➡️ Next Topic

### `03-Strings`

After Searching, continue with **Strings**, covering:

* String traversal
* Character arrays
* String manipulation
* Palindromes
* Anagrams
* Frequency counting
* Two pointers
* Sliding window
* String searching
* Pattern matching
* Advanced string problems

---

## ⭐ Keep Practicing

```text
Understand
    ↓
Implement
    ↓
Dry Run
    ↓
Analyze Complexity
    ↓
Optimize
    ↓
Solve Variations
```

> **Don't memorize the algorithm. Understand the search space.** 🔍🐍

**Happy Coding & Keep Solving! 🚀**

