# Encapsulation and methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self._current = 0

    @property
    def current(self):
        return self._current

    def read(self, count):
        if count <= 0:
            raise ValueError("Pages read must be more than 0")
        if self._current + count > self.pages:
            raise ValueError("Not enough pages left")
        self._current += count

    def __str__(self):
        return f'{self.title}: {self._current}/{self.pages}'

# use the book normally
a = Book("Python 101", 200)
a.read(30)
print(a.current)
print(a)



try:
    a.read(500)
except ValueError as e:
    print("Error:", e)
try:
    a.read(0)
except ValueError as e:
    print("Error:", e)
print(a)


a._current = 999
print(a)