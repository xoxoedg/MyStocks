CREATE DATABASE stocks;
CREATE DATABASE dev;
CREATE USER root WITH PASSWORD 'root';
GRANT ALL PRIVILEGES ON DATABASE "stocks" to root;
GRANT ALL PRIVILEGES ON DATABASE dev to root;
