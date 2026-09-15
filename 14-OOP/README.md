# 🧱 14 — Object-Oriented Programming (OOP)

> **Learn how to design Python programs using classes, objects, inheritance, polymorphism, encapsulation, and abstraction.**

Object-Oriented Programming (**OOP**) is a programming paradigm that organizes software around **objects** that contain both **data** and **behavior**.

Python is a powerful object-oriented language. Classes provide a way to bundle data and functionality together, while inheritance allows classes to reuse and extend existing behavior.

---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

* What is Object-Oriented Programming?
* Classes and Objects
* Attributes and Methods
* `self`
* `__init__()`
* Instance Variables
* Class Variables
* Instance Methods
* Class Methods
* Static Methods
* Encapsulation
* Public, Protected, and Private conventions
* Name Mangling
* Inheritance
* Types of Inheritance
* `super()`
* Method Overriding
* Polymorphism
* Duck Typing
* Abstraction
* Abstract Classes
* `abc` module
* Composition
* Aggregation
* Magic / Dunder Methods
* Properties
* Dataclasses
* OOP Best Practices
* Real-world OOP design

---

# 🧠 1. What is OOP?

**Object-Oriented Programming** is a programming approach where software is designed around objects.
**Object Oriented Programming empowers developers to build modular, maintainable and scalable applications. OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOP, object has attributes thing that has specific data and can perform certain actions using methods.
Organizes code into classes and objects.
Supports encapsulation to group data and methods together.
Enables inheritance for reusability and hierarchy.
Allows polymorphism for flexible method implementation.**

---
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/c864571f-7b1f-43b5-ab7b-ababe90b1541" />

---

An object can contain:

```text
Data
 +
Behavior
```

For example, a `Car` object may contain:

```text
Data:
    brand
    model
    speed

Behavior:
    start()
    stop()
    accelerate()
```

Conceptually:

```text
             🚗 Car
               │
       ┌───────┴────────┐
       │                │
     Data            Methods
       │                │
   brand              start()
   model              stop()
   speed              accelerate()
```

---

# 🧩 2. Why Use OOP?

Without OOP, large applications can become difficult to organize.

OOP helps with:

| Benefit             | Description                                  |
| ------------------- | -------------------------------------------- |
| ♻️ Reusability      | Reuse existing code                          |
| 🧩 Modularity       | Divide applications into logical components  |
| 🔒 Encapsulation    | Keep data and behavior together              |
| 🌳 Inheritance      | Extend existing classes                      |
| 🔄 Polymorphism     | Use a common interface for different objects |
| 🛠️ Maintainability | Easier to modify large systems               |
| 🧪 Testability      | Components can be tested independently       |

---

# 🧱 3. Class

A **class** is a blueprint for creating objects.

Syntax:

```python
class ClassName:
    # attributes
    # methods
    pass
```

Example:

```python
class Student:
    pass
```

A class definition creates a class object that can later be instantiated into objects.

---

# 👤 4. Object

An **object** is an instance of a class.

```python
class Student:
    pass


student1 = Student()
student2 = Student()
```

Here:

```text
Student
   ↓
 Class
   ↓
 ┌──────────────┐
 │              │
student1     student2
 Object         Object
```

Each instance is a separate object.

---

# 🏷️ 5. Attributes

Attributes represent the data associated with an object.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Kishor", 25)

print(student.name)
print(student.age)
```

Output:

```text
Kishor
25
```

---

# ⚙️ 6. Methods

Methods are functions defined inside a class.

```python
class Student:

    def greet(self):
        print("Hello!")


student = Student()

student.greet()
```

Output:

```text
Hello!
```

A method normally receives the instance as its first parameter, conventionally named `self`.

---

# 👤 7. Understanding `self`

`self` refers to the current instance.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Kishor")

student.display()
```

When you call:

```python
student.display()
```

Python effectively passes the instance to the method.

Conceptually:

```python
Student.display(student)
```

The name `self` is a convention, not a Python keyword, but following it is strongly recommended for readability.

---

# 🚀 8. `__init__()` Constructor

`__init__()` is commonly used to initialize an object's state.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee = Employee("Kishor", 50000)
```

When the object is created, Python automatically calls `__init__()` for initialization when it is defined.

---

# 📦 9. Instance Variables

Instance variables belong to individual objects.

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Kishor")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)
```

Each object has its own `name`.

```text
student1 → name = Kishor
student2 → name = Rahul
```

---

# 🌐 10. Class Variables

Class variables are shared by instances unless an instance provides its own attribute with the same name.

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Kishor")
student2 = Student("Rahul")

