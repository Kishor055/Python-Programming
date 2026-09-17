# 🧠 22 — Data Structures & Algorithms with Python

> A complete **Data Structures and Algorithms (DSA)** roadmap using Python — from fundamentals to advanced problem solving, competitive programming, technical interviews, and real-world applications.

---

## 📌 Overview

**Data Structures and Algorithms (DSA)** are the foundation of efficient software development.

Data structures define **how data is organized and stored**, while algorithms define **how that data is processed to solve problems**.

Learning DSA is not only about memorizing algorithms.

The real goal is to develop the ability to:

* Analyze a problem.
* Choose the appropriate data structure.
* Design an efficient algorithm.
* Analyze time and space complexity.
* Identify edge cases.
* Optimize an existing solution.
* Translate the solution into clean Python code.
* Recognize reusable problem-solving patterns.

This section provides a structured journey:

```text
Python Fundamentals
       ↓
Data Structures
       ↓
Algorithms
       ↓
Complexity Analysis
       ↓
Problem-Solving Patterns
       ↓
Advanced Algorithms
       ↓
Interview-Level Problems
       ↓
Real-World Applications
```

---

# 🎯 Learning Objectives

By completing this section, you should be able to:

* Understand fundamental data structures.
* Implement data structures from scratch.
* Analyze algorithm complexity.
* Use Python's built-in data structures effectively.
* Solve searching and sorting problems.
* Work with linked lists, stacks, and queues.
* Understand trees and graphs.
* Solve recursive and backtracking problems.
* Apply greedy algorithms.
* Understand dynamic programming.
* Use hashing effectively.
* Solve graph traversal and shortest-path problems.
* Recognize common DSA patterns.
* Optimize brute-force solutions.
* Prepare for technical interviews.

---

# 📚 Complete DSA Roadmap

```text
22-DSA-with-Python/
│
├── 01-Arrays/
├── 02-Searching/
├── 03-Sorting/
├── 04-Linked-List/
├── 05-Stack/
├── 06-Queue/
├── 07-Trees/
├── 08-Binary-Search-Tree/
├── 09-Heap/
├── 10-Hashing/
├── 11-Graphs/
├── 12-Greedy/
├── 13-Dynamic-Programming/
└── 14-Advanced-DSA/
```

---

# 🗺️ DSA Learning Map

```text
                         DSA
                          │
          ┌───────────────┴───────────────┐
          │                               │
     Data Structures                  Algorithms
          │                               │
    ┌─────┼─────┐                 ┌───────┼────────┐
    │     │     │                 │       │        │
 Arrays Lists Trees              Search  Sort    Graph
    │     │     │                 │       │        │
 Stack Queue Heap              Binary   Merge     BFS
    │     │     │              Search   Quick     DFS
 Hashing Graph BST
          │
          └──────────────┐
                         │
                Problem Solving
                         │
       ┌─────────┬───────┼────────┬──────────┐
       │         │       │        │          │
   Recursion  Greedy    DP   Backtracking  Patterns
```

---

# 🔹 What is DSA?

## Data Structure

A **data structure** is a method of organizing and storing data so that it can be accessed and modified efficiently.

Examples:

```text
Array
Linked List
Stack
Queue
Tree
Heap
Hash Table
Graph
```

---

## Algorithm

An **algorithm** is a finite sequence of steps used to solve a problem.

Example:

```text
Problem:
Find the largest number.

Algorithm:
1. Assume first element is largest.
2. Compare it with every other element.
3. Update largest when a larger value is found.
4. Return largest.
```

Python:

```python
def find_max(numbers):
    maximum = numbers[0]

    for number in numbers[1:]:
        if number > maximum:
            maximum = number

    return maximum
```

---

# 🔹 Data Structures vs Algorithms

| Data Structures  | Algorithms          |
| ---------------- | ------------------- |
| Organize data    | Process data        |
| Focus on storage | Focus on operations |
| Array            | Binary Search       |
| Linked List      | Merge Sort          |
| Stack            | DFS                 |
| Queue            | BFS                 |
| Tree             | Tree Traversal      |
| Hash Table       | Hash-based Lookup   |
| Graph            | Dijkstra            |

Both concepts work together.

