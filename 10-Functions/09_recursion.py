"""
09 - Recursion
==============

Recursion is a programming technique in which a function
calls itself to solve a problem.

A recursive function usually has two important parts:

1. Base Case
   -> Stops the recursion.

2. Recursive Case
   -> The function calls itself with a smaller/simpler input.


Basic structure:

    def function():
        if base_condition:
            return result

        return function(smaller_input)


Example:

    def countdown(n):

        if n == 0:
            return

        print(n)
        countdown(n - 1)


    countdown(5)


Output:

    5
    4
    3
    2
    1


IMPORTANT:
----------
Every recursive function must eventually reach its base case.

If the base case is missing or never reached,
Python raises RecursionError.
"""


# ============================================================
# 1. Simple Recursion
# ============================================================

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)


countdown(5)


# ============================================================
# 2. Understanding the Base Case
# ============================================================

"""
The base case tells Python when to stop.

For:

    countdown(5)

The calls are:

    countdown(5)
        countdown(4)
            countdown(3)
                countdown(2)
                    countdown(1)
                        countdown(0)

At countdown(0), the base case is reached.

The function stops calling itself.
"""


# ============================================================
# 3. Countdown Using Recursion
# ============================================================

def countdown_recursive(n):

    if n <= 0:
        print("Done!")
        return

    print(n)

    countdown_recursive(n - 1)


countdown_recursive(5)


# ============================================================
# 4. Count Up Using Recursion
# ============================================================

def count_up(n):

    if n == 0:
        return

    count_up(n - 1)

    print(n)


count_up(5)


"""
Notice the difference:

Countdown:

    print(n)
    function(n - 1)


Count up:

    function(n - 1)
    print(n)

The position of the recursive call changes the output.
"""


# ============================================================
# 5. Factorial Using Recursion
# ============================================================

"""
Factorial:

    5! = 5 × 4 × 3 × 2 × 1
       = 120

Mathematically:

    n! = n × (n - 1)!

Base case:

    0! = 1
"""


def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print("5! =", factorial(5))
print("6! =", factorial(6))
print("7! =", factorial(7))


# ============================================================
# 6. How Recursive Factorial Works
# ============================================================

"""
factorial(5)

= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)

factorial(0) returns 1.

Then the results return back:

1
2
6
24
120
"""


# ============================================================
# 7. Factorial with Input Validation
# ============================================================

def factorial_safe(n):

    if n < 0:
        return "Factorial is not defined for negative numbers."

    if n == 0:
        return 1

    return n * factorial_safe(n - 1)


print(factorial_safe(5))
print(factorial_safe(0))
print(factorial_safe(-5))


# ============================================================
# 8. Sum of Numbers Using Recursion
# ============================================================

"""
Calculate:

    1 + 2 + 3 + 4 + 5 = 15
"""


def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("Sum:", sum_numbers(5))
print("Sum:", sum_numbers(10))


# ============================================================
# 9. Sum from a to b
# ============================================================

def range_sum(a, b):

    if a > b:
        return 0

    return a + range_sum(a + 1, b)


print(range_sum(1, 5))
print(range_sum(5, 10))


# ============================================================
# 10. Power Using Recursion
# ============================================================

"""
Calculate:

    2^5 = 32
"""


def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(2, 5))
print(power(3, 4))


# ============================================================
# 11. Reverse a String Using Recursion
# ============================================================

def reverse_string(text):

    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print(reverse_string("Python"))
print(reverse_string("Hello"))


"""
Example:

reverse_string("ABC")

= reverse_string("BC") + "A"
= reverse_string("C") + "B" + "A"
= "CBA"
"""


# ============================================================
# 12. Check Palindrome Using Recursion
# ============================================================

"""
A palindrome reads the same forward and backward.

Examples:

    madam
    level
    radar
"""


def is_palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("madam"))
print(is_palindrome("level"))
print(is_palindrome("python"))


# ============================================================
# 13. Fibonacci Using Recursion
# ============================================================

