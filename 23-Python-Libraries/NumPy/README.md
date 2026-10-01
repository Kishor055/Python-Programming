# 🔢 NumPy — Numerical Computing with Python

> A structured learning module for mastering **NumPy**, Python's fundamental library for numerical computing, multidimensional arrays, mathematical operations, data manipulation, and scientific programming.

---

## 📌 Overview

**NumPy (Numerical Python)** is one of the core libraries of the Python scientific-computing ecosystem.

Its central data structure is the **`ndarray`**, a multidimensional array designed for efficient numerical operations. NumPy provides functionality for array creation and manipulation, mathematical operations, statistics, random simulation, linear algebra, sorting, indexing, and more. ([NumPy][1])

NumPy is widely used as a foundation for:

* 📊 Data Analysis
* 🤖 Machine Learning
* 🧠 Artificial Intelligence
* 📈 Data Visualization
* 🔬 Scientific Computing
* 📐 Linear Algebra
* 📉 Statistics
* 🎲 Simulation
* 🖼️ Image Processing
* ⚙️ Numerical Algorithms

---

# 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand NumPy and its role in Python
* Create and manipulate multidimensional arrays
* Understand `ndarray`, dimensions, shape, size, and dtype
* Perform array indexing and slicing
* Work with axes
* Reshape and transpose arrays
* Perform vectorized mathematical operations
* Understand broadcasting
* Apply aggregation and statistical functions
* Generate random data
* Sort and search arrays
* Work with Boolean and advanced indexing
* Perform basic linear algebra
* Read and write numerical data
* Combine NumPy with Pandas and Matplotlib
* Apply NumPy concepts to data-science and ML workflows

---

# 🧰 Installation

Install NumPy using `pip`:

```bash
pip install numpy
```

Verify the installation:

```python
import numpy as np

print(np.__version__)
```

The official NumPy documentation provides installation guidance along with beginner and user guides. ([NumPy][2])

---

# 📦 Import Convention

The standard NumPy import convention is:

```python
import numpy as np
```

The `np` alias is the conventional shorthand used throughout NumPy documentation and Python projects. ([NumPy][3])

---

# 🧠 What is NumPy?

At the center of NumPy is the multidimensional **`ndarray`**.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
```

Output:

```text
[10 20 30 40]
```

Unlike a standard Python list, a NumPy array is designed specifically for numerical operations and multidimensional data processing.

---

# 🏗️ NumPy Architecture

A simplified view of NumPy:

```text
NumPy
│
├── ndarray
│   ├── 1D Arrays
│   ├── 2D Arrays
│   └── N-D Arrays
│
├── Array Creation
│
├── Indexing & Slicing
│
├── Array Manipulation
│
├── Mathematical Operations
│
├── Broadcasting
│
├── Statistics
│
├── Random Sampling
│
├── Linear Algebra
│
└── Input / Output
```

---

# 🚀 Creating Arrays

## 1. Create an Array from a Python List

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

---

## 2. Create a 2D Array

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)
```

---

## 3. Create an Array of Zeros

```python
zeros = np.zeros((3, 4))

print(zeros)
```

---

## 4. Create an Array of Ones

```python
ones = np.ones((2, 3))

print(ones)
```

NumPy provides dedicated functions such as `zeros()` and `ones()` for creating arrays with specified shapes. ([NumPy][4])

---

## 5. Create a Range of Values

```python
numbers = np.arange(0, 10, 2)

print(numbers)
```

Output:

```text
[0 2 4 6 8]
```

---

## 6. Create Evenly Spaced Values

```python
values = np.linspace(0, 1, 5)

print(values)
```

Output:

```text
[0.   0.25 0.5  0.75 1.  ]
```

---

# 📐 Understanding Array Properties

Every NumPy array has important properties that describe its structure.

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

### Important Properties

| Property   | Meaning                    |
| ---------- | -------------------------- |
| `ndim`     | Number of dimensions       |
| `shape`    | Size of each dimension     |
| `size`     | Total number of elements   |
| `dtype`    | Data type of elements      |
| `itemsize` | Bytes used by each element |

