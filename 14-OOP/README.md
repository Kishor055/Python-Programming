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

**A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.**  

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute
Creating a Class
Here, class keyword indicates that we are creating a class followed by name of the class (Dog in this case).


class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
Explanation:

class Dog: creates a class named Dog, which acts as a blueprint for dog objects.
species is a class attribute, meaning it is shared by all instances of the class.
__init__() is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
self refers to the current object, allowing each object to store and access its own data.
self.name and self.age are instance attributes, unique to each Dog object created from the class.
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
Objects
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:

State: represented by the attributes and reflects the properties of an object.
Behavior: represented by the methods of an object and reflects the response of an object to other objects.
Identity: gives a unique name to an object and enables one object to interact with other objects.
Creating Object
Creating an object involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation.

class Dog:
    species = "Canine"  # Class attribute
​
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
​
# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)

Output
Buddy
Canine
Explanation:

dog1 = Dog("Buddy", 3): Creates an object of the Dog class with name as "Buddy" and age as 3.
dog1.name: Accesses the instance attribute name of the dog1 object.
dog1.species: Accesses the class attribute species of the dog1 object.
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
AAbsolutely. I’ll combine the **Abstraction, Polymorphism, Inheritance, `super()`, and Method Overriding** material you provided with your existing OOP structure, while keeping the README clean, professional, well-spaced, and GitHub-friendly. The source material covers the OOP foundations through advanced topics such as abstraction, polymorphism, inheritance, composition, properties, and SOLID principles. 

# 🧱 14 — Object-Oriented Programming (OOP)

> **Learn how to design Python programs using classes, objects, encapsulation, inheritance, polymorphism, abstraction, and reusable object-oriented design patterns.**

---

## 📚 Table of Contents