```text
Efficient Data Structure
          +
Efficient Algorithm
          ↓
Efficient Solution
```

---

# 🔹 Why Learn DSA?

DSA helps you understand:

* Efficiency
* Scalability
* Memory usage
* Optimization
* Problem decomposition
* Algorithmic thinking

Consider searching for an item in one million values.

A linear search may require:

```text
O(n)
```

A suitable sorted structure may allow:

```text
O(log n)
```

The choice of algorithm and data structure can therefore have a major impact on performance.

---

# ⏱️ Complexity Analysis

Before studying individual data structures, understand **complexity analysis**.

Complexity describes how resource usage grows as input size increases.

The two major measurements are:

```text
Time Complexity
Space Complexity
```

---

# 🔹 Big-O Notation

Common complexities:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)
O(n!)
```

Generally, algorithms with slower growth are preferable when practical.

---

## O(1) — Constant

```python
def get_first(items):
    return items[0]
```

The operation does not depend on the number of elements.

---

## O(n) — Linear

```python
def print_items(items):
    for item in items:
        print(item)
```

If input doubles, the number of iterations grows approximately proportionally.

---

## O(log n) — Logarithmic

Binary search is the classic example.

Each step eliminates approximately half of the remaining search space.

---

## O(n²) — Quadratic

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Two nested loops generally produce quadratic behavior when both depend on `n`.

---

## O(2ⁿ) — Exponential

Often appears in brute-force recursive solutions involving subsets or combinations.

---

# 📊 Complexity Hierarchy

A useful mental model:

```text
Usually more scalable
        ↓
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)
O(n!)
        ↓
Usually less scalable
```

This is a general growth comparison, not a guarantee that one algorithm is always preferable in every situation.

---

# 🔹 01 — Arrays

Arrays store elements in an ordered sequence.

Python's primary array-like structure is:

```python
numbers = [10, 20, 30, 40]
```

Access:

```python
numbers[2]
```

Output:

```text
30
```

### Important Operations

```text
Access
Search
Insert
Delete
Traversal
Update
```

### Common Patterns

* Two pointers
* Sliding window
* Prefix sum
* Kadane's algorithm
* Frequency counting
* In-place modification

### Typical Complexity

| Operation     | Typical Complexity |
| ------------- | -----------------: |
| Index access  |               O(1) |
| Search        |               O(n) |
| Append        |     O(1) amortized |
| Insert middle |               O(n) |
| Delete middle |               O(n) |

---

# 🔹 02 — Searching

Searching means finding a target element in a collection.

Two fundamental approaches:

```text
Linear Search
Binary Search
```

---

## Linear Search

```python
def linear_search(items, target):
    for i, value in enumerate(items):
        if value == target:
            return i

    return -1
```

Complexity:

```text
Time → O(n)
Space → O(1)
```

---

## Binary Search

Binary search requires an appropriate ordered search space, commonly a sorted array.

```python
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid

        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Complexity:

```text
Time → O(log n)
Space → O(1)
```

---

# 🔹 03 — Sorting

Sorting arranges data according to an ordering rule.

Example:

```text
Before:
5 2 8 1 3

After:
1 2 3 5 8
```

Important sorting algorithms:

```text
Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
Heap Sort
Counting Sort
Radix Sort
```

---

## Sorting Complexity

| Algorithm      |       Best |    Average |      Worst |
| -------------- | ---------: | ---------: | ---------: |
| Bubble Sort    |       O(n) |      O(n²) |      O(n²) |
| Selection Sort |      O(n²) |      O(n²) |      O(n²) |
| Insertion Sort |       O(n) |      O(n²) |      O(n²) |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort     | O(n log n) | O(n log n) |      O(n²) |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) |

Actual performance also depends on implementation, input distribution, memory behavior, and constants.

---

# 🔹 04 — Linked List

A linked list consists of nodes connected through references.

```text
10 → 20 → 30 → 40 → None
```

Each node contains:

```text
Data
Next Reference
```

Python:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Types

```text
Singly Linked List
Doubly Linked List
Circular Linked List
```

### Important Algorithms

* Traversal
* Insertion
* Deletion
* Search
* Reverse
* Find middle
* Detect cycle
* Merge sorted lists

