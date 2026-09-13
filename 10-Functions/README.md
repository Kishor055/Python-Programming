````
# 🐍 Python Functions

> **Functions are reusable blocks of code that perform a specific task.**

Functions are one of the most important building blocks of Python programming. They allow us to divide a large program into smaller, meaningful, and reusable sections.

Instead of writing the same logic repeatedly, we can define it once inside a function and call it whenever required.

---


## 📌 Why Use Functions?

Functions make programs:

- ♻️ **Reusable** — Write code once and use it multiple times.
- 🧩 **Modular** — Break a large program into smaller components.
- 📖 **Readable** — Make code easier to understand.
- 🛠️ **Maintainable** — Changes can be made in one place.
- 🧪 **Testable** — Individual functions can be tested separately.
- 🚀 **Scalable** — Large applications become easier to organize.

### Function Benefits

```text
                    FUNCTIONS
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
    Reusability     Modularity      Readability
        │               │               │
        └───────────────┼───────────────┘
                        ↓
                  Maintainability
````

---

 # 📚 Topics Covered

 1. What is a Function?
2. Defining a Function
3. Calling a Function
4. Function Arguments
5. Types of Function Arguments
6. Default Arguments
7. Keyword Arguments
8. Positional Arguments
9. Arbitrary Arguments
10. Return Statement
11. Functions Inside Functions
12. Variable Scope
13. Pass-by-Object-Reference
14. Lambda Functions
15. Recursive Functions
16. Practical Example
17. Key Takeaways

---

 # 1\. What is a Function?

 A **function** is a reusable block of code designed to perform a particular task.

 For example, instead of writing code to calculate a square every time, we can create a function:

```
def square(number):
    return number * number
```

 Now we can reuse it:

```
print(square(5))
print(square(10))
print(square(20))
```

 Output:

```
25
100
400
```

---

 # 2\. Defining a Function

 Python functions are defined using the `def` keyword.

 ## Syntax

```
def function_name(parameters):
    # function body
    statements

    return value
```

 ### Example

```
def welcome():
    print("Welcome to Python!")
```

 ### Important Parts

```
def welcome():
│   │       │
│   │       └── Colon starts the function body
│   │
│   └────────── Function name
│
└────────────── Keyword used to define a function
```

 The code inside the function is executed only when the function is called.

---

 # 3\. Calling a Function

 After defining a function, we can execute it by calling its name followed by parentheses.

```
def welcome():
    print("Welcome to Python!")

welcome()
```

 Output:

```
Welcome to Python!
```

 A function can be called multiple times:

```
def message():
    print("Learning Python")

message()
message()
message()
```

 Output:

```
Learning Python
Learning Python
Learning Python
```

---

 # 4\. Function Arguments

 Arguments are values passed to a function when it is called.

```
def greet(name):
    print("Hello", name)

greet("Kishor")
greet("Python")
```

 Output:

```
Hello Kishor
Hello Python
```

 Here:

 - `name` → **Parameter**
- `"Kishor"` → **Argument**

 ### Parameter vs Argument

```
def greet(name):
           ↑
       Parameter

greet("Kishor")
      ↑
    Argument
```

---

 # 5\. Types of Function Arguments

 Python provides different ways to pass arguments to functions.

 ### Main types

 1. Default Arguments
2. Keyword Arguments
3. Positional Arguments
4. Arbitrary Arguments

---

 # 6\. Default Arguments

 A parameter can have a default value.

 If the caller does not provide a value, Python uses the default value.

```
def student(name, course="Python"):
    print("Name:", name)
    print("Course:", course)

student("Kishor")
```

 Output:

```
Name: Kishor
Course: Python
```

 We can also provide our own value:

```
student("Kishor", "Java")
```

 Output:

```
Name: Kishor
Course: Java
```

 ### Another Example

```
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Kishor")
```

 Output:

```
Hello Guest
Hello Kishor
```

---

 # 7\. Keyword Arguments

 Keyword arguments are passed using parameter names.

```
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(name="Kishor", age=20)
```

 We can also change the order:

```
student(age=20, name="Kishor")
```

 Both produce:

```
Name: Kishor
Age: 20
```

 ### Why use keyword arguments?

 They make function calls more readable and allow arguments to be supplied in a different order.

---

 # 8\. Positional Arguments

 With positional arguments, values are assigned to parameters based on their position.

```
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Kishor", 20)
```

 Output:

```
Name: Kishor
Age: 20
```

 The first argument goes to the first parameter, and the second argument goes to the second parameter.

 ### Order Matters

```
student(20, "Kishor")
```

 This produces:

```
Name: 20
Age: Kishor
```

 Python does not automatically determine that `20` should be the age. It follows the parameter order.

---

 # 9\. Arbitrary Arguments

 Sometimes we don't know how many arguments a function will receive.

 Python provides:

 - `*args` → Multiple positional arguments
- `**kwargs` → Multiple keyword arguments

---

 ## `*args`

 `*args` collects additional positional arguments into a tuple.

```
def total(*numbers):
    result = 0

    for number in numbers:
        result += number

    return result

