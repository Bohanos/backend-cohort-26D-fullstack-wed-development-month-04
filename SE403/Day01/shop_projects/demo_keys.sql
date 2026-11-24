-- ===== DAY 1 · TOPIC 7: PRIMARY KEYS, FOREIGN KEYS AND RELATIONSHIPS =====
-- KEY IDEAS: PRIMARY KEY = unique, never NULL | FOREIGN KEY = points to another table's key
--            one-to-many: FK on the MANY side | many-to-many: junction table with two FKs
-- Terminal, inside shop_project:  psql -U postgres -d shop -f demo_keys.sql

-- --- STEP 0: clean slate (children first) ---
DROP TABLE IF EXISTS item_supplier;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS category;

-- --- STEP A: build the four tables ---
CREATE TABLE category (
    id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE item (
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        TEXT NOT NULL,
    qty         INTEGER NOT NULL DEFAULT 0 CHECK (qty >= 0),
    price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    category_id INTEGER NOT NULL REFERENCES category (id)    -- one-to-many: FK on the many side
);
CREATE TABLE supplier (
    id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE item_supplier (                                  -- junction table (many-to-many)
    item_id     INTEGER REFERENCES item (id),
    supplier_id INTEGER REFERENCES supplier (id),
    PRIMARY KEY (item_id, supplier_id)                        -- the PAIR must be unique
);

-- --- STEP B: add rows, then link them (INSERT is Day 2) ---
INSERT INTO category (name) VALUES ('Stationery'), ('Food');
INSERT INTO item (name, price, category_id) VALUES ('Pen', 0.50, 1), ('Book', 4.00, 1);
INSERT INTO supplier (name) VALUES ('Acme'), ('Bolt');
INSERT INTO item_supplier (item_id, supplier_id) VALUES (1, 1), (1, 2), (2, 1);
SELECT * FROM item_supplier;    -- Pen has two suppliers; Acme supplies two items

-- --- STEP C: break it on purpose ---
INSERT INTO item (name, price, category_id) VALUES ('Ghost', 1.00, 99);
-- ERROR:  insert or update on table "item" violates foreign key constraint "item_category_id_fkey"
DELETE FROM category WHERE id = 1;
-- ERROR:  update or delete on table "category" violates foreign key constraint "item_category_id_fkey" on table "item"
INSERT INTO item_supplier (item_id, supplier_id) VALUES (1, 1);
-- ERROR:  duplicate key value violates unique constraint "item_supplier_pkey"
INSERT INTO item_supplier (item_id, supplier_id) VALUES (NULL, 1);
-- ERROR:  null value in column "item_id" of relation "item_supplier" violates not-null constraint

-- --- STEP D: contrast demo: two values in one cell does not work ---
INSERT INTO item (name, price, category_id) VALUES ('Ruler', 1.00, '1,2');
-- ERROR:  invalid input syntax for type integer: "1,2"