### Important Pattern

```text
Slow Pointer + Fast Pointer
```

Useful for:

* Finding middle
* Cycle detection
* Related linked-list problems

---

# 🔹 05 — Stack

A stack follows:

> **LIFO — Last In, First Out**

```text
       TOP
        ↓
      ┌───┐
      │30 │
      ├───┤
      │20 │
      ├───┤
      │10 │
      └───┘
```

Operations:

```text
push
pop
peek
```

Python:

```python
stack = []

stack.append(10)
stack.append(20)

print(stack.pop())
```

Output:

```text
20
```

### Applications

* Function calls
* Recursion
* Undo operations
* Expression evaluation
* Parentheses matching
* DFS
* Backtracking
* Monotonic stack problems

---

# 🔹 06 — Queue

A queue follows:

> **FIFO — First In, First Out**

```text
Front → 10 → 20 → 30 → 40 ← Rear
```

Python:

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

print(queue.popleft())
```

Output:

```text
10
```

### Applications

* BFS
* Scheduling
* Task processing
* Message processing
* Producer-consumer systems
* Sliding-window algorithms

---

# 🔹 07 — Trees

A tree is a hierarchical data structure.

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Important terminology:

```text
Root
Parent
Child
Sibling
Leaf
Depth
Height
Subtree
```

---

## Tree Traversals

### Preorder

```text
Root → Left → Right
```

### Inorder

```text
Left → Root → Right
```

### Postorder

```text
Left → Right → Root
```

### Level Order

```text
Level by Level
```

---

# 🔹 08 — Binary Search Tree

A BST maintains an ordering relationship:

```text
Left < Root < Right
```

Example:

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40  60   80
```

Operations:

```text
Search
Insert
Delete
Minimum
Maximum
Successor
Predecessor
```

A balanced BST can provide approximately logarithmic search, insertion, and deletion behavior.

A highly skewed BST can degrade to linear behavior.

---

# 🔹 09 — Heap

A heap is a specialized tree-based data structure commonly used for priority-based operations.

Two common types:

```text
Min Heap
Max Heap
```

### Min Heap

The smallest element is at the root.

```text
          1
        /   \
       3     5
      / \
     7   9
```

Python:

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print(heapq.heappop(heap))
```

Output:

```text
2
```

### Applications

* Priority queues
* Scheduling
* Top-K problems
* Dijkstra's algorithm
* Heap sort
* Stream processing

---

# 🔹 10 — Hashing

Hashing maps keys to locations using a hash function.

Python provides:

```python
dict
set
```

Example:

```python
frequency = {}

for value in [1, 2, 2, 3, 3, 3]:
    frequency[value] = frequency.get(value, 0) + 1
```

Result:

```text
{
    1: 1,
    2: 2,
    3: 3
}
```

### Typical Average Complexity

| Operation | Average |
| --------- | ------: |
| Search    |    O(1) |
| Insert    |    O(1) |
| Delete    |    O(1) |

Hash tables have important implementation details and worst-case considerations, so these should not be interpreted as unconditional guarantees.

### Applications

* Frequency counting
* Duplicate detection
* Caching
* Fast lookup
* Grouping
* Memoization

---

# 🔹 11 — Graphs

A graph consists of:

```text
Vertices
+
Edges
```

Example:

```text
A ─── B
│     │
│     │
C ─── D
```

---

## Graph Types

```text
Directed
Undirected
Weighted
Unweighted
Cyclic
Acyclic
Connected
Disconnected
```

---

## Graph Representations

### Adjacency List

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

### Adjacency Matrix

A 2D matrix represents connections between vertices.

---

# 🔹 Graph Traversal

Two fundamental traversal algorithms:

```text
BFS
DFS
```

---

## BFS

Uses a queue.

```text
BFS → Queue
```

Applications:

* Shortest path in unweighted graphs
* Level traversal
* Multi-source BFS
* Grid problems

Complexity:

```text
O(V + E)
```

---

## DFS

Uses recursion or a stack.

```text
DFS → Stack / Recursion
```

Applications:

* Connected components
* Cycle detection
* Topological sorting
* Backtracking
* Graph exploration

Complexity:

```text
O(V + E)
```

---

# 🔹 12 — Greedy Algorithms

A greedy algorithm makes the best-looking local choice at each step.

General idea:

```text
Choose current best option
        ↓
