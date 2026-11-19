# ===== DAY 3 · TOPIC 3: RELATIONAL MODELLING =====
# KEY IDEAS: entity = a thing we store | attribute = its property | PK = unique id | FK = points to another entity's PK
from dataclasses import dataclass

# --- STEP A: two entities (each becomes a table in Week 3), written as dataclasses ---
@dataclass
class Author:                    # entity
    id: int                      # PK: identifies each author
    name: str                    # attribute

@dataclass
class Book:                      # entity
    id: int                      # PK
    title: str                   # attribute
    author_id: int               # FK: holds an Author's id (sits on the MANY side)

# --- STEP B: the records (rows) ---
authors = [Author(1, "Ada"), Author(2, "Linus")]
books = [
    Book(1, "Notes on Engines", 1),
    Book(2, "Analytical Ideas", 1),
    Book(3, "Kernel Diary", 2),
]

# --- STEP C: follow the FK in both directions (ONE author, MANY books) ---
for b in books:
    if b.author_id == 1:
        print(b.title)                     # Notes on Engines / Analytical Ideas

authors_by_id = {}                         # the long way: build a lookup dictionary
for a in authors:
    authors_by_id[a.id] = a                # key = the author's id, value = the author object
# the short way (same result): authors_by_id = {a.id: a for a in authors}
print(authors_by_id)                       # {1: Author(id=1, name='Ada'), 2: Author(id=2, name='Linus')}

print(books[2])                            # Book(id=3, title='Kernel Diary', author_id=2)
print(books[2].author_id)                  # 2
print(authors_by_id[books[2].author_id].name)   # Linus  (book 3 -> its FK 2 -> the author)

# --- STEP D: the PK identifies ONE record, even if names repeat ---
people = [Author(1, "Sam"), Author(2, "Sam")]     # same name, different PK
print(people[0].name == people[1].name, people[0].id == people[1].id)   # True False

# --- STEP E: the common mistake: a LIST of values in one field ---
# BAD DESIGN: one record per book is what we want. Here the books are squeezed into one field of the author.
# A book becomes plain text: no id, no pages, no price of its own. Titles must be edited inside the list,
# and a database column holds ONE value, so searching or counting inside a squeezed list is awkward.
bad_author = {"id": 1, "name": "Ada", "books": ["Notes on Engines", "Analytical Ideas"]}

