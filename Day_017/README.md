# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **classes** and **objects**. It helps make code more reusable, maintainable, and organized.

## 1. Naming Conventions

In Python, we commonly use three naming conventions:

### PascalCase
- Each word begins with an uppercase letter.
- There are no spaces or underscores between words.
- **Commonly used for class names in Python (PEP 8).**

Examples:
```python
class MyClass:
    pass

class StudentInformation:
    pass
```

### camelCase
- The first word begins with a lowercase letter.
- Every subsequent word begins with an uppercase letter.
- Commonly used for variables and functions in languages such as JavaScript and Java.

Examples:
```python
studentName = "John"
userAge = 25
```

### snake_case
- All letters are lowercase.
- Words are separated by underscores (`_`).
- **Recommended for variable and function names in Python (PEP 8).**

Examples:
```python
student_name = "John"
user_age = 25

def calculate_total_price():
    pass
```

### Naming Convention Comparison

| Convention | Example | Common Usage |
|---|---|---|
| PascalCase | `StudentInformation` | Python class names |
| camelCase | `studentInformation` | JavaScript/Java variables and methods |
| snake_case | `student_information` | Python variables and functions |

---

## 2. Classes and Objects

A **class** is a blueprint for creating objects. It defines the attributes (data) and methods (behavior) that its objects can have.

An **object** is an instance of a class.

Example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("BMW", "X5")
```

In this example:
- `Car` is the class.
- `my_car` is an object (instance) of `Car`.
- `brand` and `model` are instance attributes.
- `"BMW"` and `"X5"` are the values assigned to those attributes.

---

## 3. Constructors and Initialization (`__init__`)

A **constructor** is responsible for creating an object.

In Python, `__new__()` handles object creation, while **`__init__()` initializes the newly created object**.

In everyday Python programming, `__init__()` is commonly referred to as the constructor, although technically it is the initializer.

The `__init__()` method is automatically called when a new object is created through the normal class instantiation process.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 22)
student2 = Student("Bob", 25)
```

Here:
- `__init__()` initializes the instance.
- `name` and `age` are parameters.
- `self.name` and `self.age` are instance attributes.
- Each object maintains its own attribute values.

---

## 4. Default Attribute Values

Sometimes, we want to initialize an attribute with a default value without requiring the user to provide that value as an argument.

We can do this in two ways.

### Method 1: Assign a Fixed Value Inside `__init__()`

```python
class User:
    def __init__(self, name):
        self.name = name
        self.is_active = True
        self.login_count = 0

user1 = User("Alice")
```

In this example:
- `name` must be provided when creating the object.
- `is_active` is automatically initialized to `True`.
- `login_count` is automatically initialized to `0`.

### Method 2: Use Default Parameter Values

```python
class User:
    def __init__(self, name, role="guest"):
        self.name = name
        self.role = role

user1 = User("Alice")
user2 = User("Bob", "admin")
```

Here:
- `user1.role` is `"guest"`.
- `user2.role` is `"admin"`.

**Important:** Default parameters are optional arguments, while fixed attributes inside `__init__()` do not need corresponding parameters.

---

## 5. Methods

A **method** is a function defined inside a class.

An instance method operates on an object and can access or modify its attributes through `self`.

Example:

```python
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def show_speed(self):
        print(f"Current speed: {self.speed}")

my_car = Car("BMW")

my_car.accelerate(20)
my_car.show_speed()
```

Output:
```text
Current speed: 20
```

In this example:
- `accelerate()` is an instance method that modifies an attribute.
- `show_speed()` is an instance method that displays an attribute.
- `my_car.accelerate(20)` calls a method on an object.

Python also supports **class methods** and **static methods**, which behave differently from instance methods.

---

## 6. The `self` Parameter

In Python, `self` refers to the **current instance of a class**.

It allows instance methods to access and modify the attributes and other methods belonging to that object.

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

person1 = Person("Alice")
person2 = Person("Bob")

person1.introduce()
person2.introduce()
```

Output:
```text
Hello, my name is Alice
Hello, my name is Bob
```

### Important Notes About `self`

- `self` represents the specific instance on which a method is called.
- It is conventionally the first parameter of instance methods.
- Python automatically passes the instance when calling an instance method through an object.
- `self` is **not a reserved Python keyword**, but using this name is a strong convention.

For example:

```python
person1.introduce()
```

Is approximately equivalent to:

```python
Person.introduce(person1)
```

---

## 7. Instance Attributes vs. Class Attributes

Python supports two important types of attributes.

### Instance Attributes

Attributes associated with individual objects, commonly defined through `self` inside `__init__()`.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Each object has its own `name` attribute.

### Class Attributes

Attributes defined directly inside the class body and shared through the class unless overridden on an instance.

```python
class Student:
    school_name = "Python Academy"

    def __init__(self, name):
        self.name = name

student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school_name)
print(student2.school_name)
```

Output:
```text
Python Academy
Python Academy
```

Here, `school_name` is a class attribute, while `name` is an instance attribute.

---

## 8. Quick Summary

| Concept | Description |
|---|---|
| Class | A blueprint for creating objects |
| Object | An instance of a class |
| Attribute | Data associated with a class or object |
| Method | A function defined inside a class |
| `__init__()` | Initializes a newly created object |
| `__new__()` | Creates and returns a new instance |
| `self` | Refers to the current instance |
| Instance Attribute | An attribute belonging to a specific object |
| Class Attribute | An attribute defined on the class |
| Default Parameter | An optional parameter with a predefined value |
| PascalCase | Recommended naming convention for Python classes |
| snake_case | Recommended naming convention for Python variables and functions |

**Key takeaway:** A class defines the structure and behavior of objects, `__init__()` initializes their state, and `self` allows instance methods to interact with each object's attributes.