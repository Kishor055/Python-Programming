# 📚 DSA with Python — Arrays

> **Master Arrays from fundamentals to interview-level problem solving using Python.**

Welcome to **Arrays**, the first major data structure in the **Data Structures and Algorithms (DSA) with Python** section.

Arrays are one of the most fundamental data structures in programming. They provide an efficient way to store and access a collection of elements and form the foundation for many advanced concepts such as:

* Searching
* Sorting
* Two Pointers
* Sliding Window
* Prefix Sum
* Hashing
* Recursion
* Dynamic Programming
* Matrix algorithms

This chapter focuses on understanding arrays **conceptually**, implementing common operations in Python, analyzing their **time and space complexity**, and solving progressively harder problems.

---

## 📌 Table of Contents

* [🎯 Learning Objectives](#-learning-objectives)
* [🧠 What Is an Array?](#-what-is-an-array)
* [🐍 Arrays in Python](#-arrays-in-python)
* [📦 Python Lists as Dynamic Arrays](#-python-lists-as-dynamic-arrays)
* [🔢 Array Representation](#-array-representation)
* [⚡ Array Access](#-array-access)
* [➕ Insertion](#-insertion)
* [❌ Deletion](#-deletion)
* [🔎 Searching](#-searching)
* [🔄 Traversing an Array](#-traversing-an-array)
* [✏️ Updating Elements](#️-updating-elements)
* [📏 Array Length](#-array-length)
* [🔀 Array Reversal](#-array-reversal)
* [🧮 Common Array Operations](#-common-array-operations)
* [⏱️ Time Complexity](#️-time-complexity)
* [💾 Space Complexity](#-space-complexity)
* [🧩 Important Array Patterns](#-important-array-patterns)
* [1️⃣ Two Pointer Technique](#1️⃣-two-pointer-technique)
* [2️⃣ Sliding Window](#2️⃣-sliding-window)
* [3️⃣ Prefix Sum](#3️⃣-prefix-sum)
* [4️⃣ Kadane's Algorithm](#4️⃣-kadanes-algorithm)
* [5️⃣ Frequency Counting](#5️⃣-frequency-counting)
* [6️⃣ Dutch National Flag](#6️⃣-dutch-national-flag)
* [7️⃣ In-Place Algorithms](#7️⃣-in-place-algorithms)
* [🧠 Important Problems](#-important-problems)
* [🟢 Beginner Problems](#-beginner-problems)
* [🟡 Intermediate Problems](#-intermediate-problems)
* [🔴 Advanced Problems](#-advanced-problems)
* [🧪 Practice Exercises](#-practice-exercises)
* [🚀 Mini Projects](#-mini-projects)
* [💼 Interview Questions](#-interview-questions)
* [⚡ Quick Revision](#-quick-revision)
* [📋 Complexity Cheat Sheet](#-complexity-cheat-sheet)
* [🧭 Problem-Solving Strategy](#-problem-solving-strategy)
* [📖 References](#-references)
* [➡️ Next Topic](#️-next-topic)

---

# 🎯 Learning Objectives

After completing this chapter, you should be able to:

* Understand what an array is.
* Understand array indexing.
* Work with Python lists as dynamic arrays.
* Traverse arrays efficiently.
* Insert and delete elements.
* Search for elements.
* Update array values.
* Reverse arrays.
* Find minimum and maximum values.
* Calculate sums and averages.
* Remove duplicates.
* Rotate arrays.
* Merge arrays.
* Understand time and space complexity.
* Apply two-pointer techniques.
* Apply sliding-window techniques.
* Use prefix sums.
* Understand Kadane's algorithm.
* Solve common array interview problems.
* Identify appropriate algorithmic patterns.

---

# 🧠 What Is an Array?

An **array** is a data structure used to store multiple elements in an ordered collection.

Conceptually:

```text
Array
┌────┬────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└────┴────┴────┴────┴────┘
   0    1    2    3    4
```

Each element has an **index**.

The first element is generally at index:

```text
0
```

The second:

```text
1
```

and so on.

---

# 🐍 Arrays in Python

Python provides several ways to represent collections of values.

The most commonly used structure for DSA is:

```python
arr = [10, 20, 30, 40, 50]
```

Python also provides the standard-library `array` module and third-party numerical libraries such as NumPy, but **Python lists are the primary structure used for most DSA problems**.

---

# 📦 Python Lists as Dynamic Arrays

Python's `list` behaves like a dynamic array.

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

Lists can grow and shrink dynamically.

```python
numbers.append(50)

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 🔢 Array Representation

Consider:

```python
arr = [10, 20, 30, 40, 50]
```

Conceptually:

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Value:   10   20   30   40   50
```

Accessing an element:

```python
print(arr[2])
```

Output:

```text
30
```

---

# ⚡ Array Access

Array/list access by index is typically **O(1)**.

```python
arr = [10, 20, 30, 40, 50]

print(arr[0])
print(arr[3])
```

Output:

```text
10
40
```

### Why O(1)?

The index directly identifies the position of the element, allowing constant-time access in the underlying array structure.

---

# ➕ Insertion

## Append

Add an element to the end:

```python
arr = [10, 20, 30]

arr.append(40)

print(arr)
```

Output:

```text
[10, 20, 30, 40]
```

Average complexity:

```text
O(1) amortized
```

---

## Insert at a Specific Position

```python
arr = [10, 20, 30]

arr.insert(1, 15)

print(arr)
```

Output:

```text
[10, 15, 20, 30]
```

Typical complexity:

```text
O(n)
```

because elements after the insertion point may need to be shifted.

---

# ❌ Deletion

## Remove by Value

```python
arr = [10, 20, 30, 40]

arr.remove(30)

print(arr)
```

Output:

```text
[10, 20, 40]
```

Typical complexity:

```text
O(n)
```

because the element may first need to be searched for.

---

## Remove by Index

```python
arr = [10, 20, 30, 40]

del arr[1]

print(arr)
```

Output:

```text
[10, 30, 40]
```

Removing from the middle typically requires shifting elements.

---

## Pop

```python
arr = [10, 20, 30]

value = arr.pop()

print(value)
print(arr)
```

Output:

```text
30
[10, 20]
```

Removing from the end is typically:

```text
O(1)
```

---

# 🔎 Searching

## Linear Search

Linear search checks elements one by one.

```python
def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1
```

Example:

```python
arr = [10, 20, 30, 40]

print(linear_search(arr, 30))
```

Output:

```text
2
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# 🔄 Traversing an Array

Traversal means visiting every element.

```python
arr = [10, 20, 30, 40]

for value in arr:
    print(value)
```

Output:

```text
10
20
30
40
```

Using indexes:

```python
for i in range(len(arr)):
    print(arr[i])
```

---

# ✏️ Updating Elements

Array elements can be updated using indexes.

```python
arr = [10, 20, 30]

arr[1] = 25

print(arr)
```

Output:

```text
[10, 25, 30]
```

Direct indexed update is typically:

```text
O(1)
```

---

# 📏 Array Length

Use:

```python
len(arr)
```

Example:

```python
arr = [10, 20, 30, 40]

print(len(arr))
```

Output:

```text
4
```

---

# 🔄 Array Reversal

## Using `reverse()`

```python
arr = [1, 2, 3, 4, 5]

arr.reverse()

print(arr)
```

---

## Using Slicing

```python
arr = [1, 2, 3, 4, 5]

reversed_arr = arr[::-1]
```

This creates a new list.

---

## Two-Pointer Reversal

A classic DSA approach:

```python
def reverse_array(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

This is an **in-place algorithm**.

---

# 🧮 Common Array Operations

## Find Maximum

```python
def find_max(arr):

    maximum = arr[0]

    for value in arr:
        if value > maximum:
            maximum = value

    return maximum
```

---

## Find Minimum

```python
def find_min(arr):

    minimum = arr[0]

    for value in arr:
        if value < minimum:
            minimum = value

    return minimum
```

---

## Calculate Sum

```python
def array_sum(arr):

    total = 0

    for value in arr:
        total += value

    return total
```

Python also provides:

```python
sum(arr)
```

---

## Calculate Average

```python
def average(arr):

    if not arr:
        return 0

    return sum(arr) / len(arr)
```

---

# ⏱️ Time Complexity

Understanding complexity is essential in DSA.

For Python lists, common operations are approximately:

| Operation             | Average Complexity |
| --------------------- | -----------------: |
| Access by index       |               O(1) |
| Update by index       |               O(1) |
| Append                |     O(1) amortized |
| Pop from end          |               O(1) |
| Search                |               O(n) |
| Insert at beginning   |               O(n) |
| Insert in middle      |               O(n) |
| Delete from beginning |               O(n) |
| Delete from middle    |               O(n) |
| Delete by value       |               O(n) |
| Membership test       |               O(n) |

Actual complexity can depend on the specific operation and implementation details.

---

# 💾 Space Complexity

Space complexity measures additional memory used by an algorithm.

Example:

```python
def find_max(arr):
    maximum = arr[0]

    for value in arr:
        maximum = max(maximum, value)

    return maximum
```

Additional space:

```text
O(1)
```

because only a small fixed amount of extra memory is used.

---

# 🧩 Important Array Patterns

Many array problems can be solved using a small number of recurring patterns.

The most important are:

```text
Two Pointers
Sliding Window
Prefix Sum
Hashing
Binary Search
Kadane's Algorithm
Sorting
Frequency Counting
In-Place Manipulation
```

Learning these patterns is more valuable than memorizing individual solutions.

---

# 1️⃣ Two Pointer Technique

Two pointers use two indexes to process an array efficiently.

Example:

```text
left →              ← right
[1, 2, 3, 4, 5, 6, 7]
```

Basic pattern:

```python
left = 0
right = len(arr) - 1

while left < right:

    # process arr[left] and arr[right]

    left += 1
    right -= 1
```

Useful for:

* Reversing arrays
* Pair-sum problems
* Removing duplicates
* Partitioning
* Palindrome problems
* Sorted-array problems

---

## Example — Two Sum in Sorted Array

```python
def two_sum_sorted(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return [left, right]

        if total < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]
```

For a sorted array:

```text
Time:  O(n)
Space: O(1)
```

---

# 2️⃣ Sliding Window

Sliding window is useful for problems involving contiguous subarrays.

Example:

```text
[1, 2, 3, 4, 5, 6]
 ↑──────↑
 window
```

A window can expand or shrink as we process the array.

Example:

```python
def max_sum_subarray(arr, k):

    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    maximum = window_sum

    for right in range(k, len(arr)):

        window_sum += arr[right]
        window_sum -= arr[right - k]

        maximum = max(maximum, window_sum)

    return maximum
```

Complexity:

```text
Time:  O(n)
Space: O(1)
```

---

# 3️⃣ Prefix Sum

Prefix sums allow repeated range-sum queries to be answered efficiently.

For:

```text
arr = [2, 4, 1, 5, 3]
```

Prefix:

```text
[0, 2, 6, 7, 12, 15]
```

Implementation:

```python
def prefix_sum(arr):

    prefix = [0]

    for value in arr:
        prefix.append(prefix[-1] + value)

    return prefix
```

Range sum from index `left` to `right`:

```python
range_sum = prefix[right + 1] - prefix[left]
```

### Complexity

Building prefix sum:

```text
O(n)
```

Each range query:

```text
O(1)
```

---

# 4️⃣ Kadane's Algorithm

Kadane's algorithm finds the maximum sum of a contiguous subarray.

Example:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Maximum subarray:

```text
[4, -1, 2, 1]
```

Sum:

```text
6
```

Implementation:

```python
def max_subarray(arr):

    current = arr[0]
    best = arr[0]

    for value in arr[1:]:

        current = max(value, current + value)
        best = max(best, current)

    return best
```

Complexity:

```text
Time:  O(n)
Space: O(1)
```

---

# 5️⃣ Frequency Counting

Frequency counting tracks how many times each value occurs.

Example:

```python
from collections import Counter

arr = [1, 2, 2, 3, 3, 3]

frequency = Counter(arr)

print(frequency)
```

Output conceptually:

```text
1 → 1
2 → 2
3 → 3
```

Frequency counting is useful for:

* Duplicate detection
* Anagrams
* Majority elements
* Frequency-based sorting
* Counting problems

---

# 6️⃣ Dutch National Flag

The Dutch National Flag algorithm partitions an array containing three categories.

Classic example:

```text
0, 1, 2
```

Goal:

```text
[0, 0, 1, 1, 2, 2]
```

It can be solved in:

```text
Time:  O(n)
Space: O(1)
```

using three pointers:

```text
low
mid
high
```

This is an important example of in-place partitioning.

---

# 7️⃣ In-Place Algorithms

An in-place algorithm modifies the input structure without requiring another structure proportional to the input size.

Example:

```python
def reverse(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1
```

Additional space:

```text
O(1)
```

In-place techniques are especially important in interviews.

---

# 🧠 Important Problems

Array problems should be solved progressively.

A recommended progression:

```text
Basic Traversal
      ↓
Searching
      ↓
Min / Max
      ↓
Reversal
      ↓
Duplicates
      ↓
Two Sum
      ↓
Two Pointers
      ↓
Sliding Window
      ↓
Prefix Sum
      ↓
Kadane
      ↓
Partitioning
      ↓
Advanced Array Problems
```

---

# 🟢 Beginner Problems

### 1. Find Maximum

Given an array, find the largest element.

```text
Input:
[4, 2, 9, 1, 7]

Output:
9
```

---

### 2. Find Minimum

```text
Input:
[4, 2, 9, 1, 7]

Output:
1
```

---

### 3. Calculate Sum

```text
Input:
[1, 2, 3, 4]

Output:
10
```

---

### 4. Reverse an Array

```text
Input:
[1, 2, 3, 4]

Output:
[4, 3, 2, 1]
```

---

### 5. Linear Search

Find the index of a target value.

---

### 6. Count Even Numbers

```text
Input:
[1, 2, 4, 7, 8]

Output:
3
```

---

### 7. Remove Duplicates

Given:

```text
[1, 2, 2, 3, 3, 4]
```

produce:

```text
[1, 2, 3, 4]
```

---

# 🟡 Intermediate Problems

### 1. Two Sum

Find two values whose sum equals a target.

---

### 2. Move Zeroes

Input:

```text
[0, 1, 0, 3, 12]
```

Output:

```text
[1, 3, 12, 0, 0]
```

---

### 3. Rotate Array

Rotate an array by `k` positions.

---

### 4. Maximum Subarray

Use Kadane's algorithm.

---

### 5. Majority Element

Find the element appearing more than half the time when such an element exists.

---

### 6. Best Time to Buy and Sell Stock

Find the maximum possible profit from one buy and one later sell.

---

### 7. Merge Sorted Arrays

Merge two sorted arrays into one sorted result.

---

### 8. Intersection of Arrays

Find common values between arrays.

---

# 🔴 Advanced Problems

### 1. Product of Array Except Self

Return an array where each position contains the product of all other elements without using division.

---

### 2. Trapping Rain Water

Calculate how much water can be trapped between bars.

---

### 3. Maximum Product Subarray

Find the contiguous subarray with the maximum product.

---

### 4. Three Sum

Find unique triplets whose sum equals zero.

---

### 5. Four Sum

Generalize the pair/triplet concept to four values.

---

### 6. Subarray Sum Equals K

Count contiguous subarrays whose sum equals `k`.

A prefix-sum + hashing approach is commonly used.

---

### 7. Longest Consecutive Sequence

Find the length of the longest consecutive sequence.

---

### 8. Merge Intervals

Merge overlapping intervals represented as an array of pairs.

---

### 9. Maximum Circular Subarray Sum

Find the maximum subarray sum when the array is considered circular.

---

### 10. First Missing Positive

Find the smallest missing positive integer using efficient time and space complexity.

---

# 🧪 Practice Exercises

## 🟢 Level 1

* [ ] Print all elements.
* [ ] Find minimum.
* [ ] Find maximum.
* [ ] Calculate sum.
* [ ] Calculate average.
* [ ] Count even numbers.
* [ ] Count odd numbers.
* [ ] Search for an element.
* [ ] Reverse an array.
* [ ] Copy an array.

## 🟡 Level 2

* [ ] Remove duplicates.
* [ ] Find second-largest element.
* [ ] Rotate an array.
* [ ] Move zeroes.
* [ ] Merge sorted arrays.
* [ ] Find missing number.
* [ ] Find duplicate number.
* [ ] Solve Two Sum.
* [ ] Find majority element.
* [ ] Find maximum subarray.

## 🔴 Level 3

* [ ] Three Sum.
* [ ] Four Sum.
* [ ] Product Except Self.
* [ ] Trapping Rain Water.
* [ ] Maximum Product Subarray.
* [ ] Subarray Sum Equals K.
* [ ] Longest Consecutive Sequence.
* [ ] First Missing Positive.
* [ ] Maximum Circular Subarray.
* [ ] Merge Intervals.

---

# 🚀 Mini Projects

## 1. 📊 Student Marks Analyzer

Build a program that accepts student marks and calculates:

* Highest marks
* Lowest marks
* Average
* Total
* Number of passed students
* Number of failed students
* Grade distribution

---

## 2. 📈 Stock Price Analyzer

Given daily stock prices, calculate:

* Minimum price
* Maximum price
* Best buying day
* Best selling day
* Maximum possible profit

---

## 3. 🛒 Sales Data Analyzer

Given daily sales:

```python
sales = [1200, 900, 1500, 2100, 1800]
```

Calculate:

* Total sales
* Average sales
* Highest sales
* Lowest sales
* Best sales day
* Days above average

---

## 4. 🔢 Array Statistics Tool

Build a CLI application that accepts an array and provides:

```text
Maximum
Minimum
Sum
Average
Median
Duplicates
Frequency
Sorted Array
Reversed Array
```

---

# 💼 Interview Questions

## Fundamentals

1. What is an array?
2. What is an index?
3. Why does array indexing generally provide O(1) access?
4. What is the difference between an array and a linked list?
5. What is a dynamic array?
6. Why are Python lists considered dynamic arrays?
7. What is the difference between `append()` and `insert()`?
8. What is the complexity of searching a Python list?
9. What is an in-place algorithm?
10. What is array traversal?

## Intermediate

11. How would you reverse an array in-place?
12. How can you find the second-largest element in one pass?
13. How can duplicates be detected efficiently?
14. What is the two-pointer technique?
15. What is sliding window?
16. When should you use prefix sums?
17. What is Kadane's algorithm?
18. How can you move zeroes to the end of an array?
19. How can you rotate an array efficiently?
20. How can two sorted arrays be merged?

## Advanced

21. How would you solve Three Sum?
22. How does Product of Array Except Self work?
23. How can Trapping Rain Water be solved using two pointers?
24. How can prefix sums and hashing solve Subarray Sum Equals K?
25. What is the Dutch National Flag algorithm?
26. How can you find the longest consecutive sequence efficiently?
27. How would you solve First Missing Positive?
28. What is the difference between an in-place and out-of-place algorithm?
29. How do you analyze array algorithms using Big-O notation?
30. Which array patterns do you recognize immediately when reading a problem?

---

# ⚡ Quick Revision

```text
Array
│
├── Indexing
│   └── O(1)
│
├── Traversal
│   └── O(n)
│
├── Searching
│   └── O(n)
│
├── Insertion
│   ├── End → O(1) amortized
│   └── Middle/Beginning → O(n)
│
├── Deletion
│   ├── End → O(1)
│   └── Middle/Beginning → O(n)
│
├── Two Pointers
│   └── Often O(n)
│
├── Sliding Window
│   └── Often O(n)
│
├── Prefix Sum
│   ├── Build → O(n)
│   └── Query → O(1)
│
└── Kadane
    └── O(n)
```

---

# 📋 Complexity Cheat Sheet

| Problem / Operation |           Time | Extra Space |
| ------------------- | -------------: | ----------: |
| Access              |           O(1) |        O(1) |
| Update              |           O(1) |        O(1) |
| Traversal           |           O(n) |        O(1) |
| Linear Search       |           O(n) |        O(1) |
| Append              | O(1) amortized |        O(1) |
| Pop End             |           O(1) |        O(1) |
| Insert Beginning    |           O(n) |        O(1) |
| Delete Beginning    |           O(n) |        O(1) |
| Reverse In-Place    |           O(n) |        O(1) |
| Prefix Sum          |           O(n) |        O(n) |
| Two Pointer         |     Often O(n) |  Often O(1) |
| Sliding Window      |     Often O(n) |  Often O(1) |
| Kadane              |           O(n) |        O(1) |

---

# 🧭 Problem-Solving Strategy

When you receive an array problem, follow this process.

## Step 1 — Understand the Input

Ask:

```text
Is the array sorted?
Can values be negative?
Are duplicates allowed?
Is the array mutable?
What are the constraints?
```

---

## Step 2 — Identify the Pattern

Look for clues.

### Sorted array

Consider:

```text
Two Pointers
Binary Search
```

### Contiguous subarray

Consider:

```text
Sliding Window
Prefix Sum
Kadane
```

### Frequency

Consider:

```text
Hash Map
Counter
```

### In-place requirement

Consider:

```text
Two Pointers
Index manipulation
```

---

## Step 3 — Start With Brute Force

First create a correct solution.

Then ask:

```text
Can I reduce the time complexity?
Can I reduce memory?
Can I avoid repeated work?
Can I use hashing?
Can I use sorting?
Can I use two pointers?
Can I use a sliding window?
```

---

## Step 4 — Analyze Complexity

Always determine:

```text
Time Complexity
Space Complexity
```

For example:

```text
Brute Force:
O(n²)

Optimized:
O(n)
```

Understanding this difference is one of the central goals of DSA.

---

# 🏗️ Recommended Folder Structure

```text
22-DSA-with-Python/
│
├── 01-Arrays/
│   ├── README.md
│   ├── 01-traversal.py
│   ├── 02-searching.py
│   ├── 03-min-max.py
│   ├── 04-reverse-array.py
│   ├── 05-two-sum.py
│   ├── 06-two-pointers.py
│   ├── 07-sliding-window.py
│   ├── 08-prefix-sum.py
│   ├── 09-kadanes-algorithm.py
│   ├── 10-move-zeroes.py
│   ├── 11-rotate-array.py
│   ├── 12-majority-element.py
│   ├── 13-three-sum.py
│   ├── 14-product-except-self.py
│   ├── 15-trapping-rain-water.py
│   └── 16-advanced-array-problems.py
│
├── 02-Strings/
├── 03-Linked-Lists/
├── 04-Stacks/
├── 05-Queues/
├── 06-Hashing/
├── 07-Trees/
├── 08-Binary-Search-Trees/
├── 09-Heaps/
├── 10-Graphs/
├── 11-Recursion/
├── 12-Backtracking/
├── 13-Dynamic-Programming/
└── 14-Greedy-Algorithms/
```

---

# 📖 References

* [Python Documentation — Built-in Types](https://docs.python.org/3/library/stdtypes.html?utm_source=chatgpt.com)
* [Python Documentation — Lists](https://docs.python.org/3/tutorial/datastructures.html?utm_source=chatgpt.com)
* [Python Documentation — `collections`](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com)
* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)

---

# 🧠 Key Takeaways

> **Arrays are simple to understand but extremely powerful in algorithmic problem solving.**

Remember these core ideas:

```text
1. Indexing          → O(1)
2. Traversal         → O(n)
3. Searching         → O(n)
4. Insert middle     → O(n)
5. Delete middle     → O(n)
6. Two Pointers      → Often O(n)
7. Sliding Window    → Often O(n)
8. Prefix Sum        → Fast range queries
9. Kadane            → Maximum subarray
10. Hashing          → Fast frequency/lookups
```

The real skill is not memorizing solutions.

It is learning to recognize:

```text
Problem
   ↓
Pattern
   ↓
Algorithm
   ↓
Implementation
   ↓
Complexity Analysis
   ↓
Optimization
```

---

# 🏆 Mastery Checklist

Before moving to the next DSA topic, make sure you can:

* [ ] Explain arrays and indexing.
* [ ] Explain dynamic arrays.
* [ ] Traverse an array.
* [ ] Search an array.
* [ ] Insert and delete elements.
* [ ] Reverse an array in-place.
* [ ] Find minimum and maximum.
* [ ] Remove duplicates.
* [ ] Rotate an array.
* [ ] Solve Two Sum.
* [ ] Use two pointers.
* [ ] Use sliding window.
* [ ] Build prefix sums.
* [ ] Explain Kadane's algorithm.
* [ ] Use frequency counting.
* [ ] Understand in-place algorithms.
* [ ] Analyze time complexity.
* [ ] Analyze space complexity.
* [ ] Solve beginner array problems without help.
* [ ] Approach intermediate problems systematically.

---

# ➡️ Next Topic

### `02-Strings`

After arrays, move to **Strings**, where you will learn:

* String traversal
* String manipulation
* Character frequency
* Palindromes
* Anagrams
* String searching
* Two pointers
* Sliding window
* String hashing
* Pattern-based problems

---

## ⭐ Keep Practicing

```text
Learn the Pattern
       ↓
Understand the Algorithm
       ↓
Implement in Python
       ↓
Analyze Complexity
       ↓
Solve Variations
       ↓
Repeat
```

> **Don't memorize the solution. Master the pattern.** 🧠🐍

**Happy Coding & Keep Solving! 🚀**

