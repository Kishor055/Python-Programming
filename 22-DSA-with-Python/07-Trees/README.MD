# 07 — Trees in Python

> A comprehensive guide to **Tree Data Structures**, Binary Trees, Tree Traversals, Binary Search Trees, recursion, complexity, common patterns, applications, and interview problems using Python.

---

## 📌 Overview

A **Tree** is a non-linear hierarchical data structure made up of **nodes connected by edges**.

Unlike arrays, linked lists, stacks, and queues, which are generally linear structures, trees represent relationships in a hierarchy.

Examples of hierarchical structures include:

* File systems
* Organization charts
* HTML/XML documents
* Database indexes
* Decision trees
* Expression trees
* Routing structures
* Artificial intelligence search spaces

A tree can be visualized as:

```text
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
```

Here:

* `1` is the **root**.
* `2` and `3` are children of `1`.
* `4` and `5` are children of `2`.
* `6` and `7` are children of `3`.
* `4, 5, 6, 7` are leaf nodes.

---

# 📚 Table of Contents

* [What is a Tree?](#-what-is-a-tree)
* [Why Trees?](#-why-trees)
* [Tree Terminology](#-tree-terminology)
* [Tree Properties](#-tree-properties)
* [Types of Trees](#-types-of-trees)
* [Binary Tree](#-binary-tree)
* [Binary Tree Node](#-binary-tree-node)
* [Creating a Binary Tree](#-creating-a-binary-tree)
* [Tree Traversals](#-tree-traversals)
* [Preorder Traversal](#-preorder-traversal)
* [Inorder Traversal](#-inorder-traversal)
* [Postorder Traversal](#-postorder-traversal)
* [Level Order Traversal](#-level-order-traversal)
* [Recursive vs Iterative Traversal](#-recursive-vs-iterative-traversal)
* [Tree Height and Depth](#-tree-height-and-depth)
* [Count Nodes](#-count-nodes)
* [Count Leaf Nodes](#-count-leaf-nodes)
* [Search in a Binary Tree](#-search-in-a-binary-tree)
* [Binary Search Tree](#-binary-search-tree)
* [BST Operations](#-bst-operations)
* [BST Search](#-bst-search)
* [BST Insertion](#-bst-insertion)
* [BST Deletion](#-bst-deletion)
* [Minimum and Maximum](#-minimum-and-maximum)
* [Balanced Trees](#-balanced-trees)
* [Complete and Full Binary Trees](#-complete-and-full-binary-trees)
* [Perfect Binary Tree](#-perfect-binary-tree)
* [Skewed Tree](#-skewed-tree)
* [Tree vs Graph](#-tree-vs-graph)
* [Tree Applications](#-tree-applications)
* [Important Tree Patterns](#-important-tree-patterns)
* [Common Tree Problems](#-common-tree-problems)
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

# 🔹 What is a Tree?

A tree is a collection of nodes connected through edges.

Example:

```text
                 A
               /   \
              B     C
             / \     \
            D   E     F
```

The tree has:

* One root: `A`
* Six nodes
* Five edges
* Three leaf nodes: `D`, `E`, `F`

A fundamental property of a tree with `n` nodes is:

```text
Number of edges = n - 1
```

for a connected tree.

---

# 🔹 Why Trees?

Many real-world problems naturally contain hierarchical relationships.

For example, a file system:

```text
Computer
│
├── Documents
│   ├── resume.pdf
│   └── notes.txt
│
├── Pictures
│   ├── image1.jpg
│   └── image2.jpg
│
└── Projects
    ├── Python
    └── Machine-Learning
```

Representing this structure using a tree is natural and efficient.

---

# 🔹 Tree Terminology

Understanding tree terminology is essential before learning tree algorithms.

## Root

The topmost node.

```text
        A ← Root
       / \
      B   C
```

---

## Parent

A node directly above another node.

```text
      A
      |
      B
```

`A` is the parent of `B`.

---

## Child

A node directly below another node.

```text
      A
      |
      B
```

`B` is the child of `A`.

---

## Siblings

Nodes having the same parent.

```text
        A
       / \
      B   C
```

`B` and `C` are siblings.

---

## Leaf Node

A node with no children.

```text
        A
       / \
      B   C
```

`B` and `C` are leaf nodes.

---

## Internal Node

A node having at least one child.

In:

```text
        A
       / \
      B   C
```

`A` is an internal node.

---

## Edge

The connection between two nodes.

```text
A ─── B
```

The line represents an edge.

---

## Path

A sequence of nodes connected by edges.

```text
A → B → D
```

is a path.

---

## Depth

The number of edges from the root to a node.

```text
        A       depth 0
       /
      B         depth 1
     /
    D           depth 2
```

---

## Height

The number of edges on the longest downward path from a node to a leaf.

The height of a tree is the height of its root.

---

## Subtree

A node together with all of its descendants.

```text
          A
        /   \
       B     C
      / \
     D   E
```

The subtree rooted at `B` is:

```text
       B
      / \
     D   E
```

---

# 🔹 Tree Properties

Important properties:

### Property 1

A tree has exactly one path between any two nodes.

### Property 2

A tree with `n` nodes contains:

```text
n - 1
```

edges.

### Property 3

A tree contains no cycles.

### Property 4

Trees are connected structures.

---

# 🔹 Types of Trees

Important tree types include:

```text
Tree
│
├── General Tree
│
├── Binary Tree
│
│   ├── Full Binary Tree
│   ├── Complete Binary Tree
│   ├── Perfect Binary Tree
│   ├── Balanced Binary Tree
│   └── Skewed Binary Tree
│
├── Binary Search Tree
│
├── AVL Tree
│
├── Red-Black Tree
│
├── Heap
│
├── Trie
│
└── B-Tree / B+ Tree
```

This section focuses primarily on **Binary Trees** and **Binary Search Trees**.

---

# 🔹 Binary Tree

A **Binary Tree** is a tree where each node can have at most two children.

The children are generally called:

```text
Left Child
Right Child
```

Example:

```text
          10
         /  \
        20   30
       / \
      40  50
```

Each node can have:

```text
0 children
1 child
2 children
```

but never more than two children.

---

# 🔹 Binary Tree Node

A binary tree node typically contains:

```text
Data
Left Pointer
Right Pointer
```

Python implementation:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

# 🔹 Creating a Binary Tree

Example:

```python
root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
```

The resulting tree:

```text
          10
         /  \
        20   30
       / \
      40  50
```

---

# 🔹 Tree Traversals

A **tree traversal** means visiting every node of a tree according to a specific order.

The major traversals are:

```text
Depth-First Search
│
├── Preorder
├── Inorder
└── Postorder

Breadth-First Search
│
└── Level Order
```

---

# 🔹 Preorder Traversal

Order:

```text
Root → Left → Right
```

For:

```text
        A
       / \
      B   C
     / \
    D   E
```

Preorder:

```text
A → B → D → E → C
```

### Python

```python
def preorder(root):
    if root is None:
        return

    print(root.value, end=" ")

    preorder(root.left)
    preorder(root.right)
```

---

# 🔹 Inorder Traversal

Order:

```text
Left → Root → Right
```

For:

```text
        A
       / \
      B   C
     / \
    D   E
```

Inorder:

```text
D → B → E → A → C
```

### Python

```python
def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.value, end=" ")

    inorder(root.right)
```

### Important BST Property

For a valid Binary Search Tree:

> **Inorder traversal produces values in sorted order.**

---

# 🔹 Postorder Traversal

Order:

```text
Left → Right → Root
```

For:

```text
        A
       / \
      B   C
     / \
    D   E
```

Postorder:

```text
D → E → B → C → A
```

### Python

```python
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.value, end=" ")
```

---

# 🔹 Level Order Traversal

Level-order traversal visits nodes level by level.

It uses a **queue**.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Output:

```text
1 → 2 → 3 → 4 → 5 → 6 → 7
```

### Python

```python
from collections import deque


def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
```

---

# 🔹 Recursive vs Iterative Traversal

Tree traversals can be implemented using recursion or explicit stacks.

### Recursive

```python
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value)
    inorder(root.right)
```

### Iterative

```python
def inorder(root):
    stack = []
    current = root

    while current or stack:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        print(current.value)

        current = current.right
```

### Key Idea

Recursive DFS uses the **call stack**.

Iterative DFS explicitly uses a **stack**.

---

# 🔹 Tree Height and Depth

Consider:

```text
          A
         /
        B
       /
      C
     /
    D
```

Depth:

```text
A → 0
B → 1
C → 2
D → 3
```

Height of the tree:

```text
3
```

### Recursive Height

```python
def height(root):
    if root is None:
        return -1

    return 1 + max(
        height(root.left),
        height(root.right)
    )
```

If height is defined as number of nodes rather than edges, the base case and interpretation change.

Be consistent with the convention used in a problem.

---

# 🔹 Count Nodes

```python
def count_nodes(root):
    if root is None:
        return 0

    return (
        1
        + count_nodes(root.left)
        + count_nodes(root.right)
    )
```

For:

```text
        1
       / \
      2   3
```

Result:

```text
3
```

---

# 🔹 Count Leaf Nodes

```python
def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return (
        count_leaves(root.left)
        + count_leaves(root.right)
    )
```

---

# 🔹 Search in a Binary Tree

For a normal binary tree, there is no ordering property.

Therefore, in the worst case, we may need to visit every node.

```python
def search(root, target):
    if root is None:
        return False

    if root.value == target:
        return True

    return (
        search(root.left, target)
        or search(root.right, target)
    )
```

Complexity:

```text
Time  → O(n)
Space → O(h)
```

where `h` is tree height for the recursive call stack.

---

# 🔹 Binary Search Tree

A **Binary Search Tree (BST)** is a binary tree with an ordering rule.

For every node:

```text
Left subtree values < Node value < Right subtree values
```

Example:

```text
           50
          /  \
        30    70
       / \    / \
      20 40  60 80
```

This ordering allows efficient searching when the tree is reasonably balanced.

---

# 🔹 BST Search

Suppose we search for `60`.

```text
           50
          /  \
        30    70
             /
            60
```

Start:

```text
60 > 50
```

Go right.

```text
60 < 70
```

Go left.

Found `60`.

### Python

```python
def search_bst(root, target):
    if root is None:
        return None

    if root.value == target:
        return root

    if target < root.value:
        return search_bst(root.left, target)

    return search_bst(root.right, target)
```

---

# 🔹 BST Insertion

Example:

Insert:

```text
65
```

into:

```text
           50
          /  \
        30    70
             /
            60
```

Since:

```text
65 > 50
65 < 70
65 > 60
```

it becomes the right child of `60`.

```text
           50
          /  \
        30    70
             /
            60
              \
               65
```

### Python

```python
def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root
```

---

# 🔹 BST Deletion

Deletion has three major cases.

## Case 1 — Leaf Node

Delete a node with no children.

```text
    50
   /
  30
```

Remove `30`.

---

## Case 2 — One Child

```text
    50
   /
  30
    \
     40
```

Deleting `30` connects its parent directly to `40`.

---

## Case 3 — Two Children

```text
       50
      /  \
    30    70
         /  \
        60   80
```

When deleting a node with two children, a common approach is to replace it with:

* inorder successor, or
* inorder predecessor.

The **inorder successor** is the smallest value in the right subtree.

---

# 🔹 Minimum and Maximum in BST

### Minimum

Keep moving left:

```python
def find_min(root):
    current = root

    while current.left:
        current = current.left

    return current
```

### Maximum

Keep moving right:

```python
def find_max(root):
    current = root

    while current.right:
        current = current.right

    return current
```

---

# 🔹 Balanced Trees

A tree is balanced when its height remains relatively small compared with the number of nodes.

Example of balanced structure:

```text
          4
        /   \
       2     6
      / \   / \
     1   3 5   7
```

Height is approximately:

```text
O(log n)
```

This can make BST operations efficient.

---

# 🔹 Skewed Tree

A BST can become skewed depending on insertion order.

Example:

```text
10
  \
   20
     \
      30
        \
         40
           \
            50
```

This behaves much like a linked list.

Height becomes:

```text
O(n)
```

Therefore, BST operations can degrade to:

```text
O(n)
```

---

# 🔹 Full Binary Tree

Every node has either:

```text
0 children
or
2 children
```

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

---

# 🔹 Complete Binary Tree

A complete binary tree has:

* Every level completely filled except possibly the last.
* The final level is filled from left to right.

Example:

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

Heaps are commonly represented as complete binary trees.

---

# 🔹 Perfect Binary Tree

Every internal node has two children and all leaves occur at the same level.

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

For height `h`, the number of nodes is:

```text
2^(h + 1) - 1
```

when height is measured in edges.

---

# 🔹 Tree vs Graph

| Feature      | Tree                          | Graph                   |
| ------------ | ----------------------------- | ----------------------- |
| Cycles       | No                            | May exist               |
| Connectivity | Connected                     | May be disconnected     |
| Root         | Usually one root              | No required root        |
| Paths        | Unique path between two nodes | Multiple paths possible |
| Edges        | `n - 1` for a tree            | No fixed rule           |
| Hierarchy    | Natural                       | General relationships   |

A tree can be considered a special type of graph.

---

# 🔹 Tree Applications

Trees appear throughout computer science.

## File Systems

```text
Root
├── Folder
│   ├── File
│   └── File
└── Folder
```

## Databases

Database indexes use tree-based structures such as B-Trees and B+ Trees.

## Compilers

Expression trees can represent mathematical expressions.

For:

```text
(a + b) * c
```

the structure can be:

```text
        *
       / \
      +   c
     / \
    a   b
```

## HTML DOM

HTML documents naturally form hierarchical tree structures.

## Artificial Intelligence

Decision trees can represent branching decisions.

## Networking

Hierarchical routing and topology representations can use tree structures.

---

# 🔹 Important Tree Patterns

## Pattern 1 — Recursive DFS

Many tree problems naturally follow:

```python
def solve(root):
    if root is None:
        return ...

    left = solve(root.left)
    right = solve(root.right)

    return ...
```

Think:

```text
Solve left
Solve right
Combine
```

---

## Pattern 2 — Tree Height

```python
height = 1 + max(left_height, right_height)
```

Useful for:

* Height
* Diameter
* Balanced tree
* Maximum depth

---

## Pattern 3 — Level Order BFS

Use:

```python
from collections import deque
```

Useful for:

* Level order
* Minimum depth
* Level averages
* Right-side view
* Distance by levels

---

## Pattern 4 — BST Property

Always ask:

```text
Is this a Binary Search Tree?
```

If yes, exploit:

```text
left < root < right
```

---

## Pattern 5 — Path Problems

Typical approach:

```text
Root
 ↓
Choose left/right
 ↓
Continue
 ↓
Track path
```

Used in:

* Root-to-leaf paths
* Path sum
* Lowest Common Ancestor
* Maximum path problems

---

# 🔹 Common Tree Problems

### Beginner

1. Preorder Traversal
2. Inorder Traversal
3. Postorder Traversal
4. Level Order Traversal
5. Maximum Depth
6. Count Nodes
7. Count Leaves
8. Search Binary Tree
9. Invert Binary Tree

### Intermediate

1. Validate Binary Search Tree
2. Lowest Common Ancestor
3. Diameter of Binary Tree
4. Balanced Binary Tree
5. Path Sum
6. Right Side View
7. Zigzag Level Order
8. Kth Smallest Element in BST

### Advanced

1. Serialize and Deserialize Binary Tree
2. Binary Tree Maximum Path Sum
3. Construct Tree from Traversals
4. Recover BST
5. Flatten Binary Tree
6. Morris Traversal
7. Lowest Common Ancestor Variations
8. Tree Dynamic Programming

---

# 🔹 Practice Problems

## 🟢 Beginner

### Problem 1 — Tree Traversals

Given:

```text
        1
       / \
      2   3
     / \
    4   5
```

Find:

```text
Preorder
Inorder
Postorder
Level Order
```

Expected:

```text
Preorder   → 1 2 4 5 3
Inorder    → 4 2 5 1 3
Postorder  → 4 5 2 3 1
Level Order→ 1 2 3 4 5
```

---

### Problem 2 — Maximum Depth

Find the maximum depth of a binary tree.

---

### Problem 3 — Count Leaves

Count the number of leaf nodes.

---

# 🟡 Intermediate

### Problem 4 — Validate BST

Determine whether a binary tree satisfies BST ordering.

---

### Problem 5 — Lowest Common Ancestor

Given two nodes, find their lowest common ancestor.

---

### Problem 6 — Diameter

Find the longest path between any two nodes.

---

# 🔴 Advanced

### Problem 7 — Serialize and Deserialize

Convert a tree into a storable representation and reconstruct it.

---

### Problem 8 — Construct Tree

Construct a binary tree from:

```text
Preorder
+
Inorder
```

---

### Problem 9 — Maximum Path Sum

Find the maximum possible sum of a path through the tree.

---

# 🔹 Interview Questions

### Basic

1. What is a tree?
2. What is a binary tree?
3. What is a root node?
4. What is a leaf node?
5. What is tree height?
6. What is node depth?
7. What is a subtree?
8. What is tree traversal?
9. Explain preorder traversal.
10. Explain inorder traversal.
11. Explain postorder traversal.
12. Explain level-order traversal.

### Intermediate

13. What is a Binary Search Tree?
14. What is the BST property?
15. What is the difference between binary tree and BST?
16. Why does inorder traversal of a BST produce sorted values?
17. How do you search a BST?
18. How do you insert into a BST?
19. How do you delete a BST node?
20. What is an inorder successor?
21. What is a balanced tree?
22. What is a complete binary tree?
23. What is a full binary tree?
24. What is a perfect binary tree?
25. Why can a BST degrade to O(n)?

### Advanced

26. How do you find the diameter of a binary tree?
27. How do you validate a BST?
28. How do you find the lowest common ancestor?
29. How can BFS be used on trees?
30. How can DFS be implemented iteratively?
31. How do you serialize a binary tree?
32. How do you construct a tree from preorder and inorder?
33. What is tree dynamic programming?
34. What is Morris traversal?
35. What are AVL and Red-Black trees?

---

# 🔹 Common Mistakes

### ❌ Mistake 1 — Confusing Height and Depth

Remember:

```text
Depth → Root → Node
Height → Node → Deepest Leaf
```

---

### ❌ Mistake 2 — Assuming Every Binary Tree Is a BST

A binary tree only restricts the number of children.

A BST additionally imposes ordering.

---

### ❌ Mistake 3 — Forgetting Base Cases

Recursive tree algorithms usually require:

```python
if root is None:
    return ...
```

---

### ❌ Mistake 4 — Ignoring Skewed Trees

A BST is not automatically O(log n).

A skewed BST can have:

```text
Height = O(n)
```

---

### ❌ Mistake 5 — Using the Wrong Traversal

Remember:

```text
Preorder  → Root Left Right
Inorder   → Left Root Right
Postorder → Left Right Root
```

---

# 🔹 Quick Revision

```text
Tree
│
├── Root
├── Parent
├── Child
├── Sibling
├── Leaf
├── Edge
├── Path
├── Depth
└── Height
```

### Binary Tree

```text
At most 2 children
│
├── Left
└── Right
```

### Traversals

```text
DFS
├── Preorder  → Root Left Right
├── Inorder   → Left Root Right
└── Postorder → Left Right Root

BFS
└── Level Order
```

### BST

```text
Left < Root < Right
```

---

# 🔹 Complexity Cheat Sheet

Let:

```text
n = number of nodes
h = height
```

| Operation | Binary Tree | Balanced BST | Skewed BST |
| --------- | ----------: | -----------: | ---------: |
| Search    |        O(n) |     O(log n) |       O(n) |
| Insert    |       O(n)* |     O(log n) |       O(n) |
| Delete    |       O(n)* |     O(log n) |       O(n) |
| Traversal |        O(n) |         O(n) |       O(n) |
| Height    |        O(n) |     O(log n) |       O(n) |

`*` Depends on the operation and structure; an ordinary binary tree does not have the BST ordering property.

Traversal space:

```text
Recursive DFS → O(h)
BFS            → O(w)
```

where `w` is the maximum width of the tree.

---

# 🔹 Problem-Solving Strategy

When you see a tree problem:

### Step 1 — Identify the Tree Type

Ask:

```text
Binary Tree?
BST?
Heap?
Trie?
General Tree?
```

---

### Step 2 — Identify the Required Traversal

Ask:

```text
Do I need DFS?
Do I need BFS?
```

---

### Step 3 — Check for Recursion

Tree structures naturally support recursive solutions.

Think:

```text
Current Node
    ↓
Left Subtree
    ↓
Right Subtree
```

---

### Step 4 — Look for the Base Case

Usually:

```python
if root is None:
```

---

### Step 5 — Combine Subproblem Results

For example:

```python
left = solve(root.left)
right = solve(root.right)

return combine(left, right)
```

---

### Step 6 — Exploit BST Ordering

If the structure is a BST:

```text
target < root → left
target > root → right
```

This can avoid searching the entire tree.

---

# 🔹 Mastery Checklist

### Fundamentals

* [ ] Understand tree terminology
* [ ] Understand root, parent, child
* [ ] Understand leaf nodes
* [ ] Understand height and depth
* [ ] Understand paths and subtrees

### Binary Trees

* [ ] Create a binary tree
* [ ] Implement TreeNode
* [ ] Preorder traversal
* [ ] Inorder traversal
* [ ] Postorder traversal
* [ ] Level-order traversal
* [ ] Recursive traversal
* [ ] Iterative traversal

### BST

* [ ] Understand BST property
* [ ] Search BST
* [ ] Insert BST
* [ ] Delete BST
* [ ] Find minimum
* [ ] Find maximum
* [ ] Find inorder successor
* [ ] Validate BST

### Advanced

* [ ] Tree height
* [ ] Tree diameter
* [ ] Lowest Common Ancestor
* [ ] Balanced tree
* [ ] Serialize/deserialize
* [ ] Construct tree from traversals
* [ ] Maximum path sum
* [ ] Tree dynamic programming

---

# 🔹 Recommended Folder Structure

```text
22-DSA-with-Python/
│
├── 01-Arrays/
├── 02-Searching/
├── 03-Sorting/
├── 04-Linked-List/
├── 05-Stack/
├── 06-Queue/
│
└── 07-Trees/
    │
    ├── README.md
    │
    ├── tree_node.py
    ├── binary_tree.py
    │
    ├── traversals/
    │   ├── preorder.py
    │   ├── inorder.py
    │   ├── postorder.py
    │   └── level_order.py
    │
    ├── binary_search_tree/
    │   ├── search.py
    │   ├── insert.py
    │   ├── delete.py
    │   └── min_max.py
    │
    └── practice/
        ├── tree_height.py
        ├── count_nodes.py
        ├── count_leaves.py
        ├── validate_bst.py
        ├── diameter.py
        ├── lowest_common_ancestor.py
        └── serialize_tree.py
```

---

# 🔹 Learning Progression

```text
Tree Fundamentals
        ↓
Tree Terminology
        ↓
Binary Trees
        ↓
TreeNode
        ↓
Preorder
        ↓
Inorder
        ↓
Postorder
        ↓
Level Order
        ↓
Tree Height
        ↓
Binary Search Tree
        ↓
BST Search
        ↓
BST Insert
        ↓
BST Delete
        ↓
Balanced Trees
        ↓
Tree Problem Patterns
        ↓
Advanced Tree Algorithms
```

---

# 🔹 Key Takeaways

The most important concepts to remember:

```text
Tree
→ Hierarchical data structure

Binary Tree
→ At most two children

Preorder
→ Root → Left → Right

Inorder
→ Left → Root → Right

Postorder
→ Left → Right → Root

Level Order
→ BFS + Queue

BST
→ Left < Root < Right

Balanced BST
→ Approximately O(log n) operations

Skewed BST
→ Can degrade to O(n)
```

The key to mastering trees is to stop thinking of the tree as one large structure.

Instead, think recursively:

```text
                Root
               /    \
       Left Subtree  Right Subtree
            ↓             ↓
          Solve          Solve
               \         /
                Combine
```

Once this recursive mental model becomes natural, many advanced tree problems become significantly easier to understand.

---

# 🔹 References

* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)
* [Python collections.deque Documentation](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com#collections.deque)

---

# 🚀 DSA Roadmap

```text
22-DSA-with-Python/
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