"""
Fibonacci sequence:

    0, 1, 1, 2, 3, 5, 8, 13, ...

Formula:

    F(n) = F(n - 1) + F(n - 2)

Base cases:

    F(0) = 0
    F(1) = 1
"""


def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))


# ============================================================
# 14. Print Fibonacci Sequence
# ============================================================

def print_fibonacci(n):

    for i in range(n):
        print(fibonacci(i), end=" ")


print_fibonacci(10)
print()


# ============================================================
# 15. Fibonacci - Recursion Tree
# ============================================================

"""
For:

    fibonacci(5)

The function calls:

                    fib(5)
                   /      \
                fib(4)    fib(3)
                /   \      /   \
             fib(3) fib(2) fib(2) fib(1)

Each call creates more function calls.

This is why the simple recursive Fibonacci solution
becomes slow for larger values.
"""


# ============================================================
# 16. Greatest Common Divisor (GCD)
# ============================================================

"""
Euclidean algorithm:

    gcd(a, b) = gcd(b, a % b)

Base case:

    gcd(a, 0) = a
"""


def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


print("GCD:", gcd(48, 18))
print("GCD:", gcd(100, 25))


# ============================================================
# 17. Recursive Countdown with Debugging
# ============================================================

def debug_countdown(n):

    print("Entering:", n)

    if n == 0:
        print("Base case reached")
        return

    debug_countdown(n - 1)

    print("Returning from:", n)


debug_countdown(3)


"""
This demonstrates two stages:

Going down:

    Entering: 3
    Entering: 2
    Entering: 1
    Entering: 0

Coming back:

    Returning from: 1
    Returning from: 2
    Returning from: 3
"""


# ============================================================
# 18. Recursion and the Call Stack
# ============================================================

"""
Each function call is placed on the call stack.

For:

    factorial(3)

The stack grows:

    factorial(3)
    factorial(2)
    factorial(1)
    factorial(0)

After the base case:

    factorial(0) -> 1
    factorial(1) -> 1
    factorial(2) -> 2
    factorial(3) -> 6

The stack then unwinds.

Think of recursion as:

    CALLS GO DOWN
           ↓
    BASE CASE
           ↓
    RESULTS COME BACK UP
"""


# ============================================================
# 19. Recursive Multiplication
# ============================================================

"""
Calculate multiplication using repeated addition.

    4 × 3
    = 4 + 4 + 4
    = 12
"""


def multiply(a, b):

    if b == 0:
        return 0

    return a + multiply(a, b - 1)


print(multiply(4, 3))
print(multiply(7, 5))


# ============================================================
# 20. Count Digits Using Recursion
# ============================================================

def count_digits(n):

    n = abs(n)

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


print(count_digits(12345))
print(count_digits(987654))
print(count_digits(7))


# ============================================================
# 21. Sum of Digits Using Recursion
# ============================================================

"""
Example:

    1234

    1 + 2 + 3 + 4 = 10
"""


def sum_digits(n):

    n = abs(n)

    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


print(sum_digits(1234))
print(sum_digits(98765))


# ============================================================
# 22. Reverse a Number Using Recursion
# ============================================================

def reverse_number(n, result=0):

    if n == 0:
        return result

    return reverse_number(
        n // 10,
        result * 10 + n % 10
    )


print(reverse_number(12345))
print(reverse_number(9876))


# ============================================================
# 23. Count Occurrences in a List
# ============================================================

def count_value(numbers, target, index=0):

    if index == len(numbers):
        return 0

    if numbers[index] == target:
        return 1 + count_value(
            numbers,
            target,
            index + 1
        )

    return count_value(
        numbers,
        target,
        index + 1
    )


numbers = [10, 20, 10, 30, 10, 40]

print(
    count_value(numbers, 10)
)


# ============================================================
# 24. Find Maximum in a List Recursively
# ============================================================

def recursive_max(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]

    current = numbers[index]
    maximum_rest = recursive_max(
        numbers,
        index + 1
    )

    return max(current, maximum_rest)


