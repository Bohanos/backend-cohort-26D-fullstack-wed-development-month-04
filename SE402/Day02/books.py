# Classes and objects
# ideas: class = blueprint | object = one thing made from it
# self = That object | __init__ runs at creation


# define the blueprint (class)
class Book:
    def __init__(self, title, pages): # runs automatically when a Book is created
        self.title = title
        self.pages = pages
        self.current = 0

    def read(self, count):
        self.current = self.current + count

    def pages_left(self):
        return self.pages - self.current


# making objects by calling the class
a = Book("Python 101", 200)
b = Book("SQL Basics", 150)
print(a.title, a.pages)

# each object has its own values 
a.read(30)
print(a.pages_left(), b.pages_left())
print(type(a))

# How a method really works
print(Book.pages_left(a))


# print an object without __str__
print(a)