Example:

```text
Array Shape: (2, 3)
Dimensions: 2
Elements: 6
```

Understanding `shape` and `axis` is fundamental to working effectively with multidimensional NumPy arrays. ([NumPy][1])

---

# 🔍 Indexing

NumPy uses zero-based indexing.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

Output:

```text
10
30
50
```

---

# ✂️ Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
```

Output:

```text
[20 30 40]
```

### Common Slicing Pattern

```python
array[start:stop:step]
```

Example:

```python
print(arr[::2])
```

Output:

```text
[10 30 50]
```

---

# 🧩 2D Array Indexing

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0, 1])
```

Output:

```text
2
```

Accessing the second row:

```python
print(matrix[1])
```

Accessing the second column:

```python
print(matrix[:, 1])
```

---

# 🔄 Reshaping Arrays

Arrays can be reshaped without changing their underlying values.

```python
arr = np.arange(1, 7)

matrix = arr.reshape(2, 3)

print(matrix)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

# 🔁 Flattening Arrays

Convert a multidimensional array into a one-dimensional array.

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = matrix.flatten()

print(flat)
```

Output:

```text
[1 2 3 4 5 6]
```

---

# 🔃 Transpose

Transpose swaps the rows and columns.

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix.T)
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

# ➕ Mathematical Operations

NumPy supports element-wise arithmetic operations.

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```text
[11 22 33]
[ 9 18 27]
[10 40 90]
[10. 10. 10.]
```

---

# ⚡ Vectorization

One of NumPy's major advantages is performing operations on entire arrays without explicitly writing Python loops.

### Python Loop

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)
```

### NumPy

```python
numbers = np.array([1, 2, 3, 4, 5])

result = numbers * 2

print(result)
```

Output:

```text
[ 2  4  6  8 10]
```

This style of array-based computation is a key part of NumPy's numerical programming model.

---

# 📡 Broadcasting

**Broadcasting** allows NumPy to perform operations between arrays with compatible shapes, without requiring them to have identical dimensions. ([NumPy][5])

Example:

```python
arr = np.array([10, 20, 30])

result = arr + 5

print(result)
```

Output:

```text
[15 25 35]
```

The scalar `5` is conceptually applied to every element.

---

## Broadcasting with 2D Arrays

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

values = np.array([10, 20, 30])

result = matrix + values

print(result)
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

NumPy compares dimensions from the trailing/rightmost side, and dimensions are compatible when they are equal or when one of them is `1`. ([NumPy][5])

---

# 📊 Aggregation Functions

NumPy provides functions for calculating summary statistics.

```python
data = np.array([10, 20, 30, 40, 50])

print(np.sum(data))
print(np.mean(data))
print(np.min(data))
print(np.max(data))
print(np.std(data))
print(np.var(data))
```

Common functions:

| Function      | Purpose            |
| ------------- | ------------------ |
| `np.sum()`    | Sum                |
| `np.mean()`   | Mean               |
| `np.median()` | Median             |
| `np.min()`    | Minimum            |
| `np.max()`    | Maximum            |
| `np.std()`    | Standard deviation |
| `np.var()`    | Variance           |
| `np.prod()`   | Product            |

NumPy's basic statistics functionality includes operations such as mean, standard deviation, variance, covariance, minimum, maximum, and related aggregations. ([NumPy][1])

---

# 📏 Working with Axis

For multidimensional arrays, `axis` determines the direction along which an operation is performed.

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(matrix.sum(axis=0))
print(matrix.sum(axis=1))
```

Output:

```text
[50 70 90]

[ 60 150]
```

### Concept

```text
axis=0
↓
Operate vertically across rows

axis=1
→
Operate horizontally across columns
```

Understanding `axis` is one of the most important skills when working with multidimensional arrays. ([NumPy][1])

---

# 🎯 Boolean Indexing

NumPy allows arrays to be filtered using Boolean conditions.

```python
numbers = np.array([10, 15, 20, 25, 30])

result = numbers[numbers > 20]

print(result)
```

Output:

```text
[25 30]
```

---