numbers = [10, 50, 20, 80, 30]

print(
    "Maximum:",
    recursive_max(numbers)
)


# ============================================================
# 25. Find Minimum in a List Recursively
# ============================================================

def recursive_min(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]

    current = numbers[index]
    minimum_rest = recursive_min(
        numbers,
        index + 1
    )

    return min(current, minimum_rest)


numbers = [10, 50, 20, 80, 30]

print(
    "Minimum:",
    recursive_min(numbers)
)


# ============================================================
# 26. Search an Element Recursively
# ============================================================

def search(numbers, target, index=0):

    if index == len(numbers):
        return False

    if numbers[index] == target:
        return True

    return search(
        numbers,
        target,
        index + 1
    )


numbers = [10, 20, 30, 40, 50]

print(search(numbers, 30))
print(search(numbers, 100))


# ============================================================
# 27. Find Index Recursively
# ============================================================

def find_index(numbers, target, index=0):

    if index == len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return find_index(
        numbers,
        target,
        index + 1
    )


numbers = [10, 20, 30, 40, 50]

print(find_index(numbers, 30))
print(find_index(numbers, 100))


# ============================================================
# 28. Binary Search Using Recursion
# ============================================================

"""
Binary search works on a sorted list.

Example:

    [10, 20, 30, 40, 50, 60, 70]

Instead of checking every element, we check the middle.

If target is smaller:
    search left half.

If target is larger:
    search right half.
"""


def binary_search(numbers, target, low, high):

    if low > high:
        return -1

    middle = (low + high) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search(
            numbers,
            target,
            low,
            middle - 1
        )

    return binary_search(
        numbers,
        target,
        middle + 1,
        high
    )


numbers = [10, 20, 30, 40, 50, 60, 70]

index = binary_search(
    numbers,
    50,
    0,
    len(numbers) - 1
)

print("Index:", index)


# ============================================================
# 29. Nested List Recursion
# ============================================================

"""
Recursion is especially useful for nested structures.

Example:

    [1, [2, 3], [4, [5, 6]]]
"""


def print_nested(data):

    for item in data:

        if isinstance(item, list):
            print_nested(item)

        else:
            print(item)


nested = [
    1,
    [2, 3],
    [4, [5, 6]]
]

print_nested(nested)


# ============================================================
# 30. Sum a Nested List
# ============================================================

def sum_nested(data):

    total = 0

    for item in data:

        if isinstance(item, list):
            total += sum_nested(item)

        else:
            total += item

    return total


nested = [
    1,
    [2, 3],
    [4, [5, 6]]
]

print(
    "Nested Sum:",
    sum_nested(nested)
)


# ============================================================
# 31. Recursive String Processing
# ============================================================

def print_characters(text, index=0):

    if index == len(text):
        return

    print(text[index])

    print_characters(
        text,
        index + 1
    )


print_characters("Python")


# ============================================================
# 32. Count Vowels Recursively
# ============================================================

def count_vowels(text, index=0):

    if index == len(text):
        return 0

    vowels = "aeiouAEIOU"

    count = 1 if text[index] in vowels else 0

    return count + count_vowels(
        text,
        index + 1
    )


print(
    count_vowels("Python Programming")
)


# ============================================================
# 33. Check Whether a List is Sorted
# ============================================================

def is_sorted(numbers, index=0):

    if index >= len(numbers) - 1:
        return True

    if numbers[index] > numbers[index + 1]:
        return False

    return is_sorted(
        numbers,
        index + 1
    )


print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))


# ============================================================
# 34. Recursive Power with Negative Exponents
# ============================================================

def power_extended(base, exponent):

    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / power_extended(
            base,
            -exponent
        )

    return base * power_extended(
        base,
        exponent - 1
    )


print(power_extended(2, 5))
print(power_extended(2, -2))


# ============================================================
# 35. Recursion vs Loop
# ============================================================