Continue
        ↓
Build final solution
```

Examples:

* Activity Selection
* Fractional Knapsack
* Huffman Coding
* Job Sequencing
* Minimum Spanning Tree algorithms
* Interval scheduling

Important:

> A greedy strategy is not automatically correct for every optimization problem.

A greedy algorithm requires a problem structure that justifies the local-choice strategy.

---

# 🔹 13 — Dynamic Programming

Dynamic Programming (DP) solves problems by combining solutions to overlapping subproblems while storing previously computed results.

Two major approaches:

```text
Top-Down
Bottom-Up
```

---

## Top-Down

Uses recursion + memoization.

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = (
        fibonacci(n - 1, memo)
        + fibonacci(n - 2, memo)
    )

    return memo[n]
```

---

## Bottom-Up

Build the solution iteratively.

```python
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

---

## DP Recognition

Ask:

1. Are there overlapping subproblems?
2. Is there optimal substructure?
3. Can a state represent the problem?
4. Can previous results be reused?

Common DP problems:

```text
Fibonacci
Climbing Stairs
0/1 Knapsack
Coin Change
Longest Common Subsequence
Longest Increasing Subsequence
Edit Distance
House Robber
Grid Paths
```

---

# 🔹 14 — Advanced DSA

Advanced DSA combines multiple concepts and techniques.

Potential topics include:

```text
Advanced Graph Algorithms
Union-Find / DSU
Topological Sort
Minimum Spanning Tree
Dijkstra
Bellman-Ford
Floyd-Warshall
Trie
Segment Tree
Fenwick Tree
Advanced Backtracking
Advanced Dynamic Programming
Network Flow
String Algorithms
```

---

# 🔹 Recursion

Recursion is a technique where a function calls itself.

Every recursive solution generally needs:

```text
Base Case
+
Recursive Case
```

Example:

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

Execution:

```text
factorial(4)
    ↓
4 × factorial(3)
    ↓
4 × 3 × factorial(2)
    ↓
4 × 3 × 2 × factorial(1)
```

---

# 🔹 Backtracking

Backtracking explores possible choices and reverses a choice when it does not lead to a valid solution.

General pattern:

```text
Choose
  ↓
Explore
  ↓
Undo
  ↓
Choose another option
```

Used in:

* N-Queens
* Sudoku
* Permutations
* Combinations
* Subsets
* Maze solving
* Constraint satisfaction

Typical template:

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path.copy())
        return

    for choice in choices:
        if not valid(choice):
            continue

        path.append(choice)

        backtrack(path, choices)

        path.pop()
```

---

# 🔹 Important DSA Patterns

Learning patterns is more valuable than memorizing isolated solutions.

---

## 1. Two Pointers

Used when working with arrays or sequences.

```text
Left →          ← Right
```

Common problems:

* Two Sum on sorted array
* Pair problems
* Palindrome
* Container with most water
* Three Sum

---

## 2. Sliding Window

Maintains a dynamic range.

```text
[ L -------- R ]
```

Used for:

* Subarray problems
* Substring problems
* Maximum/minimum windows
* Longest/shortest valid range

---

## 3. Fast and Slow Pointers

Two pointers move at different speeds.

```text
Slow → 1 step
Fast → 2 steps
```

Used for:

* Linked-list middle
* Cycle detection
* Cycle entry problems

---

## 4. Prefix Sum

Precompute cumulative values.

```text
Array:
2  4  1  5

Prefix:
2  6  7  12
```

Useful for range-sum problems.

---

## 5. Hash Map

Use a dictionary for fast lookup.

```python
seen = {}
```

Useful for:

* Two Sum
* Frequency counting
* Duplicate detection
* Grouping
* Prefix-sum problems

---

## 6. Stack

Use when the problem involves:

* Matching
* Nested structures
* Previous/next greater elements
* Undo operations
* Monotonic behavior

---

## 7. Queue

Use when the problem involves:

* FIFO processing
* Levels
* Minimum steps
* BFS
* Multi-source propagation

---

## 8. Heap

Use when you repeatedly need:

