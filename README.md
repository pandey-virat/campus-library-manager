
# Campus Library Manager

A Python-based library management system demonstrating Object-Oriented Programming concepts.

## Features

- Abstract parent class using ABC.
- Book, Magazine and DVD classes using inheritance.
- Different late-fee calculations for each item.
- Encapsulation of item availability and member borrowing lists.
- Borrowing and returning operations.
- Exception handling for invalid operations.
- Polymorphism through late-fee calculations.

## Technologies

- Python 3.12+
- Python Standard Library

## How to Run

```bash
python3 main.py
```

## OOP Concepts and Reflection

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is abstract because it provides a common structure for all library items without defining their specific late-fee calculations. If DVD does not implement the abstract late_fee() method, Python raises a TypeError when we try to create a DVD object.

### 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Accessing item.__available directly raises an AttributeError because Python uses name mangling for double-underscore attributes. We use is_available() to read the value through a controlled interface, maintaining encapsulation.

### 3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared across all library item objects and tracks the total number of initialized items. self.title is an instance attribute, meaning each individual item has its own title.