# 🔎 Searching with `where()`

```python
numbers = np.array([10, 20, 30, 40, 50])

result = np.where(numbers > 25)

print(result)
```

You can also replace values conditionally:

```python
numbers = np.array([10, 20, 30, 40, 50])

result = np.where(numbers > 25, 1, 0)

print(result)
```

---

# 🔢 Sorting

```python
numbers = np.array([50, 10, 40, 20, 30])

sorted_numbers = np.sort(numbers)

print(sorted_numbers)
```

Output:

```text
[10 20 30 40 50]
```

For index-based sorting:

```python
indices = np.argsort(numbers)

print(indices)
```

NumPy's array functionality includes sorting, searching, selection, and ordering operations. ([NumPy][1])

---

# 🎲 Random Numbers

NumPy provides random-number generation through `numpy.random`.

For modern NumPy code, the recommended pattern is to create a `Generator` using `default_rng()`. ([NumPy][6])

```python
import numpy as np

rng = np.random.default_rng()

numbers = rng.random(5)

print(numbers)
```

---

## Reproducible Random Numbers

```python
rng = np.random.default_rng(42)

numbers = rng.random(5)

print(numbers)
```

Using a fixed seed makes pseudorandom results reproducible.

---

## Random Integers

```python
rng = np.random.default_rng(42)

numbers = rng.integers(
    1,
    100,
    size=10
)

print(numbers)
```

---

## Normal Distribution

```python
rng = np.random.default_rng(42)

values = rng.standard_normal(1000)

print(values)
```

NumPy's random module supports sampling from a variety of probability distributions. ([NumPy][6])

---

# 🧮 Universal Functions

NumPy provides mathematical functions that operate element-by-element on arrays.

```python
numbers = np.array([1, 4, 9, 16])

print(np.sqrt(numbers))
```

Other examples:

```python
np.abs()
np.exp()
np.log()
np.sin()
np.cos()
np.tan()
np.round()
```

Example:

```python
angles = np.array([0, np.pi / 2, np.pi])

print(np.sin(angles))
```

---

# 🧮 Linear Algebra

NumPy includes basic linear algebra functionality.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = A @ B

print(result)
```

The `@` operator performs matrix multiplication.

NumPy also provides the `numpy.linalg` module for linear algebra operations. ([NumPy][1])

---

## Dot Product

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)

print(result)
```

---

## Matrix Determinant

```python
matrix = np.array([
    [1, 2],
    [3, 4]
])

det = np.linalg.det(matrix)

print(det)
```

---

## Matrix Inverse

```python
matrix = np.array([
    [1, 2],
    [3, 4]
])

inverse = np.linalg.inv(matrix)

print(inverse)
```

---

# 🔗 Joining Arrays

## Concatenate

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))

print(result)
```

Output:

```text
[1 2 3 4 5 6]
```

---

## Vertical Stack

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))

print(result)
```

---

## Horizontal Stack

```python
result = np.hstack((a, b))

print(result)
```

NumPy provides a range of array manipulation functions including `concatenate`, `stack`, `hstack`, `vstack`, `reshape`, `transpose`, and related operations. ([NumPy][1])

---

# 💾 Saving and Loading Data

NumPy supports storing arrays in binary formats.

```python
arr = np.array([10, 20, 30, 40])

np.save("data.npy", arr)
```

Load the array:

```python
loaded = np.load("data.npy")

print(loaded)
```

For multiple arrays:

```python
np.savez(
    "data.npz",
    values=arr
)
```

---

# 📊 NumPy with Pandas

NumPy is frequently used alongside Pandas.

```python
import numpy as np
import pandas as pd

data = np.array([
    [1, 80],
    [2, 90],
    [3, 75]
])

df = pd.DataFrame(
    data,
    columns=["Student", "Score"]
)

print(df)
```

---

# 📈 NumPy with Matplotlib

NumPy is also commonly used to generate numerical data for visualization.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.title("Sine Wave")

plt.show()
```

This creates a natural workflow:

```text
NumPy
  ↓
Numerical Data
  ↓
Matplotlib
  ↓