```text
Minimum
Maximum
Top K
Priority
```

---

## 9. Binary Search on Answer

Sometimes binary search is performed over a range of possible answers rather than directly over an array.

General structure:

```text
low
high
  ↓
mid
  ↓
Is solution feasible?
  ↓
Adjust range
```

---

## 10. Divide and Conquer

Divide the problem into smaller independent parts.

```text
Problem
   ↓
Divide
 ↙   ↘
A     B
↓     ↓
Solve Solve
 ↘   ↙
Combine
```

Examples:

* Merge Sort
* Quick Sort
* Binary Search

---

# 🔹 Important Graph Algorithms

## BFS

```text
O(V + E)
```

---

## DFS

```text
O(V + E)
```

---

## Topological Sort

Used for directed acyclic graphs.

Applications:

* Dependency resolution
* Course scheduling
* Build systems

---

## Dijkstra's Algorithm

Finds shortest paths from a source in graphs with appropriate non-negative edge weights.

Often implemented with a priority queue.

---

## Bellman-Ford

Supports graphs that may contain negative edge weights and can detect reachable negative cycles.

---

## Floyd-Warshall

Computes all-pairs shortest paths using dynamic programming.

---

## Minimum Spanning Tree

Two classic algorithms:

```text
Kruskal
Prim
```

---

# 🔹 Important Tree Algorithms

Study:

```text
Preorder
Inorder
Postorder
Level Order
Height
Diameter
Lowest Common Ancestor
BST Search
BST Insert
BST Delete
Tree Validation
Serialization
Tree Construction
```

Advanced structures:

```text
AVL Tree
Red-Black Tree
B-Tree
Trie
Segment Tree
Fenwick Tree
```

---

# 🔹 Important Sorting Algorithms

Understand:

```text
Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
Heap Sort
Counting Sort
Radix Sort
Bucket Sort
```

Do not only memorize implementations.

Understand:

```text
Why does it work?
When should it be used?
What is its complexity?
Is it stable?
Is it in-place?
What are its limitations?
```

---

# 🔹 Sorting Properties

Important concepts:

### Stable Sorting

Equal elements maintain their relative ordering.

### In-Place Sorting

Uses limited additional memory for rearrangement.

### Adaptive Sorting

Performance can improve when the input is already partially ordered.

These properties can matter as much as asymptotic complexity in practical applications.

---

# 🔹 Important Problem-Solving Framework

When facing a new DSA problem:

## Step 1 — Understand

Identify:

```text
Input
Output
Constraints
Examples
```

---

## Step 2 — Brute Force

First find a correct straightforward solution.

```text
Correctness
   ↓
Optimization
```

---

## Step 3 — Analyze

Ask:

```text
What is the time complexity?
What is the space complexity?
```

---

## Step 4 — Identify the Pattern

Look for:

```text
Two Pointers
Sliding Window
Hashing
Stack
Queue
Binary Search
DFS
BFS
Heap
Greedy
DP
Backtracking
```

---

## Step 5 — Optimize

Look for ways to reduce:

```text
Nested loops
Repeated calculations
Unnecessary memory
Repeated searches
Duplicate work
```

---

## Step 6 — Test Edge Cases

Always test:

```text
Empty input
One element
Duplicates
Already sorted
Reverse sorted
Negative values
Large values
Boundary conditions
```

---

# 🔹 Brute Force → Optimization

A powerful DSA learning strategy:

```text
Brute Force
     ↓
Analyze Bottleneck
     ↓
Find Repeated Work
     ↓
Choose Better Data Structure
     ↓
Apply Algorithmic Pattern
     ↓
Optimize
```

Example:

```text
Nested loop
    ↓
O(n²)
    ↓
Need fast lookup
    ↓
Hash Set / Hash Map
    ↓
O(n) average approach
```

---

# 🔹 DSA Complexity Cheat Sheet

