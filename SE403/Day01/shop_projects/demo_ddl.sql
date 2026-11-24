-- ===== DAY 1 · TOPIC 5: DDL (CREATE, ALTER, DROP) =====
-- KEY IDEAS: DDL = defines structure | NUMERIC = exact (money) | IDENTITY = automatic ids | DROP = data gone
-- Terminal, inside shop_project:  psql -U postgres -d shop -f demo_ddl.sql

-- --- STEP 0: clean slate (children first) ---
DROP TABLE IF EXISTS item_supplier;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS category;

-- --- STEP A: CREATE a table ---
CREATE TABLE category (
    id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   -- id made for you
    name TEXT NOT NULL UNIQUE                                -- required, no duplicates
);

-- --- STEP B: ids are automatic (INSERT is taught on Day 2) ---
INSERT INTO category (name) VALUES ('Stationery'), ('Food');
SELECT ALL FROM category;       -- 1 Stationery | 2 Food

-- --- STEP C: ALTER: add a column, then drop it ---
ALTER TABLE category ADD COLUMN note TEXT;
SELECT * FROM category;       -- a new empty column: note
ALTER TABLE category DROP COLUMN note;

-- --- STEP D: contrast demo: exact numbers versus approximate numbers ---
SELECT 0.1::numeric + 0.2::numeric = 0.3::numeric AS numeric_exact;                          -- t
SELECT 0.1::double precision + 0.2::double precision = 0.3::double precision AS float_exact; -- f

-- --- STEP E: break it on purpose ---
CREATE TABLE category (id INTEGER);
-- ERROR:  relation "category" already exists
INSERT INTO category (id, name) VALUES (99, 'X');
-- ERROR:  cannot insert a non-DEFAULT value into column "id"
INSERT INTO category (name) VALUES ('Food');
-- ERROR:  duplicate key value violates unique constraint "category_name_key"

-- --- STEP F: DROP removes the table and its data for good ---
DROP TABLE category;
SELECT * FROM category;
-- ERROR:  relation "category" does not exist