print(student1.school)
print(student2.school)
```

Output:

```text
ABC School
ABC School
```

Python's documentation distinguishes class variables, which are shared, from instance variables, which are unique to each instance.

---

# ⚙️ 11. Instance Methods

Instance methods operate on individual objects.

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(1000)

account.deposit(500)

print(account.balance)
```

Output:

```text
1500
```

---

# 🏫 12. Class Methods

A class method operates on the class rather than a particular instance.

Use:

```python
@classmethod
```

Example:

```python
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name


Student.change_school("XYZ School")

print(Student.school)
```

`cls` conventionally refers to the class.

---

# 🔧 13. Static Methods

A static method does not require an instance or class reference.

Use:

```python
@staticmethod
```

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

Output:

```text
30
```

Use static methods when the operation logically belongs to the class but doesn't need instance or class state.

---

# 🔐 14. Encapsulation

**Encapsulation** means keeping related data and behavior together and controlling how implementation details are accessed.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
```

The `_balance` attribute communicates:

> This is an internal implementation detail.

Python relies heavily on naming conventions rather than strict access modifiers.

---

# 🟢 15. Public Members

Public members can be accessed normally.

```python
class Student:

    def __init__(self):
        self.name = "Kishor"


student = Student()

print(student.name)
```

---

# 🟡 16. Protected Convention

Python commonly uses a single underscore:

```python
_name
```

Example:

```python
class Student:

    def __init__(self):
        self._name = "Kishor"
```

This means:

> `_name` is intended for internal use.

It is a **convention**, not strict enforcement.

---

# 🔴 17. Private Variables and Name Mangling

Python doesn't provide traditional private instance variables that are completely inaccessible.

However, names beginning with two underscores trigger **name mangling**.

```python
class Student:

    def __init__(self):
        self.__name = "Kishor"
```

Trying:

```python
student.__name
```

does not directly access the attribute.

Python internally transforms the name approximately to:

```text
_Student__name
```

Name mangling is primarily designed to avoid accidental name conflicts with subclasses, not to provide absolute security.

---

# 🌳 18. Inheritance

**Inheritance** allows a class to reuse and extend another class.

```python
class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()
```

Output:

```text
Animal speaks
Dog barks
```

Python supports inheritance and allows derived classes to override methods from base classes.

---

# 🧬 19. Types of Inheritance

Common inheritance structures include:

```text
Single
Multiple
Multilevel
Hierarchical
Hybrid
```

---

# 1️⃣ Single Inheritance

```text
Animal
   ↓
 Dog
```

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

---

# 2️⃣ Multilevel Inheritance

```text
Animal
   ↓
Mammal
   ↓
Dog
```

```python
class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass
```

---

# 3️⃣ Multiple Inheritance

Python supports multiple base classes.

```text
Father ──┐
         ├── Child
Mother ──┘
```

```python
class Father:

    def skills(self):
        print("Driving")