| Data Structure |       Access |    Search |    Insert |    Delete |
| -------------- | -----------: | --------: | --------: | --------: |
| Array/List     |         O(1) |      O(n) |     O(n)* |     O(n)* |
| Linked List    |         O(n) |      O(n) |    O(1)** |    O(1)** |
| Stack          |     O(1) top |      O(n) |      O(1) |      O(1) |
| Queue          | O(1) ends*** |      O(n) |      O(1) |      O(1) |
| Hash Table     |            — | O(1) avg. | O(1) avg. | O(1) avg. |
| Balanced BST   |     O(log n) |  O(log n) |  O(log n) |  O(log n) |
| Heap           |    O(1) root |      O(n) |  O(log n) |  O(log n) |

`*` Depends on position and implementation.

`**` O(1) when the relevant node/reference is already available.

`***` With an appropriate deque-based implementation.

---

# 🔹 Algorithm Complexity Cheat Sheet

| Algorithm             |    Average / Typical Time |
| --------------------- | ------------------------: |
| Linear Search         |                      O(n) |
| Binary Search         |                  O(log n) |
| Merge Sort            |                O(n log n) |
| Quick Sort            |        O(n log n) average |
| Heap Sort             |                O(n log n) |
| BFS                   |                  O(V + E) |
| DFS                   |                  O(V + E) |
| Dijkstra              | Depends on implementation |
| Floyd-Warshall        |                     O(V³) |
| Binary Tree Traversal |                      O(n) |

---

# 🔹 Interview Preparation

DSA interviews generally test more than coding syntax.

Focus on:

```text
Problem Understanding
       ↓
Approach
       ↓
Data Structure Selection
       ↓
Algorithm
       ↓
Complexity
       ↓
Implementation
       ↓
Testing
```

### Common Interview Topics

```text
Arrays
Strings
Hashing
Linked Lists
Stacks
Queues
Trees
BST
Heap
Graphs
Recursion
Backtracking
Greedy
Dynamic Programming
Binary Search
Sorting
```

---

# 🔹 Frequently Asked Interview Problems

## Arrays

* Two Sum
* Best Time to Buy and Sell Stock
* Maximum Subarray
* Product of Array Except Self
* Rotate Array

## Strings

* Valid Anagram
* Valid Palindrome
* Longest Substring Without Repeating Characters
* Longest Palindromic Substring

## Linked List

* Reverse Linked List
* Detect Cycle
* Merge Two Sorted Lists
* Remove Nth Node From End

## Stack

* Valid Parentheses
* Min Stack
* Daily Temperatures
* Next Greater Element

## Queue / BFS

* Binary Tree Level Order Traversal
* Number of Islands
* Rotting Oranges
* Shortest Path in an Unweighted Grid

## Trees

* Maximum Depth
* Diameter
* Validate BST
* Lowest Common Ancestor
* Serialize and Deserialize

## Heap

* Kth Largest Element
* Top K Frequent Elements
* Merge K Sorted Lists

## Graphs

* Number of Islands
* Clone Graph
* Course Schedule
* Network Connectivity
* Shortest Path

## Dynamic Programming

* Climbing Stairs
* House Robber
* Coin Change
* Longest Common Subsequence
* 0/1 Knapsack

---

# 🔹 Common DSA Mistakes

### ❌ Memorizing Without Understanding

Instead:

```text
Understand → Implement → Analyze → Practice
```

---

### ❌ Ignoring Constraints

Constraints often indicate the required complexity.

For example, a very large `n` may rule out an O(n²) approach.

---

### ❌ Writing Code Immediately

First determine:

```text
What is the pattern?
What data structure fits?
What is the expected complexity?
```

---

### ❌ Ignoring Edge Cases

Always test boundaries.

---

### ❌ Not Explaining Complexity

For every solution, be able to explain:

```text
Time Complexity
Space Complexity
```

---

# 🔹 Recommended Practice Strategy

## Level 1 — Fundamentals

Start with:

```text
Arrays
Searching
Sorting
Linked Lists
Stack
Queue
```

---

## Level 2 — Core Structures

Continue with:

```text
Trees
BST
Heap
Hashing
Graphs
```

---

## Level 3 — Algorithms

Study:

```text
Recursion
Backtracking
Greedy
Dynamic Programming
Graph Algorithms
```

---

## Level 4 — Patterns

Master:

```text
Two Pointers
Sliding Window
Prefix Sum
Fast/Slow Pointers
Binary Search
Monotonic Stack
Monotonic Queue
Heap / Top-K
DFS
BFS
Union-Find
Intervals
Backtracking
DP
```

