-- Connecting with PSQL

-- -U = which role
-- SQL ends with ;
-- \commands belongs to psql, no closing (;)
-- \l lists DBs
-- \c switch DB
-- \dt list tables
-- \q quit

-- where am I connected
\conninfo

-- create a test database and list databases
CREATE DATABASE shop_test;
\l

-- switch into it and list database
\c shop_test
\dt


-- contrast demo: \l is a shortcut for a query
\l
SELECT datname FROM pg_database;


-- forget backslash
dt;

-- clean up so the file can be re-run
\c postgres
DROP DATABASE shop_test;