# ===== DAY 3 · TOPIC 2: DATACLASSES =====
# KEY IDEAS: @dataclass writes __init__, __repr__ and == for you | fields need type hints | defaults go LAST | hints are NOT enforced
from dataclasses import dataclass

# --- STEP A: the long way: a normal class that only holds data ---
class PlainBook:
    def __init__(self, title, pages, price=0.0):
        self.title = title
        self.pages = pages
        self.price = price

p1 = PlainBook("Python 101", 200)
p2 = PlainBook("Python 101", 200)
print(p1)                                   # <__main__.PlainBook object at 0x...>  (unreadable)
print(p1 == p2)                             # False  (compares the objects, not the data)
print(p1 is p2)                             # False: two different objects
print(id(p1), id(p2))                       # two different numbers (the memory identity)

# --- STEP B: the short way: same data, three lines ---
@dataclass
class Book:
    title: str                              # field with a type hint
    pages: int
    price: float = 0.0                      # field with a default: comes LAST

b1 = Book("Python 101", 200)                # __init__ was written for you
b2 = Book("Python 101", 200)
print(b1)                                   # Book(title='Python 101', pages=200, price=0.0)  (__repr__)
print(b1 == b2)                             # True   (== compares the fields)

# --- STEP C: it is still a normal class: you can add methods ---
@dataclass
class Movie:
    title: str
    minutes: int

    def hours(self):
        return self.minutes / 60

print(Movie("Up", 96).hours())              # 1.6

# --- STEP D: type hints are NOT enforced ---
odd = Book("Python 101", "many")            # pages should be int, but Python does not check
print(odd)                                  # Book(title='Python 101', pages='many', price=0.0)

