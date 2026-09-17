# 🔢 Sorting Algorithms in Python

> **Data Structures & Algorithms — Sorting**

Sorting is one of the most fundamental concepts in **Data Structures and Algorithms (DSA)**. It is the process of arranging data in a specific order, usually **ascending** or **descending**.

A strong understanding of sorting algorithms helps build the foundation for:

* Searching algorithms
* Divide and conquer
* Greedy algorithms
* Dynamic programming
* Graph algorithms
* Database indexing
* Data processing systems
* Competitive programming
* Technical interviews

This section covers sorting algorithms from **basic implementations to advanced, optimized techniques**, with Python examples, complexity analysis, and problem-solving patterns.

---

## 📚 Table of Contents

* [What is Sorting?](#-what-is-sorting)
* [Why is Sorting Important?](#-why-is-sorting-important)
* [Types of Sorting](#-types-of-sorting)
* [Sorting Terminology](#-sorting-terminology)
* [1. Bubble Sort](#-1-bubble-sort)
* [2. Selection Sort](#-2-selection-sort)
* [3. Insertion Sort](#-3-insertion-sort)
* [4. Merge Sort](#-4-merge-sort)
* [5. Quick Sort](#-5-quick-sort)
* [6. Heap Sort](#-6-heap-sort)
* [7. Counting Sort](#-7-counting-sort)
* [8. Radix Sort](#-8-radix-sort)
* [9. Bucket Sort](#-9-bucket-sort)
* [Python Built-in Sorting](#-python-built-in-sorting)
* [Key Comparison](#-sorting-algorithm-comparison)
* [Stable vs Unstable Sorting](#-stable-vs-unstable-sorting)
* [In-place vs Out-of-place](#-in-place-vs-out-of-place)
* [Adaptive Sorting](#-adaptive-sorting)
* [Divide and Conquer](#-divide-and-conquer)
* [Sorting Custom Objects](#-sorting-custom-objects)
* [Common Mistakes](#-common-mistakes)
* [Practice Problems](#-practice-problems)
* [Interview Questions](#-interview-questions)
* [Quick Revision](#-quick-revision)
* [Mastery Checklist](#-mastery-checklist)
* [References](#-references)
* [Next Topic](#-next-topic)

---

# 📌 What is Sorting?

**Sorting** is the process of rearranging elements according to a particular ordering criterion.

### Example

Unsorted:

```text
[7, 2, 9, 1, 5]
```

Ascending order:

```text
[1, 2, 5, 7, 9]
```

Descending order:

```text
[9, 7, 5, 2, 1]
```

Sorting can be performed on:

* Numbers
* Strings
* Characters
* Objects
* Records
* Tuples
* Dictionaries
* Custom data structures

---

# 🎯 Why is Sorting Important?

Sorting is useful because organized data can make other operations more efficient.

For example:

```text
Unsorted Data
     ↓
Sorting
     ↓
Organized Data
     ↓
Efficient Searching / Processing
```

### Common applications

* Database systems
* Search engines
* File systems
* E-commerce product ordering
* Ranking systems
* Scheduling
* Data analysis
* Duplicate detection
* Finding median
* Interval processing
* Computational geometry

For example, **Binary Search requires sorted data**.

---

# 🧠 Types of Sorting

Sorting algorithms can be categorized in several ways.

### Based on technique

```text
Comparison-Based
├── Bubble Sort
├── Selection Sort
├── Insertion Sort
├── Merge Sort
├── Quick Sort
└── Heap Sort

Non-Comparison-Based
├── Counting Sort
├── Radix Sort
└── Bucket Sort
```

### Comparison-based sorting

Algorithms compare elements:

```python
if arr[i] > arr[j]:
    ...
```

Examples:

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Heap Sort

### Non-comparison sorting

Algorithms use properties of the values rather than directly comparing every pair.

Examples:

* Counting Sort
* Radix Sort
* Bucket Sort

---

# 📖 Sorting Terminology

## 1. Ascending Order

Smallest → Largest

```text
1 2 3 4 5
```

## 2. Descending Order

Largest → Smallest

```text
5 4 3 2 1
```

## 3. Stable Sort

A stable sorting algorithm preserves the relative order of equal elements.

Example:

```text
(A, 80)
(B, 70)
(C, 80)
```

After sorting by marks:

```text
(B, 70)
(A, 80)
(C, 80)
```

`A` remains before `C`.

---

# 🫧 1. Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

### Example

```text
[5, 3, 8, 4, 2]
```

Compare:

```text
5 > 3 → swap
```

Result:

```text
[3, 5, 8, 4, 2]
```

Continue until the largest element moves toward the end.

### Implementation

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


numbers = [5, 3, 8, 4, 2]

print(bubble_sort(numbers))
```

Output:

```text
[2, 3, 4, 5, 8]
```

### Complexity

| Case    |  Time |
| ------- | ----: |
| Best    |  O(n) |
| Average | O(n²) |
| Worst   | O(n²) |

Space:

```text
O(1)
```

### Important

Bubble Sort is useful for learning algorithmic concepts but is generally inefficient for large datasets.

---

# 🎯 2. Selection Sort

Selection Sort repeatedly finds the smallest element from the unsorted portion and places it at the correct position.

### Example

```text
[64, 25, 12, 22, 11]
```

Find minimum:

```text
11
```

Swap with first element:

```text
[11, 25, 12, 22, 64]
```

Then repeat for the remaining elements.

### Implementation

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


numbers = [64, 25, 12, 22, 11]

print(selection_sort(numbers))
```

Output:

```text
[11, 12, 22, 25, 64]
```

### Complexity

```text
Best:    O(n²)
Average: O(n²)
Worst:   O(n²)

Space: O(1)
```

Selection Sort performs relatively few swaps, but still requires quadratic comparisons.

---

# 📝 3. Insertion Sort

Insertion Sort builds the sorted array one element at a time.

It works similarly to arranging playing cards in your hand.

### Example

```text
[5, 2, 4, 6, 1, 3]
```

Start:

```text
[5]
```

Insert `2`:

```text
[2, 5]
```

Insert `4`:

```text
[2, 4, 5]
```

Continue until the complete array is sorted.

### Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


numbers = [5, 2, 4, 6, 1, 3]

print(insertion_sort(numbers))
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

### Complexity

| Case    |  Time |
| ------- | ----: |
| Best    |  O(n) |
| Average | O(n²) |
| Worst   | O(n²) |

Space:

```text
O(1)
```

### Advantage

Insertion Sort performs well when the input is:

* Small
* Nearly sorted
* Frequently updated

---

# 🔀 4. Merge Sort

Merge Sort is a **divide-and-conquer** sorting algorithm.

It follows:

```text
Divide
   ↓
Solve
   ↓
Merge
```

### Example

```text
[8, 3, 5, 4, 7, 6, 1, 2]
```

Divide:

```text
[8, 3, 5, 4]   [7, 6, 1, 2]
```

Divide again:

```text
[8, 3] [5, 4] [7, 6] [1, 2]
```

Continue until single elements remain.

Then merge sorted pieces.

### Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [8, 3, 5, 4, 7, 6, 1, 2]

print(merge_sort(numbers))
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8]
```

### Complexity

```text
Best:    O(n log n)
Average: O(n log n)
Worst:   O(n log n)

Space: O(n)
```

### Key idea

Merge Sort guarantees:

```text
O(n log n)
```

time complexity regardless of the initial ordering.

---

# ⚡ 5. Quick Sort

Quick Sort is another **divide-and-conquer** algorithm.

It selects a **pivot** and partitions the array around it.

Example:

```text
[8, 3, 7, 4, 9, 2]
```

Choose:

```text
pivot = 4
```

Partition:

```text
Smaller       Pivot       Larger
[3, 2]         4          [8, 7, 9]
```

Then recursively sort the two partitions.

### Implementation

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


numbers = [8, 3, 7, 4, 9, 2]

print(quick_sort(numbers))
```

Output:

```text
[2, 3, 4, 7, 8, 9]
```

### Complexity

| Case    |       Time |
| ------- | ---------: |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   |      O(n²) |

The worst case can occur when partitioning is highly unbalanced.

### Important

In production Python code, prefer Python's built-in sorting rather than implementing Quick Sort manually unless the goal is learning or a specific algorithmic requirement.

---

# 🏗️ 6. Heap Sort

Heap Sort uses a **binary heap** data structure.

A max heap has the property:

```text
Parent >= Children
```

For example:

```text
        90
       /  \
     70    80
    /  \
   40   50
```

The largest element can be repeatedly extracted.

### Implementation

```python
def heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


numbers = [12, 11, 13, 5, 6, 7]

print(heap_sort(numbers))
```

Output:

```text
[5, 6, 7, 11, 12, 13]
```

### Complexity

```text
Best:    O(n log n)
Average: O(n log n)
Worst:   O(n log n)

Space: O(1)
```

Heap Sort provides predictable `O(n log n)` time but is generally less convenient than Python's built-in sorting.

---

# 🔢 7. Counting Sort

Counting Sort is a **non-comparison-based** sorting algorithm.

It counts how many times each value occurs.

Example:

```text
[4, 2, 2, 8, 3, 3, 1]
```

Frequency table:

```text
1 → 1
2 → 2
3 → 2
4 → 1
8 → 1
```

Then reconstruct the sorted array.

### Implementation

```python
def counting_sort(arr):
    if not arr:
        return arr

    maximum = max(arr)
    minimum = min(arr)

    count = [0] * (maximum - minimum + 1)

    for value in arr:
        count[value - minimum] += 1

    index = 0

    for value, frequency in enumerate(count):
        for _ in range(frequency):
            arr[index] = value + minimum
            index += 1

    return arr


numbers = [4, 2, 2, 8, 3, 3, 1]

print(counting_sort(numbers))
```

Output:

```text
[1, 2, 2, 3, 3, 4, 8]
```

### Complexity

If:

```text
n = number of elements
k = range of values
```

Then approximately:

```text
Time: O(n + k)
Space: O(k)
```

Counting Sort is useful when the value range is reasonably small.

---

# 🔢 8. Radix Sort

Radix Sort sorts numbers digit by digit.

For decimal numbers, processing commonly starts from the:

```text
Ones
 ↓
Tens
 ↓
Hundreds
 ↓
...
```

Example:

```text
170
045
075
090
802
024
002
066
```

Each digit position is processed using a stable sorting technique such as Counting Sort.

### High-level implementation

```python
def counting_sort_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for number in arr:
        digit = (number // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    maximum = max(arr)
    exp = 1

    while maximum // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


numbers = [170, 45, 75, 90, 802, 24, 2, 66]

print(radix_sort(numbers))
```

Output:

```text
[2, 24, 45, 66, 75, 90, 170, 802]
```

### Complexity

For:

```text
d = number of digits
n = number of elements
k = number of possible digit values
```

Time:

```text
O(d(n + k))
```

For decimal numbers:

```text
k = 10
```

---

# 🪣 9. Bucket Sort

Bucket Sort distributes elements into multiple buckets.

Example:

```text
Input
 ↓
Bucket 1
Bucket 2
Bucket 3
Bucket 4
 ↓
Sort each bucket
 ↓
Combine
```

It can work particularly well when values are distributed relatively uniformly across a known range.

### Example

```python
def bucket_sort(arr):
    if not arr:
        return arr

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for value in arr:
        index = min(int(value * bucket_count), bucket_count - 1)
        buckets[index].append(value)

    for bucket in buckets:
        bucket.sort()

    result = []

    for bucket in buckets:
        result.extend(bucket)

    return result


numbers = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47]

print(bucket_sort(numbers))
```

Output:

```text
[0.23, 0.25, 0.32, 0.42, 0.47, 0.52]
```

---

# 🐍 Python Built-in Sorting

In real Python applications, the preferred approach is usually:

```python
sorted()
```

or:

```python
list.sort()
```

## `sorted()`

Returns a new sorted list.

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers)

print(result)
print(numbers)
```

Output:

```text
[1, 2, 5, 8]
[5, 2, 8, 1]
```

The original list is unchanged.

---

## `list.sort()`

Sorts the list in place.

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 5, 8]
```

---

# 🔽 Descending Order

```python
numbers = [5, 2, 8, 1]

print(sorted(numbers, reverse=True))
```

Output:

```text
[8, 5, 2, 1]
```

---

# 🔑 Sorting with `key`

The `key` parameter defines what should be used for comparison.

```python
names = ["Kishor", "Alex", "Christopher", "Bob"]

result = sorted(names, key=len)

print(result)
```

Output:

```text
["Bob", "Alex", "Kishor", "Christopher"]
```

---

# 🧩 Sorting Custom Objects

Consider:

```python
students = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 72},
    {"name": "C", "marks": 91},
]
```

Sort by marks:

```python
students.sort(key=lambda student: student["marks"])

print(students)
```

Descending:

```python
students.sort(
    key=lambda student: student["marks"],
    reverse=True
)
```

This pattern is extremely useful in real-world Python applications.

---

# ⚖️ Sorting Algorithm Comparison

| Algorithm      |       Best |    Average |      Worst |      Space | Stable     |
| -------------- | ---------: | ---------: | ---------: | ---------: | ---------- |
| Bubble Sort    |       O(n) |      O(n²) |      O(n²) |       O(1) | Yes        |
| Selection Sort |      O(n²) |      O(n²) |      O(n²) |       O(1) | No*        |
| Insertion Sort |       O(n) |      O(n²) |      O(n²) |       O(1) | Yes        |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) |       O(n) | Yes        |
| Quick Sort     | O(n log n) | O(n log n) |      O(n²) | O(log n)** | Usually No |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) |       O(1) | No         |
| Counting Sort  |     O(n+k) |     O(n+k) |     O(n+k) |       O(k) | Can be     |
| Radix Sort     |  O(d(n+k)) |  O(d(n+k)) |  O(d(n+k)) |     O(n+k) | Can be     |
| Bucket Sort    |  O(n+k)*** |  O(n+k)*** |      O(n²) |     O(n+k) | Depends    |

> `*` Stability depends on implementation.
> `**` Recursive stack for a balanced implementation; implementation details can change space usage.
> `***` Depends heavily on the input distribution.

---

# 🔄 Stable vs Unstable Sorting

Suppose we have:

```text
Alice   90
Bob     80
Charlie 90
David   80
```

Sort by marks.

A stable algorithm preserves the original order among equal values:

```text
Bob     80
David   80
Alice   90
Charlie 90
```

This matters when sorting data using multiple criteria.

### Python

Python's built-in sorting is **stable**.

This allows multi-stage sorting techniques.

Example:

```python
students = [
    ("Alice", 90),
    ("Bob", 80),
    ("Charlie", 90),
    ("David", 80)
]

students.sort(key=lambda x: x[1])

print(students)
```

---

# 💾 In-place vs Out-of-place Sorting

## In-place

Uses very little additional memory and modifies the original structure.

Examples:

```text
Insertion Sort
Selection Sort
Heap Sort
```

## Out-of-place

Uses additional memory.

Example:

```text
Merge Sort
```

However, whether an algorithm is truly "in-place" can depend on the implementation.

---

# ⚡ Adaptive Sorting

An adaptive algorithm takes advantage of existing order in the input.

For example:

```text
[1, 2, 3, 4, 5, 6]
```

is already sorted.

An adaptive algorithm can exploit this structure instead of doing unnecessary work.

Insertion Sort is a classic example of an adaptive sorting algorithm.

---

# 🧠 Divide and Conquer

Merge Sort and Quick Sort are important examples of divide-and-conquer algorithms.

General pattern:

```text
Problem
   │
   ▼
Divide
   │
   ├───────┐
   ▼       ▼
Subproblem Subproblem
   │       │
   └───┬───┘
       ▼
     Combine
```

### Merge Sort

```text
Divide → Sort → Merge
```

### Quick Sort

```text
Choose Pivot → Partition → Recursively Sort
```

Understanding this pattern is important for advanced DSA.

---

# 🧮 Why O(n log n) Appears So Often

Consider repeatedly dividing an array:

```text
n
n/2
n/4
n/8
...
1
```

The number of divisions required is approximately:

```text
log₂(n)
```

If each level processes `n` elements:

```text
n × log n
```

Therefore:

```text
O(n log n)
```

This explains the complexity of algorithms such as Merge Sort and average-case Quick Sort.

---

# 🧪 Sorting with Multiple Criteria

Python allows powerful sorting using tuples.

Example:

```python
students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 85),
    ("David", 90)
]
```

Sort by marks and then name:

```python
students.sort(key=lambda x: (x[1], x[0]))

print(students)
```

Output:

```text
[
    ("Alice", 85),
    ("Charlie", 85),
    ("Bob", 90),
    ("David", 90)
]
```

---

# 🔥 Advanced Sorting Pattern: Custom Comparator

Python sorting generally works through a `key` function rather than a traditional two-argument comparator.

When a custom comparison is required:

```python
from functools import cmp_to_key


def compare(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


numbers = [5, 1, 4, 2]

numbers.sort(key=cmp_to_key(compare))

print(numbers)
```

For most practical cases, however, prefer a simple `key` function.

---

# 📊 Sorting Tuples

Python naturally compares tuples lexicographically.

```python
data = [
    (2, "B"),
    (1, "C"),
    (2, "A")
]

print(sorted(data))
```

Output:

```text
[
    (1, "C"),
    (2, "A"),
    (2, "B")
]
```

Python first compares the first element, then uses later elements when necessary.

---

# 🧹 Sorting Strings

```python
words = ["banana", "apple", "cherry"]

print(sorted(words))
```

Output:

```text
["apple", "banana", "cherry"]
```

Case-insensitive sorting:

```python
words = ["banana", "Apple", "cherry"]

print(sorted(words, key=str.lower))
```

---

# 🧠 Sorting and Searching Relationship

Sorting and searching are closely related.

For example:

```text
Unsorted array
      ↓
   Sort
      ↓
Sorted array
      ↓
Binary Search
```

Linear Search:

```text
O(n)
```

Binary Search:

```text
O(log n)
```

But Binary Search requires appropriate ordering.

This introduces an important algorithmic trade-off:

```text
Cost of sorting
+
Cost of repeated searches
```

If you search many times, preprocessing with sorting can be worthwhile.

---

# 🚨 Common Sorting Mistakes

## 1. Forgetting `sort()` returns `None`

Incorrect:

```python
numbers = numbers.sort()
```

Correct:

```python
numbers.sort()
```

or:

```python
numbers = sorted(numbers)
```

---

## 2. Confusing `sort()` and `sorted()`

```text
sort()
    ↓
modifies existing list

sorted()
    ↓
returns a new sorted iterable/list
```

---

## 3. Incorrect Binary Search Assumption

Do not apply ordinary Binary Search to an unsorted array.

Incorrect:

```text
[8, 2, 7, 1, 5]
```

Correct:

```text
[1, 2, 5, 7, 8]
```

---

## 4. Poor Pivot Selection

Quick Sort can degrade to:

```text
O(n²)
```

when partitions become highly unbalanced.

---

## 5. Ignoring Input Constraints

Choosing an algorithm without considering:

* `n`
* value range
* memory limits
* duplicate values
* data distribution
* stability requirements

can lead to inefficient solutions.

---

# 🧩 Practice Problems — Beginner

### Problem 1

Implement Bubble Sort.

```text
Input:
[5, 1, 4, 2, 8]

Output:
[1, 2, 4, 5, 8]
```

### Problem 2

Implement Selection Sort.

### Problem 3

Implement Insertion Sort.

### Problem 4

Sort an array in descending order.

### Problem 5

Find the second-largest element using sorting.

### Problem 6

Remove duplicates after sorting.

---

# 🚀 Practice Problems — Intermediate

### Problem 7

Merge two sorted arrays.

```text
A = [1, 3, 5]
B = [2, 4, 6]
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

### Problem 8

Implement Merge Sort.

### Problem 9

Implement Quick Sort.

### Problem 10

Find the kth smallest element.

### Problem 11

Sort an array containing only:

```text
0, 1, 2
```

### Problem 12

Sort an array according to frequency.

Example:

```text
Input:
[4, 6, 2, 4, 3, 4, 6]

Output:
[4, 4, 4, 6, 6, 2, 3]
```

---

# 🧠 Practice Problems — Advanced

### Problem 13 — Inversion Count

Find the number of inversions in an array.

```text
[2, 4, 1, 3, 5]
```

An inversion exists when:

```text
i < j
and
arr[i] > arr[j]
```

Expected count:

```text
3
```

Merge Sort can solve this efficiently.

---

### Problem 14 — Sort Intervals

Given:

```text
[(1, 3), (2, 6), (8, 10), (9, 12)]
```

Sort intervals by starting point.

---

### Problem 15 — Merge Intervals

Merge overlapping intervals.

Expected:

```text
[(1, 6), (8, 12)]
```

---

### Problem 16 — Largest Number

Arrange integers to create the largest possible number.

Example:

```text
[3, 30, 34, 5, 9]
```

Expected:

```text
9534330
```

---

### Problem 17 — Sort Nearly Sorted Array

Every element is at most `k` positions away from its sorted location.

Use an appropriate data structure to improve efficiency.

---

# 🎯 Interview Questions

### Beginner

1. What is sorting?
2. Why is sorting useful?
3. What is Bubble Sort?
4. What is Selection Sort?
5. What is Insertion Sort?
6. What is the difference between `sort()` and `sorted()`?
7. How do you sort in descending order?
8. What does the `key` parameter do?

### Intermediate

9. Explain Merge Sort.
10. Explain Quick Sort.
11. What is a pivot?
12. What is partitioning?
13. Why is Merge Sort `O(n log n)`?
14. What is a stable sorting algorithm?
15. What does in-place sorting mean?
16. Which sorting algorithms are adaptive?
17. What is the difference between comparison and non-comparison sorting?

### Advanced

18. Why can Quick Sort become `O(n²)`?
19. How can Quick Sort pivot selection be improved?
20. Explain Heap Sort.
21. When is Counting Sort useful?
22. Explain Radix Sort.
23. How can Merge Sort count inversions?
24. How would you sort objects using multiple criteria?
25. Why is Python's built-in sorting generally preferred in production code?
26. How does stable sorting help with multi-key sorting?
27. What sorting strategy would you choose for nearly sorted data?
28. How does sorting affect the complexity of repeated searches?

---

# ⚡ Quick Revision

```text
Bubble Sort
→ Repeatedly swap adjacent elements
→ O(n²) average/worst
→ Stable
→ In-place

Selection Sort
→ Select minimum repeatedly
→ O(n²)
→ Usually unstable
→ In-place

Insertion Sort
→ Insert each element into sorted portion
→ O(n²) average/worst
→ O(n) best
→ Stable
→ In-place

Merge Sort
→ Divide and merge
→ O(n log n)
→ Stable
→ Extra memory generally required

Quick Sort
→ Pivot + partition
→ O(n log n) average
→ O(n²) worst
→ Often in-place depending on implementation

Heap Sort
→ Binary heap
→ O(n log n)
→ In-place
→ Unstable

Counting Sort
→ Frequency counting
→ O(n + k)
→ Useful for limited integer ranges

Radix Sort
→ Sort digit by digit
→ O(d(n + k))

Bucket Sort
→ Distribute into buckets
→ Performance depends on distribution

Python Sorting
→ sorted(iterable)
→ list.sort()
→ key=
→ reverse=
```

---

# 📋 Complexity Cheat Sheet

| Algorithm |       Best |    Average |      Worst |
| --------- | ---------: | ---------: | ---------: |
| Bubble    |       O(n) |      O(n²) |      O(n²) |
| Selection |      O(n²) |      O(n²) |      O(n²) |
| Insertion |       O(n) |      O(n²) |      O(n²) |
| Merge     | O(n log n) | O(n log n) | O(n log n) |
| Quick     | O(n log n) | O(n log n) |      O(n²) |
| Heap      | O(n log n) | O(n log n) | O(n log n) |
| Counting  |     O(n+k) |     O(n+k) |     O(n+k) |
| Radix     |  O(d(n+k)) |  O(d(n+k)) |  O(d(n+k)) |
| Bucket    |    O(n+k)* |    O(n+k)* |     O(n²)* |

`*` Depends on implementation and input distribution.

---

# 🛠️ Recommended Folder Structure

```text
03-Sorting/
│
├── README.md
│
├── 01-bubble-sort.py
├── 02-selection-sort.py
├── 03-insertion-sort.py
├── 04-merge-sort.py
├── 05-quick-sort.py
├── 06-heap-sort.py
├── 07-counting-sort.py
├── 08-radix-sort.py
├── 09-bucket-sort.py
│
├── 10-sorting-custom-objects.py
├── 11-sort-by-frequency.py
├── 12-merge-intervals.py
├── 13-inversion-count.py
└── 14-kth-smallest-element.py
```

---

# 🎓 Mastery Checklist

### Fundamentals

* [ ] Understand what sorting means
* [ ] Understand ascending and descending order
* [ ] Understand stable vs unstable sorting
* [ ] Understand in-place sorting
* [ ] Understand time and space complexity

### Basic Algorithms

* [ ] Implement Bubble Sort
* [ ] Implement Selection Sort
* [ ] Implement Insertion Sort

### Advanced Comparison Sorts

* [ ] Understand Merge Sort
* [ ] Implement Merge Sort
* [ ] Understand Quick Sort
* [ ] Implement Quick Sort
* [ ] Understand Heap Sort
* [ ] Implement Heap Sort

### Non-Comparison Sorts

* [ ] Understand Counting Sort
* [ ] Understand Radix Sort
* [ ] Understand Bucket Sort

### Python

* [ ] Use `sorted()`
* [ ] Use `list.sort()`
* [ ] Use `key=`
* [ ] Use `reverse=`
* [ ] Sort custom objects
* [ ] Perform multi-key sorting

### Problem Solving

* [ ] Merge sorted arrays
* [ ] Count inversions
* [ ] Solve merge interval problems
* [ ] Find kth smallest/largest
* [ ] Sort by frequency
* [ ] Solve custom comparator problems

---

# 💡 Problem-Solving Strategy

When you encounter a sorting problem, ask:

```text
1. What is the input size?
        ↓
2. Is the data already partially sorted?
        ↓
3. Are values from a small range?
        ↓
4. Do I need stability?
        ↓
5. Do I need to preserve the original data?
        ↓
6. Is extra memory available?
        ↓
7. Do I need a custom ordering?
        ↓
8. Can sorting simplify the problem?
```

Then choose an appropriate strategy.

---

# 🏆 Key Takeaways

1. **Sorting** organizes data according to a defined ordering.
2. Bubble, Selection, and Insertion Sort are excellent for learning fundamentals.
3. Merge Sort provides guaranteed `O(n log n)` time.
4. Quick Sort is efficient on average but has an `O(n²)` worst case.
5. Heap Sort provides `O(n log n)` worst-case time with low auxiliary space.
6. Counting, Radix, and Bucket Sort can outperform comparison-based methods under suitable constraints.
7. **Stable sorting** is important when working with records and multiple sorting criteria.
8. Python provides powerful built-in sorting through `sorted()` and `list.sort()`.
9. The `key` parameter is one of the most useful tools for practical Python sorting.
10. Sorting is often a preprocessing step that enables more efficient algorithms.

---

# 📚 References

* [Python Documentation — Sorting HOW TO](https://docs.python.org/3/howto/sorting.html?utm_source=chatgpt.com)
* [Python Documentation — Built-in `sorted()`](https://docs.python.org/3/library/functions.html?utm_source=chatgpt.com#sorted)
* [Python Documentation — List `sort()`](https://docs.python.org/3/tutorial/datastructures.html?utm_source=chatgpt.com)
* [Python Documentation — `heapq`](https://docs.python.org/3/library/heapq.html?utm_source=chatgpt.com)

---

# 🗺️ DSA Learning Roadmap

```text
22-DSA-with-Python
│
├── 01-Arrays
├── 02-Searching
├── 03-Sorting
│
├── 04-Strings
├── 05-Linked-Lists
├── 06-Stacks
├── 07-Queues
├── 08-Hashing
├── 09-Recursion
├── 10-Trees
├── 11-Binary-Search-Trees
├── 12-Heap
├── 13-Graphs
├── 14-Greedy
├── 15-Dynamic-Programming
└── 16-Advanced-Algorithms
```

---

# 🚀 Next Topic

➡️ **[04-Strings](../04-Strings/README.md)**

> **Keep coding. Keep solving. Keep improving.**
> Master the fundamentals first, then optimize your approach. 🐍💻