---

# 🔹 Suggested Practice Progression

```text
Easy
 ↓
Easy + Pattern Recognition
 ↓
Medium
 ↓
Medium + Optimization
 ↓
Hard
 ↓
Mixed Timed Practice
```

Do not rush directly into difficult problems.

The objective is to recognize patterns independently.

---

# 🔹 Recommended Repository Structure

```text
22-DSA-with-Python/
│
├── README.md
│
├── 01-Arrays/
│   ├── README.md
│   └── ...
│
├── 02-Searching/
│   ├── README.md
│   └── ...
│
├── 03-Sorting/
│   ├── README.md
│   └── ...
│
├── 04-Linked-List/
│   ├── README.md
│   └── ...
│
├── 05-Stack/
│   ├── README.md
│   └── ...
│
├── 06-Queue/
│   ├── README.md
│   └── ...
│
├── 07-Trees/
│   ├── README.md
│   └── ...
│
├── 08-Binary-Search-Tree/
│   ├── README.md
│   └── ...
│
├── 09-Heap/
│   ├── README.md
│   └── ...
│
├── 10-Hashing/
│   ├── README.md
│   └── ...
│
├── 11-Graphs/
│   ├── README.md
│   └── ...
│
├── 12-Greedy/
│   ├── README.md
│   └── ...
│
├── 13-Dynamic-Programming/
│   ├── README.md
│   └── ...
│
└── 14-Advanced-DSA/
    ├── README.md
    └── ...
```

---

# 🔹 DSA Mastery Checklist

## Foundations

* [ ] Understand Big-O
* [ ] Understand time complexity
* [ ] Understand space complexity
* [ ] Analyze loops
* [ ] Analyze recursion

## Data Structures

* [ ] Arrays
* [ ] Strings
* [ ] Linked Lists
* [ ] Stack
* [ ] Queue
* [ ] Hash Table
* [ ] Trees
* [ ] BST
* [ ] Heap
* [ ] Graph
* [ ] Trie

## Algorithms

* [ ] Linear Search
* [ ] Binary Search
* [ ] Basic Sorting
* [ ] Merge Sort
* [ ] Quick Sort
* [ ] Heap Sort
* [ ] BFS
* [ ] DFS
* [ ] Topological Sort
* [ ] Shortest Path
* [ ] Minimum Spanning Tree

## Advanced Techniques

* [ ] Recursion
* [ ] Backtracking
* [ ] Two Pointers
* [ ] Sliding Window
* [ ] Prefix Sum
* [ ] Fast/Slow Pointers
* [ ] Monotonic Stack
* [ ] Monotonic Queue
* [ ] Binary Search on Answer
* [ ] Greedy
* [ ] Dynamic Programming
* [ ] Union-Find
* [ ] Divide and Conquer

---

# 🔹 30-Day DSA Study Plan

| Days  | Focus                               |
| ----- | ----------------------------------- |
| 1–2   | Complexity + Arrays                 |
| 3–4   | Searching                           |
| 5–7   | Sorting                             |
| 8–10  | Linked Lists                        |
| 11–12 | Stack                               |
| 13–14 | Queue                               |
| 15–17 | Trees                               |
| 18    | BST                                 |
| 19    | Heap                                |
| 20    | Hashing                             |
| 21–23 | Graphs                              |
| 24    | Recursion                           |
| 25    | Backtracking                        |
| 26    | Greedy                              |
| 27–29 | Dynamic Programming                 |
| 30    | Mixed revision + interview problems |

The schedule can be adjusted depending on prior experience and available study time.

---

# 🔹 DSA Mental Model

When solving a problem, think:

```text
                PROBLEM
                   │
                   ↓
             Understand
                   │
                   ↓
             Identify Input
                   │
                   ↓
             Check Constraints
                   │
                   ↓
            Brute Force Idea
                   │
                   ↓
          Find Bottleneck
                   │
                   ↓
       Choose Data Structure
                   │
                   ↓
        Identify DSA Pattern
                   │
                   ↓
             Optimize
                   │
                   ↓
             Implement
                   │
                   ↓
             Test Cases
                   │
                   ↓
          Analyze Complexity
```

