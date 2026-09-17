# 06 — Queue in Python

> A comprehensive guide to **Queue Data Structure**, its implementations, operations, complexity, patterns, applications, and interview problems using Python.

---

## 📌 Overview

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

The element that is inserted first is the element that is removed first.

A real-world example is a queue at a ticket counter:

```text
First Person → Second Person → Third Person → Fourth Person
     ↓
  Served First
```

In programming, queues are commonly used in:

* CPU scheduling
* Printer scheduling
* Task processing
* Breadth-First Search (BFS)
* Message queues
* Network request handling
* Operating systems
* Producer-consumer systems
* Graph traversal
* Event-driven applications

---

# 📚 Table of Contents

* [What is a Queue?](#-what-is-a-queue)
* [FIFO Principle](#-fifo-principle)
* [Queue Terminology](#-queue-terminology)
* [Basic Queue Operations](#-basic-queue-operations)
* [Queue Visualization](#-queue-visualization)
* [Queue Using Python List](#-queue-using-python-list)
* [Why List Can Be Inefficient](#-why-list-can-be-inefficient)
* [Queue Using deque](#-queue-using-deque)
* [Queue Class Implementation](#-queue-class-implementation)
* [Queue Using Linked List](#-queue-using-linked-list)
* [Circular Queue](#-circular-queue)
* [Priority Queue](#-priority-queue)
* [Deque](#-deque)
* [Queue Complexity](#-queue-complexity)
* [Queue vs Stack](#-queue-vs-stack)
* [Queue Applications](#-queue-applications)
* [BFS Using Queue](#-bfs-using-queue)
* [Sliding Window](#-sliding-window)
* [Monotonic Queue](#-monotonic-queue)
* [Producer-Consumer Pattern](#-producer-consumer-pattern)
* [Common Queue Problems](#-common-queue-problems)
* [Practice Problems](#-practice-problems)
* [Interview Questions](#-interview-questions)
* [Common Mistakes](#-common-mistakes)
* [Quick Revision](#-quick-revision)
* [Complexity Cheat Sheet](#-complexity-cheat-sheet)
* [Problem-Solving Strategy](#-problem-solving-strategy)
* [Mastery Checklist](#-mastery-checklist)
* [Recommended Folder Structure](#-recommended-folder-structure)
* [References](#-references)
* [Learning Roadmap](#-learning-roadmap)

---

# 🔹 What is a Queue?

A **Queue** is a linear data structure in which:

* Elements are inserted from one end.
* Elements are removed from the opposite end.
* The insertion end is called the **Rear**.
* The removal end is called the **Front**.

### Example

```text
Front                         Rear
  ↓                             ↓
┌────┬────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└────┴────┴────┴────┴────┘
  ↑                             ↑
Remove                         Insert
```

If we perform:

```text
dequeue()
```

`10` will be removed.

If we perform:

```text
enqueue(60)
```

the queue becomes:

```text
10 → 20 → 30 → 40 → 50 → 60
```

---

# 🔹 FIFO Principle

Queue follows:

> **FIFO — First In, First Out**

Suppose we insert:

```text
10
20
30
40
```

The removal order will be:

```text
10 → 20 → 30 → 40
```

### Real-World Examples

| Example          | Queue Behavior                        |
| ---------------- | ------------------------------------- |
| Ticket counter   | First customer served first           |
| Printer          | First print request processed first   |
| CPU scheduling   | Tasks wait for execution              |
| Customer support | Requests handled in order             |
| Network packets  | Packets may be processed sequentially |
| BFS              | Nodes are explored level by level     |

---

# 🔹 Queue Terminology

## 1. Enqueue

Adding an element to the queue.

```text
enqueue(10)
```

---

## 2. Dequeue

Removing an element from the front.

```text
dequeue()
```

---

## 3. Front

The element that will be removed next.

```text
Front → 10
```

---

## 4. Rear

The position where a new element is inserted.

```text
Rear → 50
```

---

## 5. Peek

View the front element without removing it.

```text
peek()
```

---

## 6. Is Empty

Checks whether the queue contains no elements.

```text
is_empty()
```

---

## 7. Size

Returns the number of elements.

```text
size()
```

---

# 🔹 Basic Queue Operations

A queue typically supports:

| Operation    | Description        |
| ------------ | ------------------ |
| `enqueue()`  | Insert element     |
| `dequeue()`  | Remove element     |
| `peek()`     | View front         |
| `is_empty()` | Check empty        |
| `size()`     | Number of elements |

---

# 🔹 Queue Visualization

Consider:

```text
enqueue(10)
```

```text
┌────┐
│ 10 │
└────┘
```

Then:

```text
enqueue(20)
```

```text
┌────┬────┐
│ 10 │ 20 │
└────┴────┘
```

Then:

```text
enqueue(30)
```

```text
┌────┬────┬────┐
│ 10 │ 20 │ 30 │
└────┴────┴────┘
```

Now:

```text
dequeue()
```

removes `10`.

```text
┌────┬────┐
│ 20 │ 30 │
└────┴────┘
```

---

# 🔹 Queue Using Python List

A simple queue can be implemented using a Python list.

```python
queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)
```

Output:

```text
[10, 20, 30]
```

To remove the first element:

```python
value = queue.pop(0)

print(value)
```

Output:

```text
10
```

---

# ⚠️ Why List Can Be Inefficient

Although this works:

```python
queue.pop(0)
```

it is not efficient for large queues.

Removing the first element requires shifting the remaining elements.

```text
Before:

10  20  30  40  50
↑

After removing 10:

20  30  40  50
```

Therefore:

```text
pop(0) → O(n)
```

For queue-heavy applications, this can become expensive.

---

# 🔹 Queue Using `deque`

Python provides an efficient queue implementation through:

```python
from collections import deque
```

Example:

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)
```

Output:

```text
deque([10, 20, 30])
```

Remove from the front:

```python
value = queue.popleft()

print(value)
```

Output:

```text
10
```

Add to the rear:

```python
queue.append(40)
```

---

# 🔹 Recommended Queue Implementation

For a normal FIFO queue, prefer:

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue.popleft())
```

This provides efficient insertion and removal from opposite ends.

---

# 🔹 Queue Class Implementation

A clean object-oriented implementation:

```python
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Usage

```python
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek())
print(q.dequeue())
print(q.size())
```

Output:

```text
10
10
2
```

---

# 🔹 Queue Using Linked List

A queue can also be implemented using a linked list.

We maintain:

```text
Front
  ↓
10 → 20 → 30 → None
                    ↑
                   Rear
```

### Node

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Queue

```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty")

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value
```

### Complexity

With both `front` and `rear` pointers:

```text
enqueue → O(1)
dequeue → O(1)
```

---

# 🔹 Circular Queue

A **Circular Queue** connects the last position back to the first position.

```text
       ┌─────────────────────┐
       ↓                     │
     [ 0 ] → [ 1 ] → [ 2 ] → [ 3 ]
       ↑                     │
       └─────────────────────┘
```

This allows previously unused positions to be reused.

### Why Circular Queue?

In a normal fixed-size queue, removing elements from the front can leave unused spaces.

Example:

```text
[ ][ ][30][40][50]
```

A circular queue can reuse those empty positions.

---

## Circular Queue Implementation

```python
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise OverflowError("Queue is full")

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return value
```

The `%` operator allows the indexes to wrap around.

---

# 🔹 Priority Queue

A **Priority Queue** removes elements based on priority rather than simple FIFO order.

For example:

```text
Task A → Priority 3
Task B → Priority 1
Task C → Priority 2
```

The highest-priority task may be processed first.

Python provides:

```python
import heapq
```

Example:

```python
import heapq

queue = []

heapq.heappush(queue, (2, "Task B"))
heapq.heappush(queue, (1, "Task A"))
heapq.heappush(queue, (3, "Task C"))

print(heapq.heappop(queue))
```

Output:

```text
(1, 'Task A')
```

Priority queues are commonly implemented using **heaps**.

---

# 🔹 Deque

A **Deque** means:

> Double-Ended Queue

Elements can be inserted and removed from both ends.

```text
Front                         Rear
  ↓                             ↓
┌────┬────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└────┴────┴────┴────┴────┘
  ↑                             ↑
Insert/Remove              Insert/Remove
```

Python:

```python
from collections import deque

dq = deque()

dq.append(10)
dq.append(20)

dq.appendleft(5)

print(dq)
```

Output:

```text
deque([5, 10, 20])
```

Remove from either side:

```python
dq.pop()
dq.popleft()
```

---

# 🔹 Queue Complexity

For a `deque`:

| Operation   | Complexity |
| ----------- | ---------: |
| Enqueue     |       O(1) |
| Dequeue     |       O(1) |
| Peek        |       O(1) |
| Check empty |       O(1) |
| Size        |       O(1) |

For a Python list used with `pop(0)`:

| Operation  |     Complexity |
| ---------- | -------------: |
| Append     | O(1) amortized |
| `pop(0)`   |           O(n) |
| Peek first |           O(1) |

Therefore:

> Use `deque` instead of repeatedly calling `list.pop(0)` for queue operations.

---

# 🔹 Queue vs Stack

| Feature               | Queue        | Stack            |
| --------------------- | ------------ | ---------------- |
| Principle             | FIFO         | LIFO             |
| Insert                | Rear         | Top              |
| Remove                | Front        | Top              |
| Example               | Waiting line | Stack of plates  |
| Main Python structure | `deque`      | `list` / `deque` |
| Common algorithm      | BFS          | DFS              |

### Queue

```text
10 → 20 → 30

Remove → 10
```

### Stack

```text
10
20
30 ← Top

Remove → 30
```

---

# 🔹 Queue Applications

Queues are fundamental in many areas of computer science.

## 1. CPU Scheduling

Operating systems can maintain processes waiting for execution.

```text
Process 1
Process 2
Process 3
Process 4
```

---

## 2. Printer Scheduling

Print jobs can wait in a queue:

```text
Document A
Document B
Document C
```

---

## 3. Breadth-First Search

BFS uses a queue to process nodes level by level.

---

## 4. Network Requests

Servers may queue incoming requests.

```text
Request → Queue → Worker → Response
```

---

## 5. Message Processing

Applications often use queues to temporarily store messages.

```text
Producer
   ↓
 Queue
   ↓
Consumer
```

---

## 6. Task Scheduling

Background tasks can be processed in order.

---

# 🔹 BFS Using Queue

One of the most important applications of a queue is **Breadth-First Search**.

BFS explores a graph or tree level by level.

Consider:

```text
        A
       / \
      B   C
     / \
    D   E
```

BFS order:

```text
A → B → C → D → E
```

### Python Implementation

```python
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()

        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

Example:

```python
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

bfs(graph, "A")
```

Output:

```text
A B C D E
```

### Why Queue?

The queue guarantees that nodes discovered earlier are processed before nodes discovered later.

This produces the level-by-level behavior of BFS.

---

# 🔹 BFS and Shortest Path

In an **unweighted graph**, BFS can be used to find the shortest number of edges from a starting node.

Example:

```text
A ─ B ─ D
│
C ─ E
```

Starting from `A`, BFS explores:

```text
Level 0 → A
Level 1 → B, C
Level 2 → D, E
```

The first time BFS reaches a node, it has found a shortest path in terms of edge count.

---

# 🔹 Queue for Level Order Traversal

Queues are also used for binary tree level-order traversal.

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Level order:

```text
1 → 2 → 3 → 4 → 5 → 6 → 7
```

Implementation:

```python
from collections import deque


def level_order(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result
```

---

# 🔹 Sliding Window

Queues and deques are extremely useful for **sliding window problems**.

Example:

```text
Array:
[1, 3, -1, -3, 5, 3, 6, 7]

Window size = 3
```

Windows:

```text
[1, 3, -1]
[3, -1, -3]
[-1, -3, 5]
[-3, 5, 3]
...
```

A deque can maintain candidates efficiently.

This leads to the classic:

> **Sliding Window Maximum**

problem.

---

# 🔹 Monotonic Queue

A **Monotonic Queue** maintains elements in increasing or decreasing order.

It is useful for:

* Sliding window maximum
* Sliding window minimum
* Range queries
* Optimization problems

Example decreasing deque:

```text
10 → 8 → 5 → 2
```

When a new larger value arrives, smaller values at the back may be removed because they can no longer become the maximum.

This technique can reduce certain sliding-window problems from:

```text
O(nk)
```

to:

```text
O(n)
```

---

# 🔹 Producer-Consumer Pattern

Queues are commonly used between producers and consumers.

```text
Producer
   │
   ▼
┌─────────┐
│  Queue  │
└─────────┘
   │
   ▼
Consumer
```

The producer adds tasks:

```python
queue.put(task)
```

The consumer processes them:

```python
task = queue.get()
```

For thread-safe communication, Python provides:

```python
from queue import Queue
```

Example:

```python
from queue import Queue

q = Queue()

q.put("Task 1")
q.put("Task 2")

print(q.get())
```

---

# 🔹 Queue Problems

Important queue-based problems include:

### Beginner

1. Implement Queue
2. Implement Queue using Stack
3. Reverse a Queue
4. Generate Binary Numbers
5. First Non-Repeating Character
6. Implement Circular Queue

### Intermediate

1. Level Order Traversal
2. BFS Traversal
3. First Negative Number in Every Window
4. Sliding Window Maximum
5. Rotten Oranges
6. Number of Islands
7. Shortest Path in an Unweighted Graph

### Advanced

1. Design a Circular Deque
2. Sliding Window Maximum
3. Constrained Subsequence Sum
4. Shortest Path Problems
5. Multi-source BFS
6. Monotonic Queue Problems
7. Task Scheduling Problems

---

# 🔹 Important Queue Patterns

## Pattern 1 — Simple FIFO

Use when elements must be processed in insertion order.

```python
from collections import deque

q = deque()

q.append(value)
q.popleft()
```

---

## Pattern 2 — BFS

```python
queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

---

## Pattern 3 — Level Processing

Useful when a problem asks:

* minimum number of steps
* level by level
* distance
* number of minutes
* nearest position

---

## Pattern 4 — Multi-Source BFS

Instead of starting BFS from one node, initialize the queue with multiple starting nodes.

```python
queue = deque(all_sources)
```

This is useful for:

* Rotten Oranges
* Distance from nearest source
* Grid propagation
* Infection/spread simulations

---

## Pattern 5 — Monotonic Deque

Useful for:

* Window maximum
* Window minimum
* Range optimization

---

# 🔹 Common Queue Mistakes

### ❌ Mistake 1 — Using `pop(0)` repeatedly

```python
queue.pop(0)
```

This can lead to O(n) removals.

### ✅ Better

```python
from collections import deque

queue.popleft()
```

---

### ❌ Mistake 2 — Forgetting Empty Queue Handling

```python
queue.popleft()
```

without checking whether the queue is empty can raise an exception.

### Better

```python
if queue:
    queue.popleft()
```

---

### ❌ Mistake 3 — Incorrect BFS Visited Handling

Marking nodes too late can result in duplicate additions.

Prefer:

```python
if neighbor not in visited:
    visited.add(neighbor)
    queue.append(neighbor)
```

---

### ❌ Mistake 4 — Confusing Queue and Stack

Remember:

```text
Queue → FIFO
Stack → LIFO
```

---

# 🔹 Practice Problems

## 🟢 Beginner

### Problem 1 — Implement Queue

Implement:

```text
enqueue()
dequeue()
peek()
is_empty()
size()
```

---

### Problem 2 — Reverse a Queue

Input:

```text
10 20 30 40
```

Output:

```text
40 30 20 10
```

---

### Problem 3 — Queue Using Two Stacks

Implement a queue using two stacks.

---

### Problem 4 — Generate Binary Numbers

Generate the first `n` binary numbers using a queue.

For:

```text
n = 5
```

Expected:

```text
1
10
11
100
101
```

---

# 🟡 Intermediate

### Problem 5 — First Non-Repeating Character

Given a stream of characters, determine the first character that has not repeated.

---

### Problem 6 — Rotten Oranges

Given a grid containing:

```text
0 → Empty
1 → Fresh Orange
2 → Rotten Orange
```

Each minute, rotten oranges infect adjacent fresh oranges.

Find the minimum time required to rot all oranges.

This is a classic **multi-source BFS** problem.

---

### Problem 7 — Binary Tree Level Order Traversal

Return nodes level by level.

---

# 🔴 Advanced

### Problem 8 — Sliding Window Maximum

Given:

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

Find the maximum value of every window.

Expected:

```text
[3,3,5,5,6,7]
```

---

### Problem 9 — Shortest Path

Given an unweighted graph, find the shortest path between two nodes.

Use:

```text
BFS + Queue
```

---

### Problem 10 — Design Circular Queue

Implement:

```text
enqueue
dequeue
front
rear
isEmpty
isFull
```

using a fixed-size array.

---

# 🔹 Interview Questions

### Basic

1. What is a queue?
2. What is FIFO?
3. What are enqueue and dequeue?
4. What is the difference between front and rear?
5. How do you implement a queue in Python?
6. Why is `deque` preferred over `list.pop(0)`?
7. What is queue overflow?
8. What is queue underflow?
9. What is a circular queue?
10. What is a deque?

### Intermediate

11. How can a queue be implemented using two stacks?
12. How can a stack be implemented using two queues?
13. Why does BFS use a queue?
14. How is BFS related to shortest paths?
15. What is a priority queue?
16. What is a monotonic queue?
17. What is multi-source BFS?
18. What is the difference between `deque` and `queue.Queue`?
19. When should a linked-list queue be used?
20. What are the applications of queues?

### Advanced

21. How does a circular queue reuse memory?
22. How does a monotonic deque solve sliding-window maximum?
23. How can BFS find the shortest path in an unweighted graph?
24. What is the producer-consumer pattern?
25. How would you design a thread-safe queue?
26. What is the complexity of BFS?
27. How does multi-source BFS work?
28. How would you implement a queue with O(1) enqueue and dequeue?
29. What is the difference between a normal queue, circular queue, priority queue, and deque?
30. How can queues be used to solve grid-based problems?

---

# 🔹 Quick Revision

```text
Queue
│
├── FIFO
│
├── Enqueue
│     └── Insert at rear
│
├── Dequeue
│     └── Remove from front
│
├── Peek
│     └── View front
│
├── Implementations
│     ├── List
│     ├── Deque
│     └── Linked List
│
├── Variants
│     ├── Circular Queue
│     ├── Priority Queue
│     └── Deque
│
└── Applications
      ├── BFS
      ├── Scheduling
      ├── Task Processing
      ├── Producer-Consumer
      └── Sliding Window
```

---

# 🔹 Complexity Cheat Sheet

| Structure         |  Enqueue |  Dequeue | Peek |
| ----------------- | -------: | -------: | ---: |
| Python List       |    O(1)* |     O(n) | O(1) |
| `deque`           |     O(1) |     O(1) | O(1) |
| Linked List Queue |     O(1) |     O(1) | O(1) |
| Priority Queue    | O(log n) | O(log n) | O(1) |

`*` Append is amortized O(1).

---

# 🔹 BFS Complexity

For a graph with:

```text
V = Vertices
E = Edges
```

BFS complexity:

```text
Time  → O(V + E)
Space → O(V)
```

The queue may contain up to O(V) vertices.

---

# 🔹 Problem-Solving Strategy

When you see a DSA problem, ask:

### Step 1 — Is the order FIFO?

If yes:

```text
Think Queue
```

### Step 2 — Does the problem involve levels?

Examples:

```text
level 1
level 2
level 3
```

Think:

```text
BFS + Queue
```

### Step 3 — Does it ask for minimum steps?

For an unweighted graph/grid:

```text
BFS
```

is often a strong candidate.

### Step 4 — Are there multiple starting points?

Consider:

```text
Multi-source BFS
```

### Step 5 — Is it a sliding-window maximum/minimum?

Consider:

```text
Monotonic Deque
```

---

# 🔹 Best Practices

### ✅ Prefer `deque`

```python
from collections import deque
```

### ✅ Use meaningful method names

```python
enqueue()
dequeue()
peek()
```

### ✅ Handle empty queues

Avoid blindly removing elements.

### ✅ Understand complexity

Do not only memorize implementation.

Understand why:

```text
deque.popleft() → O(1)
list.pop(0)    → O(n)
```

### ✅ Learn BFS thoroughly

Queue and BFS are strongly connected in DSA.

### ✅ Practice patterns

Focus on:

```text
FIFO
BFS
Level Order
Multi-source BFS
Sliding Window
Monotonic Queue
```

---

# 🔹 Mastery Checklist

### Fundamentals

* [ ] Understand FIFO
* [ ] Understand enqueue
* [ ] Understand dequeue
* [ ] Understand front and rear
* [ ] Understand peek
* [ ] Understand queue overflow/underflow

### Implementation

* [ ] Implement queue using list
* [ ] Implement queue using `deque`
* [ ] Implement queue using linked list
* [ ] Implement circular queue
* [ ] Implement deque
* [ ] Understand priority queue

### Algorithms

* [ ] BFS
* [ ] Level-order traversal
* [ ] Multi-source BFS
* [ ] Shortest path using BFS
* [ ] Sliding-window maximum
* [ ] Monotonic queue

### Problem Solving

* [ ] Reverse a queue
* [ ] Queue using two stacks
* [ ] Stack using two queues
* [ ] Rotten Oranges
* [ ] Number of Islands
* [ ] Binary Tree Level Order Traversal
* [ ] Sliding Window Maximum

---

# 🔹 Recommended Folder Structure

```text
22-DSA-with-Python/
│
├── 01-Arrays/
│   └── README.md
│
├── 02-Searching/
│   └── README.md
│
├── 03-Sorting/
│   └── README.md
│
├── 04-Linked-List/
│   └── README.md
│
├── 05-Stack/
│   └── README.md
│
└── 06-Queue/
    ├── README.md
    ├── queue.py
    ├── circular_queue.py
    ├── priority_queue.py
    ├── deque_examples.py
    ├── bfs.py
    ├── level_order.py
    ├── sliding_window.py
    └── practice/
        ├── reverse_queue.py
        ├── queue_using_stacks.py
        ├── rotten_oranges.py
        └── sliding_window_maximum.py
```

---

# 🔹 Suggested Learning Progression

```text
Queue Fundamentals
       ↓
Queue Operations
       ↓
Python deque
       ↓
Linked List Queue
       ↓
Circular Queue
       ↓
Priority Queue
       ↓
Deque
       ↓
BFS
       ↓
Level Order Traversal
       ↓
Multi-Source BFS
       ↓
Sliding Window
       ↓
Monotonic Queue
       ↓
Advanced DSA Problems
```

---

# 🔹 Key Takeaways

> **Queue = FIFO**

Remember:

```text
Insert → Rear
Remove → Front
```

For Python:

```python
from collections import deque
```

Use:

```python
queue.append(value)
queue.popleft()
```

For graphs:

```text
BFS → Queue
```

For shortest paths in unweighted graphs:

```text
BFS → Queue
```

For level-order traversal:

```text
BFS → Queue
```

For sliding-window maximum:

```text
Deque → Monotonic Queue
```

The most important idea is not simply learning the queue implementation. It is recognizing **when a queue-based pattern is the right tool for a problem**.

---

# 🔹 References

* [Python Documentation — collections.deque](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com#collections.deque)
* [Python Documentation — queue Module](https://docs.python.org/3/library/queue.html?utm_source=chatgpt.com)
* [Python Documentation — heapq](https://docs.python.org/3/library/heapq.html?utm_source=chatgpt.com)

---

# 🚀 DSA Roadmap

```text
22-DSA-with-Python
│
├── 01-Arrays
├── 02-Searching
├── 03-Sorting
├── 04-Linked-List
├── 05-Stack
├── 06-Queue
├── 07-Trees
├── 08-Binary-Search-Tree
├── 09-Heap
├── 10-Hashing
├── 11-Graphs
├── 12-Greedy
├── 13-Dynamic-Programming
└── 14-Advanced-DSA
```

### ⏭️ Next Topic

**07 — Trees**

After mastering queues, the next major step is understanding **Trees, Binary Trees, Tree Traversals, Binary Search Trees, and recursive tree algorithms**.