Visualization
```

---

# 🤖 NumPy in Machine Learning

NumPy concepts form an important foundation for understanding machine-learning computations.

A typical workflow can look like:

```text
Dataset
   ↓
NumPy Arrays
   ↓
Data Cleaning
   ↓
Feature Processing
   ↓
Mathematical Operations
   ↓
Model Training
   ↓
Prediction
```

NumPy is particularly useful for:

* Feature matrices
* Numerical transformations
* Vector operations
* Matrix operations
* Statistical calculations
* Numerical preprocessing
* Algorithm implementation

---

# 🧪 Practice Exercises

## 🟢 Beginner

* [ ] Create a 1D NumPy array
* [ ] Create a 2D NumPy array
* [ ] Check `shape`, `size`, `ndim`, and `dtype`
* [ ] Practice indexing
* [ ] Practice slicing
* [ ] Create arrays using `zeros()` and `ones()`
* [ ] Generate ranges using `arange()`
* [ ] Generate evenly spaced values using `linspace()`
* [ ] Perform basic arithmetic operations

---

## 🟡 Intermediate

* [ ] Reshape arrays
* [ ] Flatten multidimensional arrays
* [ ] Practice `axis`
* [ ] Use Boolean indexing
* [ ] Use `where()`
* [ ] Sort arrays
* [ ] Use aggregation functions
* [ ] Practice broadcasting
* [ ] Combine arrays with `concatenate()`
* [ ] Use `vstack()` and `hstack()`
* [ ] Generate random datasets

---

## 🔴 Advanced

* [ ] Implement matrix multiplication
* [ ] Calculate matrix determinants
* [ ] Work with matrix inverses
* [ ] Implement vectorized algorithms
* [ ] Build a numerical-statistics project
* [ ] Analyze a dataset using NumPy
* [ ] Generate a synthetic ML dataset
* [ ] Build a NumPy-based linear regression implementation
* [ ] Combine NumPy + Pandas + Matplotlib
* [ ] Optimize a Python loop using vectorization

---

# 📁 Suggested Directory Structure

```text
23-Python-Libraries/
│
└── NumPy/
    │
    ├── README.md
    │
    ├── 01-Introduction/
    │   └── introduction.py
    │
    ├── 02-Array-Creation/
    │   └── array_creation.py
    │
    ├── 03-Array-Properties/
    │   └── array_properties.py
    │
    ├── 04-Indexing-and-Slicing/
    │   └── indexing_slicing.py
    │
    ├── 05-Reshaping/
    │   └── reshaping.py
    │
    ├── 06-Mathematical-Operations/
    │   └── operations.py
    │
    ├── 07-Vectorization/
    │   └── vectorization.py
    │
    ├── 08-Broadcasting/
    │   └── broadcasting.py
    │
    ├── 09-Statistics/
    │   └── statistics.py
    │
    ├── 10-Boolean-and-Advanced-Indexing/
    │   └── indexing.py
    │
    ├── 11-Sorting-and-Searching/
    │   └── sorting.py
    │
    ├── 12-Random/
    │   └── random.py
    │
    ├── 13-Linear-Algebra/
    │   └── linear_algebra.py
    │
    ├── 14-Array-Manipulation/
    │   └── manipulation.py
    │
    ├── 15-File-IO/
    │   └── file_io.py
    │
    └── 16-Projects/
        └── numerical_analysis.py
```

---

# 🛠️ Recommended Learning Workflow

```text
Python Basics
      ↓
NumPy Fundamentals
      ↓
Array Creation
      ↓
Indexing & Slicing
      ↓
Shape & Axis
      ↓
Reshaping
      ↓
Vectorization
      ↓
Broadcasting
      ↓
Statistics
      ↓
Random Numbers
      ↓
Linear Algebra
      ↓
Pandas
      ↓
Matplotlib
      ↓
