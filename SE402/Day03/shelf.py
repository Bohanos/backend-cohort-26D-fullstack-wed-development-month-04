# Inheritance and composition
# Ideas: inheritance = "is a" (child extends parent)
# super() calls the parent, composition = "has a" (object hold objects)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def describe(self):
        return f"{self.title} ({self.pages} pages)"

# inheritance: another book that is a Book, plus one extra field 
class EBook(Book):
    def __init__(self, title, pages, size_mb):
        super().__init__(title, pages)
        self.size_mb = size_mb

e = EBook("Python 101", 200, 3.5)
print(e.title, e.size_mb)
print(e.describe())

# The child can extend or replace a parent method
class AudioBook(EBook):
    def __init__(self, title, pages, size_mb, hours):
        super().__init__(title, pages, size_mb)
        self.hours = hours

    def describe(self):
        return super().describe() + f", ({self.size_mb} mb) {self.hours} h audio"

print(AudioBook("SQL Basics", 150, 2.5, 6).describe())

# "is a" check 
print(isinstance(e, Book), isinstance(e, EBook))
print(isinstance(Book("x", 1), EBook))

# composition: a shelf of books (not a book)
class Shelf:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

s = Shelf()
print(s)
s.add(e)
s.add(Book("SQL Basics", 150))
print(len(s.books))                            # 2
print(s.books[0].describe()) 