"""
The same problem can often be solved using a loop.

Recursive:

    def factorial(n):
        if n == 0:
            return 1

        return n * factorial(n - 1)


Loop:

    def factorial_loop(n):

        result = 1

        for i in range(1, n + 1):
            result *= i

        return result


Both produce the same result.
"""


def factorial_loop(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial_loop(5))


# ============================================================
# 36. Recursion vs Iteration
# ============================================================

"""
Recursion:

    Function calls itself.

Advantages:
    - Elegant for tree-like problems.
    - Useful for divide-and-conquer algorithms.
    - Natural for nested data.
    - Can make some algorithms easier to understand.

Disadvantages:
    - Uses the call stack.
    - Can use more memory.
    - Can be slower than a loop.
    - Python has a recursion depth limit.

Iteration:

    Uses loops such as for and while.

Advantages:
    - Usually more memory efficient.
    - Often faster for simple repetition.
    - No recursive call stack.

Rule:
    Use recursion when it makes the problem simpler.
    Use loops when simple repetition is enough.
"""


# ============================================================
# 37. Recursion Limit
# ============================================================

import sys

print(
    "Python recursion limit:",
    sys.getrecursionlimit()
)


"""
Python limits how deeply functions can recursively call
themselves.

This helps prevent the program from exhausting the call stack.
"""


# ============================================================
# 38. Example of Infinite Recursion
# ============================================================

"""
DO NOT RUN this function.

There is no base case:

    def infinite():
        infinite()


Calling:

    infinite()

would eventually produce:

    RecursionError:
    maximum recursion depth exceeded
"""


# ============================================================
# 39. A Safer Example with a Base Case
# ============================================================

def safe_recursion(n):

    if n <= 0:
        print("Stopped.")
        return

    print(n)

    safe_recursion(n - 1)


safe_recursion(5)


# ============================================================
# 40. Recursion with Multiple Recursive Calls
# ============================================================

def countdown_two(n):

    if n <= 0:
        return

    print(n)

    countdown_two(n - 1)
    countdown_two(n - 2)


# Uncomment to see the recursive tree:
#
# countdown_two(4)


"""
A function can call itself more than once.

This creates a branching recursion tree.

Fibonacci is another example:

    fibonacci(n)
        ├── fibonacci(n - 1)
        └── fibonacci(n - 2)
"""


# ============================================================
# 41. Recursive Fibonacci with Memoization
# ============================================================

"""
Memoization stores previously calculated results.

This avoids repeating the same calculations.
"""


def fibonacci_memo(n, memo=None):

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1:
        return 1

    memo[n] = (
        fibonacci_memo(n - 1, memo)
        + fibonacci_memo(n - 2, memo)
    )

    return memo[n]


print(fibonacci_memo(30))


# ============================================================
# 42. Recursive Function with Multiple Parameters
# ============================================================

def countdown_range(start, end):

    if start > end:
        return

    print(start)

    countdown_range(
        start + 1,
        end
    )


countdown_range(1, 5)


# ============================================================
# 43. Recursive Multiplication Table
# ============================================================

def multiplication_table(number, multiplier=1):

    if multiplier > 10:
        return

    print(
        f"{number} x {multiplier} = "
        f"{number * multiplier}"
    )

    multiplication_table(
        number,
        multiplier + 1
    )


multiplication_table(5)


# ============================================================
# 44. Recursive Countdown Timer Concept
# ============================================================

def countdown_message(n):

    if n == 0:
        print("Go!")
        return

    print(n)

    countdown_message(n - 1)


countdown_message(5)


# ============================================================
# 45. Practical Example - Folder Structure
# ============================================================

"""
Recursion is commonly useful for structures such as:

    Folder
    ├── file.txt
    ├── images
    │   ├── photo1.jpg
    │   └── photo2.jpg
    └── documents
        ├── notes.txt
        └── projects
            └── project.py

A folder can contain another folder.

That means the structure is naturally recursive.
"""


# ============================================================
# 46. Practical Example - Tree-like Data
# ============================================================