class Mother:

    def cooking(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skills()
child.cooking()
```

Python supports multiple inheritance and uses a method resolution order (MRO) to determine attribute lookup.

---

# 4️⃣ Hierarchical Inheritance

```text
       Animal
       /     \
     Dog     Cat
```

```python
class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

---

# 5️⃣ Hybrid Inheritance

Hybrid inheritance combines multiple inheritance patterns.

```text
        Animal
       /      \
    Mammal    Bird
       \      /
        Hybrid
```

Python's flexible inheritance system allows complex class hierarchies, but simpler designs are usually easier to maintain.

---

# 🔄 20. Method Overriding

A child class can redefine a method inherited from its parent.

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Woof!")


dog = Dog()

dog.speak()
```

Output:

```text
Woof!
```

This is called **method overriding**.

---

# 🦸 21. `super()`

`super()` is commonly used to call functionality from a parent class.

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Bruno", "Labrador")

print(dog.name)
print(dog.breed)
```

Output:

```text
Bruno
Labrador
```

`super()` is especially important in inheritance hierarchies and cooperative multiple inheritance.

---

# 🔄 22. Polymorphism

**Polymorphism** means that different objects can provide the same interface while implementing behavior differently.

Example:

```python
class Dog:

    def speak(self):
        print("Woof!")


class Cat:

    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

```text
Woof!
Meow!
```

The same method call:

```python
animal.speak()
```

works with different object types.

---

# 🦆 23. Duck Typing

Python often uses **duck typing**.

> If an object behaves like the required type, its exact class may not matter.

Example:

```python
class Dog:

    def speak(self):
        print("Woof!")


class Person:

    def speak(self):
        print("Hello!")


def make_speak(obj):
    obj.speak()


make_speak(Dog())
make_speak(Person())
```

The function only cares that the object provides `speak()`.

This style is closely related to Python's dynamic object model and is a major part of idiomatic Python programming.

---

# 🎭 24. Abstraction

**Abstraction** means exposing the important interface while hiding unnecessary implementation details.

For example:

```text
User
 ↓
withdraw()
 ↓
Bank System
 ↓
Complex internal operations
```

The user doesn't need to know every internal implementation detail.

---

# 🧩 25. Abstract Classes

Python provides the `abc` module for defining abstract base classes.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

A subclass must implement the abstract method:

```python
class Dog(Animal):

    def speak(self):
        print("Woof!")
```

---

# 🏗️ 26. Complete Abstraction Example

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(10, 5)

print(rectangle.area())
```

Output:

```text
50
```

---

# 🧱 27. The Four Pillars of OOP

The commonly taught four pillars are:

```text
             OOP
              │
      ┌───────┼────────┐
      │       │        │
Encapsulation Inheritance Polymorphism
      │       │        │
      └──── Abstraction ────┘
```

| Pillar           | Purpose                                 |
| ---------------- | --------------------------------------- |
| 🔐 Encapsulation | Bundle and control data/behavior        |
| 🌳 Inheritance   | Reuse and extend existing classes       |
| 🔄 Polymorphism  | Same interface, different behavior      |
| 🎭 Abstraction   | Hide unnecessary implementation details |

---

# 🔗 28. Composition

**Composition** means building a class using objects of other classes.

Example:

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()

car.start()
```

Relationship:

```text
Car
 │
 └── Engine
```

Composition often provides more flexibility than deep inheritance hierarchies.

---

# 🤝 29. Aggregation

Aggregation represents a weaker "has-a" relationship where the contained object can exist independently.

Example:

```python
class Teacher:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher("Kishor")

department = Department(teacher)
```

The teacher can exist independently of the department.

---

# 🪄 30. Magic / Dunder Methods

Python provides special methods surrounded by double underscores.

Examples:

```text
__init__
__str__
__repr__
__len__
__eq__
__add__
__lt__
```

These methods allow classes to integrate naturally with Python syntax and built-in operations.

---

# 🖨️ 31. `__str__()`

`__str__()` defines a user-friendly string representation.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


student = Student("Kishor")

print(student)
```

Output:

```text
Student: Kishor
```

---

# 🔍 32. `__repr__()`

`__repr__()` is intended to provide an unambiguous representation useful for debugging and development.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name!r})"


student = Student("Kishor")

print(repr(student))
```

---

# ➕ 33. Operator Overloading

Special methods allow classes to define behavior for operators.

Example:

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2

print(p3.x, p3.y)
```

Output:

```text
6 8
```

---

# 📏 34. `__len__()`

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["A", "B", "C"])

print(len(team))
```

Output:

```text
3
```

---

# 🧪 35. `isinstance()`

Use `isinstance()` to check whether an object is an instance of a class.

```python
class Dog:
    pass


dog = Dog()

print(isinstance(dog, Dog))
```

Output:

```text
True
```

Python's documentation specifically provides `isinstance()` for checking an object's type or inheritance relationship.

---

# 🌳 36. `issubclass()`

Use `issubclass()` to check class inheritance.

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
```

Output:

```text
True
```

Python's inheritance system provides both `isinstance()` and `issubclass()` for these checks.

---

# 🔀 37. Method Resolution Order — MRO

MRO determines the order in which Python searches classes for attributes and methods.

Example:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

Typical result:

```text
[
    <class 'C'>,
    <class 'B'>,
    <class 'A'>,
    <class 'object'>
]
```

You can also use:

```python
C.__mro__
```

MRO becomes especially important with multiple inheritance.

---

# 🏠 38. Properties

Properties allow controlled attribute access using methods.

```python
class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")

        self._age = value


person = Person(25)

print(person.age)

person.age = 30

print(person.age)
```

Output:

```text
25
30
```

Properties are useful when validation or computed behavior is needed while keeping attribute-style syntax.

---

# 📊 39. Dataclasses

For classes primarily intended to store data, Python provides `dataclasses`.

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int


student = Student("Kishor", 25)

