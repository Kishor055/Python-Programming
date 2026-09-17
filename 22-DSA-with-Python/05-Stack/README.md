# 📚 Stack in Python

> **Data Structures & Algorithms — Stack**

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

The element inserted **last** is the element removed **first**.

A simple example is a stack of plates:

```text
        ┌─────────┐
        │  Plate  │  ← Last In → First Out
        ├─────────┤
        │  Plate  │
        ├─────────┤
        │  Plate  │
        ├─────────┤
        │  Plate  │
        └─────────┘
             ↑
            TOP
```

If we push:

```text
10 → 20 → 30 → 40
```

then `40` is removed first.

```text
POP → 40
POP → 30
POP → 20
POP → 10
```

Stacks are one of the most important data structures for understanding:

* Function calls
* Recursion
* Expression evaluation
* Parentheses matching
* Undo/Redo systems
* Backtracking
* Depth-First Search
* Monotonic stack problems
* Memory management concepts

---

# 📚 Table of Contents

* [What is a Stack?](#-what-is-a-stack)
* [LIFO Principle](#-lifo-principle)
* [Stack Terminology](#-stack-terminology)
* [Stack Operations](#-stack-operations)
* [Stack Implementation Using Python List](#-stack-implementation-using-python-list)
* [Stack Class](#-implementing-a-stack-class)
* [Stack Using Linked List](#-stack-using-linked-list)
* [Stack Using `deque`](#-stack-using-deque)
* [Time Complexity](#-time-complexity)
* [Overflow and Underflow](#-overflow-and-underflow)
* [Applications of Stack](#-applications-of-stack)
* [Balanced Parentheses](#-balanced-parentheses)
* [Reverse a String](#-reverse-a-string)
* [Expression Evaluation](#-expression-evaluation)
* [Infix, Prefix and Postfix](#-infix-prefix-and-postfix)
* [Infix to Postfix](#-infix-to-postfix)
* [Postfix Evaluation](#-postfix-expression-evaluation)
* [Recursion and Call Stack](#-recursion-and-call-stack)
* [Backtracking](#-backtracking)
* [Depth-First Search](#-depth-first-search)
* [Monotonic Stack](#-monotonic-stack)
* [Next Greater Element](#-next-greater-element)
* [Min Stack](#-min-stack)
* [Stack vs Queue](#-stack-vs-queue)
* [Stack vs Array](#-stack-vs-array)
* [Common Mistakes](#-common-mistakes)
* [Practice Problems](#-practice-problems)
* [Interview Questions](#-interview-questions)
* [Quick Revision](#-quick-revision)
* [Mastery Checklist](#-mastery-checklist)
* [References](#-references)
* [Next Topic](#-next-topic)

---

# 🧠 What is a Stack?

A Stack is an abstract data type in which insertion and deletion occur at the same end, called the **top**.

Consider:

```text
Stack

      TOP
       ↓
    ┌─────┐
    │ 40  │
    ├─────┤
    │ 30  │
    ├─────┤
    │ 20  │
    ├─────┤
    │ 10  │
    └─────┘
```

The only accessible end is the top.

Therefore:

```text
PUSH → add to TOP
POP  → remove from TOP
PEEK → view TOP
```

---

# 🔄 LIFO Principle

LIFO means:

> **Last In, First Out**

Suppose we perform:

```text
PUSH(10)
PUSH(20)
PUSH(30)
```

The stack becomes:

```text
TOP
 ↓
30
20
10
```

Now:

```text
POP()
```

returns:

```text
30
```

Another `POP()` returns:

```text
20
```

Therefore:

```text
Insertion order:
10 → 20 → 30

Removal order:
30 → 20 → 10
```

---

# 📖 Stack Terminology

## Push

Adds an element to the top.

```text
PUSH(50)
```

## Pop

Removes and returns the top element.

```text
POP()
```

## Peek / Top

Returns the top element without removing it.

```text
PEEK()
```

## Is Empty

Checks whether the stack contains no elements.

```text
is_empty()
```

## Size

Returns the number of elements.

```text
size()
```

---

# ⚙️ Stack Operations

The fundamental stack operations are:

| Operation | Description                  |
| --------- | ---------------------------- |
| Push      | Add an element               |
| Pop       | Remove top element           |
| Peek      | View top element             |
| Is Empty  | Check whether stack is empty |
| Size      | Number of elements           |

A properly implemented stack provides:

```text
Push → O(1)
Pop  → O(1)
Peek → O(1)
```

---

# 🐍 Stack Using Python List

Python's `list` can naturally implement a stack.

Use:

```python
append()
```

for Push and:

```python
pop()
```

for Pop.

### Example

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
```

Output:

```text
[10, 20, 30]
```

The top is:

```text
30
```

Pop:

```python
value = stack.pop()

print(value)
```

Output:

```text
30
```

Stack becomes:

```text
[10, 20]
```

---

# 👀 Peek Operation

Use:

```python
stack[-1]
```

Example:

```python
stack = [10, 20, 30]

print(stack[-1])
```

Output:

```text
30
```

Unlike `pop()`, the element is not removed.

---

# ❌ Checking Empty Stack

Never attempt:

```python
stack.pop()
```

without considering whether the stack is empty.

Use:

```python
if stack:
    print(stack.pop())
```

or:

```python
if not stack:
    print("Stack is empty")
```

---

# 🏗️ Implementing a Stack Class

A clean object-oriented implementation:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Usage

```python
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
print(stack.pop())
print(stack.size())
```

Output:

```text
30
30
2
```

---

# 🔗 Stack Using Linked List

A stack can also be implemented using a linked list.

The head of the linked list acts as the top.

```text
TOP
 ↓
[30] → [20] → [10] → None
```

### Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("Pop from empty stack")

        value = self.top.data
        self.top = self.top.next

        return value

    def peek(self):
        if self.top is None:
            raise IndexError("Peek from empty stack")

        return self.top.data
```

### Complexity

```text
Push → O(1)
Pop  → O(1)
Peek → O(1)
```

---

# 🧰 Stack Using `deque`

Python's `collections.deque` can also be used when you need efficient operations at the ends.

```python
from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
```

Output:

```text
30
```

For a normal Python application, `list` is often the simplest choice for stack behavior.

---

# ⏱️ Time Complexity

| Operation | List Stack | Linked List Stack |
| --------- | ---------: | ----------------: |
| Push      |      O(1)* |              O(1) |
| Pop       |       O(1) |              O(1) |
| Peek      |       O(1) |              O(1) |
| Is Empty  |       O(1) |              O(1) |
| Size      |       O(1) |            O(1)** |

`*` Python list append is amortized `O(1)`.

`**` If size is maintained; otherwise traversal would take `O(n)`.

---

# 🚨 Overflow and Underflow

## Stack Underflow

Occurs when attempting to remove an element from an empty stack.

```text
POP()
 ↓
Empty Stack
 ↓
Underflow
```

Example:

```python
stack = []

stack.pop()
```

This raises:

```text
IndexError
```

---

## Stack Overflow

In a fixed-capacity stack, overflow occurs when attempting to push onto a full stack.

Example:

```text
Capacity = 3

[30]
[20]
[10]

PUSH(40)
 ↓
Overflow
```

Python's dynamic list normally grows as needed, so fixed-capacity overflow is not the normal behavior of a list-based stack.

---

# 🌍 Applications of Stack

Stacks appear in many areas of computer science.

### Major applications

```text
Stack
│
├── Function Calls
├── Recursion
├── Expression Evaluation
├── Parentheses Matching
├── Undo / Redo
├── Browser History
├── Backtracking
├── DFS
├── Syntax Parsing
├── Compiler Design
└── Monotonic Stack Algorithms
```

---

# 🧩 Balanced Parentheses

One of the most common stack problems is checking whether brackets are balanced.

Example:

```text
({[]})
```

is balanced.

But:

```text
([)]
```

is not balanced.

### Algorithm

1. Read characters from left to right.
2. Push opening brackets.
3. When a closing bracket appears:

   * Check the top.
   * Make sure it matches.
   * Pop it.
4. At the end, the stack must be empty.

### Implementation

```python
def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return not stack
```

Example:

```python
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
```

Output:

```text
True
False
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

---

# 🔄 Reverse a String

A stack naturally reverses data because of LIFO.

Example:

```text
Input:

PYTHON
```

Push:

```text
P
Y
T
H
O
N
```

Pop:

```text
N
O
H
T
Y
P
```

### Implementation

```python
def reverse_string(text):
    stack = list(text)
    result = []

    while stack:
        result.append(stack.pop())

    return "".join(result)


print(reverse_string("PYTHON"))
```

Output:

```text
NOHTYP
```

---

# ➕ Infix, Prefix and Postfix

Arithmetic expressions can be represented in different forms.

## Infix

Operator is between operands.

```text
A + B
```

## Prefix

Operator comes before operands.

```text
+ A B
```

## Postfix

Operator comes after operands.

```text
A B +
```

---

# 🧮 Example

Expression:

```text
A + B * C
```

Infix:

```text
A + B * C
```

Postfix:

```text
A B C * +
```

Prefix:

```text
+ A * B C
```

Stacks are heavily used in expression conversion and evaluation.

---

# 🔄 Infix to Postfix

Consider:

```text
A + B * C
```

Because multiplication has higher precedence:

```text
A B C * +
```

A stack stores operators while operands are directly added to the output.

### Basic Implementation

```python
def precedence(operator):
    if operator in "+-":
        return 1

    if operator in "*/":
        return 2

    if operator == "^":
        return 3

    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if stack:
                stack.pop()

        else:
            while (
                stack
                and stack[-1] != '('
                and precedence(stack[-1]) >= precedence(char)
            ):
                output.append(stack.pop())

            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)
```

Example:

```python
print(infix_to_postfix("A+B*C"))
```

Output:

```text
ABC*+
```

> Handling associativity, especially for exponentiation, requires additional logic in a fully general infix-to-postfix implementation.

---

# 🧮 Postfix Expression Evaluation

Example:

```text
2 3 + 4 *
```

Steps:

```text
Push 2
Push 3
+
→ 5

Push 4
*
→ 20
```

Result:

```text
20
```

### Implementation

```python
def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(left / right)

    return stack.pop()
```

Example:

```python
print(evaluate_postfix("2 3 + 4 *"))
```

Output:

```text
20
```

---

# 📞 Recursion and Call Stack

Every function call is managed using a **call stack**.

Consider:

```python
def first():
    second()


def second():
    third()


def third():
    print("Hello")
```

Calling:

```python
first()
```

creates:

```text
TOP
 ↓
third()
second()
first()
```

When `third()` finishes:

```text
third()
```

is removed.

Then:

```text
second()
```

continues.

This is the fundamental connection between recursion and stacks.

---

# 🔁 Recursion Example

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

For:

```text
factorial(3)
```

the call stack grows approximately as:

```text
factorial(3)
factorial(2)
factorial(1)
factorial(0)
```

Then the calls return in reverse order.

---

# 🔙 Backtracking

Backtracking explores possibilities and returns to previous states when a path fails.

A stack can store states that need to be revisited.

Common examples:

* Maze solving
* Sudoku
* N-Queens
* Permutations
* Combination generation
* Path exploration

Conceptually:

```text
Choose
 ↓
Explore
 ↓
Success?
 ├── Yes → Continue
 └── No  → Backtrack
```

---

# 🌳 Depth-First Search

DFS can be implemented using a stack.

Example graph:

```text
      A
     / \
    B   C
   / \
  D   E
```

DFS can use:

```text
Stack
 ↓
A
```

Then process neighboring nodes by pushing them onto the stack.

### Iterative DFS

```python
def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
```

Complexity for an adjacency-list graph:

```text
Time:  O(V + E)
Space: O(V)
```

where:

```text
V = vertices
E = edges
```

---

# 📈 Monotonic Stack

A **Monotonic Stack** maintains elements in increasing or decreasing order.

It is a powerful pattern for solving problems involving:

* Next Greater Element
* Next Smaller Element
* Previous Greater Element
* Previous Smaller Element
* Daily Temperatures
* Stock Span
* Largest Rectangle in Histogram

Instead of repeatedly searching through earlier elements, a monotonic stack can often reduce the solution to:

```text
O(n)
```

---

# 🔼 Next Greater Element

Given:

```text
[4, 5, 2, 10]
```

The next greater element for each value is:

```text
4  → 5
5  → 10
2  → 10
10 → -1
```

### Implementation

```python
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result


numbers = [4, 5, 2, 10]

print(next_greater_element(numbers))
```

Output:

```text
[5, 10, 10, -1]
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

Each element is pushed and popped at most once.

---

# 📉 Next Smaller Element

The same idea can be modified to find the next smaller value.

```python
def next_smaller_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result
```

---

# 🥇 Min Stack

A normal stack provides:

```text
push()
pop()
peek()
```

A **Min Stack** additionally supports:

```text
get_min()
```

in `O(1)` time.

One approach is to maintain two stacks:

```text
Main Stack       Min Stack

30               30
20               20
40               20
10               10
```

### Implementation

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, value):
        self.stack.append(value)

        if not self.minimums:
            self.minimums.append(value)
        else:
            self.minimums.append(
                min(value, self.minimums[-1])
            )

    def pop(self):
        self.minimums.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.minimums[-1]
```

Complexity:

```text
Push    → O(1)
Pop     → O(1)
Top     → O(1)
Get Min → O(1)
```

---

# ⚖️ Stack vs Queue

| Feature        | Stack    | Queue           |
| -------------- | -------- | --------------- |
| Principle      | LIFO     | FIFO            |
| Insert         | Top      | Rear            |
| Remove         | Top      | Front           |
| Main operation | Push/Pop | Enqueue/Dequeue |
| Example        | Plates   | Waiting line    |
| Common use     | DFS      | BFS             |

### Stack

```text
10 → 20 → 30

POP → 30
```

### Queue

```text
10 → 20 → 30

DEQUEUE → 10
```

---

# ⚖️ Stack vs Array

A stack is an **abstract data type**, while an array/list is a concrete data structure.

A stack defines behavior:

```text
Push
Pop
Peek
```

A Python list is one possible implementation.

```text
Stack ADT
    ↓
Python list
```

A stack can also be implemented using:

```text
Linked List
Dynamic Array
Deque
```

---

# 🧠 Important Stack Patterns

Master these patterns:

```text
1. LIFO
2. Push / Pop
3. Matching pairs
4. Previous / Next element
5. Two-stack technique
6. Monotonic stack
7. Expression evaluation
8. Expression conversion
9. Backtracking
10. DFS
```

These patterns appear frequently in DSA interviews.

---

# 🚨 Common Mistakes

## 1. Popping an Empty Stack

```python
stack.pop()
```

can raise an exception when empty.

Use:

```python
if stack:
    stack.pop()
```

---

## 2. Confusing Peek and Pop

Peek:

```python
stack[-1]
```

does not remove the element.

Pop:

```python
stack.pop()
```

removes it.

---

## 3. Using the Wrong End of a List

For stack behavior, use:

```python
append()
pop()
```

at the same end.

Avoid:

```python
insert(0, value)
pop(0)
```

for high-performance stacks because operations at the beginning of a Python list are generally `O(n)`.

---

## 4. Forgetting Operator Precedence

When converting expressions, remember:

```text
()
^
*
/
+
-
```

and account for operator associativity.

---

## 5. Incorrect Operand Order

For:

```text
8 3 -
```

the calculation is:

```text
8 - 3
```

not:

```text
3 - 8
```

When evaluating:

```python
right = stack.pop()
left = stack.pop()
```

then:

```python
left - right
```

---

## 6. Forgetting Visited Nodes in DFS

Graphs may contain cycles.

Always consider:

```python
visited = set()
```

when appropriate.

---

# 🧪 Practice Problems — Beginner

### Problem 1

Implement a stack using a Python list.

### Problem 2

Implement:

```text
push()
pop()
peek()
is_empty()
size()
```

### Problem 3

Reverse a string using a stack.

### Problem 4

Check whether parentheses are balanced.

### Problem 5

Convert decimal numbers to binary using a stack.

### Problem 6

Implement a stack using a linked list.

---

# 🚀 Practice Problems — Intermediate

### Problem 7

Implement a Min Stack.

### Problem 8

Implement a stack using two queues.

### Problem 9

Evaluate a postfix expression.

### Problem 10

Convert infix expression to postfix.

### Problem 11

Find the next greater element.

### Problem 12

Find the next smaller element.

### Problem 13

Solve the Stock Span Problem.

### Problem 14

Remove adjacent duplicate characters.

Example:

```text
Input:
abbaca

Output:
ca
```

---

# 🔥 Practice Problems — Advanced

### Problem 15 — Daily Temperatures

Given daily temperatures, find how many days must pass before a warmer temperature occurs.

Example:

```text
Input:
[73, 74, 75, 71, 69, 72, 76, 73]

Output:
[1, 1, 4, 2, 1, 1, 0, 0]
```

This is a classic **monotonic stack** problem.

---

### Problem 16 — Largest Rectangle in Histogram

Given:

```text
[2, 1, 5, 6, 2, 3]
```

Find the largest rectangular area.

Expected:

```text
10
```

A monotonic stack can solve this in:

```text
O(n)
```

---

### Problem 17 — Decode String

Decode expressions such as:

```text
3[a2[c]]
```

into:

```text
accaccacc
```

Stacks are useful for managing nested structures.

---

### Problem 18 — Remove K Digits

Given a numeric string, remove `k` digits to produce the smallest possible number.

This can be solved using a monotonic stack.

---

### Problem 19 — Asteroid Collision

Simulate collisions between moving objects using a stack.

---

### Problem 20 — Basic Calculator

Evaluate an arithmetic expression containing:

```text
+
-
(
)
```

using stack-based processing.

---

# 🎯 Interview Questions

## Beginner

1. What is a stack?
2. What is LIFO?
3. What is the top of a stack?
4. What are push and pop?
5. What is peek?
6. What is stack underflow?
7. What is stack overflow?
8. How can a stack be implemented in Python?
9. Why is `list.append()` suitable for push?
10. Why is `list.pop()` suitable for pop?

## Intermediate

11. How do you implement a stack using a linked list?
12. What is the complexity of stack operations?
13. How do you check balanced parentheses?
14. How can a stack reverse a string?
15. What is the relationship between recursion and stacks?
16. What is a call stack?
17. How is DFS implemented using a stack?
18. What is a monotonic stack?
19. How do you find the next greater element?
20. What is a Min Stack?

## Advanced

21. How do you evaluate a postfix expression?
22. How do you convert infix to postfix?
23. How do operator precedence and associativity affect expression conversion?
24. How can two stacks be used to implement another data structure?
25. How does a monotonic stack achieve `O(n)` in many problems?
26. How do you solve the Largest Rectangle in Histogram problem?
27. How do you solve Daily Temperatures using a stack?
28. How are stacks used in backtracking?
29. Why can recursion cause stack overflow?
30. What are the differences between a stack ADT and a Python list?

---

# ⚡ Quick Revision

```text
Stack
→ Linear Abstract Data Type

LIFO
→ Last In, First Out

TOP
→ End where insertion/removal occurs

PUSH
→ Add element

POP
→ Remove top element

PEEK
→ View top element

EMPTY
→ No elements

Python List
→ append() + pop()

Linked List Stack
→ Head acts as Top

Basic Operations
→ O(1)

Applications
→ Recursion
→ Function calls
→ DFS
→ Backtracking
→ Expression evaluation
→ Parentheses matching
→ Undo/Redo

Monotonic Stack
→ Maintains increasing/decreasing order

Min Stack
→ get_min() in O(1)
```

---

# 📊 Complexity Cheat Sheet

| Operation / Problem  |               Time | Space |
| -------------------- | -----------------: | ----: |
| Push                 |              O(1)* |  O(1) |
| Pop                  |               O(1) |  O(1) |
| Peek                 |               O(1) |  O(1) |
| Balanced Parentheses |               O(n) |  O(n) |
| Reverse String       |               O(n) |  O(n) |
| Postfix Evaluation   |               O(n) |  O(n) |
| Infix → Postfix      |               O(n) |  O(n) |
| DFS                  |           O(V + E) |  O(V) |
| Next Greater Element |               O(n) |  O(n) |
| Min Stack            | O(1) per operation |  O(n) |
| Largest Rectangle    |               O(n) |  O(n) |

`*` Python list append is amortized `O(1)`.

---

# 🏆 Problem-Solving Strategy

When you see a stack-related problem, ask:

```text
1. Does the problem require LIFO behavior?
        ↓
2. Do I need to remember previous elements?
        ↓
3. Is there nested structure?
        ↓
4. Are there matching brackets?
        ↓
5. Do I need previous/next greater/smaller?
        ↓
6. Can a monotonic stack help?
        ↓
7. Do I need to preserve states for backtracking?
        ↓
8. Is this a DFS problem?
        ↓
9. Are there repeated minimum/maximum queries?
        ↓
10. Would two stacks simplify the design?
```

---

# 🎓 Mastery Checklist

### Fundamentals

* [ ] Understand LIFO
* [ ] Understand stack terminology
* [ ] Understand push
* [ ] Understand pop
* [ ] Understand peek
* [ ] Understand underflow
* [ ] Understand overflow

### Implementation

* [ ] Implement stack using list
* [ ] Implement stack using linked list
* [ ] Use `deque`
* [ ] Build a Stack class
* [ ] Handle empty-stack conditions

### Algorithms

* [ ] Reverse a string
* [ ] Check balanced parentheses
* [ ] Evaluate postfix expressions
* [ ] Convert infix to postfix
* [ ] Implement DFS
* [ ] Implement Min Stack
* [ ] Find Next Greater Element
* [ ] Find Next Smaller Element

### Advanced

* [ ] Understand monotonic stacks
* [ ] Solve Daily Temperatures
* [ ] Solve Stock Span
* [ ] Solve Largest Rectangle
* [ ] Solve Asteroid Collision
* [ ] Understand stack-based backtracking
* [ ] Understand call stacks and recursion

---

# 📁 Recommended Folder Structure

```text
05-Stack/
│
├── README.md
│
├── 01-stack-using-list.py
├── 02-stack-class.py
├── 03-stack-using-linked-list.py
├── 04-stack-using-deque.py
│
├── 05-balanced-parentheses.py
├── 06-reverse-string.py
├── 07-infix-to-postfix.py
├── 08-postfix-evaluation.py
│
├── 09-min-stack.py
├── 10-two-stacks.py
├── 11-next-greater-element.py
├── 12-next-smaller-element.py
├── 13-stock-span.py
│
├── 14-daily-temperatures.py
├── 15-largest-rectangle.py
├── 16-decode-string.py
├── 17-remove-k-digits.py
├── 18-asteroid-collision.py
└── 19-basic-calculator.py
```

---

# 🗺️ DSA Learning Roadmap

```text
22-DSA-with-Python
│
├── 01-Arrays
├── 02-Searching
├── 03-Sorting
├── 04-Linked-List
├── 05-Stack
│
├── 06-Queue
├── 07-Hashing
├── 08-Strings
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

# 📚 References

* [Python Documentation — Built-in Types](https://docs.python.org/3/library/stdtypes.html?utm_source=chatgpt.com)
* [Python Documentation — Lists](https://docs.python.org/3/tutorial/datastructures.html?utm_source=chatgpt.com)
* [Python Documentation — `collections.deque`](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com#collections.deque)

---

# 🚀 Next Topic

➡️ **[06-Queue](../06-Queue/README.md)**

> **Think LIFO. Master the stack. Recognize the pattern. Solve the problem.** 🐍📚