print(total(10, 20))
print(total(10, 20, 30))
print(total(1, 2, 3, 4, 5))
```

 Output:

```
30
60
15
```

 ### Understanding `*args`

```
def show(*args):
    print(args)

show(10, 20, 30)
```

 Output:

```
(10, 20, 30)
```

 So:

```
*args → tuple
```

---

 ## `**kwargs`

 `**kwargs` collects additional keyword arguments into a dictionary.

```
def student(**details):
    print(details)

student(
    name="Kishor",
    age=20,
    course="Python"
)
```

 Output:

```
{'name': 'Kishor', 'age': 20, 'course': 'Python'}
```

 We can iterate through the dictionary:

```
def student(**details):

    for key, value in details.items():
        print(key, "=", value)

student(
    name="Kishor",
    age=20,
    city="Pune"
)
```

 Output:

```
name = Kishor
age = 20
city = Pune
```

 ### Remember

```
*args    → Multiple positional arguments → Tuple

**kwargs → Multiple keyword arguments   → Dictionary
```

---

 # 10\. Return Statement

 The `return` statement sends a result from a function back to the caller.

```
def square(number):
    return number ** 2

result = square(5)

print(result)
```

 Output:

```
25
```

 The returned value can be stored in a variable and reused.

```
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
print(result * 2)
```

 Output:

```
30
60
```

---

 ## `print()` vs `return`

 ### Using `print()`

```
def add(a, b):
    print(a + b)

add(10, 20)
```

 The function displays the result.

 ### Using `return`

```
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

 The function sends the result back to the caller.

 ### Important

 If a function does not explicitly return a value, Python returns:

```
None
```

---

 ## Returning Multiple Values

 Python allows a function to return multiple values.

```
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

result = calculate(10, 5)

print(result)
```

 Output:

```
(15, 5, 50)
```

 The values can also be unpacked:

```
add, subtract, multiply = calculate(10, 5)

print(add)
print(subtract)
print(multiply)
```

---

 # 11\. Functions Inside Functions

 A function can be defined inside another function.

 This is called a **nested function** or **inner function**.

```
def outer():

    message = "Hello from outer function"

    def inner():
        print(message)

    inner()

outer()
```

 Output:

```
Hello from outer function
```

 The inner function can access variables from the enclosing function.

 Nested functions are useful for creating helper functions whose purpose is limited to a particular outer function.

---

 # 12\. Variable Scope

 **Scope** determines where a variable can be accessed.

 ## Local Variable

 A variable created inside a function is local to that function.

```
def demo():
    message = "Hello"
    print(message)

demo()
```

 `message` is available inside `demo()`.

---

 ## Global Variable

 A variable defined outside a function has global scope.

```
message = "Hello Python"

def display():
    print(message)

display()
```

 Output:

```
Hello Python
```

 ### Best Practice

 Prefer passing data through parameters and returning results instead of unnecessarily depending on global variables.

---

 # 13\. Pass-by-Object-Reference

 Python does not simply use traditional "pass by value" or "pass by reference" terminology.

 A useful way to understand Python is:

 > **Function arguments are references to objects.**

 The behavior becomes especially noticeable with **mutable** and **immutable** objects.

---

 ## Mutable Objects

 Lists, dictionaries, and sets are mutable.

 They can be changed inside a function.

```
def change_list(numbers):
    numbers[0] = 100

values = [10, 20, 30]

change_list(values)

print(values)
```

 Output:

```
[100, 20, 30]
```

 The original list was modified.

---

 ## Immutable Objects

 Integers, floats, strings, and tuples are immutable.

```
def change_number(number):
    number = 100

value = 10

change_number(value)

print(value)
```

 Output:

```
10
```

 The original integer remains unchanged.

 ### Key Idea

```
Mutable object
    ↓
Can be modified
    ↓
list, dict, set

Immutable object
    ↓
Cannot be modified in-place
    ↓
int, float, str, tuple
```

---

 # 14\. Lambda Functions

 A **lambda function** is a small anonymous function.

 ### Normal Function

```
def square(x):
    return x * x
```

 ### Lambda Version

```
square = lambda x: x * x

print(square(5))
```

 Output:

```
25
```

 Another example:

```
add = lambda a, b: a + b

print(add(10, 20))
```

 Output:

```
30
```

 Lambda functions are useful for short operations where defining a full function would be unnecessary.

---

 # 15\. Recursive Functions

 A recursive function is a function that calls itself.

 A recursive function normally needs:

 1. **Base Case** — Stops the recursion.
2. **Recursive Case** — Calls the function again.

 ### Factorial Example

```
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

 Output:

```
120
```

 ### Execution

```
factorial(5)
     ↓
5 × factorial(4)
     ↓
5 × 4 × factorial(3)
     ↓
5 × 4 × 3 × factorial(2)
     ↓
5 × 4 × 3 × 2 × factorial(1)
     ↓
