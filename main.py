
from models import LibraryItem, Book, Magazine, DVD, Member

# Create library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Science Today", 2, 45)
dvd = DVD("Introduction to AI", 3, 120)

# Create members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

print("===== CAMPUS LIBRARY MANAGER =====")

# 1. Successful borrowing
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
except ValueError as e:
    print("Could not borrow:", e)

# 2. Attempt to borrow an already borrowed book
try:
    bob.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)

# 3. Alice borrows the other items
try:
    alice.borrow(magazine)
    alice.borrow(dvd)
    print("Alice's borrowed items:", alice.borrowed_titles())
except ValueError as e:
    print("Could not borrow:", e)

# 4. Alice returns the book
try:
    fee = alice.return_item(book, days_late=3)
    print("Alice returned Python 101.")
    print("Late fee: Rs", fee)
except ValueError as e:
    print("Could not return:", e)

# 5. Bob borrows the returned book
try:
    bob.borrow(book)
    print("Bob borrowed:", book.describe())
except ValueError as e:
    print("Could not borrow:", e)

# 6. Alice returns the DVD
try:
    alice.return_item(dvd)
    print("Alice returned the DVD.")
except ValueError as e:
    print("Could not return:", e)

# 7. Bob attempts to borrow another available item
try:
    bob.borrow(dvd)
except ValueError as e:
    print("Could not borrow:", e)

# 8. Attempt to return an item Bob never borrowed
try:
    bob.return_item(magazine)
except ValueError as e:
    print("Could not return:", e)

# 9. Polymorphism
print("\n===== LATE FEE CALCULATIONS =====")

items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )

# 10. Encapsulation
print("\n===== ENCAPSULATION =====")

print("Book availability:", book.is_available())

try:
    print(book.__available)
except AttributeError as e:
    print("Private attribute access prevented:", e)

# 11. Class attribute
print("\nTotal items created:", LibraryItem.total_items)
