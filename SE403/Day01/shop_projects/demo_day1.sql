-- Run these commands from your terminal

-- Check if you have postgresql installed
-- ls "/c/Program Files/PostgreSQL/"

-- Check that psql is inside, replace 16 with the version number 
-- ls "/c/Program Files/PostgreSQL/16/bin/psql.exe"

-- Add the folder to PATH permanently replace 16 with your version number
-- echo 'export PATH="/c/Program Files/PostgreSQL/16/bin:$PATH"' >> ~/.bashrc
-- source ~/.bashrc

-- Test it
-- psql --version

-- If you prefer not to change PATH, you can run psql once with its full path and
-- replace the 16 with your own version
-- "/c/Program Files/PostgreSQL/16/bin/psql.exe" -U postgres -f demo_day1.sql

-- Running .sql file
-- psql -U postgres -f file-name.sql

-- Tell psql to print everything without stopping
-- psql -U postgres -P pager=off -f name-name.sql

-- Create database and ask the server who you are and where you are

SELECT Version();
SELECT current_user;
SELECT current_database();
SHOW port;

-- Create a database and list all databases
CREATE DATABASE shop;
\l 

-- Go inside and look down the hierarchy
\c shop
SELECT current_database();
\dn
\dt

-- Break it on purpose (running the create syntax)
CREATE DATABASE shop;

-- Case sensitivity check
CREATE DATABASE Shop;