"""
05_nested_dictionaries.py
-------------------------
Nested Dictionaries in Python.

A nested dictionary is a dictionary containing another
dictionary as a value.

Topics covered:
    1. Creating nested dictionaries
    2. Accessing nested values
    3. Updating nested values
    4. Adding nested data
    5. Removing nested data
    6. Iterating through nested dictionaries
    7. Multiple levels of nesting
    8. Lists inside dictionaries
    9. Dictionaries inside lists
    10. Practical real-world examples
"""


# ============================================================
# 1. What Is a Nested Dictionary?
# ============================================================
# A nested dictionary is a dictionary stored inside another
# dictionary.


student = {
    "name": "Alice",
    "age": 21,
    "address": {
        "city": "Pune",
        "state": "Maharashtra",
        "country": "India",
    },
}

print("Student:")
print(student)


# ============================================================
# 2. Accessing Top-Level Values
# ============================================================

print("\nName:", student["name"])
print("Age:", student["age"])


# ============================================================
# 3. Accessing Nested Values
# ============================================================
# Use multiple [] operations.


print("\nCity:", student["address"]["city"])
print("State:", student["address"]["state"])
print("Country:", student["address"]["country"])


# ============================================================
# 4. Using get() with Nested Dictionaries
# ============================================================

city = student.get("address", {}).get("city")

print("\nCity using get():", city)


# If address does not exist, {} prevents a KeyError.

email = student.get("contact", {}).get("email")

print("Email:", email)


# ============================================================
# 5. Updating a Nested Value
# ============================================================

student["address"]["city"] = "Mumbai"

print("\nAfter updating city:")
print(student)


# ============================================================
# 6. Adding a New Nested Key
# ============================================================

student["address"]["pincode"] = 411001

print("\nAfter adding pincode:")
print(student)


# ============================================================
# 7. Adding a Completely New Nested Dictionary
# ============================================================

student["contact"] = {
    "email": "alice@example.com",
    "phone": "9876543210",
}

print("\nAfter adding contact:")
print(student)


# ============================================================
# 8. Updating Multiple Nested Values
# ============================================================

student["contact"].update({
    "email": "alice@python.com",
    "phone": "9999999999",
})

print("\nUpdated contact:")
print(student["contact"])


# ============================================================
# 9. Removing a Nested Key
# ============================================================

removed_phone = student["contact"].pop("phone")

print("\nRemoved phone:", removed_phone)
print("Contact:", student["contact"])


# ============================================================
# 10. Using del on Nested Data
# ============================================================

del student["address"]["pincode"]

print("\nAfter deleting pincode:")
print(student["address"])


# ============================================================
# 11. Multiple Levels of Nesting
# ============================================================
# Dictionaries can contain dictionaries at multiple levels.


company = {
    "name": "Tech Corp",
    "location": {
        "country": "India",
        "state": "Maharashtra",
        "city": "Pune",
        "office": {
            "building": "Tech Park",
            "floor": 5,
            "room": 501,
        },
    },
}

print("\nCompany:")
print(company)


# Access deeply nested values

print(
    "Building:",
    company["location"]["office"]["building"],
)

print(
    "Floor:",
    company["location"]["office"]["floor"],
)


# ============================================================
# 12. Updating Deeply Nested Data
# ============================================================

company["location"]["office"]["floor"] = 6

print("\nUpdated floor:")
print(company["location"]["office"]["floor"])


# ============================================================
# 13. Iterating Over a Nested Dictionary
# ============================================================

student = {
    "name": "Alice",
    "address": {
        "city": "Pune",
        "state": "Maharashtra",
    },
}

print("\n--- Student Information ---")

print("Name:", student["name"])

print("\nAddress:")

for key, value in student["address"].items():
    print(f"{key}: {value}")


# ============================================================
# 14. Nested Dictionary with Multiple Students
# ============================================================

students = {
    "student_101": {
        "name": "Alice",
        "age": 21,
        "marks": 92,
    },
    "student_102": {
        "name": "Bob",
        "age": 22,
        "marks": 85,
    },
    "student_103": {
        "name": "Charlie",
        "age": 20,
        "marks": 78,
    },
}

print("\n--- Students ---")

for student_id, student_data in students.items():

    print(f"\nID: {student_id}")

    for key, value in student_data.items():
        print(f"{key}: {value}")


# ============================================================
# 15. Accessing a Specific Student
# ============================================================

student = students["student_101"]

print("\nStudent 101:")
print(student)

print("Name:", student["name"])
print("Marks:", student["marks"])


# ============================================================
# 16. Updating a Specific Student
# ============================================================

students["student_101"]["marks"] = 96

