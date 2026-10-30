# Procedural Programming vs. Object-Oriented Programming (OOP)

## 1. Procedural Programming

In procedural programming, we mainly work with functions and procedures. The program typically follows a step-by-step approach, executing instructions from top to bottom and calling functions whenever necessary.

**Fortran and COBOL** are two well-known programming languages that support procedural programming.

## 2. Object-Oriented Programming (OOP)

OOP helps us address some of the challenges that arise when developing and maintaining large programs using a purely procedural approach.

Instead of writing one huge program, we break it down into smaller, more manageable components called **objects**.

There are several benefits to this approach:

1. **Easier development:** We can divide a large project into smaller modules, allowing different development teams to work on separate parts of the project simultaneously.

2. **Code reusability:** We can write code for a specific purpose and reuse it in other projects.

   For example, imagine developing an autonomous car. We might create separate modules for:
   - Navigation
   - Camera processing
   - Lane detection

   Later, we could reuse some of these modules in another project, such as an autonomous drone.

3. **Maintainability:** Since the application is divided into smaller components, modifying or debugging one component becomes easier without affecting the entire application.

## 3. A Real-World Example of OOP: A Restaurant

Imagine that you own a restaurant.

To manage your restaurant efficiently, you need several employees, each with specific responsibilities:

- **Receptionist:** Handles customers and welcomes them.
- **Waiters and waitresses:** Take orders and deliver food to customers.
- **Chef:** Prepares and cooks the orders.
- **Cleaners:** Keep the restaurant clean and organized.

As the restaurant manager, you coordinate all these employees to provide the best possible experience for your customers.

Now, let's imagine that we want to create a virtual restaurant using programming.

We need to create these employees as **models**, which we call classes in OOP.

Each class generally has two main components:

1. **Attributes:** What an object has (its properties or data).
2. **Methods:** What an object does (its behaviors or functionality).

For example, let's create a `Waiter` class.

**Attributes:**

```python
is_holding_plate = True

tables_responsible = [3, 4, 6]
```

**Methods:**

```python
def take_order(table, order):
    pass

def take_payment(amount):
    pass
```

## 4. Important OOP Concepts

- An **object** is a combination of data (attributes) and functionality (methods).

- A **class** is a blueprint or template that defines the attributes and methods its objects can have.

- We can create as many objects as we need from a single class (blueprint).

- When naming classes, we typically follow the **PascalCase** naming convention.

  Examples:
  - `Waiter`
  - `RestaurantManager`
  - `AutonomousCar`

- When we put parentheses `()` after a class name to create an object, we are instantiating the class.

  Example:

  ```python
  waiter1 = Waiter()
  ```

  This process is called **instantiation**. Python calls the class's constructor-related initialization process to create and initialize the object. The `__init__()` method is commonly used to initialize an object's attributes.

- A **package** is a collection of related modules that we can organize and use in our Python projects.

## 5. Quick Comparison

| Concept | Procedural Programming | OOP |
|---|---|---|
| Main building blocks | Functions | Classes and objects |
| Main focus | Procedures and steps | Objects and their interactions |
| Data and functionality | Often separated | Grouped together in objects |
| Code reuse | Functions | Classes, objects, inheritance, etc. |
| Large projects | Can become difficult to maintain | Can be easier to organize and maintain |

## 6. Important Technical Notes

Since we're learning Python, there are three concepts worth remembering:

**1. OOP doesn't eliminate functions.**

We still use functions in OOP. The difference is that functions defined inside classes are called methods.

**2. OOP doesn't necessarily mean that every part of a program must be a class.**

We can combine procedural and object-oriented approaches in the same application.

**3. Python supports both procedural and object-oriented programming.**

You don't have to choose only one approach when developing a Python application.

---

## Key Takeaways

Before moving to the four main principles of OOP, make sure you clearly understand these three terms:

- **Class:** Blueprint.
- **Object:** Instance created from a class.
- **Method:** Function defined inside a class.

These three concepts are the foundation of understanding OOP in Python.