120
```

 The base condition:

```
if n == 0:
    return 1
```

 prevents infinite recursion.

---

 # 16\. Practical Example — Calculator

 Functions are especially useful when building larger programs.

```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
```

 Output:

```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

 ### Why is this better?

 Instead of one large block of code, every operation has its own responsibility:

```
Calculator
    │
    ├── add()
    ├── subtract()
    ├── multiply()
    └── divide()
```

 This makes the program easier to read, test, and modify.

---

 # 🔄 Function Execution Flow

 Consider this function:

```
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)

print(answer)
```

 Execution flow:

```
        add(10, 20)
             │
             ↓
       a = 10, b = 20
             │
             ↓
       result = 30
             │
             ↓
       return result
             │
             ↓
       answer = 30
             │
             ↓
       print(answer)
             │
             ↓
             30
```

---

 # 🧠 Function Cheat Sheet

 | Concept | Example |
| --- | --- |
| Define | `def greet():` |
| Call | `greet()` |
| Parameter | `def greet(name):` |
| Argument | `greet("Kishor")` |
| Return | `return result` |
| Default argument | `name="Guest"` |
| Keyword argument | `name="Kishor"` |
| Positional argument | `greet("Kishor")` |
| Multiple positional arguments | `*args` |
| Multiple keyword arguments | `**kwargs` |
| Nested function | Function inside function |
| Lambda | `lambda x: x * x` |
| Recursion | Function calling itself |

---

 # ⚠️ Common Mistakes

 ## Forgetting to Call the Function

```
def greet():
    print("Hello")

# Nothing happens yet
```

 You need:

```
greet()
```

---

 ## Forgetting Parentheses

 Incorrect:

```
greet
```

 Correct:

```
greet()
```

---

 ## Forgetting `return`

 Incorrect:

```
def add(a, b):
    result = a + b

print(add(10, 20))
```

 Output:

```
None
```

 Correct:

```
def add(a, b):
    return a + b
```

---

 ## Incorrect Argument Order

```
def student(name, age):
    print(name, age)

student(20, "Kishor")
```

 The values are assigned according to position.

---

 # 🏆 Best Practices

 ### 1\. Use meaningful function names

 Good:

```
calculate_total()
validate_email()
find_student()
```

 Avoid:

```
x()
abc()
fun1()
```

 ### 2\. Keep functions focused

 A function should ideally have one clear responsibility.

 ### 3\. Use parameters instead of unnecessary global variables

```
def calculate_total(price, quantity):
    return price * quantity
```

 ### 4\. Return values when they need to be reused

```
def calculate_area(length, width):
    return length * width
```

 ### 5\. Keep functions small and readable

 Small functions are generally easier to test and maintain.

---

 # 📝 Practice Questions

 Try solving these problems using functions:

 ### Beginner

 1. Write a function to print `"Hello Python"`.
2. Write a function to add two numbers.
3. Write a function to find the square of a number.
4. Write a function to check whether a number is even or odd.
5. Write a function to find the largest of two numbers.

 ### Intermediate

 6. Write a function to calculate factorial.
7. Write a function to check whether a number is prime.
8. Write a function to reverse a string.
9. Write a function to count vowels in a string.
10. Write a function to calculate the average of numbers using `*args`.

 ### Advanced

 11. Create a calculator using separate functions.
12. Create a function using `**kwargs` to display student information.
13. Write a recursive function to calculate Fibonacci numbers.
14. Write a function that accepts another function as an argument.
15. Create a menu-driven program using functions.

---

 # 🎯 Key Takeaways

 After completing this topic, you should understand:

 - ✅ What functions are
- ✅ Why functions are useful
- ✅ How to define and call functions
- ✅ Parameters and arguments
- ✅ Positional arguments
- ✅ Keyword arguments
- ✅ Default arguments
- ✅ `*args`
- ✅ `**kwargs`
- ✅ `return`
- ✅ Nested functions
- ✅ Variable scope
- ✅ Mutable vs immutable objects
- ✅ Lambda functions
- ✅ Recursive functions
- ✅ Writing modular and reusable programs

---

 # 📂 Practice Files

 The Python examples and exercises for this topic are available in this folder.

```
10-Functions/
│
├── README.md
├── ...
└── ...
```

 Explore each Python file and run the examples yourself.

---

 ## 📖 References

 - Python Functions — GeeksforGeeks
- Python Documentation — Defining Functions

---

 ⭐ **Keep practicing — mastering functions is an important step toward writing clean, reusable, and maintainable Python programs.**

````

### One recommendation for your repository

Since you already have the **“Why Use Function”** and **function syntax** images, I'd put them near the beginning of the README, immediately after the introduction:

```markdown
## 📌 Why Use Functions?

![Why Use Functions](./images/why-use-functions.png)

Functions help us create reusable, modular, readable, and maintainable code.

## 🧱 Anatomy of a Python Function

![Python Function Syntax](./images/python-function-syntax.png)
````

