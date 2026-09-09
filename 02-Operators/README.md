Python Operators

A concise and practical guide to Operators in Python, with examples designed for beginners and developers building strong Python fundamentals.

In Python programming, Operators in general are used to perform operations on values and variables.

Operators: Special symbols like -, + , * , /, etc.
Operands: Value on which the operator is applied.

---
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/7a1201b6-1bcf-46f4-9e8f-052228971fda" />

---

📌 Overview

Operators are special symbols or keywords used to perform operations on values and variables.

a = 10
b = 5

print(a + b)  # 15


In the expression above:

+ is the operator
a and b are the operands
🧩 Types of Operators

Python provides several categories of operators:

Operator Type	Purpose	Examples
Arithmetic	Mathematical operations	+, -, *, /
Comparison	Compare values	==, !=, >, <
Logical	Combine conditions	and, or, not
Bitwise	Operations on binary bits	&, `
Assignment	Assign/update values	=, +=, -=, *=
Identity	Check object identity	is, is not
Membership	Check collection membership	in, not in
Ternary	Conditional expression	x if condition else y
1. Arithmetic Operators

Used for mathematical calculations.

a = 15
b = 4

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation

Operators
Operator	Description
+	Addition
-	Subtraction
*	Multiplication
/	Division
//	Floor division
%	Modulus
**	Exponentiation

/ produces a floating-point result, while // performs floor division.

2. Comparison Operators

Comparison operators compare two values and return either True or False.

a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
3. Logical Operators

Logical operators are used to combine or modify conditions.

age = 25
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

Operator	Description
and	True when both conditions are true
or	True when at least one condition is true
not	Reverses the Boolean result
Precedence
not → and → or

4. Bitwise Operators

Bitwise operators perform operations at the binary-bit level.

a = 10
b = 4

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 2)  # Left shift
print(a >> 2)  # Right shift

Operator	Operation
&	Bitwise AND
`	`
^	Bitwise XOR
~	Bitwise NOT
<<	Left shift
>>	Right shift
5. Assignment Operators

Assignment operators assign values to variables and can also update existing values.

x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0


Common assignment operators:

=     +=     -=     *=
/=    //=    %=     **=
&=    |=     ^=     <<=    >>=

6. Identity Operators

Identity operators check whether two variables refer to the same object.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True

Operator	Meaning
is	Same object
is not	Different objects
is vs ==
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False


== compares values, while is checks object identity.

7. Membership Operators

Membership operators check whether a value exists in a sequence or collection.

languages = ["Python", "Java", "C++"]

print("Python" in languages)      # True
print("JavaScript" not in languages)  # True

Operator	Meaning
in	Value exists in collection
not in	Value does not exist in collection
8. Ternary Operator

Python provides a compact conditional expression for choosing between two values.

Syntax
value_if_true if condition else value_if_false

Example
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


Output:

Adult


This is useful when a simple if-else decision needs to be expressed in one line.

⚡ Operator Precedence

When an expression contains multiple operators, precedence determines which operation is evaluated first.

result = 10 + 20 * 3

print(result)


Output:

70


Multiplication is evaluated before addition.

Using parentheses makes the intended order explicit:

result = (10 + 20) * 3

print(result)  # 90

Best Practice

Prefer parentheses when an expression could be difficult to read.

total = (price * quantity) + tax


Readable code is better than relying heavily on memorized precedence rules.

🔄 Operator Associativity

When operators have the same precedence, associativity determines the evaluation direction.

print(100 / 10 * 2)


Operators such as / and * are evaluated from left to right.

Exponentiation behaves differently:

print(2 ** 3 ** 2)


This evaluates as:

2 ** (3 ** 2)


Result:

512

💻 Practical Example

The following example combines multiple operator types:

marks = 85
attendance = 90

passed = marks >= 40 and attendance >= 75

print("Marks:", marks)
print("Attendance:", attendance)
print("Passed:", passed)

result = "PASS" if passed else "FAIL"
print("Result:", result)


Output:

Marks: 85
Attendance: 90
Passed: True
Result: PASS

📁 Recommended File Structure
python-learning/
│
├── 01_variables.py
├── 02_comments.py
├── 03_data_types.py
├── 04_data_types.py
├── 05_input_output.py
├── 06_type_casting.py
├── 07_operators.py
│
└── README.md

🎯 Learning Objectives

After completing this topic, you should be able to:

Understand Python operators and operands.
Perform mathematical calculations.
Compare values using relational operators.
Build complex conditions using logical operators.
Work with binary data using bitwise operators.
Update variables using assignment operators.
Understand the difference between is and ==.
Check collection membership using in and not in.
Write compact conditional expressions.
Understand operator precedence and associativity.
🧠 Quick Reference
# Arithmetic
+  -  *  /  //  %  **

# Comparison
==  !=  >  <  >=  <=

# Logical
and  or  not

# Bitwise
&  |  ^  ~  <<  >>

# Assignment
=  +=  -=  *=  /=  //=  %=  **=

# Identity
is  is not

# Membership
in  not in

# Ternary
value_if_true if condition else value_if_false

▶️ Running the Example

Make sure Python is installed, then run:

python 07_operators.py


On systems where python maps to Python 2 or is unavailable:

python3 07_operators.py

📚 Reference
{"fallbackMarkdown":"GeeksforGeeks — Python Operators
","reference":{"matched_text":"","prefix":null,"start_idx":7788,"end_idx":7881,"safe_urls":[],"refs":[],"alt":"GeeksforGeeks — Python Operators
","prompt_text":null,"type":"url","layout":null,"title":"GeeksforGeeks — Python Operators","item":{"title":"GeeksforGeeks — Python Operators","url":"https://www.geeksforgeeks.org/python/python-operators/?utm_source=chatgpt.com","attribution":"geeksforgeeks.org","pub_date":null,"snippet":null,"attribution_segments":null,"supporting_websites":[],"refs":[],"hue":null,"attributions":null},"logo":null},"showLoginRequiredCard":false}
⭐ Key Takeaway

Operators are fundamental building blocks of Python expressions.

Mastering them early makes it easier to understand conditions, loops, functions, data structures, algorithms, and object-oriented programming.

Happy Coding! 🚀
