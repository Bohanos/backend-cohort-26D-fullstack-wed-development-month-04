-- ===== DAY 1 · TOPIC 6: CONSTRAINTS =====
-- KEY IDEAS: constraints = rules the database enforces | NOT NULL, UNIQUE, CHECK, DEFAULT
-- Terminal, inside shop_project:  psql -U postgres -d shop -f demo_constraints.sql

-- --- STEP 0: clean slate ---
DROP TABLE IF EXISTS item_supplier;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS category;

-- --- STEP A: build both tables with the slide's rules ---
CREATE TABLE category (
    id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE item (
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        TEXT NOT NULL,                          -- value required
    qty         INTEGER NOT NULL DEFAULT 0              -- used when none is given
                CHECK (qty >= 0),                       -- condition must be true
    price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    category_id INTEGER NOT NULL REFERENCES category (id)
);

-- --- STEP B: good rows (INSERT is Day 2) ---
INSERT INTO category (name) VALUES ('Stationery'), ('Food');
INSERT INTO item (name, price, category_id) VALUES ('Pen', 0.50, 1);          -- qty not given
INSERT INTO item (name, qty, price, category_id) VALUES ('Book', 3, 4.00, 1);
SELECT * FROM item;     -- Pen has qty 0 (DEFAULT); Book has qty 3

-- --- STEP C: break it on purpose, one rule at a time ---
INSERT INTO item (name, qty, price, category_id) VALUES (NULL, 1, 1.00, 1);
-- ERROR:  null value in column "name" of relation "item" violates not-null constraint
INSERT INTO item (name, qty, price, category_id) VALUES ('Ruler', -1, 1.00, 1);
-- ERROR:  new row for relation "item" violates check constraint "item_qty_check"
INSERT INTO item (name, qty, price, category_id) VALUES ('Ruler', 1, -5.00, 1);
-- ERROR:  new row for relation "item" violates check constraint "item_price_check"

-- --- STEP D: contrast demo: a table with NO rules accepts bad data ---
CREATE TABLE item_nocheck (name TEXT, qty INTEGER);
INSERT INTO item_nocheck VALUES (NULL, -5);     -- works: INSERT 0 1
SELECT * FROM item_nocheck;                     -- a nameless item with qty -5
DROP TABLE item_nocheck;