---

# 🔹 Golden Rules of DSA

### Rule 1

> First make the solution correct, then make it efficient.

### Rule 2

> Always understand the constraints before choosing an algorithm.

### Rule 3

> Choose the data structure based on the operations you need.

### Rule 4

> Learn patterns instead of memorizing hundreds of solutions.

### Rule 5

> Always analyze time and space complexity.

### Rule 6

> Practice explaining your solution, not just coding it.

---

# 🔹 From Beginner to Advanced

```text
                    DSA
                     │
             ┌───────┴───────┐
             │               │
       Data Structures    Algorithms
             │               │
        ┌────┴────┐      ┌───┴────┐
        │         │      │        │
      Linear   Nonlinear Search   Sort
        │         │
   Arrays       Trees
   Stack        Graphs
   Queue        Heap
   Linked List  Hashing
        │         │
        └────┬────┘
             ↓
          Patterns
             ↓
       Problem Solving
             ↓
      Advanced Algorithms
             ↓
       Interview Mastery
```

---

# 🚀 Final Goal

The ultimate objective of studying DSA is not to memorize algorithms.

It is to develop the ability to look at a new problem and ask:

```text
What do I know?
       ↓
What is the constraint?
       ↓
What data structure fits?
       ↓
What pattern applies?
       ↓
What is the simplest correct solution?
       ↓
Can I optimize it?
       ↓
What are the time and space complexities?
```

When these questions become automatic, you are developing genuine algorithmic problem-solving skills.

---

# 📖 References

* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)
* [Python collections Documentation](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com)
* [Python heapq Documentation](https://docs.python.org/3/library/heapq.html?utm_source=chatgpt.com)

---

# 🏆 DSA Completion Checklist

```text
┌─────────────────────────────────────────────┐
│          PYTHON DSA MASTER CHECKLIST        │
├─────────────────────────────────────────────┤
│                                             │
│  ☐ Complexity Analysis                      │
│  ☐ Arrays                                   │
│  ☐ Searching                                │
│  ☐ Sorting                                  │
│  ☐ Linked Lists                             │
│  ☐ Stack                                    │
│  ☐ Queue                                    │
│  ☐ Trees                                    │
│  ☐ Binary Search Tree                       │
│  ☐ Heap                                     │
│  ☐ Hashing                                  │
│  ☐ Graphs                                   │
│  ☐ Recursion                                │
│  ☐ Backtracking                             │
│  ☐ Greedy Algorithms                        │
│  ☐ Dynamic Programming                      │
│  ☐ Two Pointers                             │
│  ☐ Sliding Window                           │
│  ☐ Prefix Sum                               │
│  ☐ Fast/Slow Pointers                       │
│  ☐ Binary Search Patterns                   │
│  ☐ Monotonic Stack                          │
│  ☐ Monotonic Queue                          │
│  ☐ BFS                                      │
│  ☐ DFS                                      │
│  ☐ Shortest Path                            │
│  ☐ Topological Sort                         │
│  ☐ Union-Find                               │
│  ☐ Advanced DSA                             │
│                                             │
└─────────────────────────────────────────────┘
```

---

# 🔗 DSA Roadmap

```text
22-DSA-with-Python
│
├── 01-Arrays
│
├── 02-Searching
│
├── 03-Sorting
│
├── 04-Linked-List
│
├── 05-Stack
│
├── 06-Queue
│
├── 07-Trees
│
├── 08-Binary-Search-Tree
│
├── 09-Heap
│
├── 10-Hashing
│
├── 11-Graphs
│
├── 12-Greedy
│
├── 13-Dynamic-Programming
│
└── 14-Advanced-DSA
```

### ⭐ Recommended Learning Order

**Complexity → Arrays → Searching → Sorting → Linked Lists → Stack → Queue → Trees → BST → Heap → Hashing → Graphs → Recursion → Backtracking → Greedy → Dynamic Programming → Advanced DSA**

---

## 💡 Keep Building. Keep Solving. Keep Optimizing.

> **Understand the problem. Choose the right data structure. Apply the right algorithm. Analyze the complexity. Write clean code.**

**Happy Coding & Problem Solving! 🚀🐍**