print(student)
```

Dataclasses can automatically provide useful methods such as an initializer and representation, reducing boilerplate.

---

# 🏢 40. Real-World OOP Example — E-Commerce

A simple e-commerce system might contain:

```text
E-Commerce System
│
├── User
│
├── Product
│
├── Cart
│
├── Order
│
├── Payment
│
└── Delivery
```

Example:

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        return sum(
            product.price
            for product in self.products
        )


cart = Cart()

cart.add_product(Product("Laptop", 50000))
cart.add_product(Product("Mouse", 1000))

print(cart.total())
```

Output:

```text
51000
```

This example demonstrates **classes, objects, composition, methods, and encapsulation of behavior**.

---

# 🏦 41. Real-World OOP Example — Bank System

Possible design:

```text
Bank
│
├── Account
│   ├── SavingsAccount
│   └── CurrentAccount
│
├── Customer
│
└── Transaction
```

Inheritance:

```text
Account
   │
   ├── SavingsAccount
   │
   └── CurrentAccount
```

Polymorphism:

```python
account.withdraw()
```

can behave differently depending on the account type.

---

# 🏥 42. Real-World OOP Example — Healthcare System

A healthcare application could contain:

```text
Healthcare System
│
├── Patient
├── Doctor
├── Appointment
├── Prescription
├── Hospital
└── Billing
```

Example:

```python
class Patient:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(
            f"Patient: {self.name}, "
            f"Age: {self.age}"
        )


patient = Patient("Kishor", 25)

patient.display()
```

---

# 🧠 43. OOP Design Principles

As your projects become larger, learn these principles:

```text
SOLID
│
├── S → Single Responsibility
├── O → Open/Closed
├── L → Liskov Substitution
├── I → Interface Segregation
└── D → Dependency Inversion
```

These principles help developers design maintainable object-oriented systems.

---

# ⚠️ 44. Common OOP Mistakes

## ❌ Using classes for everything

Not every problem requires a class.

Sometimes a simple function is better:

```python
def calculate_tax(amount):
    return amount * 0.18
```

---

## ❌ Overusing inheritance

Avoid unnecessarily deep hierarchies:

```text
A
 ↓
B
 ↓
C
 ↓
D
 ↓
E
 ↓
F
```

Prefer composition when it provides a simpler design.

---

## ❌ Incorrect class variables

Be careful with mutable class attributes:

```python
class Student:

    subjects = []
```

This list is shared between instances.

Prefer:

```python
class Student:

    def __init__(self):
        self.subjects = []
```

---

## ❌ Ignoring `self`

Incorrect:

```python
class Student:

    def display():
        print("Hello")
```

Correct:

```python
class Student:

    def display(self):
        print("Hello")
```

---

# 🧪 45. Practice Exercises

## 🟢 Beginner

1. Create a `Student` class.
2. Create a `Car` class.
3. Add attributes using `__init__()`.
4. Create instance methods.
5. Create class variables.
6. Create class methods.
7. Create static methods.
8. Practice `self`.

---

## 🟡 Intermediate

9. Build a `BankAccount` class.
10. Build an `Employee` class.
11. Practice inheritance.
12. Practice method overriding.
13. Practice `super()`.
14. Create a polymorphic program.
15. Practice encapsulation.
16. Create custom properties.

---

## 🔴 Advanced

17. Build an e-commerce system.
18. Build a banking application.
19. Build a library management system.
20. Build a hospital management system.
21. Build a vehicle rental system.
22. Build a student management system.
23. Implement abstract classes.
24. Use composition instead of unnecessary inheritance.
25. Design a project using SOLID principles.

---

# 🏆 46. Mini Project — Library Management System

### Project Structure

```text
library_management/
│
├── main.py
│
├── models/
│   ├── book.py
│   ├── member.py
│   └── librarian.py
│
└── services/
    └── library.py
```

### Core Classes

```text
Book
Member
Librarian
Library
```

### Expected Features

```text
Add Book
   ↓
Register Member
   ↓
Issue Book
   ↓
Return Book
   ↓
Search Book
   ↓
Display Available Books
```

This project should demonstrate:

```text
Classes
Objects
Encapsulation
Composition
Inheritance
Polymorphism
Exception Handling
Modules
Packages
```

---

# 💬 47. Interview Questions

## Basic

**Q1. What is OOP?**

A programming paradigm that organizes software around objects containing data and behavior.

**Q2. What is a class?**

A class is a blueprint/type from which objects can be instantiated.

**Q3. What is an object?**

An instance of a class.

**Q4. What is `self`?**

The conventional name for the instance reference passed to instance methods.

**Q5. What is `__init__()`?**

A special method commonly used to initialize an object's state.

---

## Intermediate

**Q6. What is inheritance?**

A mechanism that allows a class to derive from one or more base classes.

**Q7. What is polymorphism?**