print("\nUpdated Alice's marks:")
print(students["student_101"])


# ============================================================
# 17. Adding a New Student
# ============================================================

students["student_104"] = {
    "name": "David",
    "age": 23,
    "marks": 88,
}

print("\nAfter adding David:")
print(students)


# ============================================================
# 18. Removing a Student
# ============================================================

removed_student = students.pop("student_104")

print("\nRemoved student:")
print(removed_student)

print("Remaining students:")
print(students)


# ============================================================
# 19. Nested Dictionary with Lists
# ============================================================
# A dictionary value can contain a list.


employee = {
    "name": "Alice",
    "department": "Engineering",
    "skills": [
        "Python",
        "SQL",
        "Git",
    ],
}

print("\nEmployee skills:")
print(employee["skills"])


# Access individual list elements

print("Primary skill:", employee["skills"][0])


# Add a new skill

employee["skills"].append("Docker")

print("Updated skills:")
print(employee["skills"])


# ============================================================
# 20. Dictionary Inside a List
# ============================================================
# This structure is very common when working with APIs and
# JSON data.


students = [
    {
        "id": 101,
        "name": "Alice",
        "marks": 92,
    },
    {
        "id": 102,
        "name": "Bob",
        "marks": 85,
    },
    {
        "id": 103,
        "name": "Charlie",
        "marks": 78,
    },
]

print("\n--- Student List ---")

for student in students:
    print(student)


# Access first student

print("\nFirst student:")
print(students[0])


print("Name:", students[0]["name"])
print("Marks:", students[0]["marks"])


# ============================================================
# 21. Updating Dictionary Inside a List
# ============================================================

students[0]["marks"] = 95

print("\nUpdated first student:")
print(students[0])


# ============================================================
# 22. Nested Dictionary with Lists and Dictionaries
# ============================================================

company = {
    "name": "Tech Corp",
    "employees": [
        {
            "id": 101,
            "name": "Alice",
            "skills": ["Python", "SQL"],
        },
        {
            "id": 102,
            "name": "Bob",
            "skills": ["Java", "Spring"],
        },
    ],
}

print("\nCompany employees:")

for employee in company["employees"]:
    print(employee["name"])

    print("Skills:")

    for skill in employee["skills"]:
        print("-", skill)


# ============================================================
# 23. Nested Dictionary for Product Catalog
# ============================================================

products = {
    "laptop": {
        "name": "Laptop Pro",
        "price": 75000,
        "stock": 10,
    },
    "mouse": {
        "name": "Wireless Mouse",
        "price": 1200,
        "stock": 25,
    },
    "keyboard": {
        "name": "Mechanical Keyboard",
        "price": 3500,
        "stock": 15,
    },
}

print("\n--- Product Catalog ---")

for product_id, product in products.items():

    print(f"\nProduct ID: {product_id}")
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Stock:", product["stock"])


# ============================================================
# 24. Filtering Nested Dictionary Data
# ============================================================
# Find products with stock less than 20.


low_stock_products = {
    product_id: product
    for product_id, product in products.items()
    if product["stock"] < 20
}

print("\nLow-stock products:")
print(low_stock_products)


# ============================================================
# 25. Finding the Most Expensive Product
# ============================================================

most_expensive = max(
    products,
    key=lambda product_id: products[product_id]["price"],
)

print("\nMost expensive product:")
print(most_expensive)

print(
    "Price:",
    products[most_expensive]["price"],
)


# ============================================================
# 26. Nested Dictionary for Employee Management
# ============================================================

employees = {
    101: {
        "name": "Alice",
        "department": "Engineering",
        "salary": 75000,
    },
    102: {
        "name": "Bob",
        "department": "Marketing",
        "salary": 65000,
    },
    103: {
        "name": "Charlie",
        "department": "Engineering",
        "salary": 80000,
    },
}

print("\n--- Employees ---")

for employee_id, employee in employees.items():

    print(
        f"{employee_id}: "
        f"{employee['name']} - "
        f"{employee['department']} - "
        f"{employee['salary']}"
    )


# ============================================================
# 27. Filter Employees by Department
# ============================================================

engineering_team = {
    employee_id: employee
    for employee_id, employee in employees.items()
    if employee["department"] == "Engineering"
}

print("\nEngineering team:")
print(engineering_team)


# ============================================================
# 28. Calculate Total Salary
# ============================================================

total_salary = sum(
    employee["salary"]
    for employee in employees.values()
)

print("\nTotal salary:", total_salary)


# ============================================================
# 29. Nested Dictionary for API-Style Data
# ============================================================
# JSON and REST APIs commonly use structures similar to this.


api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 101,
            "name": "Alice",
            "profile": {
                "city": "Pune",
                "country": "India",
            },
        }
    },
}