* [🎯 Learning Objectives](#-learning-objectives)
* [🧠 What is OOP?](#-1-what-is-oop)
* [🧩 Why Use OOP?](#-2-why-use-oop)
* [🧱 Classes](#-3-class)
* [👤 Objects](#-4-object)
* [🏷️ Attributes](#-5-attributes)
* [⚙️ Methods](#-6-methods)
* [`self`](#-7-understanding-self)
* [`__init__()`](#-8-init-constructor)
* [Instance Variables](#-9-instance-variables)
* [Class Variables](#-10-class-variables)
* [Instance, Class & Static Methods](#-11-method-types)
* [🔐 Encapsulation](#-12-encapsulation)
* [Access Conventions](#-13-access-specifiers)
* [Getter & Setter](#-14-getter-and-setter)
* [🌳 Inheritance](#-15-inheritance)
* [Types of Inheritance](#-16-types-of-inheritance)
* [`super()`](#-17-super)
* [Method Overriding](#-18-method-overriding)
* [🔄 Polymorphism](#-19-polymorphism)
* [Compile-Time Polymorphism](#-20-compile-time-polymorphism)
* [Runtime Polymorphism](#-21-runtime-polymorphism)
* [Duck Typing](#-22-duck-typing)
* [Operator Polymorphism](#-23-polymorphism-in-operators)
* [Built-in Function Polymorphism](#-24-polymorphism-in-built-in-functions)
* [🎭 Abstraction](#-25-abstraction)
* [Abstract Base Classes](#-26-abstract-base-class)
* [Abstract Methods](#-27-abstract-methods)
* [Concrete Methods](#-28-concrete-methods)
* [Abstract Properties](#-29-abstract-properties)
* [Abstract Class Instantiation](#-30-abstract-class-instantiation)
* [The Four Pillars](#-31-the-four-pillars-of-oop)
* [Composition](#-32-composition)
* [Aggregation](#-33-aggregation)
* [Magic / Dunder Methods](#-34-magic--dunder-methods)
* [Properties](#-35-properties)
* [Dataclasses](#-36-dataclasses)
* [`isinstance()` & `issubclass()`](#-37-isinstance-and-issubclass)
* [MRO](#-38-method-resolution-order--mro)
* [Real-World Examples](#-39-real-world-oop-examples)
* [SOLID Principles](#-40-oop-design-principles)
* [Common Mistakes](#-41-common-oop-mistakes)
* [Practice Exercises](#-42-practice-exercises)
* [Mini Project](#-43-mini-project)
* [Interview Questions](#-44-interview-questions)
* [Quick Revision](#-45-quick-revision)
* [Best Practices](#-46-best-practices)
* [References](#-47-references)
* [Next Topic](#-48-next-topic)

---

# 🎯 Learning Objectives

By the end of this chapter, you will understand:

* Object-Oriented Programming
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
* Public, Protected and Private conventions
* Name Mangling
* Inheritance
* Types of Inheritance
* `super()`
* Method Overriding
* Polymorphism
* Duck Typing
* Abstraction
* Abstract Base Classes
* `abc` module
* Abstract Methods
* Abstract Properties
* Composition
* Aggregation
* Magic / Dunder Methods
* Properties
* Dataclasses
* MRO
* SOLID principles
* Real-world OOP design

---

# 🧠 1. What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software around **objects** containing both:

```text
Data
 +
Behavior
```

For example, a `Car` object may contain:

```text
Data
├── brand
├── model
└── speed

Behavior
├── start()
├── stop()
└── accelerate()
```

Conceptually:

```text
                 🚗 Car
                   │
          ┌────────┴────────┐
          │                 │
         Data            Methods
          │                 │
       brand              start()
       model               stop()
       speed            accelerate()
```

OOP helps developers build applications that are:

* Modular
* Reusable
* Maintainable
* Scalable
* Easier to test

---

# 🧩 2. Why Use OOP?

| Benefit             | Description                                 |
| ------------------- | ------------------------------------------- |
| ♻️ Reusability      | Reuse existing classes and functionality    |
| 🧩 Modularity       | Divide applications into logical components |
| 🔐 Encapsulation    | Keep data and related behavior together     |
| 🌳 Inheritance      | Reuse and extend existing classes           |
| 🔄 Polymorphism     | Same interface, different implementations   |
| 🎭 Abstraction      | Hide unnecessary implementation details     |
| 🛠️ Maintainability | Easier to maintain large applications       |
| 🧪 Testability      | Components can be tested independently      |

---

# 🧱 3. Class

A **class** is a blueprint used to create objects.

A class can contain:

* Attributes
* Methods
* Constructors
* Class variables
* Class methods
* Static methods

### Basic Syntax

```python
class ClassName:
    # attributes
    # methods
    pass
```

### Example

```python
class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here:

* `Dog` → class
* `species` → class variable
* `name` → instance variable
* `age` → instance variable
* `__init__()` → initialization method
* `self` → current object

---

# 👤 4. Object

An **object** is an instance of a class.

```python
class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)
```

### Output

```text
Buddy
Canine
```

Conceptually:

```text
             Dog
              │
            Class
              │
       ┌──────┴──────┐
       │             │
     dog1           dog2
    Object         Object
```

Each object has its own identity and instance state.

---

# 🏷️ 5. Attributes

Attributes represent data associated with an object.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Kishor", 25)

print(student.name)
print(student.age)
```

### Output

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

### Output

```text
Hello!
```

Instance methods normally receive the current instance as their first parameter, conventionally named `self`.

---

# 👤 7. Understanding `self`

`self` refers to the current object.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Kishor")
student.display()
```

Conceptually:

```python
student.display()
```

is similar to:

```python
Student.display(student)
```

> `self` is a naming convention, not a Python keyword. Following the convention is strongly recommended.

---

# 🚀 8. `__init__()` Constructor

`__init__()` is commonly used to initialize an object's state.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee = Employee("Kishor", 50000)

print(employee.name)
print(employee.salary)
```

When an object is created, Python calls `__init__()` for initialization when it is defined.

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

### Output

```text
Kishor
Rahul
```

Conceptually:

```text
student1 → name = Kishor
student2 → name = Rahul
```

Each object maintains its own instance state.

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

### Output

```text
ABC School
ABC School
```

---

# ⚙️ 11. Method Types

Python classes commonly use three method types.

## 11.1 Instance Method

Works with an individual object.

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

## 11.2 Class Method

Works with the class.

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

## 11.3 Static Method

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

Use static methods when an operation logically belongs to the class but does not require object or class state.

---

# 🔐 12. Encapsulation

**Encapsulation** means keeping related data and behavior together while controlling access to internal implementation details.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
```

The `_balance` naming convention communicates:

> This attribute is intended for internal use.

Python relies primarily on conventions rather than strict access modifiers.

---

# 🔑 13. Access Specifiers

Python commonly uses three access conventions.

| Type         | Syntax   | Meaning                            |
| ------------ | -------- | ---------------------------------- |
| 🟢 Public    | `name`   | Normal public access               |
| 🟡 Protected | `_name`  | Intended for internal/subclass use |
| 🔴 Private   | `__name` | Name mangling is applied           |

---

## 🟢 Public Members

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


emp = Employee("John")

emp.display_name()
print(emp.name)
```

Output:

```text
John
John
```

---

## 🟡 Protected Members

A single underscore indicates an internal/protected convention.

```python
class Employee:

    def __init__(self, name, age):
        self.name = name
        self._age = age


class SubEmployee(Employee):

    def show_age(self):
        print("Age:", self._age)


emp = SubEmployee("Ross", 30)

print(emp.name)
emp.show_age()
```

Output:

```text
Ross
Age: 30
```

> `_age` is not strictly private. Python does not enforce this convention.

---

## 🔴 Private Members

Double underscores trigger **name mangling**.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)


emp = Employee("Robert", 60000)

print(emp.name)
emp.show_salary()
```

Output:

```text
Robert
Salary: 60000
```

Direct access:

```python
print(emp.__salary)
```

raises:

```text
AttributeError
```

Python internally transforms the name approximately into:

```text
_Employee__salary
```

Name mangling helps prevent accidental name conflicts; it is not a security mechanism.

---

# 🔧 14. Getter and Setter

Getter and setter methods provide controlled access to internal data.

```python
class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")


emp = Employee()

print(emp.get_salary())

emp.set_salary(60000)

print(emp.get_salary())
```

Output:

```text
50000
60000
```

The setter can validate values before updating internal state.

---

# 🌳 15. Inheritance

**Inheritance** allows a child class to reuse and extend a parent class.

```python
class Animal:

    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)


class Dog(Animal):

    def sound(self):
        print(self.name, "barks")


dog = Dog("Buddy")

dog.info()
dog.sound()
```

Output:

```text
Animal name: Buddy
Buddy barks
```

### Benefits

* Code reusability
* Extensibility
* Hierarchical modeling
* Method overriding
* Polymorphism

---

# 🧬 16. Types of Inheritance

Python supports several inheritance structures.

```text
1. Single
2. Multilevel
3. Multiple
4. Hierarchical
5. Hybrid
```

---

## 16.1 Single Inheritance

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

## 16.2 Multilevel Inheritance

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

## 16.3 Multiple Inheritance

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

Python uses **MRO** to determine the lookup order.

---

## 16.4 Hierarchical Inheritance

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

## 16.5 Hybrid Inheritance

Hybrid inheritance combines multiple inheritance patterns.

```text
         Animal
        /      \
     Mammal    Bird
        \      /
         Hybrid
```

Complex hierarchies should be used carefully because they can become difficult to maintain.

---

# 🦸 17. `super()`

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

### Why use `super()`?

Without `super()`, you may need to duplicate parent initialization logic.

```text
Parent Class
     ↓
super()
     ↓
Child Class
```

`super()` also becomes important in cooperative multiple inheritance.

---

# 🔄 18. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method inherited from its parent.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()
```

Output:

```text
Bark
```

The child implementation takes precedence when the method is called on a `Dog` object.

---

# 🔄 19. Polymorphism

**Polymorphism** means "many forms".

It allows the same interface or operation to behave differently depending on the object or data involved.

Real-world example:

```text
Payment
   │
   ├── Credit Card
   ├── UPI
   ├── NetBanking
   └── Wallet
```

All may expose:

```python
process_payment()
```

but each implementation can behave differently.

---

# 🕐 20. Compile-Time Polymorphism

Python does **not** support traditional compile-time method overloading like languages such as Java or C++.

However, similar behavior can be achieved using:

* Default arguments
* `*args`
* `**kwargs`

Example:

```python
class Calculator:

    def multiply(self, a=1, b=1, *args):

        result = a * b

        for num in args:
            result *= num

        return result


calc = Calculator()

print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))
```

Output:

```text
1
4
6
24
```

This is **overloading-like behavior**, not traditional compile-time method overloading.

---

# 🕐 21. Runtime Polymorphism

Runtime polymorphism occurs when a method call resolves to an implementation based on the actual object.

```python
class Animal:

    def sound(self):
        return "Some generic sound"


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):

    def sound(self):
        return "Meow"


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.sound())
```

Output:

```text
Bark
Meow
Some generic sound
```

The same call:

```python
animal.sound()
```

produces different behavior.

---

# 🦆 22. Duck Typing

Python frequently uses **duck typing**.

> If an object provides the required behavior, its exact class may not matter.

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

Output:

```text
Woof!
Hello!
```

The function does not care whether `obj` is a `Dog` or `Person`.

It only requires:

```python
obj.speak()
```

---

# ➕ 23. Polymorphism in Operators

The same operator can perform different operations depending on operand types.

```python
print(5 + 10)

print("Hello " + "World!")

print([1, 2] + [3, 4])
```

Output:

```text
15
Hello World!
[1, 2, 3, 4]
```

This is operator polymorphism.

Python implements much of this behavior using special methods such as:

```python
__add__()
```

---

# 🧰 24. Polymorphism in Built-in Functions

Built-in functions can also work with different object types.

```python
print(len("Hello"))
print(len([1, 2, 3]))

print(max(1, 3, 2))
print(max("a", "z", "m"))
```

Output:

```text
5
3
3
z
```

The same function adapts its behavior to the object supplied.

---

# 🎭 25. Abstraction

**Abstraction** means exposing essential functionality while hiding unnecessary implementation details.

Real-world example:

```text
                 Shape
                   │
        ┌──────────┼──────────┐
        │          │          │
      Circle    Rectangle   Triangle
```

All shapes may support:

```text
draw()
resize()
get_area()
```

But their internal implementations are different.

```text
User
  │
  ↓
draw()
  │
  ↓
Complex internal implementation
```

The user only needs to know **what the object can do**, not every detail of **how it does it**.

---

# 🧩 26. Abstract Base Class

Python provides the `abc` module for creating **Abstract Base Classes (ABCs)**.

```python
from abc import ABC, abstractmethod
```

An abstract class acts as a blueprint for subclasses.

Example:

```python
from abc import ABC, abstractmethod


class Greet(ABC):

    @abstractmethod
    def say_hello(self):
        pass


class English(Greet):

    def say_hello(self):
        return "Hello!"


g = English()

print(g.say_hello())
```

Output:

```text
Hello!
```

`Greet` defines the required interface, while `English` provides the implementation.

---

# 🔹 27. Abstract Methods

An abstract method defines behavior that subclasses are expected to implement.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
```

A concrete subclass must implement the abstract method before it can normally be instantiated.

---

# 🔹 28. Concrete Methods

An abstract class can also contain fully implemented methods.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"


class Dog(Animal):

    def make_sound(self):
        return "Bark"


dog = Dog()

print(dog.move())
```

Output:

```text
Moving
```

The `move()` method is inherited directly because it already has an implementation.

---

# 🔹 29. Abstract Properties

Abstract properties can enforce that subclasses provide a particular property.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @property
    @abstractmethod
    def species(self):
        pass


class Dog(Animal):

    @property
    def species(self):
        return "Canine"


dog = Dog()

print(dog.species)
```

Output:

```text
Canine
```

The subclass must implement the required property.

---

# 🚫 30. Abstract Class Instantiation

An abstract class containing unimplemented abstract members cannot normally be instantiated.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


animal = Animal()
```

This raises a `TypeError` because `Animal` still has an abstract method.

The intended pattern is:

```text
Abstract Class
      ↓
Concrete Subclass
      ↓
Object
```

---

# 🏛️ 31. The Four Pillars of OOP

The four commonly taught pillars are:

```text
                    OOP
                     │
        ┌────────────┼────────────┐
        │            │            │
 Encapsulation   Inheritance  Polymorphism
        │            │            │
        └──────── Abstraction ────┘
```

| Pillar           | Purpose                                 |
| ---------------- | --------------------------------------- |
| 🔐 Encapsulation | Bundle data and behavior                |
| 🌳 Inheritance   | Reuse and extend classes                |
| 🔄 Polymorphism  | Same interface, different behavior      |
| 🎭 Abstraction   | Hide unnecessary implementation details |

---

# 🔗 32. Composition

**Composition** means creating a class using objects of another class.

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

This represents a **has-a** relationship.

Composition often provides more flexibility than deep inheritance hierarchies.

---

# 🤝 33. Aggregation

Aggregation represents a weaker **has-a** relationship.

The contained object can exist independently.

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

Here:

```text
Teacher
   ↑
   │
Department
```

The `Teacher` can exist independently of `Department`.

---

# 🪄 34. Magic / Dunder Methods

Special methods are surrounded by double underscores.

Examples:

```text
__init__()
__str__()
__repr__()
__len__()
__eq__()
__add__()
__lt__()
```

They allow custom classes to integrate naturally with Python syntax and built-in operations.

---

## `__str__()`

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

## `__repr__()`

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name!r})"


student = Student("Kishor")

print(repr(student))
```

`__repr__()` is useful for debugging and development.

---

## `__add__()`

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

## `__len__()`

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

# 🏠 35. Properties

Properties allow controlled attribute access while retaining attribute-style syntax.

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

Properties are useful for:

* Validation
* Computed values
* Controlled access
* Maintaining a clean API

---

# 📊 36. Dataclasses

For classes primarily designed to store data, Python provides `dataclasses`.

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int


student = Student("Kishor", 25)

print(student)
```

Dataclasses can automatically generate useful methods and reduce boilerplate.

---

# 🧪 37. `isinstance()` and `issubclass()`

## `isinstance()`

Checks whether an object is an instance of a class.

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

---

## `issubclass()`

Checks whether a class inherits from another class.

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

---

# 🔀 38. Method Resolution Order — MRO

**MRO** determines the order in which Python searches classes for attributes and methods.

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

Typical order:

```text
C
↓
B
↓
A
↓
object
```

You can also inspect:

```python
C.__mro__
```

MRO is especially important in multiple inheritance.

---

# 🏢 39. Real-World OOP Examples

## 🛒 E-Commerce System

```text
E-Commerce
│
├── User
├── Product
├── Cart
├── Order
├── Payment
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

---

# 🏦 Banking System

Possible design:

```text
Bank
│
├── Customer
├── Account
│   ├── SavingsAccount
│   └── CurrentAccount
└── Transaction
```

Polymorphism can allow:

```python
account.withdraw()
```

to behave differently for different account types.

---

# 🏥 Healthcare System

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

# 🧠 40. OOP Design Principles

As applications become larger, learn **SOLID** principles.

```text
SOLID
│
├── S → Single Responsibility
├── O → Open/Closed
├── L → Liskov Substitution
├── I → Interface Segregation
└── D → Dependency Inversion
```

These principles help create maintainable and extensible object-oriented systems.

---

# ⚠️ 41. Common OOP Mistakes

## ❌ Using Classes for Everything

Not every problem requires a class.

Sometimes a function is better:

```python
def calculate_tax(amount):
    return amount * 0.18
```

---

## ❌ Overusing Inheritance

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

Prefer composition when it creates a simpler design.

---

## ❌ Incorrect Mutable Class Variables

Avoid:

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

## ❌ Forgetting `self`

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

# 🧪 42. Practice Exercises

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
17. Create an abstract `Animal` class.
18. Implement multiple subclasses.

---

## 🔴 Advanced

19. Build an e-commerce system.
20. Build a banking application.
21. Build a library management system.
22. Build a hospital management system.
23. Build a vehicle rental system.
24. Build a student management system.
25. Implement abstract classes.
26. Implement polymorphic payment methods.
27. Use composition instead of unnecessary inheritance.
28. Design a project using SOLID principles.

---

# 🏆 43. Mini Project — Library Management System

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

The project should demonstrate:

```text
Classes
Objects
Encapsulation
Inheritance
Polymorphism
Abstraction
Composition
Exception Handling
Modules
Packages
```

---

# 💬 44. Interview Questions

## 🟢 Basic

### Q1. What is OOP?

OOP is a programming paradigm that organizes software around objects containing data and behavior.

### Q2. What is a class?

A class is a blueprint/type from which objects can be instantiated.

### Q3. What is an object?

An object is an instance of a class.

### Q4. What is `self`?

`self` is the conventional name for the instance reference passed to instance methods.

### Q5. What is `__init__()`?

`__init__()` is commonly used to initialize an object's state.

---

## 🟡 Intermediate

### Q6. What is inheritance?

Inheritance allows a class to derive from one or more base classes.

### Q7. What is polymorphism?

Polymorphism allows a common interface to work with objects that provide different implementations.

### Q8. What is encapsulation?

Encapsulation combines related data and behavior while controlling access to implementation details.

### Q9. What is abstraction?

Abstraction exposes essential behavior while hiding unnecessary implementation details.

### Q10. What is method overriding?

When a subclass provides its own implementation of an inherited method.

### Q11. What is `super()`?

`super()` provides access to functionality defined in parent classes according to Python's method resolution order.

---

## 🔴 Advanced

### Q12. What is multiple inheritance?

When a class inherits from more than one base class.

### Q13. What is MRO?

**Method Resolution Order** defines the order Python follows when searching classes for attributes and methods.

### Q14. What is duck typing?

A programming style where an object's supported behavior matters more than its exact class.

### Q15. What is name mangling?

Python transforms names beginning with two underscores inside a class to reduce accidental name conflicts.

### Q16. Composition vs inheritance?

```text
Inheritance
"is-a"

Composition
"has-a"
```

### Q17. Does Python support traditional method overloading?

No. Python does not support traditional compile-time method overloading. Default arguments, `*args`, and `**kwargs` can provide similar behavior.

### Q18. Can an abstract class be instantiated?

Not when it still contains unimplemented abstract methods or properties.

---

# 📌 45. Quick Revision

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
│   ├── Public
│   ├── Protected
│   └── Private
│
├── Inheritance
│   ├── Single
│   ├── Multilevel
│   ├── Multiple
│   ├── Hierarchical
│   └── Hybrid
│
├── Method Overriding
│
├── Polymorphism
│   ├── Runtime
│   ├── Duck Typing
│   └── Operator
│
├── Abstraction
│   ├── ABC
│   ├── Abstract Method
│   └── Abstract Property
│
├── Composition
│
├── Aggregation
│
├── Magic Methods
│
├── Properties
│
├── Dataclasses
│
├── MRO
│
└── SOLID Principles
```

---

# 🧭 OOP Mental Model

Think of OOP as designing a real-world system:

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
Inheritance / Composition
    ↓
Polymorphism
    ↓
Abstraction
    ↓
Build Application
```

Example:

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

# 🏆 46. Best Practices

### ✅ Keep Classes Focused

Each class should have a clear responsibility.

### ✅ Prefer Composition When Appropriate

```text
Has-a
```

relationships can often be easier to maintain than deep inheritance hierarchies.

### ✅ Use Meaningful Names

Prefer:

```python
class BankAccount:
```

over:

```python
class Data:
```

### ✅ Keep Methods Small

Each method should have a clear purpose.

### ✅ Validate Data

Protect important object state with validation.

### ✅ Use Properties

Use:

```python
@property
```

when controlled attribute access is useful.

### ✅ Follow Python Naming Conventions

```text
PascalCase  → Classes
snake_case  → Functions / Methods / Variables
UPPER_CASE  → Constants
```

### ✅ Don't Over-Engineer

Use OOP when it makes the design clearer.

---

# 📚 47. References

### Recommended Reading

* **GeeksforGeeks — Python OOP Concepts**
* **Python Documentation — Classes**
* **Python Documentation — Data Model**
* **Python Documentation — `abc`**
* **Python Documentation — `dataclasses`**

The provided learning material also emphasizes abstraction through `ABC`/`abstractmethod`, polymorphism through overriding and duck typing, and inheritance through reusable parent/child class relationships. 

---

# 🎯 Key Takeaway

> **OOP is about modeling a system as interacting objects that combine state and behavior.**

The learning journey:

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
Method Overriding
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

# ⏭️ 48. Next Topic

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

This version is structured as a **single professional chapter README**, with the material you supplied integrated rather than leaving Abstraction, Polymorphism, and Inheritance as disconnected sections.

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