The ability to use a common interface with objects that provide different implementations.

**Q8. What is encapsulation?**

Bundling data and related behavior together while controlling or conventionally restricting access to implementation details.

**Q9. What is abstraction?**

Representing essential behavior while hiding unnecessary implementation details.

**Q10. What is method overriding?**

When a subclass provides its own implementation of an inherited method.

---

## Advanced

**Q11. What is multiple inheritance?**

When a class inherits from more than one base class.

**Q12. What is MRO?**

Method Resolution Order — the order Python follows when searching classes for attributes and methods.

**Q13. What is duck typing?**

A programming style where an object's supported behavior matters more than its specific class.

**Q14. Composition vs inheritance?**

```text
Inheritance
"is-a"

Composition
"has-a"
```

**Q15. What is name mangling?**

Python transforms names beginning with two underscores inside a class to reduce accidental name conflicts.

---

# 📌 48. Quick Revision

```text
OBJECT-ORIENTED PROGRAMMING
│
├── Class
│   └── Blueprint
│
├── Object
│   └── Instance
│
├── Attributes
│   ├── Instance Variables
│   └── Class Variables
│
├── Methods
│   ├── Instance
│   ├── Class
│   └── Static
│
├── Encapsulation
│
├── Inheritance
│   ├── Single
│   ├── Multiple
│   ├── Multilevel
│   ├── Hierarchical
│   └── Hybrid
│
├── Polymorphism
│
├── Abstraction
│
├── Composition
│
├── Magic Methods
│
├── Properties
│
├── Dataclasses
│
└── SOLID Principles
```

---

# 🧭 49. OOP Mental Model

Think of OOP like building a real-world system:

```text
Real World
    ↓
Identify Entities
    ↓
Create Classes
    ↓
Create Objects
    ↓
Add Attributes
    ↓
Add Methods
    ↓
Define Relationships
    ↓
Use Inheritance / Composition
    ↓
Apply Polymorphism
    ↓
Build Application
```

For example:

```text
Real World
    ↓
Bank
    ↓
Account
    ↓
SavingsAccount
    ↓
Customer
    ↓
Transaction
```

---

# 🏆 50. Best Practices

### ✅ Keep classes focused

A class should have a clear responsibility.

### ✅ Prefer composition when appropriate

```text
Has-a
```

relationships are often easier to maintain than deep inheritance.

### ✅ Use meaningful names

```python
class BankAccount:
```

is better than:

```python
class Data:
```

### ✅ Keep methods small

Each method should ideally have a clear purpose.

### ✅ Protect invariants

Validate data when necessary.

### ✅ Use properties for controlled access

```python
@property
```

### ✅ Follow Python conventions

Use:

```text
PascalCase → Classes
snake_case → methods/functions/variables
UPPER_CASE → constants
```

### ✅ Don't over-engineer

Use OOP when it makes the design clearer.

---

# 📚 References

### Recommended Reading

* [GeeksforGeeks — Python OOP Concepts](https://www.geeksforgeeks.org/python/python-oops-concepts/)
* [Python Documentation — Classes](https://docs.python.org/3/tutorial/classes.html)
* [Python Documentation — Data Model](https://docs.python.org/3/reference/datamodel.html)
* [Python Documentation — `abc`](https://docs.python.org/3/library/abc.html)
* [Python Documentation — `dataclasses`](https://docs.python.org/3/library/dataclasses.html)

The Python documentation is particularly useful for understanding classes, instances, inheritance, multiple inheritance, name mangling, and method behavior.

---

# 🎯 Key Takeaway

> **OOP is about modeling a system as interacting objects that combine state and behavior.**

The core journey is:

```text
Class
  ↓
Object
  ↓
Attributes + Methods
  ↓
Encapsulation
  ↓
Inheritance
  ↓
Polymorphism
  ↓
Abstraction
  ↓
Composition
  ↓
Design Principles
  ↓
Real-World Applications
```

Once you understand OOP, you can move from writing individual Python programs to designing **larger, modular, maintainable software systems**.

---

## ⏭️ Next Topic

➡️ **[15 — Advanced Python](../15-Advanced-Python/)**

Continue your Python journey:

```text
11. Modules & Packages
          ↓
12. File Handling
          ↓
13. Exception Handling
          ↓
14. Object-Oriented Programming
          ↓
15. Advanced Python
```

---

⭐ **Keep coding. Keep designing. Keep building.**

[1]: https://docs.python.org/3/tutorial/classes.html?utm_source=chatgpt.com "9. Classes — Python 3.14.7 documentation"