print("\n--- API Response ---")

print("Status:", api_response["status"])

print(
    "User:",
    api_response["data"]["user"]["name"],
)

print(
    "City:",
    api_response["data"]["user"]["profile"]["city"],
)


# ============================================================
# 30. Safely Accessing Deeply Nested Data
# ============================================================

city = (
    api_response
    .get("data", {})
    .get("user", {})
    .get("profile", {})
    .get("city")
)

print("\nSafely accessed city:", city)


# ============================================================
# 31. Nested Dictionary Comprehension
# ============================================================
# Create multiplication tables.


tables = {
    number: {
        multiplier: number * multiplier
        for multiplier in range(1, 6)
    }
    for number in range(1, 4)
}

print("\n--- Multiplication Tables ---")
print(tables)


# Access:

print("3 x 5 =", tables[3][5])


# ============================================================
# 32. Practical Example — Student Report
# ============================================================

students = {
    "Alice": {
        "math": 90,
        "science": 85,
        "english": 88,
    },
    "Bob": {
        "math": 75,
        "science": 80,
        "english": 72,
    },
    "Charlie": {
        "math": 95,
        "science": 92,
        "english": 90,
    },
}

print("\n--- Student Reports ---")

for name, subjects in students.items():

    total = sum(subjects.values())
    average = total / len(subjects)

    print(f"\n{name}")
    print("Marks:", subjects)
    print("Total:", total)
    print("Average:", average)


# ============================================================
# 33. Find Top Student
# ============================================================

top_student = max(
    students,
    key=lambda name: sum(students[name].values()),
)

print("\nTop student:", top_student)


# ============================================================
# 34. Practical Example — Shopping Cart
# ============================================================

cart = {
    "laptop": {
        "price": 75000,
        "quantity": 1,
    },
    "mouse": {
        "price": 1200,
        "quantity": 2,
    },
    "keyboard": {
        "price": 3500,
        "quantity": 1,
    },
}

total = 0

for product, details in cart.items():

    subtotal = (
        details["price"]
        * details["quantity"]
    )

    total += subtotal

    print(
        f"{product}: "
        f"{details['price']} x "
        f"{details['quantity']} = "
        f"{subtotal}"
    )

print("Cart total:", total)


# ============================================================
# 35. Practical Example — Configuration
# ============================================================

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "production_db",
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": False,
    },
}

print("\n--- Application Configuration ---")

print("Database host:", config["database"]["host"])
print("Database port:", config["database"]["port"])
print("Server port:", config["server"]["port"])
print("Debug:", config["server"]["debug"])


# ============================================================
# 36. Common Nested Dictionary Pattern
# ============================================================
#
# A very common structure:
#
#     data = {
#         "id": {
#             "field": value,
#             "field": value,
#         }
#     }
#
# Example:
#
#     users = {
#         101: {
#             "name": "Alice",
#             "email": "alice@example.com",
#         },
#         102: {
#             "name": "Bob",
#             "email": "bob@example.com",
#         },
#     }
#
# Access:
#
#     users[101]["name"]
#
# Update:
#
#     users[101]["name"] = "Alice Smith"
#
# ============================================================


# ============================================================
# 37. Important Rules
# ============================================================
#
# 1. A dictionary can contain another dictionary.
#
# 2. Nested values can be accessed using multiple [] calls.
#
# 3. get() can make nested access safer.
#
# 4. Lists and dictionaries can be combined.
#
# 5. Dictionaries inside lists are common in API responses.
#
# 6. Nested dictionaries are frequently used for:
#       - JSON data
#       - API responses
#       - configuration
#       - databases
#       - user profiles
#       - product catalogs
#       - employee records
#
# 7. Avoid unnecessary nesting when a flatter structure
#    would be easier to understand.
#
# 8. For deeply nested data, helper functions or data classes
#    may improve maintainability.
#
# ============================================================


# ============================================================
# 38. Key Takeaways
# ============================================================
#
# Nested dictionary:
#
#     {
#         "user": {
#             "name": "Alice",
#             "age": 21
#         }
#     }
#
# Access:
#
#     data["user"]["name"]
#
# Safe access:
#
#     data.get("user", {}).get("name")
#
# Update:
#
#     data["user"]["name"] = "Bob"
#
# Add:
#
#     data["user"]["city"] = "Pune"
#
# Remove:
#
#     data["user"].pop("city")
#
# Iterate:
#
#     for key, value in data["user"].items():
#         print(key, value)
#
# Nested dictionaries are one of the most important Python
# data structures for handling structured and JSON-like data.
#
# Next:
# 06_dictionary_unpacking.py
# ============================================================