Machine Learning
```

---

# 💡 Important Concepts to Master

| Concept            | Importance |
| ------------------ | ---------- |
| `ndarray`          | ⭐⭐⭐⭐⭐      |
| `shape`            | ⭐⭐⭐⭐⭐      |
| `axis`             | ⭐⭐⭐⭐⭐      |
| Indexing           | ⭐⭐⭐⭐⭐      |
| Slicing            | ⭐⭐⭐⭐⭐      |
| Reshaping          | ⭐⭐⭐⭐⭐      |
| Vectorization      | ⭐⭐⭐⭐⭐      |
| Broadcasting       | ⭐⭐⭐⭐⭐      |
| Aggregation        | ⭐⭐⭐⭐       |
| Boolean Indexing   | ⭐⭐⭐⭐       |
| Random Sampling    | ⭐⭐⭐⭐       |
| Linear Algebra     | ⭐⭐⭐⭐       |
| Array Manipulation | ⭐⭐⭐⭐       |

---

# ⚡ NumPy Cheat Sheet

### Import

```python
import numpy as np
```

### Create Array

```python
np.array([1, 2, 3])
```

### Zeros

```python
np.zeros((3, 3))
```

### Ones

```python
np.ones((3, 3))
```

### Range

```python
np.arange(0, 10)
```

### Evenly Spaced

```python
np.linspace(0, 1, 10)
```

### Shape

```python
arr.shape
```

### Dimensions

```python
arr.ndim
```

### Reshape

```python
arr.reshape(2, 3)
```

### Sum

```python
arr.sum()
```

### Mean

```python
arr.mean()
```

### Minimum

```python
arr.min()
```

### Maximum

```python
arr.max()
```

### Standard Deviation

```python
arr.std()
```

### Sort

```python
np.sort(arr)
```

### Random Generator

```python
rng = np.random.default_rng()
```

### Matrix Multiplication

```python
A @ B
```

---

# 🧠 Key Takeaways

After completing this module, you should understand:

```text
NumPy
│
├── ndarray
│
├── Array Creation
│
├── Dimensions
├── Shape
├── Size
├── Data Types
│
├── Indexing
├── Slicing
├── Boolean Indexing
│
├── Reshaping
├── Transpose
├── Concatenation
│
├── Vectorization
├── Broadcasting
│
├── Mathematical Operations
├── Statistics
│
├── Random Sampling
│
├── Linear Algebra
│
└── File I/O
```

---

# 📚 Official Learning Resources

* **NumPy Documentation:** [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
* **NumPy Quickstart:** [https://numpy.org/doc/stable/user/quickstart.html](https://numpy.org/doc/stable/user/quickstart.html)
* **Absolute Beginner's Guide:** [https://numpy.org/doc/stable/user/absolute_beginners.html](https://numpy.org/doc/stable/user/absolute_beginners.html)
* **User Guide:** [https://numpy.org/doc/stable/user/](https://numpy.org/doc/stable/user/)
* **API Reference:** [https://numpy.org/doc/stable/reference/](https://numpy.org/doc/stable/reference/)
* **Broadcasting:** [https://numpy.org/doc/stable/user/basics.broadcasting.html](https://numpy.org/doc/stable/user/basics.broadcasting.html)
* **Random Sampling:** [https://numpy.org/doc/stable/reference/random/](https://numpy.org/doc/stable/reference/random/)

The official documentation provides beginner material, a detailed user guide, API reference, and coverage of numerical operations, array manipulation, statistics, random simulation, linear algebra, and more. ([NumPy][2])

---

# 🚀 Next Step

After mastering NumPy, continue with:

```text
NumPy
  ↓
Pandas
  ↓
Matplotlib
  ↓
Seaborn
  ↓
Exploratory Data Analysis
  ↓
Machine Learning
  ↓
Artificial Intelligence
```

NumPy provides the numerical foundation that makes the transition into **Data Science, Machine Learning, and AI** much easier.

---

## 👨‍💻 Repository

This module is part of the **Python Programming** learning repository.

**Repository:** `Kishor055/Python-Programming`

**Module:** `23-Python-Libraries/NumPy`

---

## 📄 License

This educational material is maintained as part of the repository and is intended for **learning, practice, and educational use**.

---

⭐ **If this repository helps you learn Python, consider giving it a star on GitHub.**
