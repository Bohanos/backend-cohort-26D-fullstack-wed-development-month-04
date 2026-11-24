-- Roles and shemas
-- roles = database user (LOGIN lets it connect)
-- GRANT gives, REVOKE removes
-- schema = namespace inside a data base (default: public)
-- command = psql -U postgres -d shop -f demo_roles.sql

-- Creating a role for an app and checking it
CREATE ROLE app_user LOGIN PASSWORD 'pass_word';
SELECT rolname, rolcanlogin FROM pg_roles WHERE rolname = 'app_user';

-- create a schema with one table
CREATE SCHEMA store;
CREATE TABLE store.note (id INTEGER, txt TEXT);

-- grant only what the app needs
GRANT CONNECT ON DATABASE shop TO app_user;
GRANT USAGE ON SCHEMA store TO app_user;
GRANT SELECT ON ALL TABLES IN SCHEMA store To app_user;

-- act as app_use
SET ROLE app_user;
SELECT current_user;
SELECT * FROM store.note;

-- confirm permissions
INSERT INTO store.note VALUES (1, 'hi');
CREATE TABLE store.other (id INTEGER);

-- the super user ignores the rules
RESET ROLE;
INSERT INTO store.note VALUES (1, 'hi');

-- clean up and re-run file
DROP SCHEMA store CASCADE;
DROP OWNED BY app_user;
DROP ROLE app_user;