tree = {
    "name": "Root",
    "children": [
        {
            "name": "Folder A",
            "children": []
        },
        {
            "name": "Folder B",
            "children": [
                {
                    "name": "Folder C",
                    "children": []
                }
            ]
        }
    ]
}


def print_tree(node, level=0):

    print("  " * level + node["name"])

    for child in node["children"]:
        print_tree(
            child,
            level + 1
        )


print_tree(tree)


# ============================================================
# 47. Practical Example - Nested Dictionary Search
# ============================================================

def find_name(node, target):

    if node["name"] == target:
        return True

    for child in node.get("children", []):

        if find_name(child, target):
            return True

    return False


print(find_name(tree, "Folder C"))
print(find_name(tree, "Folder X"))


# ============================================================
# 48. Base Case + Recursive Case
# ============================================================

"""
Every recursive function should be easy to divide into:

BASE CASE
---------

The condition that stops recursion.


RECURSIVE CASE
--------------

The part that calls the function again with
a smaller or simpler problem.


Example:

    def factorial(n):

        # Base case
        if n == 0:
            return 1

        # Recursive case
        return n * factorial(n - 1)
"""


# ============================================================
# 49. Three Questions for Any Recursive Function
# ============================================================

"""
When writing recursion, ask:

1. What is my base case?

2. What is my recursive case?

3. Does every recursive call move toward the base case?


Example:

    def countdown(n):

        if n == 0:          # 1. Base case
            return

        print(n)

        countdown(n - 1)    # 2. Recursive case

                            # 3. n gets smaller
"""


# ============================================================
# 50. Common Recursion Mistakes
# ============================================================

"""
Mistake 1:
----------
No base case.

    def test(n):
        return test(n - 1)


Mistake 2:
----------
Base case exists but is never reached.

    def test(n):
        if n == 0:
            return

        test(n + 1)


Mistake 3:
----------
Wrong recursive condition.

Mistake 4:
----------
Creating too many recursive calls.

Mistake 5:
----------
Using recursion where a simple loop is clearer.
"""


# ============================================================
# 51. Mini Practice
# ============================================================

# Practice 1:
# Write a recursive function to print numbers from 1 to 10.


# Practice 2:
# Write a recursive function to print numbers from 10 to 1.


# Practice 3:
# Write a recursive function to calculate factorial.


# Practice 4:
# Write a recursive function to calculate the sum from
# 1 to n.


# Practice 5:
# Write a recursive function to calculate x^n.


# Practice 6:
# Write a recursive function to reverse a string.


# Practice 7:
# Write a recursive function to check whether a string
# is a palindrome.


# Practice 8:
# Write a recursive function to calculate the nth
# Fibonacci number.


# Practice 9:
# Write a recursive function to find the maximum value
# in a list.


# Practice 10:
# Write a recursive function to search for an element
# in a list.


# Practice 11:
# Write a recursive function to count the digits of
# a number.


# Practice 12:
# Write a recursive function to calculate the sum of
# all digits in a number.


# Practice 13:
# Write a recursive function to count vowels in a string.


# Practice 14:
# Write a recursive function to check whether a list
# is sorted.


# Practice 15:
# Create a recursive function that prints a nested list.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. Recursion means a function calls itself.

2. Every recursive function needs a base case.

3. The recursive case calls the function again.

4. Each recursive call should move toward the base case.

5. Factorial is a classic recursion example.

6. Fibonacci demonstrates multiple recursive calls.

7. Recursion uses the call stack.

8. Python has a recursion depth limit.

9. Too much recursion can cause RecursionError.

10. Recursion is useful for:
       - Trees
       - Nested lists
       - Nested dictionaries
       - Divide-and-conquer algorithms
       - Searching
       - Backtracking
       - Mathematical problems

11. Many recursive problems can also be solved using loops.

12. Recursion is not always better than iteration.

13. Use recursion when it makes the solution clearer.

14. For simple repetition, a loop is often more efficient.

15. Memoization can improve recursive algorithms by
    storing previously calculated results.
"""
