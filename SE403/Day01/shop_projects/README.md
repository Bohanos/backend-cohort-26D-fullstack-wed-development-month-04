<!-- Run in order, inside this folder: -->
psql -U postgres -d shop -f schema.sql
psql -U postgres -d shop -f seed.sql
psql -U postgres -d shop -f queries.sql